#!/usr/bin/env python3
"""Report jars embedded under overrides/mods/ in client zip and mrpack.

Missing archive paths return no findings. This script does not rewrite files.
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

DEFAULT_PREFIX = "overrides/mods/"
GUIDANCE = (
    "If a listed jar is actually on CurseForge, re-install it with "
    "packwiz curseforge install --addon-id <id> --file-id <id> so the "
    "export can reference it externally. If it is not on CurseForge, "
    "confirm the embed is genuinely unavoidable."
)


def _embedded_mod_jars(
    archive_path: Path | str,
    overrides_prefix: str = DEFAULT_PREFIX,
) -> list[str]:
    path = Path(archive_path)
    if not path.is_file():
        return []
    prefix = overrides_prefix.replace("\\", "/").rstrip("/") + "/"
    names: list[str] = []
    try:
        with zipfile.ZipFile(path) as archive:
            for info in archive.infolist():
                name = info.filename.replace("\\", "/")
                if info.is_dir() or not name.lower().endswith(".jar"):
                    continue
                if name.startswith(prefix):
                    names.append(Path(name).name)
    except zipfile.BadZipFile:
        print(f"warning: not a zip: {path}", file=sys.stderr)
        return []
    return sorted(names)


def report_embedded_mods(
    client_zip: Path | str | None,
    mrpack: Path | str | None,
) -> dict[str, list[str]]:
    findings: dict[str, list[str]] = {}
    for label, archive in (("client_zip", client_zip), ("mrpack", mrpack)):
        if not archive:
            continue
        names = _embedded_mod_jars(archive)
        if names:
            findings[Path(archive).name] = names
    return findings


def print_report(findings: dict[str, list[str]]) -> None:
    if not findings:
        print("all referenced externally, good")
        return
    print("embedded jars (not referenced externally):")
    for artifact, jars in findings.items():
        print(f"  {artifact}:")
        for jar in jars:
            print(f"    - {jar}")
    print(GUIDANCE)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List jars packed into overrides/mods/ of a CurseForge zip and mrpack."
    )
    parser.add_argument("client_zip")
    parser.add_argument("mrpack")
    args = parser.parse_args()
    print_report(report_embedded_mods(args.client_zip, args.mrpack))


if __name__ == "__main__":
    main()
