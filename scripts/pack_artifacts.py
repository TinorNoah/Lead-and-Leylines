#!/usr/bin/env python3
"""Build local pack artifacts for ATLauncher and the test server."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tomllib
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from check_exports import print_report, report_embedded_mods
from read_pack_versions import PACK_TOML, ROOT, read_pack

PACK_DIR = ROOT / "pack"
MODS_DIR = PACK_DIR / "mods"
CONFIG_DIR = PACK_DIR / "config"
GLOBAL_PACKS_DIR = PACK_DIR / "global_packs"
# Instance folders that are not mods/: Point Blank zips, TaCZ gun-pack jars.
SIDED_FOLDERS = ("pointblank", "tacz")
DIST_DIR = ROOT / "dist"
LOCAL_MOD_CACHE = ROOT / ".cache" / "mod-files"
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
    findings = report_embedded_mods(paths["client_zip"], paths["mrpack"])
    print_report(findings)
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
        "hash": str(download.get("hash") or ""),
        "hash_format": str(download.get("hash-format") or ""),
    }


def _user_cache_dir() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Caches"
    if sys.platform == "win32":
        return Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData" / "Local")))
    return Path(os.environ.get("XDG_CACHE_HOME", str(Path.home() / ".cache")))


def packwiz_cache_dir() -> Path:
    override = os.environ.get("PACKWIZ_CACHE")
    if override:
        return Path(override)
    return _user_cache_dir() / "packwiz" / "cache"


def _algo_for(hash_format: str, file_hash: str) -> str | None:
    name = hash_format.lower().replace("-", "")
    if name in {"sha1", "sha256", "sha512"}:
        return name
    length = len(file_hash)
    if length == 40:
        return "sha1"
    if length == 64:
        return "sha256"
    if length == 128:
        return "sha512"
    return None


def _file_digest(path: Path, algo: str) -> str:
    hasher = hashlib.new(algo)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _hash_matches(path: Path, file_hash: str, hash_format: str) -> bool:
    if not file_hash or not path.is_file() or path.stat().st_size <= 0:
        return False
    algo = _algo_for(hash_format, file_hash)
    if algo is None:
        return False
    return _file_digest(path, algo) == file_hash.lower()


def _load_packwiz_index(cache: Path) -> dict[str, Path]:
    index_path = cache / "index.json"
    if not index_path.is_file():
        return {}
    data = json.loads(index_path.read_text())
    hashes = data.get("Hashes") or {}
    sha256s = hashes.get("sha256") or []
    lengths = hashes.get("length-bytes") or []
    found: dict[str, Path] = {}
    for algo in ("sha1", "sha256", "sha512"):
        for index, value in enumerate(hashes.get(algo) or []):
            if not value or index >= len(sha256s) or not sha256s[index]:
                continue
            digest = str(sha256s[index])
            # Packwiz stores <hash[:2]>/<hash[2:]>, not the full hash as the filename.
            path = cache / digest[:2] / digest[2:]
            if not path.is_file() or path.stat().st_size <= 0:
                continue
            if index < len(lengths) and str(lengths[index]) not in {"", "None"}:
                try:
                    expected = int(lengths[index])
                except (TypeError, ValueError):
                    expected = 0
                if expected and path.stat().st_size != expected:
                    continue
            found[str(value).lower()] = path
    return found


class ModFileCache:
    """Reuse packwiz's content cache, then jars this repo downloaded earlier."""

    def __init__(
        self,
        packwiz_cache: Path | None = None,
        local_cache: Path | None = None,
    ) -> None:
        self.packwiz_cache = packwiz_cache if packwiz_cache is not None else packwiz_cache_dir()
        self.local_cache = local_cache if local_cache is not None else LOCAL_MOD_CACHE
        self._index: dict[str, Path] | None = None

    def index(self) -> dict[str, Path]:
        if self._index is None:
            self._index = _load_packwiz_index(self.packwiz_cache)
        return self._index

    def find(self, filename: str, file_hash: str, hash_format: str) -> Path | None:
        digest = file_hash.lower()
        if digest:
            local = self.local_cache / digest
            if _hash_matches(local, digest, hash_format):
                return local
            indexed = self.index().get(digest)
            if indexed is not None:
                return indexed
        imported = self.packwiz_cache / "import" / filename
        if imported.is_file() and (
            not digest or _hash_matches(imported, digest, hash_format)
        ):
            return imported
        return None

    def remember(self, file_hash: str, hash_format: str, src: Path) -> None:
        digest = file_hash.lower()
        if not digest or _algo_for(hash_format, digest) is None:
            return
        if not _hash_matches(src, digest, hash_format):
            src.unlink(missing_ok=True)
            raise SystemExit(f"hash mismatch for {src.name}")
        dest = self.local_cache / digest
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copyfile(src, dest)


def _download(url: str, dest: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            dest.write_bytes(response.read())
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"download failed for {dest.name}: HTTP {exc.code} {url}") from exc


def _place_cached(src: Path, dest: Path) -> None:
    try:
        os.link(src, dest)
    except OSError:
        shutil.copyfile(src, dest)


def _copy_or_download(cache: ModFileCache, meta: dict[str, str], dest: Path) -> bool:
    """Place a cached file at dest. Return True when a download was required."""
    cached = cache.find(meta["filename"], meta["hash"], meta["hash_format"])
    if cached is not None:
        _place_cached(cached, dest)
        return False
    print(f"  download {meta['filename']}")
    _download(meta["url"], dest)
    cache.remember(meta["hash"], meta["hash_format"], dest)
    return True


def build_server_mods_zip(pack: dict[str, str], dest: Path) -> Path:
    work = DIST_DIR / "_server-build"
    if work.exists():
        shutil.rmtree(work)
    mods_out = work / "mods"
    mods_out.mkdir(parents=True)

    cache = ModFileCache()
    included = 0
    skipped_client = 0
    extra = 0
    downloaded = 0
    for toml_path in sorted(MODS_DIR.glob("*.pw.toml")):
        meta = _mod_meta(toml_path)
        if meta["side"] == "client":
            skipped_client += 1
            continue
        if not meta["url"] or not meta["filename"]:
            raise SystemExit(f"{toml_path.name} is missing download url or filename")
        if _copy_or_download(cache, meta, mods_out / meta["filename"]):
            downloaded += 1
        included += 1

    for folder in SIDED_FOLDERS:
        source = PACK_DIR / folder
        if not source.is_dir():
            continue
        out = work / folder
        out.mkdir(parents=True, exist_ok=True)
        for toml_path in sorted(source.glob("*.pw.toml")):
            meta = _mod_meta(toml_path)
            if meta["side"] == "client":
                skipped_client += 1
                continue
            if not meta["url"] or not meta["filename"]:
                raise SystemExit(f"{toml_path.name} is missing download url or filename")
            if _copy_or_download(cache, meta, out / meta["filename"]):
                downloaded += 1
            extra += 1

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

    if GLOBAL_PACKS_DIR.is_dir():
        shutil.copytree(GLOBAL_PACKS_DIR, work / "global_packs", dirs_exist_ok=True)
        print("  copied pack/global_packs into server zip")

    if included == 0:
        print("  no server/both mods; writing an empty server-mods zip")

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in work.rglob("*"):
            if file_path.is_file():
                archive.write(file_path, file_path.relative_to(work).as_posix())
    shutil.rmtree(work)
    print(
        f"server mods zip {dest.name} ({included} jars, {extra} pack files, "
        f"skipped {skipped_client} client-only, "
        f"{included + extra - downloaded} cached, {downloaded} downloaded)"
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
        "  3. Name the instance and click Install.\n"
        "  4. Set that instance's Java arguments to -XX:+UseZGC (pack/user_jvm_args.txt).\n"
        "  5. Play.\n"
        "  CurseForge search will not find this pack until that listing is public."
    )


def build_all() -> tuple[dict[str, str], dict[str, Path]]:
    pack = read_pack(PACK_TOML)
    paths = export_client_artifacts(pack)
    build_server_mods_zip(pack, paths["server_zip"])
    return pack, paths
