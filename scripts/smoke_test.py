#!/usr/bin/env python3
"""Boot a local dedicated server from the current pack/ tree.

Never talks to the panel, .env panel credentials, or any remote host besides
Maven / mod download URLs already used by pack_artifacts. Exit 0 on a clean
boot, non-zero on crash or timeout.
"""

from __future__ import annotations

import argparse
import os
import queue
import re
import shutil
import socket
import subprocess
import sys
import threading
import time
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from envfile import load_env_file
from pack_artifacts import DIST_DIR, USER_AGENT, build_server_mods_zip, dist_paths
from read_pack_versions import PACK_TOML, read_pack

WORK_DIR = DIST_DIR / "_smoke-test"
INSTALLER_NAME = "neoforge-installer.jar"
BOOT_DONE = re.compile(r"Done \(|For help, type", re.I)
BOOT_BAD = re.compile(r"\bException\b|\[.*/ERROR\]|\[ERROR\]|\bFATAL\b")
DEFAULT_TIMEOUT_S = 300
DEFAULT_MEMORY_MB = 4096
MAVEN_INSTALLER = (
    "https://maven.neoforged.net/releases/net/neoforged/neoforge/"
    "{version}/neoforge-{version}-installer.jar"
)


def java_major(java: str) -> int | None:
    result = subprocess.run(
        [java, "-version"],
        check=False,
        capture_output=True,
        text=True,
    )
    text = f"{result.stderr}\n{result.stdout}"
    match = re.search(r'version "(\d+)', text)
    return int(match.group(1)) if match else None


def find_java() -> str:
    home = os.environ.get("JAVA_HOME", "").strip()
    candidates: list[str] = []
    if home:
        for name in ("java", "java.exe"):
            candidate = Path(home) / "bin" / name
            if candidate.is_file():
                candidates.append(str(candidate))
    which = shutil.which("java")
    if which:
        candidates.append(which)
    brew = Path("/opt/homebrew/opt/openjdk@21/bin/java")
    if brew.is_file():
        candidates.append(str(brew))
    seen: set[str] = set()
    for java in candidates:
        if java in seen:
            continue
        seen.add(java)
        major = java_major(java)
        if major is not None and major >= 21:
            return java
        if major is not None:
            print(f"skipping Java {major} at {java}; need 21+")
    raise SystemExit(
        "no Java 21 on PATH or JAVA_HOME; install Java 21 or set JAVA_HOME"
    )


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def download(url: str, dest: Path) -> None:
    print(f"downloading {url}")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=180) as response:
        dest.write_bytes(response.read())


def install_neoforge(pack: dict[str, str], work: Path, java: str) -> None:
    if pack["loader"].lower() != "neoforge":
        raise SystemExit(f"local smoke test expects NeoForge, got {pack['loader']!r}")
    version = pack["loader_version"]
    stamp = work / ".neoforge-version"
    unix_args = list(work.glob("libraries/net/neoforged/neoforge/*/unix_args.txt"))
    if stamp.read_text(encoding="utf-8").strip() == version if stamp.is_file() else False:
        if unix_args:
            print(f"reusing NeoForge {version} in {work}")
            return
    installer = work / INSTALLER_NAME
    download(MAVEN_INSTALLER.format(version=version), installer)
    print(f"installing NeoForge {version}")
    result = subprocess.run(
        [java, "-jar", str(installer), "--installServer"],
        cwd=work,
        check=False,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"NeoForge installer failed with exit {result.returncode}")
    stamp.write_text(version + "\n", encoding="utf-8")


def write_eula_and_properties(work: Path, port: int) -> None:
    (work / "eula.txt").write_text("eula=true\n", encoding="utf-8")
    (work / "server.properties").write_text(
        "\n".join(
            [
                "online-mode=false",
                "sync-chunk-writes=false",
                f"server-port={port}",
                "server-ip=127.0.0.1",
                "motd=Lead and Leylines smoke test",
                "max-tick-time=-1",
                "spawn-protection=0",
                "",
            ]
        ),
        encoding="utf-8",
    )


def sync_overlay_and_mods(pack: dict[str, str], work: Path) -> None:
    jvm_args = ROOT / "pack" / "user_jvm_args.txt"
    run_sh = ROOT / "server" / "run.sh"
    if not jvm_args.is_file() or not run_sh.is_file():
        raise SystemExit("missing pack/user_jvm_args.txt or server/run.sh")
    shutil.copy2(jvm_args, work / "user_jvm_args.txt")
    shutil.copy2(run_sh, work / "run.sh")
    os.chmod(work / "run.sh", 0o755)
    paths = dist_paths(pack)
    print("assembling server-side mods")
    build_server_mods_zip(pack, paths["server_zip"])
    mods_dir = work / "mods"
    if mods_dir.exists():
        shutil.rmtree(mods_dir)
    mods_dir.mkdir(parents=True)

    with zipfile.ZipFile(paths["server_zip"]) as archive:
        for info in archive.infolist():
            name = info.filename.replace("\\", "/")
            if name.startswith("mods/") and name.lower().endswith(".jar"):
                archive.extract(info, work)
            if name.startswith("config/") or name.startswith("global_packs/"):
                archive.extract(info, work)


def crash_reports(work: Path) -> list[Path]:
    folder = work / "crash-reports"
    if not folder.is_dir():
        return []
    return sorted(path for path in folder.iterdir() if path.is_file())


def log_tail(lines: list[str], count: int = 80) -> str:
    return "".join(lines[-count:])


def server_command(work: Path, java: str, memory_mb: int) -> list[str]:
    """Dedicated boot: run.sh on Unix; Java + win_args.txt on Windows (no WSL)."""
    if os.name != "nt":
        return ["bash", "run.sh"]
    matches = list(work.glob("libraries/net/neoforged/neoforge/*/win_args.txt"))
    if not matches:
        raise SystemExit("missing win_args.txt; NeoForge is not installed yet")
    win_args = matches[0].relative_to(work).as_posix()
    return [
        java,
        "-Xms128M",
        f"-Xmx{memory_mb}M",
        "@user_jvm_args.txt",
        f"@{win_args}",
        "nogui",
    ]


def run_server(
    work: Path,
    java: str,
    timeout_s: int,
    memory_mb: int,
) -> int:
    env = os.environ.copy()
    env["SERVER_MEMORY"] = str(memory_mb)
    # Overlay run.sh execs `java`; put the resolved binary first on PATH.
    env["PATH"] = str(Path(java).parent) + os.pathsep + env.get("PATH", "")
    command = server_command(work, java, memory_mb)
    print(f"starting server in {work} (timeout {timeout_s}s, {memory_mb}M)")
    process = subprocess.Popen(
        command,
        cwd=work,
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    lines: list[str] = []
    bad: list[str] = []
    booted = False
    deadline = time.monotonic() + timeout_s
    output: queue.Queue[str | None] = queue.Queue()

    def _reader() -> None:
        assert process.stdout is not None
        try:
            for line in process.stdout:
                output.put(line)
        finally:
            output.put(None)

    threading.Thread(target=_reader, daemon=True).start()
    try:
        while True:
            if crash_reports(work):
                print("crash-report appeared")
                print(log_tail(lines))
                return 1
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                print("timeout waiting for boot-complete")
                print(log_tail(lines))
                if bad:
                    print("--- flagged lines ---")
                    print("".join(bad[-40:]))
                return 1
            if process.poll() is not None and output.empty():
                print(f"server exited {process.returncode} before boot-complete")
                print(log_tail(lines))
                return process.returncode or 1
            try:
                line = output.get(timeout=min(1.0, max(remaining, 0.1)))
            except queue.Empty:
                continue
            if line is None:
                print(f"server exited {process.returncode} before boot-complete")
                print(log_tail(lines))
                return process.returncode or 1
            lines.append(line)
            print(line, end="")
            if BOOT_BAD.search(line):
                bad.append(line)
            if BOOT_DONE.search(line):
                booted = True
                break
        if not booted:
            print("timeout waiting for boot-complete")
            print(log_tail(lines))
            return 1
        print("boot-complete; sending stop")
        assert process.stdin is not None
        try:
            process.stdin.write("stop\n")
            process.stdin.flush()
        except BrokenPipeError:
            pass
        try:
            process.wait(timeout=60)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=10)
            print("server did not stop after stop command")
            return 1
        if crash_reports(work):
            print("crash-report appeared after stop")
            print(log_tail(lines))
            return 1
        print("smoke test passed")
        return 0
    finally:
        if process.poll() is None:
            process.kill()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    load_env_file(ROOT / ".env")
    parser = argparse.ArgumentParser(
        description="Boot the current pack locally and wait for a clean dedicated-server start."
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT_S,
        help=f"seconds to wait for boot-complete (default {DEFAULT_TIMEOUT_S})",
    )
    parser.add_argument(
        "--memory",
        type=int,
        default=DEFAULT_MEMORY_MB,
        help=f"server Xmx megabytes (default {DEFAULT_MEMORY_MB})",
    )
    parser.add_argument(
        "--keep",
        action="store_true",
        help="leave dist/_smoke-test in place after the run",
    )
    args = parser.parse_args()
    pack = read_pack(PACK_TOML)
    java = find_java()
    print(f"java {java}")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    try:
        install_neoforge(pack, WORK_DIR, java)
        sync_overlay_and_mods(pack, WORK_DIR)
        write_eula_and_properties(WORK_DIR, free_port())
        code = run_server(WORK_DIR, java, args.timeout, args.memory)
    except KeyboardInterrupt:
        code = 130
    if not args.keep and code == 0:
        # Keep the NeoForge install cache; only drop world and logs.
        for name in ("world", "logs", "crash-reports"):
            path = WORK_DIR / name
            if path.is_dir():
                shutil.rmtree(path)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
