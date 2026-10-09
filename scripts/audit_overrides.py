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


def build_item_index(jars: list[Path]) -> dict[str, set[str]]:
    """Map mod_id -> the item/block ids the pack can actually resolve.

    Built from jar contents (`assets/<ns>/models/item/**` and
    `assets/<ns>/blockstates/**`) rather than from a running registry, because
    this script must not boot the game. Two known limits, both handled by
    reporting them rather than guessing:

    - `minecraft:` is never indexed, because the vanilla jar is not in
      `mods/`. Every `minecraft:` id is treated as resolvable.
    - An item with no model file (some are generated) will look missing. Such
      ids are reported under `maybe-missing`, never as a deletion candidate.
    """
    index: dict[str, set[str]] = {}
    for jar in jars:
        try:
            with zipfile.ZipFile(jar) as zf:
                for name in zf.namelist():
                    m = re.match(
                        r"(?:.*/)?assets/([a-z0-9_.-]+)/models/item/(.+)\.json$", name
                    )
                    if m:
                        index.setdefault(m.group(1), set()).add(m.group(2))
                        continue
                    m = re.match(
                        r"(?:.*/)?assets/([a-z0-9_.-]+)/blockstates/(.+)\.json$", name
                    )
                    if m:
                        index.setdefault(m.group(1), set()).add("block:" + m.group(2))
        except (zipfile.BadZipFile, OSError):
            continue
    return index


def item_resolvable(item_id: str, index: dict[str, set[str]]) -> bool:
    """True if the item has a model or blockstate somewhere in the pack."""
    ns, _, path = item_id.partition(":")
    if not path:
        # No namespace means "this mod's namespace", which we cannot resolve
        # statically, so do not claim it is missing.
        return True
    if ns == "minecraft":
        return True
    entries = index.get(ns)
    if entries is None:
        return False
    return path in entries or f"block:{path}" in entries


def upstream_recipe_body(
    key: str, jars: list[Path], cache: dict[str, str | None]
) -> str | None:
    """The mod's own copy of a recipe we override, if the mod still ships it."""
    if key in cache:
        return cache[key]
    ns, _, rest = key.partition(":")
    path = f"data/{ns}/{rest}.json"
    body: str | None = None
    for jar in jars:
        try:
            with zipfile.ZipFile(jar) as zf:
                if path in zf.namelist():
                    body = zf.read(path).decode("utf-8", "replace")
                    break
        except (zipfile.BadZipFile, OSError):
            continue
    cache[key] = body
    return body


def classify_failure(why: str) -> str:
    """Bucket a recorded failure reason.

    Only the `missing item` bucket is something this script can verify has been
    fixed by checking that the item now resolves. The other three need a running
    registry or a boot, so they must not be reported as re-enable candidates.
    """
    low = why.lower()
    if "unknown item" in low or "unregistered item" in low or "no attributes" in low:
        return "missing item"
    if "serializer" in low:
        return "unknown recipe serializer"
    if "tag" in low:
        return "stale or missing tag"
    if any(
        k in low
        for k in ("amount", "`id`", "vs `item`", "codec", "malformed", "format", "shape")
    ):
        return "malformed recipe json"
    if "loot" in low or "element" in low:
        return "loot table element"
    return "unclassified"


def ledger_causes() -> dict[str, str]:
    """Map recipe id -> recorded cause, parsed from the load-fix inventory.

    Prose in a markdown table is a fragile source, so an unparsed row is simply
    absent and the tool reports it as unclassified rather than guessing.
    """
    ledger = ROOT / "docs" / "mods" / "load-fixes-inventory.md"
    if not ledger.is_file():
        return {}
    causes: dict[str, str] = {}
    text = ledger.read_text(encoding="utf-8")
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        for cell in cells:
            m = re.fullmatch(r"`([a-z0-9_]+:[a-z0-9_./]+)`", cell)
            if m:
                causes.setdefault(m.group(1), cells[1] if cells[0].startswith("`") else "")
                break
    return causes


def lookup_cause(key: str, causes: dict[str, str]) -> str:
    """Find a ledger cause for an override key, tolerating format drift.

    The ledger writes ids like `ae_universal_press:overloadprocessorpress` while
    the override path is `data/ae_universal_press/recipe/overloadprocessorpress`,
    so the key carries a kind segment (`recipe/`, `tags/`, `data_maps/`, ...) the
    ledger omits. Try the exact key first, then the key without that segment.
    """
    if key in causes:
        return causes[key]
    ns, _, rest = key.partition(":")
    trimmed = rest.split("/", 1)[1] if "/" in rest else rest
    for candidate in (f"{ns}:{trimmed}", f"{ns}:{rest}", trimmed):
        if candidate in causes:
            return causes[candidate]
    return ""


ITEM_REF = re.compile(
    r'"(?:item|id|fluid)"\s*:\s*"([a-z0-9_.-]+:[a-z0-9_./-]+)"'
)
TAG_REF = re.compile(r'"tag"\s*:\s*"([a-z0-9_.-]+:[a-z0-9_./-]+)"')


def analyse_recipe_items(
    key: str, jars: list[Path], index: dict[str, set[str]], installed: dict[str, bool],
    cause: str = "",
) -> dict:
    """Why did this recipe fail, and is the cause gone?

    Reads the mod's original recipe, pulls out every item it needs, and reports
    which of those the pack cannot resolve.

    The important part is the `verdict`, which is deliberately conservative: it
    only claims the cause is gone for the ONE failure class this can actually
    verify. A recipe disabled for a malformed-JSON or serializer reason may well
    have every item present and still be broken, so it is reported as needing a
    boot test rather than as a re-enable candidate.
    """
    body = upstream_recipe_body(key, jars, {})
    bucket = classify_failure(cause) if cause else "unclassified"
    out: dict = {
        "upstream": "not shipped",
        "cause": cause or "(not recorded in the ledger)",
        "cause_class": bucket,
        "items": [],
        "tags": [],
        "unresolvable": [],
        "ns_installed": installed.get(key.split(":")[0]),
        "verdict": "UNKNOWN - needs a boot test",
        "why_verdict": "",
    }
    if body is None:
        out["verdict"] = "OVERRIDE IS DEAD WEIGHT"
        out["why_verdict"] = "upstream no longer ships this path"
        return out

    parses = True
    parse_error = ""
    try:
        json.loads(body)
    except json.JSONDecodeError as exc:
        parses = False
        parse_error = f"upstream json does not parse: {exc.msg} at line {exc.lineno}"

    out["parses"] = parses
    if not parses:
        out["parse_error"] = parse_error

    # "id" is as important as "item": 1.21.1 uses it for results and containers,
    # which is exactly where a missing-item failure hides. Matching only "item"
    # once produced a false RE-ENABLE CANDIDATE on a recipe whose container held
    # the unregistered item.
    items = sorted(set(ITEM_REF.findall(body)))
    tags = sorted(set(TAG_REF.findall(body)))
    unresolvable = [i for i in items if not item_resolvable(i, index)]
    out["items"] = items
    out["tags"] = tags
    out["unresolvable"] = unresolvable

    if not parses:
        out["verdict"] = "STILL BROKEN"
        out["why_verdict"] = parse_error
    elif bucket == "missing item" and not unresolvable:
        out["verdict"] = "RE-ENABLE CANDIDATE"
        out["why_verdict"] = "cause was a missing item, and every item now resolves"
    elif bucket == "missing item" and unresolvable:
        out["verdict"] = "STILL BLOCKED"
        out["why_verdict"] = "items still unresolvable: " + ", ".join(unresolvable)
    elif bucket in ("unclassified", "unclassified "):
        out["verdict"] = "UNKNOWN - needs a boot test"
        out["why_verdict"] = "no recorded cause, so nothing can be concluded from files"
    else:
        out["verdict"] = "UNKNOWN - needs a boot test"
        out["why_verdict"] = (
            f"cause was '{bucket}', which an item-existence check cannot verify"
        )
    return out


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


# Not every override under load-fixes is a recipe. Calling them all recipes
# mislabels 20+ of them and makes the item analysis meaningless for those.
KINDS = {
    "recipe": "recipe",
    "recipes": "recipe",
    "tags": "tag",
    "loot_table": "loot table",
    "loot_modifiers": "loot modifier",
    "advancement": "advancement",
    "worldgen": "worldgen",
    "neoforge": "neoforge data",
    "data_maps": "data map",
}


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


def kind_of(key: str) -> str:
    _, _, rest = key.partition(":")
    head = rest.split("/", 1)[0]
    return KINDS.get(head, head)


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
        "--items",
        action="store_true",
        help="also read each mod's original recipe and report which items the pack "
        "cannot resolve. Requires --inventory. This is what turns 'needs a boot "
        "test' into an answer for most recipes.",
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
    causes: dict[str, str] = {}
    if args.inventory:
        jars = jar_paths()
        if not jars:
            print("no jars found in .cache; run a packwiz refresh first", file=sys.stderr)
        for ns in {ns for ns, _, _ in recipes + loot}:
            installed[ns] = namespace_is_installed(ns, jars)
        shipped = shipped_entries(jars, {key for _, key, _ in recipes + loot})
        if args.items:
            print("indexing items across jars (one pass, this is the slow part)...", file=sys.stderr)
            item_index = build_item_index(jars)
            causes = ledger_causes()

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
            entry = {
                "id": key,
                "file": str(path.relative_to(ROOT)),
                "verdict": verdict,
                "reason": reason,
            }
            if args.items and kind_of(key) == "recipe":
                analysis = analyse_recipe_items(
                    key, jars, item_index, installed, lookup_cause(key, causes)
                )
                entry["analysis"] = analysis
            report[group].append(entry)

    def sort_key(entry: dict) -> tuple[int, str]:
        order = {"UNNECESSARY": 0, "LIKELY UNNECESSARY": 1}
        if args.batch == "removed":
            return (order.get(entry["verdict"], 2), entry["id"])
        return (2, entry["id"])

    for group in ("recipes", "loot_tables"):
        report[group].sort(key=sort_key)

    for group, label in (("recipes", "Disabled recipes"), ("loot_tables", "Empty loot tables")):
        rows = report[group]
        unneeded = [r for r in rows if r["verdict"] == "UNNECESSARY"]
        print(f"\n=== {label}: {len(rows)} total, {len(unneeded)} look unnecessary ===")
        if not args.inventory:
            print("  (run with --inventory to actually check; needs cached jars)")
            continue
        if unneeded:
            by_reason: dict[str, list[str]] = {}
            for row in unneeded:
                by_reason.setdefault(row["reason"], []).append(row["id"])
            for reason, ids in by_reason.items():
                print(f"\n  -- {reason} ({len(ids)}) --")
                for i in sorted(ids):
                    print(f"     {i}")
        else:
            print("  all overrides still look load-bearing")

        if not (args.items and group == "recipes"):
            continue

        by_kind: dict[str, int] = {}
        for r in rows:
            k = kind_of(r["id"])
            by_kind[k] = by_kind.get(k, 0) + 1
        print("  overrides by kind: " + ", ".join(f"{k} {v}" for k, v in sorted(by_kind.items(), key=lambda kv: -kv[1])))
        analysed = [r for r in rows if "analysis" in r]
        if not analysed:
            continue
        dead = [r for r in analysed if r["analysis"]["upstream"] == "not shipped"]
        blocked = [r for r in analysed if r["analysis"]["unresolvable"]]
        clean = [
            r for r in analysed
            if r["analysis"]["upstream"] == "shipped" and not r["analysis"]["unresolvable"]
        ]

        print("\n  --- per-recipe item analysis ---")
        by_kind: dict[str, int] = {}
        for r in rows:
            k = kind_of(r["id"])
            by_kind[k] = by_kind.get(k, 0) + 1
        print("  overrides by kind: " + ", ".join(f"{k} {v}" for k, v in sorted(by_kind.items(), key=lambda kv: -kv[1])))
        analysed = [r for r in rows if "analysis" in r]
        if not analysed:
            continue
        buckets: dict[str, list[str]] = {}
        for r in analysed:
            buckets.setdefault(r["analysis"]["verdict"], []).append(r["id"])
        order = [
            "RE-ENABLE CANDIDATE",
            "OVERRIDE IS DEAD WEIGHT",
            "STILL BLOCKED",
            "STILL BROKEN",
            "UNKNOWN - needs a boot test",
        ]
        for verdict in order:
            ids = buckets.get(verdict)
            if not ids:
                continue
            print(f"\n  {verdict} ({len(ids)}):")
            for i in sorted(ids):
                print(f"     {i}")
        print(
            "\n  Only RE-ENABLE CANDIDATE is actionable from files alone: the recorded"
            "\n  cause was a missing item and every item now resolves. Everything else"
            "\n  needs a boot test, because its cause was malformed JSON, a missing"
            "\n  serializer, a stale tag, or was never recorded."
        )
        if any(r["analysis"]["tags"] for r in analysed):
            print(
                "\n  note: tag references are found but NOT resolved -- a tag expands to"
                " whatever is inside it, which needs a running registry."
            )
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
