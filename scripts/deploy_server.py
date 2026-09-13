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
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from read_pack_versions import PACK_TOML, read_pack

CURSEFORGE_GENERIC_UUID = "019bbf16-a3f3-470a-9c0b-f3995b5e032a"
CURSEFORGE_GENERIC_NAME = "CurseForge Generic"
EGG_IMPORT_URL = (
    "https://raw.githubusercontent.com/panel-eggs/minecraft/refs/heads/main"
    "/java/curseforge/egg-curse-forge-generic.json"
)
DEFAULT_PANEL = "https://example.invalid"
DEFAULT_NODE_FQDN = "example.invalid"
DEFAULT_NODE_NAME = "node"
DEFAULT_EXTERNAL_ID = "lead-and-leylines"
SECRET_MARKERS = ("KEY", "TOKEN", "SECRET", "PASSWORD", "AUTHORIZATION")


def load_env_file(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


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


def find_egg(client: PanelClient) -> dict[str, Any] | None:
    for item in client.paginate("/api/application/eggs"):
        egg = attrs(item)
        if str(egg.get("uuid") or "").lower() == CURSEFORGE_GENERIC_UUID:
            return egg
        if str(egg.get("name") or "").lower() == CURSEFORGE_GENERIC_NAME.lower():
            return egg
    return None


def import_egg(client: PanelClient) -> dict[str, Any]:
    print(f"importing missing egg from {EGG_IMPORT_URL}")
    egg_json = fetch_json(EGG_IMPORT_URL)
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
) -> dict[str, Any]:
    body = {
        "name": name,
        "description": description,
        "user": owner_id,
        "egg": egg["id"],
        "docker_image": image,
        "startup": egg.get("startup"),
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
) -> dict[str, Any]:
    updated = client.patch(
        f"/api/application/servers/{server_id}/startup",
        {
            "startup": egg.get("startup"),
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create or update the Lead and Leylines test server"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="resolve node/egg/owner/allocation and print the plan without writing",
    )
    parser.add_argument(
        "--reinstall",
        action="store_true",
        help="reinstall after create/update so the egg pulls the current CurseForge file",
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
        help="poll until the egg reports installed",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="print the existing server and exit",
    )
    return parser.parse_args()


def main() -> None:
    load_env_file(ROOT / ".env")
    load_env_file(ROOT / "server" / ".env")
    args = parse_args()

    pack = read_pack(PACK_TOML)
    panel = env("PANEL_URL", DEFAULT_PANEL)
    token = require_env("PANEL_API_KEY")
    node_fqdn = env("PANEL_NODE_FQDN", DEFAULT_NODE_FQDN)
    node_name = env("PANEL_NODE_NAME", DEFAULT_NODE_NAME)
    owner_name = env("PANEL_OWNER_USERNAME", "tinor")
    server_name = env("PANEL_SERVER_NAME") or pack["name"]
    external_id = env("PANEL_EXTERNAL_ID", DEFAULT_EXTERNAL_ID)
    memory = int(env("PANEL_MEMORY_MB", "8192"))
    disk = int(env("PANEL_DISK_MB", "0"))
    port = env("PANEL_PORT") or None
    project_id = env("CURSEFORGE_PROJECT_ID")
    version_id = env("CURSEFORGE_VERSION_ID", "latest")
    cf_api_key = env("CURSEFORGE_API_KEY")

    client = PanelClient(panel, token)
    node = find_node(client, node_fqdn, node_name)
    egg = find_egg(client)
    if egg is None:
        if args.dry_run:
            print(f"egg {CURSEFORGE_GENERIC_NAME!r} is missing; would import from {EGG_IMPORT_URL}")
            egg = {"id": None, "name": CURSEFORGE_GENERIC_NAME, "docker_images": {}, "startup": ""}
        else:
            egg = import_egg(client)
            found = find_egg(client)
            if found:
                egg = found
    owner = find_owner(client, owner_name)
    server = find_server(client, external_id, server_name)

    if args.status:
        if not server:
            raise SystemExit(f"no the panel server named {server_name!r} / external_id={external_id}")
        print_server(client, server)
        return

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
            "Creating/updating the panel server with install skipped (blocked-on-publish)."
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
    allocation = None
    if server is None:
        allocation = pick_allocation(client, int(node["id"]), port)

    print(f"pack {pack['pack_version']} Minecraft {pack['minecraft']} {pack['loader']} {pack['loader_version']}")
    print(f"panel {panel}")
    print(f"node id={node['id']} name={node.get('name')} fqdn={node.get('fqdn')}")
    print(f"egg id={egg.get('id')} name={egg.get('name')}")
    print(f"owner id={owner.get('id')} username={owner.get('username')}")
    print(f"image {image}")
    print(f"memory {memory}MiB disk {disk or 'unlimited'}")
    if server:
        print("existing server:")
        print_server(client, server)
    elif allocation:
        ip = allocation.get("ip_alias") or allocation.get("ip")
        print(f"new allocation id={allocation.get('id')} {ip}:{allocation.get('port')}")
    print(f"PROJECT_ID={project_id} VERSION_ID={version_id} skip_scripts={skip_scripts}")

    if args.dry_run:
        print("dry-run: no writes")
        raise SystemExit(2 if blocked else 0)

    environment = build_environment(project_id, version_id, cf_api_key)
    description = (
        f"{server_name} test server. Egg tracks the last published CurseForge file, not git."
    )

    if server is None:
        assert allocation is not None
        server = create_server(
            client,
            name=server_name,
            description=description,
            owner_id=int(owner["id"]),
            egg=egg,
            image=image,
            environment=environment,
            allocation_id=int(allocation["id"]),
            memory=memory,
            disk=disk,
            external_id=external_id,
            start=not skip_scripts,
            skip_scripts=skip_scripts,
        )
        print("created the panel server")
    else:
        client.patch(
            f"/api/application/servers/{server['id']}/details",
            {
                "name": server_name,
                "user": int(owner["id"]),
                "description": description,
                "external_id": external_id,
            },
        )
        server = update_startup(
            client,
            int(server["id"]),
            egg=egg,
            image=image,
            environment=environment,
            skip_scripts=skip_scripts,
        )
        print("updated the panel server startup/environment")

    if args.reinstall and not skip_scripts:
        client.post(f"/api/application/servers/{server['id']}/reinstall")
        print("reinstall requested")

    if args.wait and not skip_scripts:
        server = wait_installed(client, int(server["id"]), args.wait)

    detail = attrs(client.get(f"/api/application/servers/{server['id']}"))
    print_server(client, detail)
    if blocked:
        raise SystemExit(
            "blocked-on-publish: set CURSEFORGE_PROJECT_ID in .env, then rerun "
            "python scripts/deploy_server.py --reinstall"
        )


if __name__ == "__main__":
    main()
