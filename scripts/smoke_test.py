#!/usr/bin/env python3
"""Boot a local dedicated server from the current pack/ tree.

Default: boot, generate chunks with Chunk Pregenerator, record /tick query
metrics, and write docs/smoke-runs/. --skip-bench keeps the original
boot-only check. Never talks to the panel or .env panel credentials.
Never installs Spark (or anything else) into pack/mods/.
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
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from envfile import load_env_file
from pack_artifacts import DIST_DIR, USER_AGENT, build_server_mods_zip, dist_paths
from read_pack_versions import PACK_TOML, read_pack
import smoke_metrics as metrics

WORK_DIR = DIST_DIR / "_smoke-test"
REPORTS_DIR = ROOT / "docs" / "smoke-runs"
SPARK_CACHE = ROOT / ".cache" / "dev-tools"
INSTALLER_NAME = "neoforge-installer.jar"
BOOT_DONE = re.compile(r"Done \(|For help, type", re.I)
BOOT_BAD = re.compile(r"\bException\b|\[.*/ERROR\]|\[ERROR\]|\bFATAL\b")
UNKNOWN_COMMAND = re.compile(r"Unknown (?:or incomplete )?command", re.I)
DEFAULT_BOOT_TIMEOUT_S = 300
DEFAULT_BENCH_TIMEOUT_S = 900
DEFAULT_MEMORY_MB = 4096
DEFAULT_RADIUS = 8
TICK_INTERVAL_S = 12
STOP_WAIT_S = 60
MAVEN_INSTALLER = (
    "https://maven.neoforged.net/releases/net/neoforged/neoforge/"
    "{version}/neoforge-{version}-installer.jar"
)


@dataclass
class BenchState:
    boot_s: float | None = None
    spawn_elapsed_ms: int | None = None
    idle: metrics.TickSample | None = None
    mid: metrics.TickSample | None = None
    post: metrics.TickSample | None = None
    pregen_s: float | None = None
    chunks: int | None = None
    cps: float | None = None
    rss_idle_kb: int | None = None
    rss_mid_kb: int | None = None
    rss_post_kb: int | None = None
    world_bytes: int | None = None
    sparkprofile_path: str | None = None
    lines: list[str] = field(default_factory=list)
    fail_reason: str | None = None


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
                "level-seed=1",
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
    for folder in ("pointblank", "tacz"):
        extra = work / folder
        if extra.exists():
            shutil.rmtree(extra)

    with zipfile.ZipFile(paths["server_zip"]) as archive:
        for info in archive.infolist():
            name = info.filename.replace("\\", "/")
            if name.startswith("mods/") and name.lower().endswith(".jar"):
                archive.extract(info, work)
            if name.startswith(("pointblank/", "tacz/", "config/", "global_packs/")):
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


class LiveServer:
    def __init__(
        self,
        work: Path,
        java: str,
        timeout_s: int,
        memory_mb: int,
    ) -> None:
        self.work = work
        self.timeout_s = timeout_s
        self.lines: list[str] = []
        self.bad: list[str] = []
        env = os.environ.copy()
        env["SERVER_MEMORY"] = str(memory_mb)
        env["PATH"] = str(Path(java).parent) + os.pathsep + env.get("PATH", "")
        command = server_command(work, java, memory_mb)
        print(f"starting server in {work} (timeout {timeout_s}s, {memory_mb}M)")
        self.process = subprocess.Popen(
            command,
            cwd=work,
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
        )
        self.output: queue.Queue[str | None] = queue.Queue()
        self.deadline = time.monotonic() + timeout_s
        threading.Thread(target=self._reader, daemon=True).start()

    def _reader(self) -> None:
        assert self.process.stdout is not None
        try:
            for line in self.process.stdout:
                self.output.put(line)
        finally:
            self.output.put(None)

    def remaining(self) -> float:
        return self.deadline - time.monotonic()

    def rss_kb(self) -> int | None:
        if self.process.poll() is not None:
            return None
        return metrics.process_rss_kb(self.process.pid)

    def send(self, command: str) -> None:
        print(f"> {command}")
        assert self.process.stdin is not None
        self.process.stdin.write(command + "\n")
        self.process.stdin.flush()

    def _handle_line(self, line: str) -> None:
        self.lines.append(line)
        print(line, end="")
        if BOOT_BAD.search(line):
            self.bad.append(line)

    def wait_line(self, max_wait: float) -> str | None:
        """Return a log line, '' on timeout/idle, or None if the process died."""
        if self.process.poll() is not None and self.output.empty():
            return None
        wait = min(max_wait, 1.0)
        if self.remaining() > 0:
            wait = min(wait, max(self.remaining(), 0.05))
        try:
            line = self.output.get(timeout=wait)
        except queue.Empty:
            return ""
        if line is None:
            return None
        self._handle_line(line)
        return line

    def drain(self, seconds: float) -> None:
        until = time.monotonic() + seconds
        while time.monotonic() < until and self.remaining() > 0:
            line = self.wait_line(min(0.5, until - time.monotonic()))
            if line is None:
                return

    def wait_boot(self) -> str | None:
        """Return None on success, or a fail reason."""
        while True:
            if crash_reports(self.work):
                print("crash-report appeared")
                print(log_tail(self.lines))
                return "crash-report during boot"
            if self.remaining() <= 0:
                print("timeout waiting for boot-complete")
                print(log_tail(self.lines))
                if self.bad:
                    print("--- flagged lines ---")
                    print("".join(self.bad[-40:]))
                return "timeout waiting for boot-complete"
            if self.process.poll() is not None and self.output.empty():
                print(f"server exited {self.process.returncode} before boot-complete")
                print(log_tail(self.lines))
                return f"server exited {self.process.returncode} before boot-complete"
            line = self.wait_line(1.0)
            if line is None:
                print(f"server exited {self.process.returncode} before boot-complete")
                print(log_tail(self.lines))
                return f"server exited {self.process.returncode} before boot-complete"
            if line and BOOT_DONE.search(line):
                return None

    def wait_tick_query(self, wait_s: float = 15.0) -> metrics.TickSample | None:
        start_index = len(self.lines)
        try:
            self.send("tick query")
        except BrokenPipeError:
            return None
        until = time.monotonic() + wait_s
        found: metrics.TickSample | None = None
        while time.monotonic() < until and self.remaining() > 0:
            line = self.wait_line(min(0.5, until - time.monotonic()))
            if line is None:
                break
            sample = metrics.parse_tick_query("".join(self.lines[start_index:]))
            if sample and sample.p50_ms is not None:
                return sample
            if sample:
                found = sample
        return found or metrics.parse_tick_query("".join(self.lines[start_index:]))

    def stop(self, kill_ok: bool = False) -> int:
        if self.process.poll() is not None:
            return self.process.returncode or 1
        print("sending stop")
        try:
            self.send("stop")
        except BrokenPipeError:
            pass
        wait_s = 20 if kill_ok else STOP_WAIT_S
        until = time.monotonic() + wait_s
        while time.monotonic() < until:
            if self.process.poll() is not None:
                break
            self.wait_line(0.5)
        if self.process.poll() is None:
            self.process.kill()
            try:
                self.process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
            if kill_ok:
                print("killed leftover Java process after stop (Spark agent threads)")
            else:
                print("server did not stop after stop command")
                return 1
        if crash_reports(self.work):
            print("crash-report appeared after stop")
            print(log_tail(self.lines))
            return 1
        return 0

    def kill(self) -> None:
        if self.process.poll() is None:
            self.process.kill()
            try:
                self.process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass


def write_smoke_report(state: BenchState, passed: bool, note: str | None) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    index_path = REPORTS_DIR / "index.md"
    previous = metrics.previous_index_run(index_path)
    commit, change_note = metrics.collect_change_note(ROOT, previous, note)
    when = datetime.now(timezone.utc)
    stamp = metrics.report_stem(when)
    cant = metrics.summarize_cant_keep_up(state.lines)
    report = metrics.SmokeReport(
        timestamp=stamp,
        passed=passed,
        change_note=change_note,
        note=note,
        boot_s=state.boot_s,
        spawn_elapsed_ms=state.spawn_elapsed_ms,
        idle=state.idle,
        mid=state.mid,
        post=state.post,
        pregen_s=state.pregen_s,
        chunks=state.chunks,
        cps=state.cps,
        cant_keep_up=cant,
        rss_idle_kb=state.rss_idle_kb,
        rss_mid_kb=state.rss_mid_kb,
        rss_post_kb=state.rss_post_kb,
        world_bytes=state.world_bytes,
        sparkprofile_path=state.sparkprofile_path,
        log_tail=None
        if passed
        else ((state.fail_reason + "\n") if state.fail_reason else "") + log_tail(state.lines),
    )
    path = REPORTS_DIR / f"{stamp}.md"
    path.write_text(metrics.render_report(report), encoding="utf-8")
    cps_summary = f"{state.cps:.2f}" if state.cps is not None else "—"
    metrics.insert_index_row(
        index_path,
        metrics.IndexRow(
            timestamp=stamp,
            commit=commit,
            passed=passed,
            tps_summary=metrics.tps_index_summary(state.idle, state.mid, state.post),
            cps_summary=cps_summary,
            report_rel=path.name,
        ),
    )
    print(f"wrote {path.relative_to(ROOT)}")
    return path


def _fail(state: BenchState, reason: str) -> str:
    print(reason)
    print(log_tail(state.lines))
    state.fail_reason = reason
    return reason


def run_benchmark(
    server: LiveServer,
    state: BenchState,
    radius: int,
    profile: bool,
) -> str | None:
    """Return a fail reason, or None on success."""
    state.spawn_elapsed_ms = metrics.parse_spawn_elapsed_ms(state.lines)
    server.drain(5.0)
    if crash_reports(server.work):
        return _fail(state, "crash-report after boot")
    if server.remaining() <= 0:
        return _fail(state, "timeout after boot")

    state.idle = server.wait_tick_query()
    state.rss_idle_kb = server.rss_kb()
    if state.idle is None:
        print("warning: idle /tick query did not parse")

    if profile:
        window = min(180, max(60, int(server.remaining()) - 90))
        seen_profiles = set(server.work.rglob("*.sparkprofile"))
        try:
            server.send(f"spark profiler start --timeout {window}")
        except BrokenPipeError:
            return _fail(state, "server closed stdin before spark start")
        server.drain(2.0)

    pregen_cmd = f"pregen start gen radius smoketest SQUARE 0 0 {radius}"
    pregen_started = time.monotonic()
    try:
        server.send(pregen_cmd)
        server.drain(1.0)
        server.send("pregen info listen")
    except BrokenPipeError:
        return _fail(state, "server closed stdin before pregen")

    next_tick = time.monotonic() + TICK_INTERVAL_S
    finished = False
    last_progress: metrics.PregenProgress | None = None
    last_logged: tuple[int, int] | None = None
    complete_since: float | None = None

    while not finished:
        if crash_reports(server.work):
            return _fail(state, "crash-report during pregen")
        if server.remaining() <= 0:
            return _fail(state, "timeout during pregen")
        if server.process.poll() is not None:
            return _fail(
                state,
                f"server exited {server.process.returncode} during pregen",
            )
        line = server.wait_line(0.5)
        if line is None:
            return _fail(
                state,
                f"server exited {server.process.returncode} during pregen",
            )
        if line:
            if UNKNOWN_COMMAND.search(line) and "pregen" in "".join(state.lines[-8:]).lower():
                return _fail(state, "pregen command was not recognized")
            progress = metrics.parse_pregen_progress(line)
            if progress:
                last_progress = progress
                logged = (progress.done, progress.total)
                if logged != last_logged:
                    print(f"pregen {progress.done}/{progress.total} chunks", flush=True)
                    last_logged = logged
                if progress.total > 0 and progress.done >= progress.total:
                    if complete_since is None:
                        complete_since = time.monotonic()
                else:
                    complete_since = None
            if metrics.parse_pregen_finished(line):
                finished = True
                break
        if any(metrics.parse_pregen_finished(item) for item in server.lines):
            finished = True
            break
        if complete_since is not None and time.monotonic() - complete_since >= 8.0:
            finished = True
            break
        if time.monotonic() >= next_tick:
            sample = server.wait_tick_query()
            if sample and state.mid is None:
                state.mid = sample
                state.rss_mid_kb = server.rss_kb()
            next_tick = time.monotonic() + TICK_INTERVAL_S

    state.pregen_s = time.monotonic() - pregen_started
    done, total = metrics.latest_pregen_total(state.lines)
    if done is not None and total is not None and done >= total:
        state.chunks = total
    elif last_progress is not None:
        state.chunks = last_progress.total if last_progress.done >= last_progress.total else None
    finished_chunks = None
    for line in state.lines:
        parsed = metrics.parse_pregen_finished(line)
        if parsed:
            finished_chunks = parsed.chunks
    if finished_chunks is not None:
        state.chunks = finished_chunks
    state.cps = metrics.average_cps(state.chunks, state.pregen_s)

    server.drain(3.0)
    state.post = server.wait_tick_query()
    state.rss_post_kb = server.rss_kb()

    if profile:
        try:
            server.send("spark profiler stop --save-to-file")
        except BrokenPipeError:
            print("warning: could not stop spark profiler")
        until = time.monotonic() + 20.0
        while time.monotonic() < until and server.remaining() > 0:
            line = server.wait_line(0.5)
            if line is None:
                break
            written = metrics.parse_spark_written(line) if line else None
            if written:
                state.sparkprofile_path = str(written)
                break
            found = metrics.find_sparkprofile(server.work, after=seen_profiles)
            if found:
                state.sparkprofile_path = str(found)
                break
        if not state.sparkprofile_path:
            found = metrics.find_sparkprofile(server.work, after=seen_profiles)
            if found:
                state.sparkprofile_path = str(found)
            else:
                print("warning: spark profiler produced no .sparkprofile file")
        try:
            server.send("spark profiler cancel")
        except BrokenPipeError:
            pass
        server.drain(2.0)

    if state.chunks is None:
        return _fail(state, "pregen finished without a chunk count in the log")
    return None


def run_server(
    work: Path,
    java: str,
    timeout_s: int,
    memory_mb: int,
    skip_bench: bool,
    radius: int,
    profile: bool,
    note: str | None,
) -> int:
    state = BenchState()
    server = LiveServer(work, java, timeout_s, memory_mb)
    try:
        boot_started = time.monotonic()
        boot_fail = server.wait_boot()
        state.lines = server.lines
        state.boot_s = time.monotonic() - boot_started
        if boot_fail:
            state.fail_reason = boot_fail
            if not skip_bench:
                write_smoke_report(state, passed=False, note=note)
            return 1
        if skip_bench:
            print("boot-complete")
            code = server.stop()
            if code == 0:
                print("smoke test passed")
            return code

        print("boot-complete; starting pregen benchmark")
        bench_fail = run_benchmark(server, state, radius, profile)
        state.lines = server.lines
        stop_code = server.stop(kill_ok=profile)
        state.world_bytes = metrics.dir_size_bytes(work / "world")
        if bench_fail:
            write_smoke_report(state, passed=False, note=note)
            return 1
        if stop_code != 0:
            state.fail_reason = "server did not stop cleanly"
            write_smoke_report(state, passed=False, note=note)
            return stop_code
        write_smoke_report(state, passed=True, note=note)
        print("smoke test passed")
        return 0
    finally:
        state.lines = server.lines
        server.kill()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Boot the current pack locally. Default: generate chunks and write "
            "a docs/smoke-runs/ report. Use --skip-bench for a boot-only check."
        )
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=None,
        help=(
            f"seconds for the whole run (default {DEFAULT_BOOT_TIMEOUT_S} with "
            f"--skip-bench, {DEFAULT_BENCH_TIMEOUT_S} otherwise)"
        ),
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
        help="do not wipe dist/_smoke-test/world after a successful run",
    )
    parser.add_argument(
        "--skip-bench",
        action="store_true",
        help="boot-only check: no pregen, no report",
    )
    parser.add_argument(
        "--radius",
        type=int,
        default=DEFAULT_RADIUS,
        help=f"Chunk Pregenerator radius (default {DEFAULT_RADIUS})",
    )
    parser.add_argument(
        "--note",
        default=None,
        help="free-text note stored in the smoke-run report",
    )
    parser.add_argument(
        "--profile",
        action="store_true",
        help=(
            "copy a gitignored Spark jar into the throwaway server and save a "
            ".sparkprofile during pregen (not a pack mod)"
        ),
    )
    return parser.parse_args(argv)


def wipe_runtime(work: Path) -> None:
    for name in ("world", "logs", "crash-reports"):
        path = work / name
        if path.is_dir():
            shutil.rmtree(path)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    load_env_file(ROOT / ".env")
    args = parse_args()
    if args.profile and args.skip_bench:
        print("warning: --profile implies a benchmark; ignoring --skip-bench")
        args.skip_bench = False
    if args.timeout is None:
        args.timeout = (
            DEFAULT_BOOT_TIMEOUT_S if args.skip_bench else DEFAULT_BENCH_TIMEOUT_S
        )
    pack = read_pack(PACK_TOML)
    java = find_java()
    print(f"java {java}")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    code = 1
    try:
        install_neoforge(pack, WORK_DIR, java)
        sync_overlay_and_mods(pack, WORK_DIR)
        if args.profile:
            jar = metrics.ensure_spark_jar(SPARK_CACHE)
            copied = metrics.copy_spark_into_mods(jar, WORK_DIR / "mods")
            print(f"copied Spark into throwaway mods: {copied}")
        write_eula_and_properties(WORK_DIR, free_port())
        wipe_runtime(WORK_DIR)
        code = run_server(
            WORK_DIR,
            java,
            args.timeout,
            args.memory,
            skip_bench=args.skip_bench,
            radius=args.radius,
            profile=args.profile,
            note=args.note,
        )
    except KeyboardInterrupt:
        code = 130
    if not args.keep and code == 0:
        wipe_runtime(WORK_DIR)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
