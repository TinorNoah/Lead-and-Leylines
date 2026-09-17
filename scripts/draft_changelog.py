#!/usr/bin/env python3
"""Draft changelog bullets from pack/mods/*.pw.toml diffs.

Prints a starting point only. Do not write this into CHANGELOG.md; rewrite it
into player-facing language with the update-changelog skill.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_MODS = Path("pack/mods")


def git_output(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def list_tomls(ref: str | None) -> dict[str, str]:
    """Map stem -> blob text. ref=None means the working tree."""
    out: dict[str, str] = {}
    if ref is None:
        folder = ROOT / PACK_MODS
        if not folder.is_dir():
            return out
        for path in sorted(folder.glob("*.pw.toml")):
            out[path.stem] = path.read_text(encoding="utf-8")
        return out
    listing = git_output(["ls-tree", "-r", "--name-only", ref, str(PACK_MODS)])
    for line in listing.splitlines():
        path = line.strip()
        if not path.endswith(".pw.toml"):
            continue
        blob = git_output(["show", f"{ref}:{path}"])
        out[Path(path).stem] = blob
    return out


def meta(text: str, stem: str) -> dict[str, str]:
    data = tomllib.loads(text)
    update = data.get("update") or {}
    curseforge = update.get("curseforge") or {}
    modrinth = update.get("modrinth") or {}
    return {
        "name": str(data.get("name") or stem),
        "filename": str(data.get("filename") or ""),
        "cf_file": str(curseforge.get("file-id") or ""),
        "mr_version": str(modrinth.get("version") or ""),
    }


def pin(info: dict[str, str]) -> str:
    if info["cf_file"]:
        return f"file-id {info['cf_file']}"
    if info["mr_version"]:
        return f"modrinth {info['mr_version']}"
    return info["filename"] or "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Draft changelog lines from pack/mods *.pw.toml diffs."
    )
    parser.add_argument(
        "old",
        nargs="?",
        default="HEAD",
        help="git ref for the previous state (default HEAD)",
    )
    parser.add_argument(
        "new",
        nargs="?",
        default=None,
        help="git ref for the new state (default: working tree)",
    )
    args = parser.parse_args()
    old_label = args.old
    new_label = args.new if args.new is not None else "working tree"
    previous = {stem: meta(text, stem) for stem, text in list_tomls(args.old).items()}
    current = {stem: meta(text, stem) for stem, text in list_tomls(args.new).items()}

    added = [current[stem]["name"] for stem in sorted(set(current) - set(previous))]
    removed = [previous[stem]["name"] for stem in sorted(set(previous) - set(current))]
    updated: list[str] = []
    for stem in sorted(set(current) & set(previous)):
        before = previous[stem]
        after = current[stem]
        if (before["cf_file"], before["mr_version"], before["filename"]) == (
            after["cf_file"],
            after["mr_version"],
            after["filename"],
        ):
            continue
        updated.append(f"{after['name']}: {pin(before)} -> {pin(after)}")

    print(f"draft from {old_label} -> {new_label}")
    print("rewrite these into player-facing CHANGELOG.md bullets; do not paste as-is.")
    print()
    print("Added:")
    if added:
        for name in added:
            print(f"  - {name}")
    else:
        print("  (none)")
    print("Removed:")
    if removed:
        for name in removed:
            print(f"  - {name}")
    else:
        print("  (none)")
    print("Updated:")
    if updated:
        for line in updated:
            print(f"  - {line}")
    else:
        print("  (none)")


if __name__ == "__main__":
    main()
