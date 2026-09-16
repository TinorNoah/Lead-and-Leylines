#!/usr/bin/env python3
"""Upload pack artifacts to GitHub Releases, CurseForge, and Modrinth.

Never print tokens or project secrets. GitHub Release body is the changelog
the operator passed in — do not append server or hosting details.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
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


def curseforge_version_types(token: str) -> dict[int, str]:
    payload = _request(
        f"{CURSEFORGE_UPLOAD}/game/version-types",
        headers={"X-Api-Token": token, "User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    if not isinstance(payload, list):
        raise SystemExit("CurseForge game version types response was not a list")
    types: dict[int, str] = {}
    for item in payload:
        if not isinstance(item, dict) or "id" not in item:
            continue
        types[int(item["id"])] = str(item.get("name") or "")
    if not types:
        raise SystemExit("CurseForge returned no game version types")
    return types


def curseforge_game_version_ids(
    token: str,
    minecraft: str,
    loader: str,
) -> list[int]:
    types = curseforge_version_types(token)
    payload = _request(
        f"{CURSEFORGE_UPLOAD}/game/versions",
        headers={"X-Api-Token": token, "User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    if not isinstance(payload, list):
        raise SystemExit("CurseForge game versions response was not a list")
    family = ".".join(minecraft.split(".")[:2])
    slug = minecraft.replace(".", "-")
    minecraft_hits: list[tuple[int, str]] = []
    loader_ids: list[int] = []
    environment_ids: list[int] = []
    for item in payload:
        if not isinstance(item, dict) or "id" not in item:
            continue
        type_id = int(item.get("gameVersionTypeID") or 0)
        type_name = types.get(type_id, "")
        if type_id not in types:
            continue
        version_id = int(item["id"])
        name = str(item.get("name") or "")
        item_slug = str(item.get("slug") or "")
        if name == minecraft and (not item_slug or item_slug in {slug, minecraft}):
            minecraft_hits.append((version_id, type_name))
        elif name.lower() == loader.lower():
            loader_ids.append(version_id)
        elif name in {"Client", "Server"}:
            environment_ids.append(version_id)

    def minecraft_rank(hit: tuple[int, str]) -> tuple[int, int, int]:
        type_name = hit[1].lower()
        return (
            int(type_name.startswith("minecraft")),
            int(family in type_name),
            len(type_name),
        )

    minecraft_hits.sort(key=minecraft_rank, reverse=True)
    minecraft_ids = [minecraft_hits[0][0]] if minecraft_hits else []
    loader_ids = list(dict.fromkeys(loader_ids))
    environment_ids = list(dict.fromkeys(environment_ids))
    if len(minecraft_ids) != 1:
        raise SystemExit(
            f"CurseForge expected one {minecraft!r} game version, found "
            f"{[(hit[0], hit[1]) for hit in minecraft_hits]}"
        )
    if len(loader_ids) != 1:
        raise SystemExit(
            f"CurseForge expected one {loader!r} loader version, found {loader_ids}"
        )
    if len(environment_ids) != 2:
        raise SystemExit(
            "CurseForge expected Client and Server environments, "
            f"found {environment_ids}"
        )
    chosen = minecraft_ids + loader_ids + environment_ids
    print(f"curseforge gameVersions {chosen}")
    return chosen


def upload_curseforge(
    *,
    project_id: str,
    token: str,
    zip_path: Path,
    name: str,
    changelog: str,
    minecraft: str,
    loader: str,
    channel: str,
    parent_file_id: int | None = None,
) -> int:
    metadata: dict[str, Any] = {
        "changelog": changelog,
        "changelogType": "markdown",
        "displayName": name,
        "releaseType": channel,
    }
    if parent_file_id is not None:
        metadata["parentFileID"] = parent_file_id
    else:
        metadata["gameVersions"] = curseforge_game_version_ids(
            token, minecraft, loader
        )
    body, content_type = multipart.encode(
        [
            ("metadata", json.dumps(metadata).encode("utf-8"), None, "application/json"),
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
    if not file_id:
        raise SystemExit(f"CurseForge did not return a file id for {zip_path.name}")
    print(f"curseforge file {file_id} ({zip_path.name})")
    return int(file_id)


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
    server_zip: Path | None = None,
) -> None:
    resolved, reason = resolve(project, token)
    if not resolved:
        print(f"Modrinth upload skipped: {reason}")
        return
    fields = [
        (
            "client",
            mrpack.read_bytes(),
            mrpack.name,
            "application/x-modrinth-modpack+zip",
        )
    ]
    file_parts = ["client"]
    total_size = mrpack.stat().st_size
    if server_zip is not None:
        fields.append(
            ("server", server_zip.read_bytes(), server_zip.name, "application/zip")
        )
        file_parts.append("server")
        total_size += server_zip.stat().st_size
    data = json.dumps(
        {
            "name": name,
            "version_number": version,
            "changelog": changelog,
            "dependencies": [],
            "game_versions": [minecraft],
            "version_type": channel,
            "loaders": [loader],
            "featured": channel == "release",
            "status": "listed",
            "project_id": resolved,
            "file_parts": file_parts,
            "primary_file": "client",
            "environment": "client_and_server",
        }
    ).encode("utf-8")
    body, content_type = multipart.encode(
        [("data", data, None, "application/json"), *fields]
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
        timeout=max(180, 60 + total_size // 50_000),
    )
    version_id = payload.get("id") if isinstance(payload, dict) else None
    extra = f" + {server_zip.name}" if server_zip is not None else ""
    print(f"modrinth version {version_id or mrpack.name}{extra} ({reason})")


def dispatch_store_publish(
    *,
    owner: str,
    repo: str,
    tag: str,
    channel: str,
    token: str,
    skip_curseforge: bool = False,
    skip_modrinth: bool = False,
) -> None:
    inputs = {"tag": tag, "channel": channel}
    if skip_curseforge:
        inputs["skip_curseforge"] = "true"
    if skip_modrinth:
        inputs["skip_modrinth"] = "true"
    _request(
        f"{GITHUB_API}/repos/{owner}/{repo}/actions/workflows/publish-stores.yml/dispatches",
        method="POST",
        headers={**github_headers(token), "Content-Type": "application/json"},
        data=json.dumps({"ref": "main", "inputs": inputs}).encode("utf-8"),
    )
    print(f"store publish dispatched for {tag} as {channel}")


def wait_for_store_publish(
    *,
    owner: str,
    repo: str,
    tag: str,
    token: str,
    timeout_s: int = 2700,
) -> str:
    started = datetime.now(timezone.utc) - timedelta(seconds=20)
    deadline = time.time() + timeout_s
    run_id: int | None = None
    expected = f"Publish stores {tag}"
    while time.time() < deadline:
        payload = _request(
            f"{GITHUB_API}/repos/{owner}/{repo}/actions/workflows/"
            "publish-stores.yml/runs?event=workflow_dispatch&per_page=10",
            headers=github_headers(token),
        )
        runs = payload.get("workflow_runs") if isinstance(payload, dict) else None
        if not run_id:
            for run in runs or []:
                if not isinstance(run, dict):
                    continue
                name = str(run.get("display_title") or run.get("name") or "")
                created_raw = str(run.get("created_at") or "")
                if expected not in name:
                    continue
                created = datetime.fromisoformat(created_raw.replace("Z", "+00:00"))
                if created < started:
                    continue
                run_id = int(run["id"])
                url = str(run.get("html_url") or "")
                print(f"store publish {url}")
                break
        if run_id:
            run = _request(
                f"{GITHUB_API}/repos/{owner}/{repo}/actions/runs/{run_id}",
                headers=github_headers(token),
            )
            if not isinstance(run, dict):
                raise SystemExit("GitHub Actions run payload was not an object")
            status = str(run.get("status") or "")
            conclusion = str(run.get("conclusion") or "")
            url = str(run.get("html_url") or "")
            if status == "completed":
                if conclusion != "success":
                    raise SystemExit(f"store publish {conclusion}: {url}")
                print(f"store publish {conclusion} {url}")
                return url
        time.sleep(20)
    raise SystemExit(f"timed out waiting for store publish of {tag}")
