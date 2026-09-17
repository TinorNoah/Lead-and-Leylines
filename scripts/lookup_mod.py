#!/usr/bin/env python3
"""Look up a CurseForge and/or Modrinth slug for minecraft-modding Step 2.

Prints last-updated date, Minecraft versions, loaders, dependencies, and
license/distribution flags. Does not decide whether the mod belongs in the pack.
Never prints API keys.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from envfile import load_env_file
from read_pack_versions import PACK_TOML, read_pack

USER_AGENT = "TinorNoah/Lead-and-Leylines (github.com/TinorNoah/Lead-and-Leylines)"
MODRINTH_API = "https://api.modrinth.com/v2"
CURSEFORGE_API = "https://api.curseforge.com/v1"
MINECRAFT_GAME_ID = 432
MODS_CLASS_ID = 6
CF_LOADER = {
    0: "any",
    1: "forge",
    2: "cauldron",
    3: "liteloader",
    4: "fabric",
    5: "quilt",
    6: "neoforge",
}
CF_RELATION = {
    1: "embedded",
    2: "optional",
    3: "required",
    4: "tool",
    5: "incompatible",
    6: "include",
}


def cf_key() -> str:
    for name in ("CURSEFORGE_API_KEY", "CF_API_KEY"):
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return ""


def fetch_json(url: str, headers: dict[str, str]) -> Any:
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 404}:
            return None
        raise SystemExit(f"lookup failed: HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"lookup failed: {exc}") from exc


def fetch_modrinth_project(slug: str) -> dict[str, Any] | None:
    data = fetch_json(
        f"{MODRINTH_API}/project/{urllib.parse.quote(slug, safe='')}",
        {"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    return data if isinstance(data, dict) else None


def fetch_modrinth_versions(slug: str) -> list[dict[str, Any]]:
    data = fetch_json(
        f"{MODRINTH_API}/project/{urllib.parse.quote(slug, safe='')}/version",
        {"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict)]


def print_modrinth(slug: str, pack: dict[str, str]) -> None:
    project = fetch_modrinth_project(slug)
    print("== Modrinth ==")
    if not project:
        print(f"  not found: {slug}")
        return
    license_info = project.get("license") or {}
    license_name = ""
    if isinstance(license_info, dict):
        license_name = str(license_info.get("id") or license_info.get("name") or "")
    print(f"  name: {project.get('title') or slug}")
    print(f"  id: {project.get('id')}")
    print(f"  updated: {project.get('updated') or project.get('published')}")
    print(f"  loaders: {', '.join(str(item) for item in project.get('loaders') or [])}")
    print(
        "  minecraft: "
        + ", ".join(str(item) for item in project.get("game_versions") or [])
    )
    print(f"  license: {license_name or '(none listed)'}")
    print(f"  client/server: {project.get('client_side')} / {project.get('server_side')}")
    versions = fetch_modrinth_versions(slug)
    mc = pack["minecraft"]
    loader = pack["loader"].lower()
    matching = [
        version
        for version in versions
        if mc in (version.get("game_versions") or [])
        and loader in [str(item).lower() for item in (version.get("loaders") or [])]
    ]
    chosen = matching[0] if matching else (versions[0] if versions else None)
    if not chosen:
        print("  dependencies: (no versions returned)")
        return
    label = "matching pack.toml" if matching else "latest listed"
    print(
        f"  {label} version: {chosen.get('version_number')} "
        f"({chosen.get('id')}) {chosen.get('date_published')}"
    )
    deps = chosen.get("dependencies") or []
    if not deps:
        print("  dependencies: none listed")
        return
    print("  dependencies:")
    for dep in deps:
        if not isinstance(dep, dict):
            continue
        kind = dep.get("dependency_type") or "?"
        ident = dep.get("project_id") or dep.get("file_name") or dep.get("version_id")
        print(f"    - {kind}: {ident}")


def curseforge_headers(key: str) -> dict[str, str]:
    return {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "x-api-key": key,
    }


def fetch_curseforge_mod(slug: str, key: str) -> dict[str, Any] | None:
    query = urllib.parse.urlencode(
        {
            "gameId": MINECRAFT_GAME_ID,
            "classId": MODS_CLASS_ID,
            "slug": slug,
        }
    )
    payload = fetch_json(
        f"{CURSEFORGE_API}/mods/search?{query}",
        curseforge_headers(key),
    )
    if not isinstance(payload, dict):
        return None
    data = payload.get("data")
    if not isinstance(data, list) or not data:
        return None
    first = data[0]
    return first if isinstance(first, dict) else None


def fetch_curseforge_files(
    mod_id: int,
    key: str,
    minecraft: str,
    loader: str,
) -> list[dict[str, Any]]:
    loader_id = next(
        (number for number, name in CF_LOADER.items() if name == loader.lower()),
        None,
    )
    query: dict[str, Any] = {"gameVersion": minecraft, "pageSize": 50}
    if loader_id is not None:
        query["modLoaderType"] = loader_id
    payload = fetch_json(
        f"{CURSEFORGE_API}/mods/{mod_id}/files?{urllib.parse.urlencode(query)}",
        curseforge_headers(key),
    )
    if not isinstance(payload, dict):
        return []
    data = payload.get("data")
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict)]


def print_curseforge(slug: str, pack: dict[str, str]) -> None:
    print("== CurseForge ==")
    key = cf_key()
    if not key:
        print(
            "  skipped: set CURSEFORGE_API_KEY in .env "
            "(CurseForge Core API key from console.curseforge.com). "
            "The upload token is not this key."
        )
        return
    mod = fetch_curseforge_mod(slug, key)
    if not mod:
        print(f"  not found or unauthorized: {slug}")
        return
    dates = [str(mod.get("dateModified") or ""), str(mod.get("dateReleased") or "")]
    print(f"  name: {mod.get('name')}")
    print(f"  id: {mod.get('id')}")
    print(f"  updated: {dates[0] or dates[1] or '(unknown)'}")
    indexes = mod.get("latestFilesIndexes") or []
    versions: set[str] = set()
    loaders: set[str] = set()
    if isinstance(indexes, list):
        for item in indexes:
            if not isinstance(item, dict):
                continue
            game = item.get("gameVersion")
            if game:
                versions.add(str(game))
            loader_id = item.get("modLoader")
            if loader_id in CF_LOADER:
                loaders.add(CF_LOADER[int(loader_id)])
    print("  minecraft: " + ", ".join(sorted(versions)) if versions else "  minecraft: (see files)")
    print("  loaders: " + ", ".join(sorted(loaders)) if loaders else "  loaders: (see files)")
    allow = mod.get("allowModDistribution")
    print(f"  allowModDistribution: {allow}")
    print(f"  license: (CurseForge has no license field; distribution flag above)")
    files = fetch_curseforge_files(int(mod["id"]), key, pack["minecraft"], pack["loader"])
    if not files:
        print("  dependencies: (no files for this pack.toml Minecraft/loader)")
        return
    chosen = files[0]
    print(
        f"  matching file: {chosen.get('displayName') or chosen.get('fileName')} "
        f"(file-id {chosen.get('id')}) {chosen.get('fileDate')}"
    )
    deps = chosen.get("dependencies") or []
    if not deps:
        print("  dependencies: none listed")
        return
    print("  dependencies:")
    for dep in deps:
        if not isinstance(dep, dict):
            continue
        kind = CF_RELATION.get(int(dep.get("relationType") or 0), str(dep.get("relationType")))
        print(f"    - {kind}: modId {dep.get('modId')}")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    load_env_file(ROOT / ".env")
    parser = argparse.ArgumentParser(
        description="Look up a CurseForge/Modrinth slug for minecraft-modding research."
    )
    parser.add_argument("slug", help="project slug on CurseForge and/or Modrinth")
    args = parser.parse_args()
    pack = read_pack(PACK_TOML)
    print(
        f"pack.toml {pack['minecraft']} {pack['loader']} {pack['loader_version']} "
        f"(filter matching files against this)"
    )
    print_curseforge(args.slug, pack)
    print_modrinth(args.slug, pack)


if __name__ == "__main__":
    main()
