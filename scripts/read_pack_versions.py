#!/usr/bin/env python3
"""Read pack identity from pack/pack.toml. No hardcoded game versions."""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_TOML = ROOT / "pack" / "pack.toml"


def read_pack(path: Path) -> dict[str, str]:
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    pack_version = data.get("version")
    versions = data.get("versions")
    if not pack_version or not isinstance(versions, dict):
        raise SystemExit(f"pack.toml missing version or [versions]: {path}")
    minecraft = versions.get("minecraft")
    if not minecraft:
        raise SystemExit(f"pack.toml [versions] missing minecraft: {path}")
    loader_keys = [key for key in versions if key != "minecraft"]
    if len(loader_keys) != 1:
        raise SystemExit(
            f"expected exactly one loader key in [versions], found {loader_keys}"
        )
    loader = loader_keys[0]
    return {
        "pack_version": str(pack_version),
        "minecraft": str(minecraft),
        "loader": str(loader),
        "loader_version": str(versions[loader]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--github-output",
        action="store_true",
        help="append KEY=value lines to $GITHUB_OUTPUT",
    )
    args = parser.parse_args()
    if not PACK_TOML.is_file():
        raise SystemExit(f"missing {PACK_TOML}")
    result = read_pack(PACK_TOML)
    if args.github_output:
        github_output = Path(sys.environ.get("GITHUB_OUTPUT", ""))
        if not github_output:
            raise SystemExit("GITHUB_OUTPUT is not set")
        with github_output.open("a", encoding="utf-8") as handle:
            for key, value in result.items():
                handle.write(f"{key}={value}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
