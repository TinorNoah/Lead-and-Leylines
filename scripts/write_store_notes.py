#!/usr/bin/env python3
"""Write the CHANGELOG.md ## [X.Y.Z] section for store publish jobs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from read_pack_versions import ROOT, read_pack
from release import CHANGELOG_FILE, changelog_has_real_bullets, extract_changelog_section


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="notes.md",
        help="path to write the extracted changelog section",
    )
    parser.add_argument(
        "--version",
        help="pack version without v (default: pack.toml)",
    )
    args = parser.parse_args()
    version = args.version or read_pack(ROOT / "pack" / "pack.toml")["pack_version"]
    if not CHANGELOG_FILE.is_file():
        raise SystemExit(f"missing {CHANGELOG_FILE}")
    section = extract_changelog_section(
        CHANGELOG_FILE.read_text(encoding="utf-8"),
        version,
    )
    if section is None:
        raise SystemExit(f"CHANGELOG.md has no ## [{version}] section")
    if not changelog_has_real_bullets(section):
        raise SystemExit(f"## [{version}] has no bullet entries")
    Path(args.output).write_text(section + "\n", encoding="utf-8")
    print(f"wrote {args.output} ({len(section.splitlines())} lines)")


if __name__ == "__main__":
    main()
