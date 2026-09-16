#!/usr/bin/env python3
"""Upload GitHub Release client + server artifacts to CurseForge and Modrinth."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from publish_stores import upload_curseforge, upload_modrinth
from read_pack_versions import ROOT, read_pack


def env(name: str) -> str:
    return os.environ.get(name, "").strip()


def find_artifacts(folder: Path) -> dict[str, Path]:
    servers = sorted(folder.glob("*-server-mods.zip"))
    mrpacks = sorted(folder.glob("*.mrpack"))
    clients = sorted(
        path for path in folder.glob("*.zip") if not path.name.endswith("-server-mods.zip")
    )
    if len(servers) != 1 or len(mrpacks) != 1 or len(clients) != 1:
        names = [path.name for path in folder.iterdir() if path.is_file()]
        raise SystemExit(
            "expected one client zip, one server-mods zip, and one mrpack in "
            f"{folder}; found {names}"
        )
    return {"client_zip": clients[0], "server_zip": servers[0], "mrpack": mrpacks[0]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifacts", default="artifacts")
    parser.add_argument("--channel", required=True, choices=("alpha", "beta", "release"))
    parser.add_argument("--notes", default="notes.md")
    parser.add_argument("--skip-curseforge", action="store_true")
    parser.add_argument("--skip-modrinth", action="store_true")
    args = parser.parse_args()
    pack = read_pack(ROOT / "pack" / "pack.toml")
    name = f"{pack['name']} {pack['pack_version']}"
    changelog = Path(args.notes).read_text(encoding="utf-8").strip()
    if not changelog:
        raise SystemExit(f"empty changelog: {args.notes}")
    paths = find_artifacts(Path(args.artifacts))
    cf_token = env("CURSEFORGE_TOKEN")
    cf_project = env("CURSEFORGE_PROJECT_ID")
    mr_token = env("MODRINTH_TOKEN")
    mr_project = env("MODRINTH_PROJECT_ID")
    if not args.skip_curseforge:
        if not (cf_token and cf_project):
            raise SystemExit("CURSEFORGE_TOKEN and CURSEFORGE_PROJECT_ID are required")
        parent_id = upload_curseforge(
            project_id=cf_project,
            token=cf_token,
            zip_path=paths["client_zip"],
            name=name,
            changelog=changelog,
            minecraft=pack["minecraft"],
            loader=pack["loader"],
            channel=args.channel,
        )
        upload_curseforge(
            project_id=cf_project,
            token=cf_token,
            zip_path=paths["server_zip"],
            name=f"{name} (server)",
            changelog=changelog,
            minecraft=pack["minecraft"],
            loader=pack["loader"],
            channel=args.channel,
            parent_file_id=parent_id,
        )
    if not args.skip_modrinth:
        if not (mr_token and mr_project):
            raise SystemExit("MODRINTH_TOKEN and MODRINTH_PROJECT_ID are required")
        upload_modrinth(
            project=mr_project,
            token=mr_token,
            mrpack=paths["mrpack"],
            name=name,
            version=pack["pack_version"],
            changelog=changelog,
            minecraft=pack["minecraft"],
            loader=pack["loader"],
            channel=args.channel,
            server_zip=paths["server_zip"],
        )


if __name__ == "__main__":
    main()
