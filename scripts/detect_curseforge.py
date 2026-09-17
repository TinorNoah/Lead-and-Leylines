#!/usr/bin/env python3
"""One-shot wrapper: packwiz curseforge detect, then refresh.

Manual maintenance only. Do not call this from release.py.
Detect looks at jars already in pack/mods/, not at .pw.toml files alone.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
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


def run_packwiz(*args: str) -> subprocess.CompletedProcess[str]:
    command = [packwiz_bin(), *args]
    print("+", " ".join(command))
    result = subprocess.run(
        command,
        cwd=PACK_DIR,
        check=False,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"packwiz {' '.join(args)} failed with exit {result.returncode}")
    return result


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    mods_dir = PACK_DIR / "mods"
    mods_dir.mkdir(parents=True, exist_ok=True)
    jars = sorted(mods_dir.glob("*.jar"))
    print(f"packwiz curseforge detect in {PACK_DIR} ({len(jars)} jar(s) in pack/mods/)")
    if jars:
        run_packwiz("curseforge", "detect", "-y")
    else:
        print("no jars to fingerprint; skipping detect")
    run_packwiz("refresh")
    print(
        "detect finished. Review git diff on pack/mods/*.pw.toml: "
        "files that gained [update.curseforge] can be referenced on CurseForge export. "
        "No jars in pack/mods/ means detect had nothing to scan."
    )


if __name__ == "__main__":
    main()
