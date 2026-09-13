#!/usr/bin/env python3
"""Turn a Modrinth slug or id into the 8-character project id.

The Modrinth upload API needs the 8-character id. Unpublished listings 404
without a token that can read the project. Never print tokens.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ID_RE = re.compile(r"^[0-9A-Za-z]{8}$")
USER_AGENT = "TinorNoah/Lead-and-Leylines (github.com/TinorNoah/Lead-and-Leylines)"


def write_github_output(values: dict[str, str]) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        raise SystemExit("GITHUB_OUTPUT is not set")
    with Path(path).open("a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def fetch_project(project: str, token: str) -> dict[str, object] | None:
    request = urllib.request.Request(
        f"https://api.modrinth.com/v2/project/{urllib.parse.quote(project, safe='')}",
        headers={
            "User-Agent": USER_AGENT,
            "Authorization": token,
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 404}:
            return None
        raise SystemExit(f"Modrinth project lookup failed: HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Modrinth project lookup failed: {exc}") from exc


def resolve(project: str, token: str) -> tuple[str | None, str]:
    if ID_RE.fullmatch(project):
        return project, "already an id"
    data = fetch_project(project, token)
    if not data:
        return (
            None,
            "could not resolve Modrinth slug to an id (listing unpublished or "
            "token missing PROJECT_READ). Set MODRINTH_PROJECT_ID to the "
            "8-character id from the Modrinth dashboard, not the slug",
        )
    resolved = str(data.get("id") or "")
    if not ID_RE.fullmatch(resolved):
        return None, "Modrinth API did not return an 8-character project id"
    return resolved, "resolved from slug"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--github-output", action="store_true")
    args = parser.parse_args()
    project = os.environ.get("MODRINTH_PROJECT_ID", "").strip()
    token = os.environ.get("MODRINTH_TOKEN", "").strip()
    if not project or not token:
        raise SystemExit("MODRINTH_PROJECT_ID and MODRINTH_TOKEN are required")
    resolved, reason = resolve(project, token)
    if resolved:
        print(f"Modrinth project id {resolved} ({reason})")
        if args.github_output:
            write_github_output({"ok": "true", "id": resolved})
        return
    print(reason)
    if args.github_output:
        write_github_output({"ok": "false", "id": "", "reason": reason})
        return
    raise SystemExit(reason)


if __name__ == "__main__":
    main()
