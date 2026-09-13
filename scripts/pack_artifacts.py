#!/usr/bin/env python3
"""Build local pack artifacts for ATLauncher and the test server."""

from __future__ import annotations

import shutil
import subprocess
import tomllib
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from read_pack_versions import PACK_TOML, ROOT, read_pack

PACK_DIR = ROOT / "pack"
MODS_DIR = PACK_DIR / "mods"
CONFIG_DIR = PACK_DIR / "config"
DIST_DIR = ROOT / "dist"
USER_AGENT = "LeadAndLeylines-deploy/1.0 (packwiz local share)"


def slug_name(pack: dict[str, str]) -> str:
    return pack["name"].replace(" ", "-")


def dist_paths(pack: dict[str, str]) -> dict[str, Path]:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    base = f"{slug_name(pack)}-{pack['pack_version']}"
    return {
        "client_zip": DIST_DIR / f"{base}.zip",
        "mrpack": DIST_DIR / f"{base}.mrpack",
        "server_zip": DIST_DIR / f"{base}-server-mods.zip",
    }


def run_packwiz(*args: str) -> None:
    command = ["packwiz", *args]
    result = subprocess.run(command, cwd=PACK_DIR, check=False)
    if result.returncode != 0:
        raise SystemExit(f"packwiz {' '.join(args)} failed with exit {result.returncode}")


def export_client_artifacts(pack: dict[str, str]) -> dict[str, Path]:
    paths = dist_paths(pack)
    print("packwiz refresh")
    run_packwiz("refresh")
    print(f"exporting ATLauncher CurseForge zip -> {paths['client_zip'].name}")
    run_packwiz("curseforge", "export", "-y", "-o", str(paths["client_zip"]))
    print(f"exporting ATLauncher mrpack -> {paths['mrpack'].name}")
    run_packwiz(
        "modrinth",
        "export",
        "-y",
        "--restrictDomains=false",
        "-o",
        str(paths["mrpack"]),
    )
    return paths


def _mod_meta(path: Path) -> dict[str, str]:
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    download = data.get("download") or {}
    update = data.get("update") or {}
    curseforge = update.get("curseforge") or {}
    filename = str(data.get("filename") or "")
    url = str(download.get("url") or "")
    if not url and curseforge.get("file-id"):
        file_id = int(curseforge["file-id"])
        url = (
            "https://mediafilez.forgecdn.net/files/"
            f"{file_id // 1000}/{file_id % 1000}/"
            f"{urllib.parse.quote(filename)}"
        )
    return {
        "name": str(data.get("name") or path.stem),
        "side": str(data.get("side") or "both").lower(),
        "filename": filename,
        "url": url,
    }


def _download(url: str, dest: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            dest.write_bytes(response.read())
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"download failed for {dest.name}: HTTP {exc.code} {url}") from exc


def build_server_mods_zip(pack: dict[str, str], dest: Path) -> Path:
    work = DIST_DIR / "_server-build"
    if work.exists():
        shutil.rmtree(work)
    mods_out = work / "mods"
    mods_out.mkdir(parents=True)

    included = 0
    skipped_client = 0
    for toml_path in sorted(MODS_DIR.glob("*.pw.toml")):
        meta = _mod_meta(toml_path)
        if meta["side"] == "client":
            skipped_client += 1
            continue
        if not meta["url"] or not meta["filename"]:
            raise SystemExit(f"{toml_path.name} is missing download url or filename")
        print(f"  server mod {meta['filename']}")
        _download(meta["url"], mods_out / meta["filename"])
        included += 1

    if CONFIG_DIR.is_dir():
        copied = False
        for item in CONFIG_DIR.iterdir():
            if item.name.startswith("."):
                continue
            target = work / "config" / item.name
            target.parent.mkdir(parents=True, exist_ok=True)
            if item.is_dir():
                shutil.copytree(item, target, dirs_exist_ok=True)
            else:
                shutil.copy2(item, target)
            copied = True
        if copied:
            print("  copied pack/config into server zip")

    if included == 0:
        raise SystemExit("no server/both mods found to zip")

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in work.rglob("*"):
            if file_path.is_file():
                archive.write(file_path, file_path.relative_to(work).as_posix())
    shutil.rmtree(work)
    print(
        f"server mods zip {dest.name} ({included} jars, skipped {skipped_client} client-only)"
    )
    return dest


def atlauncher_instructions(paths: dict[str, Path]) -> str:
    zip_path = paths["client_zip"]
    mrpack_path = paths["mrpack"]
    return (
        "ATLauncher (friends):\n"
        "  1. Send them the .mrpack (preferred) or the .zip from dist/.\n"
        f"     {mrpack_path}\n"
        f"     {zip_path}\n"
        "  2. Instances tab -> Import -> Browse -> select that file -> Import.\n"
        "  3. Name the instance and click Install, then Play.\n"
        "  CurseForge/Modrinth search will not find this pack until those listings are public."
    )


def build_all() -> tuple[dict[str, str], dict[str, Path]]:
    pack = read_pack(PACK_TOML)
    paths = export_client_artifacts(pack)
    build_server_mods_zip(pack, paths["server_zip"])
    return pack, paths
