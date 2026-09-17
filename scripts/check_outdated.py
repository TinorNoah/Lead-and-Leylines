#!/usr/bin/env python3
"""Report which mods packwiz update --all would change, without touching pack/.

Copies pack/ to a temp directory, runs the update there, diffs *.pw.toml, prints
the report, then deletes the copy. Report-only; never writes the real pack/.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_DIR = ROOT / "pack"


def packwiz_bin() -> str:
    found = shutil.which("packwiz")
    if found:
        return found
    fallback = Path.home() / "go" / "bin" / "packwiz"
    if fallback.is_file():
        return str(fallback)
    raise SystemExit("packwiz not found on PATH (also checked ~/go/bin/packwiz)")


def identity(path: Path) -> dict[str, str]:
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    update = data.get("update") or {}
    curseforge = update.get("curseforge") or {}
    modrinth = update.get("modrinth") or {}
    return {
        "name": str(data.get("name") or path.stem),
        "filename": str(data.get("filename") or ""),
        "cf_project": str(curseforge.get("project-id") or ""),
        "cf_file": str(curseforge.get("file-id") or ""),
        "mr_version": str(modrinth.get("version") or ""),
    }


def index_mods(folder: Path) -> dict[str, dict[str, str]]:
    mods = folder / "mods"
    if not mods.is_dir():
        return {}
    return {path.stem: identity(path) for path in sorted(mods.glob("*.pw.toml"))}


def format_pin(meta: dict[str, str]) -> str:
    if meta["cf_file"]:
        return f"curseforge file-id {meta['cf_file']} ({meta['filename']})"
    if meta["mr_version"]:
        return f"modrinth version {meta['mr_version']} ({meta['filename']})"
    return meta["filename"] or "(unpinned)"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    if not PACK_DIR.is_dir():
        raise SystemExit(f"missing {PACK_DIR}")
    before = index_mods(PACK_DIR)
    with tempfile.TemporaryDirectory(prefix="lead-leylines-outdated-") as raw:
        work = Path(raw) / "pack"
        shutil.copytree(PACK_DIR, work)
        command = [packwiz_bin(), "update", "--all", "-y"]
        print("+", " ".join(command), f"(in {work})")
        result = subprocess.run(command, cwd=work, check=False, text=True)
        if result.returncode != 0:
            print(f"packwiz update --all exited {result.returncode} in the temp copy")
        after = index_mods(work)
    changed: list[str] = []
    for stem in sorted(set(before) | set(after)):
        old = before.get(stem)
        new = after.get(stem)
        if old == new:
            continue
        if old and new:
            changed.append(
                f"  {new['name']}: {format_pin(old)} -> {format_pin(new)}"
            )
        elif new:
            changed.append(f"  added in temp update (unexpected): {new['name']}")
        else:
            changed.append(f"  removed in temp update (unexpected): {old['name']}")
    if not changed:
        print("no updates available")
        return
    print(f"{len(changed)} update(s) available (real pack/ untouched):")
    print("\n".join(changed))


if __name__ == "__main__":
    main()
