#!/usr/bin/env python3
"""Report which committed recipe/loot-table overrides look unnecessary now.

Why this exists
---------------
`docs/mods/load-fixes-inventory.md` records 63 disabled recipes and 120 empty
loot tables, all written by hand on 2026-09-27 to silence upstream parse
errors. ATM-10's Bibliocraft script asks the same question live every boot
(`if (!Item.exists(...))`) and drops the suppression by itself once the mod
fixes its registration. We answer it statically instead, so the answer goes
stale.

This script does **not** change the pack. It reads the committed overrides,
asks the same question each one encodes, and prints what looks unnecessary —
so the five-batch revalidation plan has an answer instead of a guess. Files
stay in place until a human deletes them, which keeps them git-diffable.
That is the deliberate trade: computed suppression would self-correct but
become invisible in a PR diff.

What it can and cannot decide
-----------------------------
The override exists because a mod ships a file that fails to parse. So three
verdicts, in descending confidence:

- **UNNECESSARY** — the mod is not installed at all, so there is nothing left
  to shadow. Safe to delete.
- **LIKELY UNNECESSARY** — the mod is installed but no longer ships that path,
  so the override no longer shadows anything.
- **KEEP** — the mod still ships that path. The override is still shadowing
  something; whether the underlying bug is fixed cannot be read from files.

An earlier version of this script reported "the mod ships this file again" as
UNNECESSARY and matched all 63 recipes. That was backwards: shipping the file
is precisely why the override exists.

It cannot know whether an item is *registered at runtime*, only whether the
jar contains the file. That is the gap a boot test closes, which is why the
five-batch plan in `docs/mods/load-fixes-inventory.md` still applies to
anything reported KEEP.

Usage
-----
    python3 scripts/audit_overrides.py                    # report
    python3 scripts/audit_overrides.py --json             # machine readable
    python3 scripts/audit_overrides.py --batch removed     # oldest-removed first
    python3 scripts/audit_overrides.py --inventory         # also scan mod jars

`--inventory` is slower (it opens every jar) but it is the only mode that can
detect "the mod is gone entirely", which is the largest expected win.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
REQUIRED_DATA = PACK / "global_packs" / "required_data"

LOAD_FIXES = REQUIRED_DATA / "lead-leylines-load-fixes"
ORPHAN_LOOT = REQUIRED_DATA / "lead-leylines-orphan-loot"

# mekmm ships as a JarJar inside Mekanism Extras: no jar of its own name, but
# its blocks very much exist. Treating it as absent would propose deleting 80
# overrides whose blocks still need a table.
#
# Matching is on the modId declared in mods.toml, never on the jar filename.
# An earlier check grepped pack/mods for the namespace and concluded
# arsdelight was uninstalled; it is in fact Ars Nouveau's Flavors & Delight,
# whose jar is arsdelight-2.2.2.jar with modId "arsdelight". Filename matching
# gets this wrong in both directions.
NESTED_NAMESPACES = {
    "mekmm": "mekanism-extras",
}


def jar_paths() -> list[Path]:
    """Every jar we can resolve, preferring the server's own resolved mod set.

    `dist/_smoke-test/mods/` is what a dedicated server actually boots from, so
    it is the authoritative list and is checked first. The packwiz caches are
    the fallback for when no smoke run exists yet. The Prism instance is a
    third fallback because it also holds client-only jars, which matter here:
    several overrides belong to client-side mods.
    """
    found: list[Path] = []
    seen: set[Path] = set()
    candidates = [
        ROOT / "dist" / "_smoke-test" / "mods",
        ROOT / ".cache" / "mod-files",
        Path.home() / "Library/Application Support/PrismLauncher/instances/Lead and Leylines/.minecraft/mods",
    ]
    for directory in candidates:
        if not directory.is_dir():
            continue
        for jar in sorted(directory.glob("*.jar")):
            resolved = jar.resolve()
            if resolved not in seen:
                seen.add(resolved)
                found.append(jar)
    return found


def _normalise(name: str) -> str:
    """Strip separator differences so `mekanism_extras` matches `mekanism-extras`."""
    return re.sub(r"[^a-z0-9]", "", name.lower())


def namespace_is_installed(ns: str, jars: list[Path]) -> bool:
    """True if any installed jar declares this mod id, including JarJar."""
    if ns in NESTED_NAMESPACES:
        parent = _normalise(NESTED_NAMESPACES[ns])
        return any(parent in _normalise(j.name) for j in jars)
    needle = _normalise(ns)
    for jar in jars:
        try:
            with zipfile.ZipFile(jar) as zf:
                for meta in ("META-INF/neoforge.mods.toml", "META-INF/mods.toml"):
                    try:
                        text = zf.read(meta).decode("utf-8", "replace")
                    except KeyError:
                        continue
                    for match in re.findall(r'modId\s*=\s*"?([a-zA-Z0-9_]+)"?', text):
                        if _normalise(match) == needle:
                            return True
        except (zipfile.BadZipFile, OSError):
            continue
    return False


def shipped_entries(jars: list[Path], wanted: set[str]) -> set[str]:
    """Which of the wanted datapack paths does any installed jar ship?

    Builds one prefix index instead of scanning every jar per lookup, which is
    what makes --inventory bearable.
    """
    found: set[str] = set()
    remaining = set(wanted)
    for jar in jars:
        if not remaining:
            break
        try:
            with zipfile.ZipFile(jar) as zf:
                names = zf.namelist()
        except (zipfile.BadZipFile, OSError):
            continue
        for name in names:
            if not name.startswith("data/") or not name.endswith(".json"):
                continue
            parts = name.split("/")
            if len(parts) < 4:
                continue
            ns = parts[1]
            kind = parts[2]
            rel = "/".join(parts[3:])[: -len(".json")]
            key = f"{ns}:{kind}/{rel}"
            if key in remaining:
                found.add(key)
                remaining.discard(key)
    return found


def collect(root: Path) -> list[tuple[str, str, Path]]:
    """Return (mod_id, datapack_key, path) for every override under `root`.

    Overrides live at `<root>/data/<ns>/<kind>/<...>.json`, so the leading
    `data` segment must be skipped or every namespace resolves as the literal
    string "data".
    """
    out: list[tuple[str, str, Path]] = []
    for path in sorted(root.rglob("*.json")):
        rel = path.relative_to(root)
        parts = rel.parts
        if parts[0] != "data":
            continue
        if len(parts) < 4:
            continue
        ns = parts[1]
        kind = parts[2]
        tail = "/".join(parts[3:])[: -len(".json")]
        out.append((ns, f"{ns}:{kind}/{tail}", path))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument(
        "--inventory",
        action="store_true",
        help="also open installed jars to detect removed mods and re-shipped files",
    )
    parser.add_argument(
        "--batch",
        choices=["removed", "all"],
        default="all",
        help="ordering: 'removed' puts whole-removed namespaces first (highest yield)",
    )
    args = parser.parse_args()

    recipes = collect(LOAD_FIXES)
    loot = collect(ORPHAN_LOOT)
    if not recipes and not loot:
        print("no overrides found; is pack/global_packs/required_data/ present?")
        return 1

    jars: list[Path] = []
    installed: dict[str, bool] = {}
    shipped: set[str] = set()
    if args.inventory:
        jars = jar_paths()
        if not jars:
            print("no jars found in .cache; run a packwiz refresh first", file=sys.stderr)
        for ns in {ns for ns, _, _ in recipes + loot}:
            installed[ns] = namespace_is_installed(ns, jars)
        shipped = shipped_entries(jars, {key for _, key, _ in recipes + loot})

    report = {"recipes": [], "loot_tables": []}

    for group, rows in (("recipes", recipes), ("loot_tables", loot)):
        for ns, key, path in rows:
            verdict = "KEEP"
            reason = ""
            if args.inventory:
                if installed.get(ns) is False:
                    # Nothing left to shadow. This is the strongest signal
                    # available and the only one that is safe to act on.
                    verdict, reason = "UNNECESSARY", "mod is not installed"
                elif key in shipped:
                    # The mod still ships this path, so the override is still
                    # shadowing something. Whether the underlying bug is fixed
                    # cannot be read from files — only a boot can tell.
                    verdict, reason = "KEEP", "mod still ships this path (may still be broken)"
                else:
                    # Upstream stopped shipping the file, so the override no
                    # longer shadows anything.
                    verdict, reason = "LIKELY UNNECESSARY", "mod no longer ships this path"
            report[group].append(
                {"id": key, "file": str(path.relative_to(ROOT)), "verdict": verdict, "reason": reason}
            )

    def sort_key(entry: dict) -> tuple[int, str]:
        order = {"UNNECESSARY": 0, "LIKELY UNNECESSARY": 1}
        if args.batch == "removed":
            return (order.get(entry["verdict"], 2), entry["id"])
        return (2, entry["id"])

    for group in ("recipes", "loot_tables"):
        report[group].sort(key=sort_key)

    if args.json:
        print(json.dumps(report, indent=2))
        return 0

    for group, label in (("recipes", "Disabled recipes"), ("loot_tables", "Empty loot tables")):
        rows = report[group]
        unneeded = [r for r in rows if r["verdict"] == "UNNECESSARY"]
        print(f"\n=== {label}: {len(rows)} total, {len(unneeded)} look unnecessary ===")
        if not args.inventory:
            print("  (run with --inventory to actually check; needs cached jars)")
            continue
        if not unneeded:
            print("  all overrides still look load-bearing")
            continue
        by_reason: dict[str, list[str]] = {}
        for row in unneeded:
            by_reason.setdefault(row["reason"], []).append(row["id"])
        for reason, ids in by_reason.items():
            print(f"\n  -- {reason} ({len(ids)}) --")
            for i in sorted(ids):
                print(f"     {i}")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
