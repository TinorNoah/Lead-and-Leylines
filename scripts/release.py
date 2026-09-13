#!/usr/bin/env python3
"""Ship a Lead and Leylines release: git tag, GitHub Actions Release, the panel.

CI still exports zip + mrpack and creates the GitHub Release. This script does
not upload CurseForge/Modrinth files or print tokens.

  python scripts/release.py
  python scripts/release.py --dry-run
  python scripts/release.py --no-panel
  python scripts/release.py --no-wait
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from read_pack_versions import ROOT, read_pack

README = ROOT / "README.md"
RELEASE_WORKFLOW = "release.yml"


def run(
    command: list[str],
    *,
    check: bool = True,
    capture: bool = False,
) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(command))
    result = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=capture,
    )
    if check and result.returncode != 0:
        if capture and result.stderr:
            sys.stderr.write(result.stderr)
        raise SystemExit(f"command failed ({result.returncode}): {' '.join(command)}")
    return result


def git_output(command: list[str]) -> str:
    result = run(["git", *command], capture=True)
    return (result.stdout or "").strip()


def readme_pack_version() -> str | None:
    text = README.read_text(encoding="utf-8")
    match = re.search(r"^\| Pack version \| ([^|]+) \|$", text, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def assert_ready(pack: dict[str, str], *, dry_run: bool) -> str:
    branch = git_output(["rev-parse", "--abbrev-ref", "HEAD"])
    if branch != "main":
        raise SystemExit(f"release from main only (on {branch})")
    status = git_output(["status", "--porcelain"])
    if status and not dry_run:
        raise SystemExit("working tree is dirty; commit or stash before releasing")
    readme_version = readme_pack_version()
    if readme_version != pack["pack_version"]:
        raise SystemExit(
            f"README pack version {readme_version!r} does not match "
            f"pack.toml {pack['pack_version']!r}"
        )
    tag = f"v{pack['pack_version']}"
    local = git_output(["tag", "-l", tag])
    if local:
        raise SystemExit(f"tag {tag} already exists locally")
    remote = run(
        ["git", "ls-remote", "--tags", "origin", f"refs/tags/{tag}"],
        capture=True,
    )
    if (remote.stdout or "").strip():
        raise SystemExit(f"tag {tag} already exists on origin")
    return tag


def wait_for_github_release(tag: str, timeout: int) -> str:
    deadline = time.time() + timeout
    while time.time() < deadline:
        result = run(
            ["gh", "release", "view", tag, "--json", "url,isDraft"],
            check=False,
            capture=True,
        )
        if result.returncode == 0:
            payload = json.loads(result.stdout or "{}")
            url = str(payload.get("url") or "")
            if url and not payload.get("isDraft"):
                return url
        time.sleep(10)
        print(f"waiting for GitHub Release {tag}...")
    raise SystemExit(
        f"timed out waiting for GitHub Release {tag}; check Actions, then "
        "python scripts/deploy_server.py --from-local if the panel was skipped"
    )


def deploy_panel() -> None:
    script = ROOT / "scripts" / "deploy_server.py"
    run([sys.executable, str(script), "--from-local"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Tag pack.toml version, push, wait for GitHub Release, deploy the panel"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the plan without tagging, pushing, or deploying",
    )
    parser.add_argument(
        "--no-panel",
        action="store_true",
        help="skip the panel (GitHub tag/release only)",
    )
    parser.add_argument(
        "--no-wait",
        action="store_true",
        help="do not wait for the GitHub Release workflow",
    )
    parser.add_argument(
        "--wait-timeout",
        type=int,
        default=900,
        metavar="SECONDS",
        help="how long to wait for the GitHub Release (default 900)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pack = read_pack(ROOT / "pack" / "pack.toml")
    tag = assert_ready(pack, dry_run=args.dry_run)
    print(
        f"release {pack['name']} {pack['pack_version']} "
        f"(Minecraft {pack['minecraft']} {pack['loader']} {pack['loader_version']})"
    )
    print(f"tag {tag}")
    print(f"workflow {RELEASE_WORKFLOW}")
    if args.dry_run:
        print("dry-run: not tagging, pushing, or deploying")
        return
    run(["git", "push", "origin", "HEAD"])
    run(["git", "tag", tag])
    run(["git", "push", "origin", tag])
    sha = git_output(["rev-parse", "HEAD"])
    actions = git_output(["remote", "get-url", "origin"])
    repo_web = actions.removesuffix(".git").replace("git@github.com:", "https://github.com/")
    print(f"commit {sha}")
    print(f"actions {repo_web}/actions")
    release_url = ""
    if not args.no_wait:
        release_url = wait_for_github_release(tag, args.wait_timeout)
        print(f"github release {release_url}")
    else:
        print(f"github release will appear at {repo_web}/releases/tag/{tag}")
    if not args.no_panel:
        deploy_panel()
    print("done")
    if release_url:
        print(release_url)


if __name__ == "__main__":
    main()
