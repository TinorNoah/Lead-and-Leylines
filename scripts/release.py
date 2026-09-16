#!/usr/bin/env python3
"""Publish a Lead and Leylines pack version from this machine.

Pass a tag. Notes default to the matching ## [X.Y.Z] section in CHANGELOG.md
(the GitHub Release body and CurseForge/Modrinth notes). Only --channel release
uploads to CurseForge/Modrinth; alpha/beta are GitHub prereleases plus the
test-server update. This script never edits CHANGELOG.md. Do not put server or
hosting details in the notes; they are not part of the public release.

  python scripts/release.py v0.0.3 --channel alpha --dry-run
  python scripts/release.py v0.0.3 --channel release
  python scripts/release.py v0.0.3 --changelog notes.md
  python scripts/release.py 0.0.3 --notes "- EMI and Create"
  python scripts/release.py v0.0.3 --skip-server
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from envfile import load_env_file
from pack_artifacts import build_server_mods_zip, export_client_artifacts
from publish_stores import (
    create_github_release,
    upload_curseforge,
    upload_github_asset,
    upload_modrinth,
)
from read_pack_versions import ROOT, read_pack

README = ROOT / "README.md"
CHANGELOG_FILE = ROOT / "CHANGELOG.md"
CHANNELS = ("alpha", "beta", "release")
SECTION_HEADING = re.compile(r"^## \[")
BULLET_LINE = re.compile(r"^[-*+]\s+\S")


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


def load_secrets() -> None:
    load_env_file(ROOT / ".env")
    load_env_file(ROOT / "server" / ".env")


def env(name: str) -> str:
    return os.environ.get(name, "").strip()


def normalize_tag(raw: str) -> tuple[str, str]:
    value = raw.strip()
    if not value:
        raise SystemExit("tag is empty")
    version = value[1:] if value.lower().startswith("v") else value
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise SystemExit(f"tag must be vX.Y.Z (got {raw!r})")
    return f"v{version}", version


def changelog_has_real_bullets(text: str) -> bool:
    for line in text.splitlines():
        if BULLET_LINE.match(line.strip()):
            return True
    return False


def extract_changelog_section(text: str, version: str) -> str | None:
    heading = re.compile(rf"^## \[{re.escape(version)}\](?:\s|$)")
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if heading.match(line)), None)
    if start is None:
        return None
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if SECTION_HEADING.match(lines[index]):
            end = index
            break
    return "\n".join(lines[start:end]).strip()


def read_changelog(args: argparse.Namespace, version: str) -> str:
    if args.changelog and args.notes:
        raise SystemExit("use either --changelog or --notes, not both")
    if args.changelog:
        path = Path(args.changelog)
        if not path.is_file():
            raise SystemExit(f"changelog file not found: {path}")
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            raise SystemExit("changelog is empty")
        return text
    if args.notes:
        text = str(args.notes).strip()
        if not text:
            raise SystemExit("changelog is empty")
        return text
    if not CHANGELOG_FILE.is_file():
        raise SystemExit(
            "changelog required: CHANGELOG.md is missing "
            "(or pass --changelog FILE / --notes TEXT)"
        )
    section = extract_changelog_section(
        CHANGELOG_FILE.read_text(encoding="utf-8"),
        version,
    )
    if section is None:
        raise SystemExit(
            f"changelog required: CHANGELOG.md has no ## [{version}] section "
            "(or pass --changelog FILE / --notes TEXT)"
        )
    if not changelog_has_real_bullets(section):
        raise SystemExit(
            f"changelog required: ## [{version}] has no bullet entries "
            "(category headers alone do not count)"
        )
    return section


def store_skip_reason(
    store: str,
    *,
    channel: str,
    publish_to_stores: bool,
    skip_flag: bool,
    flag_name: str,
    has_creds: bool,
) -> str | None:
    if not publish_to_stores:
        return f"{store}: skip (channel is {channel!r}, not 'release')"
    if skip_flag:
        return f"{store}: skip ({flag_name})"
    if not has_creds:
        return f"{store}: skip (missing token/id)"
    return None


def readme_pack_version() -> str | None:
    text = README.read_text(encoding="utf-8")
    match = re.search(r"^\| Pack version \| ([^|]+) \|$", text, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def origin_owner_repo() -> tuple[str, str]:
    raw = git_output(["remote", "get-url", "origin"])
    raw = raw.removesuffix(".git")
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


def assert_ready(pack: dict[str, str], tag: str, version: str, *, dry_run: bool) -> None:
    if pack["pack_version"] != version:
        raise SystemExit(
            f"pack.toml version {pack['pack_version']!r} does not match tag {tag}"
        )
    readme_version = readme_pack_version()
    if readme_version != version:
        raise SystemExit(
            f"README pack version {readme_version!r} does not match tag {tag}"
        )
    branch = git_output(["rev-parse", "--abbrev-ref", "HEAD"])
    if branch != "main":
        raise SystemExit(f"release from main only (on {branch})")
    status = git_output(["status", "--porcelain"])
    if status and not dry_run:
        raise SystemExit("working tree is dirty; commit or stash before releasing")
    if dry_run:
        return
    local = git_output(["tag", "-l", tag])
    if local:
        raise SystemExit(f"tag {tag} already exists locally")
    remote = run(
        ["git", "ls-remote", "--tags", "origin", f"refs/tags/{tag}"],
        capture=True,
    )
    if (remote.stdout or "").strip():
        raise SystemExit(f"tag {tag} already exists on origin")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Tag, create a GitHub Release from a changelog, and upload "
            "CurseForge/Modrinth artifacts"
        )
    )
    parser.add_argument("tag", help="release tag (vX.Y.Z or X.Y.Z)")
    parser.add_argument(
        "--changelog",
        metavar="FILE",
        help=(
            "markdown notes used as the GitHub/CurseForge/Modrinth body "
            "(default: ## [X.Y.Z] section in CHANGELOG.md)"
        ),
    )
    parser.add_argument(
        "--notes",
        help="changelog text (instead of --changelog)",
    )
    parser.add_argument(
        "--channel",
        choices=CHANNELS,
        default="alpha",
        help="store release channel (default alpha)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the plan without tagging, uploading, or deploying",
    )
    parser.add_argument(
        "--skip-curseforge",
        action="store_true",
        help="do not upload the CurseForge zip",
    )
    parser.add_argument(
        "--skip-modrinth",
        action="store_true",
        help="do not upload the Modrinth mrpack",
    )
    parser.add_argument(
        "--skip-server",
        action="store_true",
        help="do not update the dedicated test server",
    )
    return parser.parse_args()


def deploy_server() -> None:
    script = ROOT / "scripts" / "deploy_server.py"
    run([sys.executable, str(script), "--from-local"])


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    load_secrets()
    args = parse_args()
    tag, version = normalize_tag(args.tag)
    publish_to_stores = args.channel == "release"
    skip_curseforge = args.skip_curseforge or not publish_to_stores
    skip_modrinth = args.skip_modrinth or not publish_to_stores
    changelog = read_changelog(args, version)
    cf_token = env("CURSEFORGE_TOKEN")
    cf_project = env("CURSEFORGE_PROJECT_ID")
    mr_token = env("MODRINTH_TOKEN")
    mr_project = env("MODRINTH_PROJECT_ID")
    print(f"channel {args.channel}")
    for reason in (
        store_skip_reason(
            "CurseForge",
            channel=args.channel,
            publish_to_stores=publish_to_stores,
            skip_flag=args.skip_curseforge,
            flag_name="--skip-curseforge",
            has_creds=bool(cf_token and cf_project),
        ),
        store_skip_reason(
            "Modrinth",
            channel=args.channel,
            publish_to_stores=publish_to_stores,
            skip_flag=args.skip_modrinth,
            flag_name="--skip-modrinth",
            has_creds=bool(mr_token and mr_project),
        ),
    ):
        if reason:
            print(reason)
    print("--- changelog ---")
    print(changelog)
    print("---")
    sys.stdout.flush()
    pack = read_pack(ROOT / "pack" / "pack.toml")
    assert_ready(pack, tag, version, dry_run=args.dry_run)
    owner, repo = origin_owner_repo()
    name = f"{pack['name']} {version}"
    gh_token = env("GH_TOKEN") or env("GITHUB_TOKEN")
    print(
        f"release {name} "
        f"(Minecraft {pack['minecraft']} {pack['loader']} {pack['loader_version']})"
    )
    print(f"tag {tag}")
    print(f"github {owner}/{repo}")
    if not gh_token:
        print("GitHub: missing GH_TOKEN in .env (stores and GitHub Release skipped)")
    if args.skip_server:
        print("WARNING: skipping dedicated server update (--skip-server)")
    else:
        print("dedicated server: will update after GitHub (or immediately if GitHub is skipped)")
    if args.dry_run:
        print("dry-run: not tagging, uploading, or deploying")
        return
    url = ""
    if gh_token:
        paths = export_client_artifacts(pack)
        zip_path = paths["client_zip"]
        mrpack_path = paths["mrpack"]
        if not zip_path.is_file() or not mrpack_path.is_file():
            raise SystemExit("packwiz export did not produce zip and mrpack")
        print(f"exporting server mods zip -> {paths['server_zip'].name}")
        build_server_mods_zip(pack, paths["server_zip"])
        if git_output(["status", "--porcelain"]):
            raise SystemExit("packwiz export dirtied the tree; commit the refresh and rerun")
        run(["git", "push", "origin", "HEAD"])
        run(["git", "tag", "-a", tag, "-m", name])
        run(["git", "push", "origin", tag])
        sha = git_output(["rev-parse", "HEAD"])
        print(f"commit {sha}")
        url, release_id = create_github_release(
            owner=owner,
            repo=repo,
            tag=tag,
            name=name,
            body=changelog,
            token=gh_token,
            target=sha,
            prerelease=args.channel != "release",
        )
        upload_github_asset(
            owner=owner, repo=repo, release_id=release_id, path=zip_path, token=gh_token
        )
        upload_github_asset(
            owner=owner, repo=repo, release_id=release_id, path=mrpack_path, token=gh_token
        )
        upload_github_asset(
            owner=owner,
            repo=repo,
            release_id=release_id,
            path=paths["server_zip"],
            token=gh_token,
        )
        print(f"github release {url}")
        if not skip_curseforge and cf_token and cf_project:
            upload_curseforge(
                project_id=cf_project,
                token=cf_token,
                zip_path=zip_path,
                name=name,
                changelog=changelog,
                minecraft=pack["minecraft"],
                channel=args.channel,
            )
        elif not skip_curseforge:
            print("CurseForge upload skipped: CURSEFORGE_TOKEN or CURSEFORGE_PROJECT_ID not set")
        if not skip_modrinth and mr_token and mr_project:
            upload_modrinth(
                project=mr_project,
                token=mr_token,
                mrpack=mrpack_path,
                name=name,
                version=version,
                changelog=changelog,
                minecraft=pack["minecraft"],
                loader=pack["loader"],
                channel=args.channel,
            )
        elif not skip_modrinth:
            print("Modrinth upload skipped: MODRINTH_TOKEN or MODRINTH_PROJECT_ID not set")
    if not args.skip_server:
        deploy_server()
    if not gh_token:
        raise SystemExit("set GH_TOKEN in .env to create the GitHub Release (never commit it)")
    print("done")
    print(url)


if __name__ == "__main__":
    main()
