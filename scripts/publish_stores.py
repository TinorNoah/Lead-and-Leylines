#!/usr/bin/env python3
"""Upload pack artifacts to GitHub Releases, CurseForge, and Modrinth.

Never print tokens or project secrets. GitHub Release body is the changelog
the operator passed in — do not append server or hosting details.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import multipart
from resolve_modrinth_project import USER_AGENT, resolve

GITHUB_API = "https://api.github.com"
CURSEFORGE_UPLOAD = "https://minecraft.curseforge.com/api"
MODRINTH_API = "https://api.modrinth.com/v2"


def _read_error(exc: urllib.error.HTTPError) -> str:
    detail = exc.read().decode("utf-8", errors="replace")
    return detail[:4000]


def _request(
    url: str,
    *,
    method: str = "GET",
    headers: dict[str, str] | None = None,
    data: bytes | None = None,
    timeout: int = 120,
) -> Any:
    request = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read()
            if not payload:
                return None
            content = response.headers.get("Content-Type") or ""
            if "json" in content or payload[:1] in (b"{", b"["):
                return json.loads(payload.decode("utf-8"))
            return payload
    except urllib.error.HTTPError as exc:
        raise SystemExit(
            f"{method} {url} failed: HTTP {exc.code}\n{_read_error(exc)}"
        ) from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"{method} {url} failed: {exc}") from exc


def github_headers(token: str) -> dict[str, str]:
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }


def create_github_release(
    *,
    owner: str,
    repo: str,
    tag: str,
    name: str,
    body: str,
    token: str,
    target: str,
    prerelease: bool,
) -> tuple[str, int]:
    payload = _request(
        f"{GITHUB_API}/repos/{owner}/{repo}/releases",
        method="POST",
        headers={**github_headers(token), "Content-Type": "application/json"},
        data=json.dumps(
            {
                "tag_name": tag,
                "target_commitish": target,
                "name": name,
                "body": body,
                "draft": False,
                "prerelease": prerelease,
            }
        ).encode("utf-8"),
    )
    if not isinstance(payload, dict) or not payload.get("html_url") or not payload.get("id"):
        raise SystemExit("GitHub did not return a release URL")
    return str(payload["html_url"]), int(payload["id"])


def upload_github_asset(
    *,
    owner: str,
    repo: str,
    release_id: int,
    path: Path,
    token: str,
) -> None:
    query = urllib.parse.urlencode({"name": path.name})
    url = (
        f"https://uploads.github.com/repos/{owner}/{repo}/releases/"
        f"{release_id}/assets?{query}"
    )
    content_type = "application/zip" if path.suffix == ".zip" else "application/octet-stream"
    _request(
        url,
        method="POST",
        headers={
            **github_headers(token),
            "Content-Type": content_type,
        },
        data=path.read_bytes(),
        timeout=max(120, 60 + path.stat().st_size // 50_000),
    )
    print(f"github asset {path.name}")


def github_release_by_tag(
    *,
    owner: str,
    repo: str,
    tag: str,
    token: str,
) -> dict[str, Any]:
    payload = _request(
        f"{GITHUB_API}/repos/{owner}/{repo}/releases/tags/{urllib.parse.quote(tag)}",
        headers=github_headers(token),
    )
    if not isinstance(payload, dict) or not payload.get("id"):
        raise SystemExit(f"GitHub has no release for tag {tag}")
    return payload


def delete_github_asset(
    *,
    owner: str,
    repo: str,
    asset_id: int,
    token: str,
) -> None:
    _request(
        f"{GITHUB_API}/repos/{owner}/{repo}/releases/assets/{asset_id}",
        method="DELETE",
        headers=github_headers(token),
    )


def github_download_url(*, owner: str, repo: str, tag: str, filename: str) -> str:
    return (
        f"https://github.com/{owner}/{repo}/releases/download/"
        f"{urllib.parse.quote(tag)}/{urllib.parse.quote(filename)}"
    )


def replace_github_release_asset(
    *,
    owner: str,
    repo: str,
    tag: str,
    path: Path,
    token: str,
) -> str:
    release = github_release_by_tag(owner=owner, repo=repo, tag=tag, token=token)
    release_id = int(release["id"])
    for asset in release.get("assets") or []:
        if not isinstance(asset, dict):
            continue
        if str(asset.get("name") or "") != path.name:
            continue
        delete_github_asset(
            owner=owner, repo=repo, asset_id=int(asset["id"]), token=token
        )
        print(f"github replaced {path.name}")
        break
    upload_github_asset(
        owner=owner, repo=repo, release_id=release_id, path=path, token=token
    )
    return github_download_url(owner=owner, repo=repo, tag=tag, filename=path.name)


def curseforge_minecraft_version_ids(token: str, minecraft: str) -> list[int]:
    payload = _request(
        f"{CURSEFORGE_UPLOAD}/game/versions",
        headers={"X-Api-Token": token, "User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    if not isinstance(payload, list):
        raise SystemExit("CurseForge game versions response was not a list")
    ids = [
        int(item["id"])
        for item in payload
        if isinstance(item, dict) and str(item.get("name") or "") == minecraft
    ]
    if not ids:
        raise SystemExit(f"CurseForge has no game version named {minecraft!r}")
    return ids


def upload_curseforge(
    *,
    project_id: str,
    token: str,
    zip_path: Path,
    name: str,
    changelog: str,
    minecraft: str,
    channel: str,
) -> None:
    version_ids = curseforge_minecraft_version_ids(token, minecraft)
    metadata = json.dumps(
        {
            "changelog": changelog,
            "changelogType": "markdown",
            "displayName": name,
            "gameVersions": version_ids,
            "releaseType": channel,
        }
    ).encode("utf-8")
    body, content_type = multipart.encode(
        [
            ("metadata", metadata, None, "application/json"),
            ("file", zip_path.read_bytes(), zip_path.name, "application/zip"),
        ]
    )
    payload = _request(
        f"{CURSEFORGE_UPLOAD}/projects/{urllib.parse.quote(project_id)}/upload-file",
        method="POST",
        headers={
            "X-Api-Token": token,
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
            "Content-Type": content_type,
        },
        data=body,
        timeout=max(180, 60 + zip_path.stat().st_size // 50_000),
    )
    file_id = payload.get("id") if isinstance(payload, dict) else None
    print(f"curseforge file {file_id or zip_path.name}")


def upload_modrinth(
    *,
    project: str,
    token: str,
    mrpack: Path,
    name: str,
    version: str,
    changelog: str,
    minecraft: str,
    loader: str,
    channel: str,
) -> None:
    resolved, reason = resolve(project, token)
    if not resolved:
        print(f"Modrinth upload skipped: {reason}")
        return
    data = json.dumps(
        {
            "name": name,
            "version_number": version,
            "changelog": changelog,
            "dependencies": [],
            "game_versions": [minecraft],
            "version_type": channel,
            "loaders": [loader],
            "featured": True,
            "status": "listed",
            "project_id": resolved,
            "file_parts": ["file"],
            "primary_file": "file",
            "environment": "client_and_server",
        }
    ).encode("utf-8")
    body, content_type = multipart.encode(
        [
            ("data", data, None, "application/json"),
            ("file", mrpack.read_bytes(), mrpack.name, "application/x-modrinth-modpack+zip"),
        ]
    )
    payload = _request(
        f"{MODRINTH_API}/version",
        method="POST",
        headers={
            "Authorization": token,
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
            "Content-Type": content_type,
        },
        data=body,
        timeout=max(180, 60 + mrpack.stat().st_size // 50_000),
    )
    version_id = payload.get("id") if isinstance(payload, dict) else None
    print(f"modrinth version {version_id or mrpack.name} ({reason})")
