#!/usr/bin/env python3
"""Wings daemon client (node token). Never print tokens."""

from __future__ import annotations

import json
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


class Wings:
    def __init__(self, base: str, token: str, server_uuid: str, timeout: int = 120) -> None:
        self.base = base.rstrip("/")
        self.token = token
        self.uuid = server_uuid
        self.timeout = timeout
        self.ssl = ssl.create_default_context()

    def request(
        self,
        method: str,
        path: str,
        query: dict[str, Any] | None = None,
        body: Any | None = None,
        raw_body: bytes | None = None,
        content_type: str | None = None,
        timeout: int | None = None,
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
            headers["Content-Type"] = content_type or "application/octet-stream"
        request = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(
                request, context=self.ssl, timeout=timeout or self.timeout
            ) as response:
                payload = response.read()
                if not payload:
                    return None
                content = response.headers.get("Content-Type") or ""
                if "json" in content:
                    return json.loads(payload.decode("utf-8"))
                return payload
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            if exc.code in {400, 404} and path.endswith("/files/list-directory"):
                return []
            raise SystemExit(
                f"Wings {method} {path} failed: HTTP {exc.code}\n{detail[:2000]}"
            ) from exc
        except urllib.error.URLError as exc:
            raise SystemExit(f"Wings {method} {path} failed: {exc}") from exc

    def list_directory(self, directory: str = "/") -> list[dict[str, Any]]:
        payload = self.request(
            "GET",
            f"/api/servers/{self.uuid}/files/list-directory",
            query={"directory": directory},
        )
        if payload is None:
            return []
        if isinstance(payload, list):
            return [item for item in payload if isinstance(item, dict)]
        if isinstance(payload, dict):
            data = payload.get("data") or payload.get("attributes") or []
            if isinstance(data, list):
                return [item for item in data if isinstance(item, dict)]
        raise SystemExit("unexpected Wings list-directory payload")

    def names(self, directory: str = "/") -> set[str]:
        return {str(item.get("name") or "") for item in self.list_directory(directory)}

    def has(self, name: str, directory: str = "/") -> bool:
        return name in self.names(directory)

    def read_file(self, remote_path: str, timeout: int | None = None) -> bytes:
        if not remote_path.startswith("/"):
            remote_path = "/" + remote_path
        payload = self.request(
            "GET",
            f"/api/servers/{self.uuid}/files/contents",
            query={"file": remote_path},
            timeout=timeout or self.timeout,
        )
        if payload is None:
            return b""
        if isinstance(payload, bytes):
            return payload
        if isinstance(payload, str):
            return payload.encode("utf-8")
        raise SystemExit(f"unexpected Wings contents payload for {remote_path}")

    def write_file(
        self,
        remote_path: str,
        data: bytes,
        content_type: str = "application/octet-stream",
        timeout: int | None = None,
    ) -> None:
        if not remote_path.startswith("/"):
            remote_path = "/" + remote_path
        wait = timeout or max(self.timeout, 300, 60 + len(data) // 50_000)
        last_error: SystemExit | None = None
        for attempt in range(1, 4):
            try:
                self.request(
                    "POST",
                    f"/api/servers/{self.uuid}/files/write",
                    query={"file": remote_path},
                    raw_body=data,
                    content_type=content_type,
                    timeout=wait,
                )
                return
            except SystemExit as exc:
                if "urlopen error" not in str(exc):
                    raise
                last_error = exc
                print(f"  upload attempt {attempt}/3 failed: {exc}")
                time.sleep(2 * attempt)
        raise last_error or SystemExit(f"Wings write failed for {remote_path}")

    def delete(self, names: list[str], root: str = "/") -> None:
        existing = self.names(root)
        targets = [name for name in names if name in existing]
        if not targets:
            return
        self.request(
            "POST",
            f"/api/servers/{self.uuid}/files/delete",
            body={"root": root, "files": targets},
        )

    def pull_file(
        self,
        url: str,
        *,
        root: str = "/",
        file_name: str | None = None,
        foreground: bool = True,
        timeout: int | None = None,
    ) -> Any:
        body: dict[str, Any] = {
            "url": url,
            "root": root,
            "foreground": foreground,
            "use_header": False,
        }
        if file_name:
            body["file_name"] = file_name
        return self.request(
            "POST",
            f"/api/servers/{self.uuid}/files/pull",
            body=body,
            timeout=timeout or 1800,
        )

    def decompress(self, filename: str, root: str = "/") -> None:
        self.request(
            "POST",
            f"/api/servers/{self.uuid}/files/decompress",
            body={"root": root, "file": filename},
            timeout=max(self.timeout, 600),
        )

    def power(self, action: str, ignore_http: tuple[int, ...] = ()) -> None:
        try:
            self.request(
                "POST",
                f"/api/servers/{self.uuid}/power",
                body={"action": action},
            )
        except SystemExit as exc:
            if any(f"HTTP {code}" in str(exc) for code in ignore_http):
                return
            raise

    def state(self) -> str:
        payload = self.request("GET", f"/api/servers/{self.uuid}")
        if isinstance(payload, dict):
            return str(payload.get("state") or payload.get("status") or "")
        return ""

    def wait_state(self, wanted: set[str], timeout: int) -> str:
        deadline = time.time() + timeout
        last = ""
        while time.time() < deadline:
            last = self.state() or "(unknown)"
            print(f"  wings state={last}")
            if last.lower() in {item.lower() for item in wanted}:
                return last
            time.sleep(3)
        raise SystemExit(f"timed out waiting for Wings state {sorted(wanted)} ({last})")

    def wait_any(self, names: set[str], timeout: int, directory: str = "/") -> str:
        deadline = time.time() + timeout
        last: set[str] = set()
        while time.time() < deadline:
            last = self.names(directory)
            found = last & names
            if found:
                return next(iter(found))
            print(f"  waiting for any of {sorted(names)}; have {sorted(last)[:12]}")
            time.sleep(5)
        raise SystemExit(f"timed out waiting for any of {sorted(names)}; have {sorted(last)}")


def wings_base_url(node_fqdn: str, configuration: dict[str, Any]) -> str:
    api = configuration.get("api") or {}
    ssl_cfg = api.get("ssl") if isinstance(api, dict) else {}
    enabled = bool((ssl_cfg or {}).get("enabled")) if isinstance(ssl_cfg, dict) else True
    port = int((api or {}).get("port") or (443 if enabled else 8080))
    scheme = "https" if enabled else "http"
    if (scheme == "https" and port == 443) or (scheme == "http" and port == 80):
        return f"{scheme}://{node_fqdn}"
    return f"{scheme}://{node_fqdn}:{port}"


def node_configuration(payload: Any) -> dict[str, Any]:
    if isinstance(payload, dict) and "attributes" in payload:
        inner = payload["attributes"]
        if isinstance(inner, dict):
            return inner
    if isinstance(payload, dict):
        return payload
    raise SystemExit("unexpected node configuration payload")
