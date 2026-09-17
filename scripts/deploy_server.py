#!/usr/bin/env python3
"""Create or update the Lead and Leylines test server on the dedicated server.

Uses the Application API (papp_ keys). Never prints API tokens or CurseForge keys.
Secrets come from the environment or a gitignored .env — not from git.
"""

from __future__ import annotations

import argparse
import json
import os
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from envfile import load_env_file
from pack_artifacts import atlauncher_instructions, build_all
from publish_stores import replace_github_release_asset
from wings import Wings, node_configuration, wings_base_url
from read_pack_versions import PACK_TOML, read_pack

CURSEFORGE_GENERIC_UUID = "019bbf16-a3f3-470a-9c0b-f3995b5e032a"
CURSEFORGE_GENERIC_NAME = "CurseForge Generic"
NEOFORGE_EGG_UUID = "e23e092f-b803-4f34-82cf-2d6518c6351a"
NEOFORGE_EGG_NAME = "NeoForge"
SERVER_MODS_REMOTE = "lead-and-leylines-server-mods.zip"
NEOFORGE_STARTUP = "bash run.sh"
DEFAULT_NODE_NAME = "node"
DEFAULT_EXTERNAL_ID = "lead-and-leylines"
SECRET_MARKERS = ("KEY", "TOKEN", "SECRET", "PASSWORD", "AUTHORIZATION")


def env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def require_env(name: str) -> str:
    value = env(name)
    if not value:
        raise SystemExit(f"missing {name} (set it in .env, never commit that file)")
    return value


def attrs(item: dict[str, Any]) -> dict[str, Any]:
    if "attributes" in item and isinstance(item["attributes"], dict):
        return item["attributes"]
    return item


def redact(value: Any) -> Any:
    if isinstance(value, dict):
        out = {}
        for key, inner in value.items():
            if any(marker in str(key).upper() for marker in SECRET_MARKERS):
                out[key] = f"<redacted len={len(str(inner))}>"
            else:
                out[key] = redact(inner)
        return out
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value


def java_label(minecraft: str) -> str:
    """Pick the egg Java image label from the Minecraft version in pack.toml."""
    parts = minecraft.split(".")
    try:
        minor = int(parts[1]) if len(parts) > 1 else 0
    except ValueError as exc:
        raise SystemExit(f"unreadable Minecraft version {minecraft!r}") from exc
    if minor >= 21:
        return "Java 21"
    if minor >= 18:
        return "Java 17"
    if minor >= 17:
        return "Java 16"
    if minor >= 13:
        return "Java 11"
    return "Java 8"


class PanelClient:
    def __init__(self, base: str, token: str, timeout: int = 60) -> None:
        self.base = base.rstrip("/")
        self.token = token
        self.timeout = timeout
        self.ssl = ssl.create_default_context()

    def request(
        self,
        method: str,
        path: str,
        query: dict[str, Any] | None = None,
        body: Any | None = None,
        content_type: str | None = None,
        raw_body: bytes | None = None,
    ) -> Any:
        url = self.base + path
        if query:
            url += "?" + urllib.parse.urlencode(
                {key: value for key, value in query.items() if value is not None}
            )
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "User-Agent": "lead-and-leylines-deploy/1.0",
        }
        data = raw_body
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = content_type or "application/json"
        elif raw_body is not None:
            headers["Content-Type"] = content_type or "application/json"
        request = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, context=self.ssl, timeout=self.timeout) as response:
                payload = response.read()
                if not payload:
                    return None
                if "json" in (response.headers.get("Content-Type") or ""):
                    return json.loads(payload.decode("utf-8"))
                return payload.decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            try:
                parsed = json.loads(detail)
                detail = json.dumps(redact(parsed), indent=2)
            except json.JSONDecodeError:
                pass
            raise SystemExit(f"the panel {method} {path} failed: HTTP {exc.code}\n{detail}") from exc
        except urllib.error.URLError as exc:
            raise SystemExit(f"the panel {method} {path} failed: {exc}") from exc

    def get(self, path: str, query: dict[str, Any] | None = None) -> Any:
        return self.request("GET", path, query=query)

    def post(self, path: str, body: Any | None = None, **kwargs: Any) -> Any:
        return self.request("POST", path, body=body, **kwargs)

    def patch(self, path: str, body: Any) -> Any:
        return self.request("PATCH", path, body=body)

    def paginate(self, path: str, query: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        page = 1
        params = dict(query or {})
        while True:
            params["page"] = page
            params.setdefault("per_page", 100)
            payload = self.get(path, params)
            chunk = payload.get("data") if isinstance(payload, dict) else payload
            if not isinstance(chunk, list):
                raise SystemExit(f"unexpected list payload from {path}")
            items.extend(chunk)
            meta = (payload.get("meta") or {}).get("pagination") or {}
            total_pages = int(meta.get("total_pages") or 1)
            if page >= total_pages:
                return items
            page += 1


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "lead-and-leylines-deploy/1.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def find_node(client: PanelClient, fqdn: str, name: str) -> dict[str, Any]:
    nodes = [attrs(item) for item in client.paginate("/api/application/nodes")]
    fqdn_l = fqdn.lower()
    name_l = name.lower()
    for node in nodes:
        if str(node.get("fqdn") or "").lower() == fqdn_l:
            return node
    for node in nodes:
        if str(node.get("name") or "").lower() == name_l:
            return node
    listing = ", ".join(
        f"{node.get('name')} ({node.get('fqdn')})" for node in nodes
    ) or "(none)"
    raise SystemExit(f"no the panel node matching fqdn={fqdn!r} or name={name!r}; have: {listing}")


def find_egg_by(client: PanelClient, uuid: str, name: str) -> dict[str, Any] | None:
    uuid_l = uuid.lower()
    name_l = name.lower()
    for item in client.paginate("/api/application/eggs"):
        egg = attrs(item)
        if str(egg.get("uuid") or "").lower() == uuid_l:
            return egg
        if str(egg.get("name") or "").lower() == name_l:
            return egg
    return None


def find_egg(client: PanelClient) -> dict[str, Any] | None:
    return find_egg_by(client, CURSEFORGE_GENERIC_UUID, CURSEFORGE_GENERIC_NAME)


def find_neoforge_egg(client: PanelClient) -> dict[str, Any] | None:
    return find_egg_by(client, NEOFORGE_EGG_UUID, NEOFORGE_EGG_NAME)


def egg_with_variables(client: PanelClient, egg_id: int) -> dict[str, Any]:
    return attrs(client.get(f"/api/application/eggs/{egg_id}", {"include": "variables"}))


def environment_from_egg(egg: dict[str, Any], overrides: dict[str, str]) -> dict[str, str]:
    values: dict[str, str] = {}
    rel = (egg.get("relationships") or {}).get("variables") or {}
    for raw in rel.get("data") or []:
        variable = attrs(raw)
        key = variable.get("env_variable")
        if key:
            values[str(key)] = str(variable.get("default_value") or "")
    values.update(overrides)
    return values


def neoforge_environment(pack: dict[str, str]) -> dict[str, str]:
    if pack["loader"].lower() != "neoforge":
        raise SystemExit(
            f"local panel deploy expects NeoForge; pack.toml loader is {pack['loader']!r}"
        )
    return {
        "MC_VERSION": pack["minecraft"],
        "NEOFORGE_VERSION": pack["loader_version"],
        "SERVER_JARFILE": "server.jar",
    }


def import_egg(client: PanelClient) -> dict[str, Any]:
    egg_url = require_env("EGG_IMPORT_URL")
    print("importing missing egg")
    egg_json = fetch_json(egg_url)
    created = client.post(
        "/api/application/eggs/import",
        raw_body=json.dumps(egg_json).encode("utf-8"),
        content_type="application/json",
    )
    egg = attrs(created.get("attributes", created) if isinstance(created, dict) else created)
    if "attributes" in created:
        egg = attrs(created)
    else:
        data = created.get("data") if isinstance(created, dict) else created
        egg = attrs(data) if isinstance(data, dict) else egg
    print(f"imported egg id={egg.get('id')} name={egg.get('name')}")
    return egg


def find_owner(client: PanelClient, username: str) -> dict[str, Any]:
    users = [attrs(item) for item in client.paginate("/api/application/users")]
    wanted = username.lower()
    for user in users:
        if str(user.get("username") or "").lower() == wanted:
            return user
        if str(user.get("email") or "").lower() == wanted:
            return user
    listing = ", ".join(str(user.get("username")) for user in users) or "(none)"
    raise SystemExit(f"no the panel user matching {username!r}; have: {listing}")


def find_server(
    client: PanelClient, external_id: str, name: str
) -> dict[str, Any] | None:
    try:
        payload = client.get(f"/api/application/servers/external/{urllib.parse.quote(external_id)}")
        if payload:
            return attrs(payload if "attributes" in payload else payload.get("data", payload))
    except SystemExit as exc:
        if "HTTP 404" not in str(exc):
            raise
    wanted = name.lower()
    for item in client.paginate("/api/application/servers"):
        server = attrs(item)
        if str(server.get("external_id") or "") == external_id:
            return server
        if str(server.get("name") or "").lower() == wanted:
            return server
    return None


def pick_allocation(
    client: PanelClient, node_id: int, port: str | None
) -> dict[str, Any]:
    allocations = [
        attrs(item)
        for item in client.paginate(f"/api/application/nodes/{node_id}/allocations")
    ]
    free = [item for item in allocations if not item.get("assigned") and not item.get("server_id")]
    if port:
        wanted = int(port)
        for item in free:
            if int(item.get("port") or 0) == wanted:
                return item
        raise SystemExit(f"no free allocation on node {node_id} for port {wanted}")
    if not free:
        raise SystemExit(f"node {node_id} has no free allocations")
    return free[0]


def copy_curseforge_api_key(client: PanelClient, egg_id: int) -> str | None:
    for item in client.paginate("/api/application/servers"):
        server = attrs(item)
        if int(server.get("egg") or 0) != egg_id:
            continue
        detail = attrs(
            client.get(f"/api/application/servers/{server['id']}")
        )
        environment = (detail.get("container") or {}).get("environment") or {}
        key = str(environment.get("API_KEY") or "").strip()
        if key:
            print(
                f"using CurseForge console key already stored on the dedicated server server {server.get('name')!r}"
            )
            return key
    return None


def docker_image(egg: dict[str, Any], minecraft: str) -> str:
    images = egg.get("docker_images") or {}
    if not isinstance(images, dict) or not images:
        raise SystemExit(f"egg {egg.get('name')} has no docker_images")
    label = java_label(minecraft)
    if label in images:
        return str(images[label])
    raise SystemExit(
        f"egg {egg.get('name')} has no {label} image for Minecraft {minecraft}; "
        f"have {sorted(images)}"
    )


def allocation_summary(client: PanelClient, server: dict[str, Any]) -> str:
    allocation_id = server.get("allocation")
    if not allocation_id:
        return "(no allocation)"
    node_id = server.get("node")
    if not node_id:
        return f"allocation {allocation_id}"
    for item in client.paginate(f"/api/application/nodes/{node_id}/allocations"):
        allocation = attrs(item)
        if allocation.get("id") == allocation_id:
            ip = allocation.get("ip_alias") or allocation.get("ip")
            return f"{ip}:{allocation.get('port')}"
    return f"allocation {allocation_id}"


def print_server(client: PanelClient, server: dict[str, Any]) -> None:
    identifier = server.get("identifier") or server.get("uuid")
    print(
        f"server id={server.get('id')} uuid={server.get('uuid')} "
        f"identifier={identifier} name={server.get('name')!r}"
    )
    print(f"  node={server.get('node')} egg={server.get('egg')} owner={server.get('user')}")
    print(f"  address={allocation_summary(client, server)}")
    print(f"  panel={client.base}/server/{identifier}")


def build_environment(project_id: str, version_id: str, api_key: str) -> dict[str, str]:
    return {
        "PROJECT_ID": project_id,
        "VERSION_ID": version_id,
        "API_KEY": api_key,
    }


def create_server(
    client: PanelClient,
    *,
    name: str,
    description: str,
    owner_id: int,
    egg: dict[str, Any],
    image: str,
    environment: dict[str, str],
    allocation_id: int,
    memory: int,
    disk: int,
    external_id: str,
    start: bool,
    skip_scripts: bool,
    startup: str | None = None,
) -> dict[str, Any]:
    body = {
        "name": name,
        "description": description,
        "user": owner_id,
        "egg": egg["id"],
        "docker_image": image,
        "startup": startup or egg.get("startup"),
        "environment": environment,
        "skip_scripts": skip_scripts,
        "oom_killer": False,
        "start_on_completion": start and not skip_scripts,
        "external_id": external_id,
        "limits": {
            "memory": memory,
            "swap": 0,
            "disk": disk,
            "io": 500,
            "cpu": 0,
        },
        "feature_limits": {
            "databases": 0,
            "allocations": 0,
            "backups": 0,
        },
        "allocation": {"default": allocation_id},
    }
    created = client.post("/api/application/servers", body)
    return attrs(created if "attributes" in created else created.get("data", created))


def update_startup(
    client: PanelClient,
    server_id: int,
    *,
    egg: dict[str, Any],
    image: str,
    environment: dict[str, str],
    skip_scripts: bool,
    startup: str | None = None,
) -> dict[str, Any]:
    updated = client.patch(
        f"/api/application/servers/{server_id}/startup",
        {
            "startup": startup or egg.get("startup"),
            "environment": environment,
            "egg": egg["id"],
            "image": image,
            "skip_scripts": skip_scripts,
        },
    )
    return attrs(updated if "attributes" in updated else updated.get("data", updated))


def wait_installed(client: PanelClient, server_id: int, timeout: int) -> dict[str, Any]:
    deadline = time.time() + timeout
    last = ""
    while time.time() < deadline:
        detail = attrs(client.get(f"/api/application/servers/{server_id}"))
        installed = (detail.get("container") or {}).get("installed")
        status = detail.get("status")
        last = f"installed={installed} status={status}"
        print(f"  waiting: {last}")
        if installed in (1, True, "1", "installed"):
            return detail
        if status in {"install_failed", "install failed"}:
            raise SystemExit("the panel install failed; check the panel console")
        time.sleep(10)
    raise SystemExit(f"timed out waiting for install ({last})")


def upsert_server(
    client: PanelClient,
    *,
    server: dict[str, Any] | None,
    server_name: str,
    owner_id: int,
    egg: dict[str, Any],
    image: str,
    environment: dict[str, str],
    description: str,
    external_id: str,
    allocation: dict[str, Any] | None,
    memory: int,
    disk: int,
    skip_scripts: bool,
    start: bool,
    startup: str | None = None,
) -> dict[str, Any]:
    if server is None:
        if allocation is None:
            raise SystemExit("no allocation available to create the panel server")
        created = create_server(
            client,
            name=server_name,
            description=description,
            owner_id=owner_id,
            egg=egg,
            image=image,
            environment=environment,
            allocation_id=int(allocation["id"]),
            memory=memory,
            disk=disk,
            external_id=external_id,
            start=start,
            skip_scripts=skip_scripts,
            startup=startup,
        )
        print("created the panel server")
        return created
    client.patch(
        f"/api/application/servers/{server['id']}/details",
        {
            "name": server_name,
            "user": owner_id,
            "description": description,
            "external_id": external_id,
        },
    )
    updated = update_startup(
        client,
        int(server["id"]),
        egg=egg,
        image=image,
        environment=environment,
        skip_scripts=skip_scripts,
        startup=startup,
    )
    print("updated the panel server startup/environment")
    return updated


def origin_owner_repo() -> tuple[str, str]:
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise SystemExit("git remote get-url origin failed")
    raw = (result.stdout or "").strip().removesuffix(".git")
    if raw.startswith("git@github.com:"):
        owner_repo = raw.split(":", 1)[1]
    elif "github.com/" in raw:
        owner_repo = raw.split("github.com/", 1)[1]
    else:
        raise SystemExit(f"origin is not a GitHub URL: {raw}")
    parts = [part for part in owner_repo.strip("/").split("/") if part]
    if len(parts) < 2:
        raise SystemExit(f"cannot parse GitHub owner/repo from {raw}")
    return parts[0], parts[1]


def publish_server_zip_to_github(pack: dict[str, str], zip_path: Path) -> str | None:
    token = env("GH_TOKEN") or env("GITHUB_TOKEN")
    if not zip_path.is_file():
        raise SystemExit(f"server mods zip missing: {zip_path}")
    if not token:
        print(
            "GH_TOKEN unset: Wings will take the local server-mods zip "
            "(set GH_TOKEN in .env to attach it to the GitHub Release)"
        )
        return None
    owner, repo = origin_owner_repo()
    tag = f"v{pack['pack_version']}"
    print(f"attaching {zip_path.name} to GitHub Release {tag}")
    return replace_github_release_asset(
        owner=owner, repo=repo, tag=tag, path=zip_path, token=token
    )


def connect_wings(client: PanelClient, node: dict[str, Any], server: dict[str, Any]) -> Wings:
    payload = client.get(f"/api/application/nodes/{node['id']}/configuration")
    configuration = node_configuration(payload)
    token = str(configuration.get("token") or "")
    if not token:
        raise SystemExit("node configuration did not include a Wings token")
    fqdn = str(node.get("fqdn") or "")
    if not fqdn:
        raise SystemExit("node has no fqdn for Wings")
    uuid = str(server.get("uuid") or "")
    if not uuid:
        raise SystemExit("server has no uuid for Wings")
    return Wings(wings_base_url(fqdn, configuration), token, uuid)


def zip_has_jars(zip_path: Path) -> bool:
    with zipfile.ZipFile(zip_path) as archive:
        return any(
            not info.is_dir() and info.filename.replace("\\", "/").endswith(".jar")
            for info in archive.infolist()
        )


def upload_jars_from_zip(wings: Wings, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path) as archive:
        members = [
            info
            for info in archive.infolist()
            if not info.is_dir() and info.filename.replace("\\", "/").endswith(".jar")
        ]
        if members:
            print(f"uploading {len(members)} jars to /mods")
            for info in members:
                name = Path(info.filename.replace("\\", "/")).name
                data = archive.read(info)
                print(f"  {name} ({len(data)} bytes)")
                wings.write_file(f"/mods/{name}", data, "application/java-archive")
        else:
            print(f"{zip_path.name} contains no jars (empty pack)")
        configs = [
            info
            for info in archive.infolist()
            if not info.is_dir()
            and info.filename.replace("\\", "/").startswith("config/")
        ]
        if configs:
            print(f"uploading {len(configs)} pack configs")
            for info in configs:
                name = info.filename.replace("\\", "/")
                data = archive.read(info)
                print(f"  {name} ({len(data)} bytes)")
                wings.write_file(f"/{name}", data, "application/octet-stream")


def write_overlay(wings: Wings) -> None:
    overlay = ROOT / "server"
    pack_jvm = ROOT / "pack" / "user_jvm_args.txt"
    mapping = [
        (overlay / "run.sh", "/run.sh"),
        (pack_jvm, "/user_jvm_args.txt"),
        (overlay / "ops.json", "/ops.json"),
    ]
    for path, remote in mapping:
        if path.is_file():
            print(f"  uploading overlay {remote.lstrip('/')}")
            wings.write_file(remote, path.read_bytes(), "application/octet-stream")


def _follow_redirects(url: str) -> str:
    headers = {"User-Agent": "LeadAndLeylines-deploy/1.0"}
    request = urllib.request.Request(url, method="HEAD", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.geturl()
    except urllib.error.HTTPError as exc:
        if exc.code not in {403, 405}:
            raise
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        final = response.geturl()
        response.read(0)
        return final


def upload_server_mods(
    wings: Wings, zip_path: Path, *, github_url: str | None = None
) -> None:
    print("stopping server so mods can be replaced")
    wings.power("stop", ignore_http=(409,))
    try:
        wings.wait_state({"offline", "stopped"}, timeout=90)
    except SystemExit as exc:
        print(f"  {exc}")
        print("  sending kill")
        wings.power("kill", ignore_http=(409,))
        try:
            wings.wait_state({"offline", "stopped"}, timeout=30)
        except SystemExit:
            print("  continuing; Wings did not report offline")

    print(f"uploading {zip_path.name} ({zip_path.stat().st_size} bytes)")
    expect_jars = zip_has_jars(zip_path)
    wings.delete(["mods", SERVER_MODS_REMOTE])
    pulled = False
    if github_url:
        print("Wings pulling server mods zip from the GitHub Release")
        try:
            wings.pull_file(
                github_url,
                root="/",
                file_name=SERVER_MODS_REMOTE,
                foreground=True,
                timeout=1800,
            )
            pulled = True
        except SystemExit as exc:
            print(f"  GitHub pull failed ({exc}); retrying via redirect target")
            try:
                wings.pull_file(
                    _follow_redirects(github_url),
                    root="/",
                    file_name=SERVER_MODS_REMOTE,
                    foreground=True,
                    timeout=1800,
                )
                pulled = True
            except SystemExit as exc2:
                print(f"  GitHub pull failed ({exc2}); trying a local zip write")
    if not pulled:
        try:
            wings.write_file(
                f"/{SERVER_MODS_REMOTE}", zip_path.read_bytes(), "application/zip"
            )
        except SystemExit as exc:
            print(f"  zip upload failed ({exc}); uploading jars individually")
            wings.delete([SERVER_MODS_REMOTE])
            upload_jars_from_zip(wings, zip_path)
            wings.write_file("/eula.txt", b"eula=true\n", "text/plain")
            write_overlay(wings)
            _wait_for_mods(wings, expect_jars=expect_jars)
            return
    print("decompressing server mods zip")
    wings.decompress(SERVER_MODS_REMOTE)
    wings.delete([SERVER_MODS_REMOTE])
    wings.write_file("/eula.txt", b"eula=true\n", "text/plain")
    write_overlay(wings)
    _wait_for_mods(wings, expect_jars=expect_jars)


def _wait_for_mods(wings: Wings, *, expect_jars: bool = True) -> None:
    if not expect_jars:
        print("  empty pack: no server mods to wait for")
        return
    deadline = time.time() + 120
    while time.time() < deadline:
        try:
            names = wings.names("/mods") if wings.has("mods") else set()
        except SystemExit:
            names = set()
        jars = [name for name in names if name.endswith(".jar")]
        if jars:
            print(f"  mods/ has {len(jars)} jars")
            return
        print("  waiting for mods/ jars")
        time.sleep(3)
    raise SystemExit("mods/ did not appear after decompress")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create or update the Lead and Leylines test server"
    )
    parser.add_argument(
        "--from-local",
        action="store_true",
        help="export the current pack tree, attach the server-mods zip to the GitHub Release, and have Wings pull it",
    )
    parser.add_argument(
        "--share-only",
        action="store_true",
        help="export ATLauncher zip/mrpack (and server mods zip) without touching the panel",
    )
    parser.add_argument(
        "--curseforge",
        action="store_true",
        help="use the CurseForge Generic egg and a published CurseForge project id",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="resolve node/egg/owner/allocation and print the plan without writing",
    )
    parser.add_argument(
        "--reinstall",
        action="store_true",
        help="reinstall the egg (wipes the world). Local deploys reinstall automatically when NeoForge is missing or versions changed",
    )
    parser.add_argument(
        "--skip-install",
        action="store_true",
        help="create/update the server but skip the egg install script",
    )
    parser.add_argument(
        "--wait",
        type=int,
        default=0,
        metavar="SECONDS",
        help="poll until the egg reports installed (local reinstall defaults to 600)",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="print the existing server and exit",
    )
    return parser.parse_args()


def print_plan(
    pack: dict[str, str],
    *,
    panel: str,
    node: dict[str, Any],
    egg: dict[str, Any],
    owner: dict[str, Any],
    image: str,
    memory: int,
    disk: int,
    extra: str,
) -> None:
    print(
        f"pack {pack['pack_version']} Minecraft {pack['minecraft']} "
        f"{pack['loader']} {pack['loader_version']}"
    )
    print(f"panel {panel}")
    print(f"node id={node['id']} name={node.get('name')} fqdn={node.get('fqdn')}")
    print(f"egg id={egg.get('id')} name={egg.get('name')}")
    print(f"owner id={owner.get('id')} username={owner.get('username')}")
    print(f"image {image}")
    print(f"memory {memory}MiB disk {disk or 'unlimited'}")
    print(extra)


def deploy_from_local(
    args: argparse.Namespace,
    *,
    client: PanelClient,
    pack: dict[str, str],
    panel: str,
    node: dict[str, Any],
    owner: dict[str, Any],
    server: dict[str, Any] | None,
    server_name: str,
    external_id: str,
    memory: int,
    disk: int,
    port: str | None,
) -> None:
    egg = find_neoforge_egg(client)
    if egg is None:
        raise SystemExit(
            f"the panel is missing the {NEOFORGE_EGG_NAME!r} egg "
            f"(uuid {NEOFORGE_EGG_UUID}). Import it on the panel, then rerun."
        )
    if egg.get("id"):
        egg = egg_with_variables(client, int(egg["id"]))
    image = docker_image(egg, pack["minecraft"]) if egg.get("docker_images") else "(unknown)"
    allocation = None if server else pick_allocation(client, int(node["id"]), port)
    loader_env = neoforge_environment(pack)
    environment = environment_from_egg(egg, loader_env)
    previous_egg = int((server or {}).get("egg") or 0)
    previous_env = ((server or {}).get("container") or {}).get("environment") or {}
    print_plan(
        pack,
        panel=panel,
        node=node,
        egg=egg,
        owner=owner,
        image=image,
        memory=memory,
        disk=disk,
        extra=(
            f"local deploy NEOFORGE_VERSION={loader_env['NEOFORGE_VERSION']}; "
            "Wings pulls the GitHub Release server-mods zip when GH_TOKEN is set, "
            "otherwise the local zip (CurseForge listing not required)"
        ),
    )
    if server:
        print("existing server:")
        print_server(client, server)
    elif allocation:
        ip = allocation.get("ip_alias") or allocation.get("ip")
        print(f"new allocation id={allocation.get('id')} {ip}:{allocation.get('port')}")

    if args.dry_run:
        print(
            "dry-run: would export ATLauncher files, attach the server-mods zip to "
            "the GitHub Release, switch this server to the NeoForge egg, install NeoForge, "
            "then have Wings pull that zip"
        )
        return

    print("building local pack artifacts")
    _pack, paths = build_all()
    print(atlauncher_instructions(paths))

    description = (
        f"{server_name} test server. Wings pulls the GitHub Release server-mods zip "
        "until a CurseForge file exists."
    )
    server = upsert_server(
        client,
        server=server,
        server_name=server_name,
        owner_id=int(owner["id"]),
        egg=egg,
        image=image,
        environment=environment,
        description=description,
        external_id=external_id,
        allocation=allocation,
        memory=memory,
        disk=disk,
        skip_scripts=False,
        start=False,
        startup=NEOFORGE_STARTUP,
    )
    if not server.get("uuid"):
        server = attrs(client.get(f"/api/application/servers/{server['id']}"))
    wings = connect_wings(client, node, server)
    loader_files = wings.has("unix_args.txt") or wings.has("libraries")
    needs_reinstall = bool(
        args.reinstall
        or previous_egg != int(egg["id"])
        or str(previous_env.get("MC_VERSION") or "") != pack["minecraft"]
        or str(previous_env.get("NEOFORGE_VERSION") or "")
        != loader_env["NEOFORGE_VERSION"]
        or not loader_files
    )
    wait_seconds = args.wait or (600 if needs_reinstall else 0)
    if needs_reinstall:
        print(
            "reinstalling NeoForge egg (this wipes the world and other files on the volume)"
        )
        try:
            client.post(f"/api/application/servers/{server['id']}/reinstall")
        except SystemExit as exc:
            if "HTTP 409" not in str(exc):
                raise
            print("  reinstall already in progress")
        server = wait_installed(client, int(server["id"]), wait_seconds or 600)
        wings.wait_any({"unix_args.txt", "libraries"}, timeout=max(wait_seconds or 0, 300))
    elif wait_seconds:
        server = wait_installed(client, int(server["id"]), wait_seconds)

    upload_server_mods(
        wings,
        paths["server_zip"],
        github_url=publish_server_zip_to_github(pack, paths["server_zip"]),
    )
    print("starting server")
    wings.power("start")
    detail = attrs(client.get(f"/api/application/servers/{server['id']}"))
    print_server(client, detail)
    print(
        "Watch the panel console for NeoForge 'Done'. Application API keys cannot read live logs."
    )
    print(atlauncher_instructions(paths))


def deploy_from_curseforge(
    args: argparse.Namespace,
    *,
    client: PanelClient,
    pack: dict[str, str],
    panel: str,
    node: dict[str, Any],
    owner: dict[str, Any],
    server: dict[str, Any] | None,
    server_name: str,
    external_id: str,
    memory: int,
    disk: int,
    port: str | None,
    project_id: str,
    version_id: str,
    cf_api_key: str,
) -> None:
    egg = find_egg(client)
    if egg is None:
        if args.dry_run:
            print(
                f"egg {CURSEFORGE_GENERIC_NAME!r} is missing; "
                "would import from EGG_IMPORT_URL"
            )
            egg = {
                "id": None,
                "name": CURSEFORGE_GENERIC_NAME,
                "docker_images": {},
                "startup": "",
            }
        else:
            egg = import_egg(client)
            found = find_egg(client)
            if found:
                egg = found
    if not cf_api_key and egg.get("id"):
        cf_api_key = copy_curseforge_api_key(client, int(egg["id"])) or ""

    skip_scripts = bool(args.skip_install)
    blocked = False
    if not project_id:
        blocked = True
        project_id = "zip"
        skip_scripts = True
        print(
            "CURSEFORGE_PROJECT_ID is unset and the pack is not public on CurseForge yet. "
            "Use `python scripts/deploy_server.py --from-local` until a store file exists, "
            "or set CURSEFORGE_PROJECT_ID and rerun with --curseforge --reinstall."
        )
    if not cf_api_key:
        blocked = True
        skip_scripts = True
        print(
            "CURSEFORGE_API_KEY is unset and no existing CurseForge Generic server had one to copy. "
            "Install will be skipped until that egg variable is set."
        )
        cf_api_key = "missing"

    image = docker_image(egg, pack["minecraft"]) if egg.get("docker_images") else "(unknown)"
    allocation = None if server else pick_allocation(client, int(node["id"]), port)
    print_plan(
        pack,
        panel=panel,
        node=node,
        egg=egg,
        owner=owner,
        image=image,
        memory=memory,
        disk=disk,
        extra=f"PROJECT_ID={project_id} VERSION_ID={version_id} skip_scripts={skip_scripts}",
    )
    if server:
        print("existing server:")
        print_server(client, server)
    elif allocation:
        ip = allocation.get("ip_alias") or allocation.get("ip")
        print(f"new allocation id={allocation.get('id')} {ip}:{allocation.get('port')}")

    if args.dry_run:
        print("dry-run: no writes")
        raise SystemExit(2 if blocked else 0)

    environment = build_environment(project_id, version_id, cf_api_key)
    description = (
        f"{server_name} test server. Egg tracks the last published CurseForge file, not git."
    )
    server = upsert_server(
        client,
        server=server,
        server_name=server_name,
        owner_id=int(owner["id"]),
        egg=egg,
        image=image,
        environment=environment,
        description=description,
        external_id=external_id,
        allocation=allocation,
        memory=memory,
        disk=disk,
        skip_scripts=skip_scripts,
        start=not skip_scripts,
    )
    if args.reinstall and not skip_scripts:
        client.post(f"/api/application/servers/{server['id']}/reinstall")
        print("reinstall requested")
    if args.wait and not skip_scripts:
        server = wait_installed(client, int(server["id"]), args.wait)
    detail = attrs(client.get(f"/api/application/servers/{server['id']}"))
    print_server(client, detail)
    if blocked:
        raise SystemExit(
            "blocked-on-publish: use `python scripts/deploy_server.py --from-local` "
            "or set CURSEFORGE_PROJECT_ID and rerun with --curseforge --reinstall"
        )


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(line_buffering=True)
    load_env_file(ROOT / ".env")
    load_env_file(ROOT / "server" / ".env")
    args = parse_args()
    if args.from_local and args.curseforge:
        raise SystemExit("use either --from-local or --curseforge, not both")

    pack = read_pack(PACK_TOML)
    project_id = env("CURSEFORGE_PROJECT_ID")
    from_local = bool(args.from_local or args.share_only or (not args.curseforge and not project_id))

    if args.share_only:
        if args.dry_run:
            print("dry-run: would export ATLauncher zip/mrpack and server mods zip to dist/")
            return
        _pack, paths = build_all()
        print(atlauncher_instructions(paths))
        return

    panel = require_env("PANEL_URL")
    token = require_env("PANEL_API_KEY")
    node_fqdn = require_env("PANEL_NODE_FQDN")
    node_name = env("PANEL_NODE_NAME", DEFAULT_NODE_NAME)
    owner_name = env("PANEL_OWNER_USERNAME", "tinor")
    server_name = env("PANEL_SERVER_NAME") or pack["name"]
    external_id = env("PANEL_EXTERNAL_ID", DEFAULT_EXTERNAL_ID)
    memory = int(env("PANEL_MEMORY_MB", "8192"))
    disk = int(env("PANEL_DISK_MB", "0"))
    port = env("PANEL_PORT") or None
    version_id = env("CURSEFORGE_VERSION_ID", "latest")
    cf_api_key = env("CURSEFORGE_API_KEY")

    client = PanelClient(panel, token)
    node = find_node(client, node_fqdn, node_name)
    owner = find_owner(client, owner_name)
    server = find_server(client, external_id, server_name)
    if server:
        server = attrs(client.get(f"/api/application/servers/{server['id']}"))

    if args.status:
        if not server:
            raise SystemExit(f"no the panel server named {server_name!r} / external_id={external_id}")
        print_server(client, server)
        return

    common = {
        "client": client,
        "pack": pack,
        "panel": panel,
        "node": node,
        "owner": owner,
        "server": server,
        "server_name": server_name,
        "external_id": external_id,
        "memory": memory,
        "disk": disk,
        "port": port,
    }
    if from_local:
        deploy_from_local(args, **common)
        return
    deploy_from_curseforge(
        args,
        **common,
        project_id=project_id,
        version_id=version_id,
        cf_api_key=cf_api_key,
    )


if __name__ == "__main__":
    main()
