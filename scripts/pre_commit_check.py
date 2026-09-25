#!/usr/bin/env python3
"""Local pre-commit checks against the staged index.

Hard-blocks staged .jar files. Warns (exit 0) if pack/mods *.pw.toml is staged
without CHANGELOG.md or docs/installed/catalog.toml in the same commit.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def staged_files() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "-z"],
        cwd=ROOT,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr.decode("utf-8", errors="replace"))
        raise SystemExit(result.returncode)
    raw = result.stdout.split(b"\0")
    return [name.decode("utf-8") for name in raw if name]


def main() -> None:
    files = staged_files()
    jars = [name for name in files if name.lower().endswith(".jar")]
    if jars:
        print("pre-commit: refusing staged .jar files:", file=sys.stderr)
        for name in jars:
            print(f"  {name}", file=sys.stderr)
        print("Never commit jars. Stage packwiz TOML only.", file=sys.stderr)
        raise SystemExit(1)

    pw_tomls = [
        name
        for name in files
        if name.startswith("pack/mods/") and name.endswith(".pw.toml")
    ]
    changelog_staged = "CHANGELOG.md" in files
    if pw_tomls and not changelog_staged:
        print(
            "pre-commit: pack/mods *.pw.toml is staged but CHANGELOG.md is not. "
            "If players will notice this, run the update-changelog skill. "
            "Not blocking: splitting the changelog into a later commit is fine."
        )
    catalog_staged = "docs/installed/catalog.toml" in files
    if pw_tomls and not catalog_staged:
        print(
            "pre-commit: pack/mods *.pw.toml is staged but docs/installed/catalog.toml "
            "is not. Add or remove the catalog row, then run "
            "python3 scripts/installed_catalog.py. Not blocking."
        )
    raise SystemExit(0)


if __name__ == "__main__":
    main()
