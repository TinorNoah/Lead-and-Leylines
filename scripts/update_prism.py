#!/usr/bin/env python3
"""Sync the local Prism instance to the current pack/ tree.

Uses packwiz serve plus packwiz-installer-bootstrap (the same loop as
CONTRIBUTING.md). Does not start the game. Instance path is gitignored .env
or auto-discovered from PrismLauncher; never hardcoded in git.
"""

from __future__ import annotations

import configparser
import os
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from envfile import load_env_file
from read_pack_versions import PACK_TOML, read_pack

PACK_DIR = ROOT / "pack"
BOOTSTRAP_JAR = "packwiz-installer-bootstrap.jar"
BOOTSTRAP_URL = (
    "https://github.com/packwiz/packwiz-installer-bootstrap/releases/"
    "download/v0.0.3/packwiz-installer-bootstrap.jar"
)
USER_AGENT = "LeadAndLeylines-prism/1.0"
INSTALLER_TIMEOUT_S = 900
SERVE_WAIT_S = 30


def load_secrets() -> None:
    load_env_file(ROOT / ".env")
    load_env_file(ROOT / "server" / ".env")


def env(name: str) -> str:
    return os.environ.get(name, "").strip()


def default_prism_root() -> Path:
    override = env("PRISM_ROOT")
    if override:
        return Path(override)
    appdata = os.environ.get("APPDATA", "")
    if appdata:
        return Path(appdata) / "PrismLauncher"
    return Path.home() / "AppData" / "Roaming" / "PrismLauncher"


def instance_display_name(instance_dir: Path) -> str | None:
    cfg_path = instance_dir / "instance.cfg"
    if not cfg_path.is_file():
        return None
    parser = configparser.ConfigParser(interpolation=None)
    parser.optionxform = str
    text = cfg_path.read_text(encoding="utf-8")
    if not text.lstrip().startswith("["):
        text = "[General]\n" + text
    parser.read_string(text)
    for section in parser.sections():
        if parser.has_option(section, "name"):
            return parser.get(section, "name").strip()
    return None


def instance_java(instance_dir: Path) -> str | None:
    cfg_path = instance_dir / "instance.cfg"
    if not cfg_path.is_file():
        return None
    parser = configparser.ConfigParser(interpolation=None)
    parser.optionxform = str
    text = cfg_path.read_text(encoding="utf-8")
    if not text.lstrip().startswith("["):
        text = "[General]\n" + text
    parser.read_string(text)
    raw = ""
    for section in parser.sections():
        if parser.has_option(section, "JavaPath"):
            raw = parser.get(section, "JavaPath").strip()
            break
    if not raw:
        return None
    path = Path(raw)
    if path.name.lower() == "javaw.exe":
        sibling = path.with_name("java.exe")
        if sibling.is_file():
            return str(sibling)
    if path.is_file():
        return str(path)
    return raw


def minecraft_dir(instance_dir: Path) -> Path:
    dotted = instance_dir / ".minecraft"
    if dotted.is_dir():
        return dotted
    plain = instance_dir / "minecraft"
    if plain.is_dir():
        return plain
    raise SystemExit(f"no .minecraft folder in {instance_dir}")


def find_instance(pack_name: str) -> Path | None:
    explicit = env("PRISM_INSTANCE_DIR")
    if explicit:
        path = Path(explicit)
        if not (path / "instance.cfg").is_file():
            raise SystemExit(
                f"PRISM_INSTANCE_DIR has no instance.cfg: {path}"
            )
        return path
    instances = default_prism_root() / "instances"
    if not instances.is_dir():
        return None
    matches: list[Path] = []
    for child in sorted(instances.iterdir()):
        if not child.is_dir():
            continue
        name = instance_display_name(child)
        if name == pack_name:
            matches.append(child)
    if not matches:
        return None
    if len(matches) > 1:
        print(
            f"Prism: {len(matches)} instances named {pack_name!r}; "
            "using the first. Set PRISM_INSTANCE_DIR to pick one."
        )
    return matches[0]


def ensure_bootstrap(minecraft: Path) -> Path:
    dest = minecraft / BOOTSTRAP_JAR
    if dest.is_file():
        return dest
    print(f"downloading {BOOTSTRAP_JAR}")
    request = urllib.request.Request(BOOTSTRAP_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        dest.write_bytes(response.read())
    return dest


def resolve_java(instance_dir: Path) -> str:
    configured = instance_java(instance_dir)
    if configured:
        return configured
    home = env("JAVA_HOME")
    if home:
        candidate = Path(home) / "bin" / "java.exe"
        if candidate.is_file():
            return str(candidate)
        posix = Path(home) / "bin" / "java"
        if posix.is_file():
            return str(posix)
    which = shutil.which("java")
    if which:
        return which
    raise SystemExit("no Java for Prism: set instance JavaPath or JAVA_HOME")


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def wait_for_pack(url: str) -> None:
    deadline = time.time() + SERVE_WAIT_S
    last_error = ""
    while time.time() < deadline:
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=2) as response:
                if response.status == 200:
                    return
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
        time.sleep(0.25)
    raise SystemExit(f"packwiz serve did not become ready at {url}: {last_error}")


def start_serve(port: int) -> subprocess.Popen[str]:
    command = ["packwiz", "serve", "--refresh=false", "-p", str(port)]
    print("+", " ".join(command))
    kwargs: dict[str, object] = {
        "cwd": PACK_DIR,
        "stdout": subprocess.PIPE,
        "stderr": subprocess.STDOUT,
        "text": True,
    }
    if sys.platform == "win32":
        kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
    return subprocess.Popen(command, **kwargs)


def stop_serve(proc: subprocess.Popen[str]) -> None:
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=5)


def run_installer(java: str, bootstrap: Path, pack_url: str, minecraft: Path) -> None:
    command = [java, "-jar", str(bootstrap), "-g", pack_url]
    print("+", " ".join(command))
    result = subprocess.run(
        command,
        cwd=minecraft,
        check=False,
        timeout=INSTALLER_TIMEOUT_S,
    )
    if result.returncode != 0:
        raise SystemExit(
            f"packwiz-installer failed ({result.returncode}) in {minecraft.name}"
        )


def update_prism() -> Path | None:
    load_secrets()
    pack = read_pack(PACK_TOML)
    instance = find_instance(pack["name"])
    if instance is None:
        print(
            "Prism: skip (no instance named "
            f"{pack['name']!r}; set PRISM_INSTANCE_DIR in .env)"
        )
        return None
    minecraft = minecraft_dir(instance)
    java = resolve_java(instance)
    bootstrap = ensure_bootstrap(minecraft)
    port = free_port()
    pack_url = f"http://127.0.0.1:{port}/pack.toml"
    print(f"Prism instance {instance.name} ({pack['name']} {pack['pack_version']})")
    print(f"installer {pack_url}")
    proc = start_serve(port)
    try:
        wait_for_pack(pack_url)
        run_installer(java, bootstrap, pack_url, minecraft)
    finally:
        stop_serve(proc)
    print(f"Prism synced to pack {pack['pack_version']}")
    return instance


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    update_prism()


if __name__ == "__main__":
    main()
