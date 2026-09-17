#!/usr/bin/env python3
"""Upload GitHub Release client + server artifacts to CurseForge."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from publish_stores import upload_curseforge
from read_pack_versions import ROOT, read_pack


def env(name: str) -> str:
    return os.environ.get(name, "").strip()


def find_artifacts(folder: Path) -> dict[str, Path]:
    servers = sorted(folder.glob("*-server-mods.zip"))
    clients = sorted(
        path for path in folder.glob("*.zip") if not path.name.endswith("-server-mods.zip")
    )
    if len(servers) != 1 or len(clients) != 1:
        names = [path.name for path in folder.iterdir() if path.is_file()]
        raise SystemExit(
            f"expected one client zip and one server-mods zip in {folder}; found {names}"
        )
    return {"client_zip": clients[0], "server_zip": servers[0]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifacts", default="artifacts")
    parser.add_argument("--channel", required=True, choices=("alpha", "beta", "release"))
    parser.add_argument("--notes", default="notes.md")
    parser.add_argument("--skip-curseforge", action="store_true")
    args = parser.parse_args()
    pack = read_pack(ROOT / "pack" / "pack.toml")
    name = f"{pack['name']} {pack['pack_version']}"
    changelog = Path(args.notes).read_text(encoding="utf-8").strip()
    if not changelog:
        raise SystemExit(f"empty changelog: {args.notes}")
    paths = find_artifacts(Path(args.artifacts))
    cf_token = env("CURSEFORGE_TOKEN")
    cf_project = env("CURSEFORGE_PROJECT_ID")
    if args.skip_curseforge:
        print("CurseForge: skip (--skip-curseforge)")
        return
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


if __name__ == "__main__":
    main()
