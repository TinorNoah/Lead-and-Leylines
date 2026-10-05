#!/usr/bin/env python3
"""Benchmark the save path across a set of configurations.

Purpose
-------
`scripts/smoke_test.py` measures boot time, `/tick query`, `/neoforge generate`
CPS, and RSS. It never issues `save-all`, never times a flush, and never
measures how long shutdown takes. So it cannot answer "which chunk-save
optimizer is worth keeping". This script can.

What it measures, per configuration
-----------------------------------
1. `flush_ms`   — wall time for `save-all flush` to return, sampled N times.
                  This is the chunk-save latency a player feels as a stall.
2. `stop_ms`    — wall time from the `stop` command to process exit. Shutdown
                  forces a full synchronous save, so this is the worst case.
3. `tick_*`     — MSPT percentiles from `/tick query` taken right after a
                  flush, to catch a save that offloads work onto the tick loop
                  instead of removing it.
4. `integrity`  — chunk file count and total world bytes after shutdown, plus
                  whether the server logged any save error. A config that
                  saves faster but loses chunks fails here.
5. `worst_flush_ms` / `flush_spread` — reliability across repeats, not just the
                  best run. An optimizer with a long tail is worse than a
                  steady one even at equal mean.

Why repeats matter
------------------
Single smoke runs on this pack have varied between ~15.9 and ~21.2 average CPS
and ~68s to ~95s boot time with no code change (docs/smoke-runs/2026-10-05T*).
That variance is larger than most effects worth measuring. Every configuration
therefore runs `--trials` times against an identical pre-generated world, and
results are reported as a median across trials plus the observed spread.

World state
-----------
The world is generated ONCE, by the baseline configuration, and then copied for
every trial. Comparing saves against a freshly generated world each time would
measure worldgen, not saving. Each trial gets a private copy so trials cannot
contaminate each other.

This script does not modify the pack. It builds the server mod set from the
packwiz index the same way smoke_test.py does, then removes or keeps specific
jars to form each configuration.
"""

from __future__ import annotations

import argparse
import json
import os
import queue
import re
import shutil
import statistics
import subprocess
import sys
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pack_artifacts import DIST_DIR, build_server_mods_zip, dist_paths
from read_pack_versions import PACK_TOML, read_pack
import smoke_metrics as metrics
from smoke_test import find_java, free_port, server_command, write_eula_and_properties

BENCH_ROOT = DIST_DIR / "_save-bench"
BASELINE_WORLD = BENCH_ROOT / "baseline-world"

BOOT_DONE = re.compile(r"Done \(|For help, type", re.I)
# Deliberately narrow. A first attempt matched "corrupt" anywhere in a line and
# flagged the unrelated `forbidden_arcanus:corrupt_lost_soul` "has no attributes"
# error as a save failure. Only phrases the server actually emits on a failed
# write count here.
SAVE_ERROR = re.compile(
    r"Failed to save|Exception saving|Could not save|Error saving chunk|"
    r"Failed to write|Region file.*(corrupt|invalid)|"
    r"java\.io\.(FileNotFoundException|IOException).*region",
    re.I,
)
# Lines that indicate a save actually started/finished, used only for logging
# what the server did rather than as the primary timing signal (we time the
# command round trip against the server's own acknowledgement).
SAVE_ACK = re.compile(r"Saved the game|All dimensions are saved", re.I)

DEFAULT_MEMORY_MB = 8192
DEFAULT_TRIALS = 3
DEFAULT_FLUSHES = 4

# Jars that form the save-path stack under test. Keyed by the jar filename as it
# appears in the packwiz manifest, because that is what actually lands in
# dist/_smoke-test/mods.
SAVE_STACK = {
    "c2me": "c2me-neoforge-mc1.21.1-0.4.0-alpha.0.122.jar",
    "smoothchunk": "smoothchunk-1.21-4.1.jar",
    "fastasyncworldsave": "fastasyncworldsave-1.21-2.6.jar",
}
# Cupboard is a hard dependency of fastasyncworldsave (verified from its
# neoforge.mods.toml) and of six other mods in the pack, so it stays in every
# configuration. Smooth Chunk Save was removed from the pack on 2026-10-05 after
# this benchmark showed it slower than running nothing; it is kept here only so
# the historical configurations stay reproducible.
SHARED_KEEP = {"cupboard-1.21.1-4.2.jar"}


@dataclass
class TrialResult:
    label: str
    trial: int
    flush_ms: list[float] = field(default_factory=list)
    stop_ms: float | None = None
    tick_after_flush: metrics.TickSample | None = None
    world_bytes: int | None = None
    region_files: int | None = None
    save_errors: list[str] = field(default_factory=list)
    exit_code: int | None = None
    stopped_cleanly: bool = False

    def to_json(self) -> dict:
        return {
            "label": self.label,
            "trial": self.trial,
            "flush_ms": [round(x, 1) for x in self.flush_ms],
            "flush_median_ms": round(statistics.median(self.flush_ms), 1) if self.flush_ms else None,
            "flush_max_ms": round(max(self.flush_ms), 1) if self.flush_ms else None,
            "stop_ms": round(self.stop_ms, 1) if self.stop_ms else None,
            "mspt_p95_after_flush": self.tick_after_flush.p95_ms if self.tick_after_flush else None,
            "mspt_p99_after_flush": self.tick_after_flush.p99_ms if self.tick_after_flush else None,
            "world_bytes": self.world_bytes,
            "region_files": self.region_files,
            "save_errors": self.save_errors[:5],
            "exit_code": self.exit_code,
            "stopped_cleanly": self.stopped_cleanly,
        }


class BenchServer:
    """Minimal server driver: boot, flush, tick query, stop. No pregen."""

    def __init__(self, work: Path, java: str, memory_mb: int, timeout_s: int) -> None:
        self.work = work
        self.timeout_s = timeout_s
        self.deadline = time.monotonic() + timeout_s
        self.lines: list[str] = []
        env = os.environ.copy()
        env["SERVER_MEMORY"] = str(memory_mb)
        env["PATH"] = str(Path(java).parent) + os.pathsep + env.get("PATH", "")
        self.process = subprocess.Popen(
            server_command(work, java, memory_mb),
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

    def _next_line(self, max_wait: float) -> str | None:
        if self.process.poll() is not None and self.output.empty():
            return None
        wait = min(max_wait, 0.5)
        if self.remaining() > 0:
            wait = min(wait, max(self.remaining(), 0.05))
        try:
            line = self.output.get(timeout=wait)
        except queue.Empty:
            return ""
        if line is None:
            return None
        self.lines.append(line)
        return line

    def send(self, command: str) -> None:
        print(f"    > {command}", flush=True)
        assert self.process.stdin is not None
        self.process.stdin.write(command + "\n")
        self.process.stdin.flush()

    def wait_boot(self) -> str | None:
        while True:
            if self.remaining() <= 0:
                return "timeout waiting for boot"
            if self.process.poll() is not None and self.output.empty():
                return f"server exited {self.process.returncode} before boot"
            line = self._next_line(1.0)
            if line is None:
                return f"server exited {self.process.returncode} before boot"
            if line and BOOT_DONE.search(line):
                return None

    def drain_quiet(self, seconds: float = 1.0) -> None:
        """Absorb output already in flight so a later wait cannot match it."""
        until = time.monotonic() + seconds
        while time.monotonic() < until:
            line = self._next_line(0.1)
            if line is None:
                return

    def timed_flush(self, max_wait: float) -> float | None:
        """Time `save-all flush` until the server reports the save completed.

        Output is drained first. Without that, a second flush returns ~0ms
        because it matches the *previous* flush's acknowledgement still sitting
        in the buffer, which is exactly what the first run of this script did.
        """
        self.drain_quiet(1.5)
        start_index = len(self.lines)
        start = time.monotonic()
        self.send("save-all flush")
        while time.monotonic() - start < max_wait and self.remaining() > 0:
            line = self._next_line(0.1)
            if line is None:
                return None
            if SAVE_ACK.search("".join(self.lines[start_index:])):
                return (time.monotonic() - start) * 1000.0
        return None

    def tick_query(self, wait_s: float = 20.0) -> metrics.TickSample | None:
        start_index = len(self.lines)
        try:
            self.send("tick query")
        except BrokenPipeError:
            return None
        until = time.monotonic() + wait_s
        found: metrics.TickSample | None = None
        while time.monotonic() < until and self.remaining() > 0:
            line = self._next_line(0.25)
            if line is None:
                break
            sample = metrics.parse_tick_query("".join(self.lines[start_index:]))
            if sample and sample.p50_ms is not None:
                return sample
            if sample:
                found = sample
        return found or metrics.parse_tick_query("".join(self.lines[start_index:]))

    def timed_stop(self, max_wait: float) -> tuple[float | None, bool, int | None]:
        start = time.monotonic()
        try:
            self.send("stop")
        except BrokenPipeError:
            pass
        until = time.monotonic() + max_wait
        while time.monotonic() < until:
            if self.process.poll() is not None:
                break
            self._next_line(0.25)
        if self.process.poll() is None:
            self.process.kill()
            try:
                self.process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                pass
            return (time.monotonic() - start) * 1000.0, False, self.process.returncode
        elapsed = (time.monotonic() - start) * 1000.0
        try:
            code = self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            code = self.process.returncode
        return elapsed, True, code

    def save_errors(self) -> list[str]:
        return [line for line in self.lines if SAVE_ERROR.search(line)]


def assemble_server(pack: dict[str, str], dest: Path) -> Path:
    """Build a fresh server directory with the same mods smoke_test uses."""
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    write_eula_and_properties(dest, free_port())
    shutil.copy2(ROOT / "pack" / "user_jvm_args.txt", dest / "user_jvm_args.txt")
    run_sh = ROOT / "server" / "run.sh"
    shutil.copy2(run_sh, dest / "run.sh")
    os.chmod(dest / "run.sh", 0o755)
    paths = dist_paths(pack)
    build_server_mods_zip(pack, paths["server_zip"])
    mods_dir = dest / "mods"
    mods_dir.mkdir()
    import zipfile

    with zipfile.ZipFile(paths["server_zip"]) as archive:
        for info in archive.infolist():
            name = info.filename.replace("\\", "/")
            if name.startswith("mods/") and name.lower().endswith(".jar"):
                archive.extract(info, dest)
            if name.startswith(("pointblank/", "tacz/", "config/", "global_packs/")):
                archive.extract(info, dest)
    return dest


def install_neoforge(work: Path, pack: dict[str, str], java: str) -> None:
    """Install the pinned NeoForge into a prepared work dir.

    Delegates to smoke_test.install_neoforge so the version pin, the
    `.neoforge-version` stamp, and the MAVEN_INSTALLER URL stay in one place.
    """
    from smoke_test import install_neoforge as smoke_install

    smoke_install(pack, work, java)


def apply_config(work: Path, pack_config: Path) -> None:
    if pack_config.is_dir():
        dest = work / "config"
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(pack_config, dest)


def set_mods(work: Path, keep: set[str]) -> None:
    """Remove every save-stack jar not in `keep`, so the config is exact."""
    mods = work / "mods"
    for key, jar in SAVE_STACK.items():
        target = mods / jar
        if target.is_file() and jar not in keep:
            target.unlink()
            print(f"    removed {jar}")
    for jar in SHARED_KEEP:
        assert (mods / jar).is_file(), f"shared dep missing: {jar}"


def world_stats(work: Path) -> tuple[int, int]:
    world = work / "world"
    if not world.is_dir():
        return (0, 0)
    total = 0
    regions = 0
    for path in world.rglob("*.mca"):
        total += path.stat().st_size
        regions += 1
    return (total, regions)


def generate_baseline_world(work: Path, java: str, memory_mb: int, radius: int, timeout_s: int) -> None:
    """Boot with the full stack and pregen, then keep that world for all trials."""
    if BASELINE_WORLD.exists():
        print(f"reusing baseline world at {BASELINE_WORLD}")
        return
    print("generating baseline world with the full save stack (this is slow once)")
    # A world left in the template from an earlier run carries session.lock, and
    # the next boot refuses to start. The baseline world lives at BASELINE_WORLD,
    # so the template never needs one.
    stale = work / "world"
    if stale.exists():
        shutil.rmtree(stale)
    server = BenchServer(work, java, memory_mb, timeout_s)
    reason = server.wait_boot()
    if reason:
        raise SystemExit(f"baseline boot failed: {reason}")
    # Same command shape smoke_test.py uses: /neoforge generate start x y z radius <skip>
    print(f"  generating radius {radius}", flush=True)
    server.send(f"neoforge generate start 0 0 0 {radius} false")
    start_index = len(server.lines)
    finished = False
    complete_since: float | None = None
    last_logged: tuple[int, int] | None = None
    gen_deadline = time.monotonic() + 1800
    next_status = time.monotonic() + 5.0
    while not finished and time.monotonic() < gen_deadline and server.remaining() > 0:
        line = server._next_line(0.5)
        if line is None:
            raise SystemExit("server died during generation")
        if line and metrics.parse_pregen_finished(line):
            finished = True
            break
        if time.monotonic() >= next_status:
            try:
                server.send("neoforge generate status")
            except BrokenPipeError:
                raise SystemExit("server closed stdin during generation status")
            next_status = time.monotonic() + 5.0
        progress = metrics.parse_pregen_progress(line)
        if progress:
            if (progress.done, progress.total) != last_logged:
                print(f"  pregen {progress.done}/{progress.total} chunks", flush=True)
                last_logged = (progress.done, progress.total)
            if progress.total > 0 and progress.done >= progress.total:
                # Require the count to hold at total for a few seconds. Matching
                # a bare "generated N chunks" line instead declared completion
                # after 32 of 2401 chunks and left generation running into `stop`.
                if complete_since is None:
                    complete_since = time.monotonic()
            else:
                complete_since = None
        if complete_since is not None and time.monotonic() - complete_since >= 8.0:
            finished = True
    if not finished:
        raise SystemExit("baseline generation did not finish in time")
    done, total = metrics.latest_pregen_total(server.lines[start_index:])
    print(f"  generated {done}/{total} chunks", flush=True)
    if done is None or (total and done < total):
        raise SystemExit(f"baseline generation incomplete: {done}/{total}")
    elapsed, clean, code = server.timed_stop(180)
    print(f"  baseline stopped in {elapsed/1000:.1f}s clean={clean} exit={code}")
    generated = work / "world"
    if not generated.is_dir():
        raise SystemExit("baseline world was not created")
    shutil.copytree(generated, BASELINE_WORLD)


def run_trial(
    label: str,
    trial: int,
    template: Path,
    keep: set[str],
    pack: dict[str, str],
    java: str,
    memory_mb: int,
    flushes: int,
    timeout_s: int,
) -> TrialResult:
    work = BENCH_ROOT / f"{label}-trial{trial}"
    if work.exists():
        shutil.rmtree(work)
    shutil.copytree(template, work, symlinks=True)
    if (work / "world").exists():
        shutil.rmtree(work / "world")
    shutil.copytree(BASELINE_WORLD, work / "world")
    set_mods(work, keep)
    result = TrialResult(label=label, trial=trial)
    print(f"  [{label} trial {trial}] booting", flush=True)
    server = BenchServer(work, java, memory_mb, timeout_s)
    reason = server.wait_boot()
    if reason:
        result.save_errors.append(f"boot: {reason}")
        return result
    for i in range(flushes):
        ms = server.timed_flush(120)
        if ms is None:
            result.save_errors.append(f"flush {i} did not complete")
            break
        result.flush_ms.append(ms)
        print(f"    flush {i}: {ms:.0f} ms", flush=True)
    if result.flush_ms:
        result.tick_after_flush = server.tick_query()
    result.stop_ms, result.stopped_cleanly, result.exit_code = server.timed_stop(180)
    result.save_errors.extend(server.save_errors())
    result.world_bytes, result.region_files = world_stats(work)
    print(
        f"    stop {result.stop_ms/1000:.1f}s clean={result.stopped_cleanly} "
        f"world={result.world_bytes} regions={result.region_files} errors={len(result.save_errors)}",
        flush=True,
    )
    shutil.rmtree(work, ignore_errors=True)
    return result


def summarize(results: list[TrialResult]) -> None:
    print("\n=== save-path benchmark summary ===")
    by_label: dict[str, list[TrialResult]] = {}
    for r in results:
        by_label.setdefault(r.label, []).append(r)
    def ms(values: list[float]) -> str:
        return f"{statistics.median(values):.0f}" if values else "n/a"

    def secs(values: list[float]) -> str:
        return f"{statistics.median(values) / 1000:.1f}" if values else "n/a"

    # Only the FIRST flush after boot does real work: the world was just
    # generated or copied, so every chunk is dirty. Flushing again saves almost
    # nothing (measured 183-235 ms vs 8676 ms on the same config). So flush[0] is
    # the headline number and later flushes only prove the mod is not deferring
    # work indefinitely.
    print(
        f"{'config':<20} {'trials':>7} {'flush0 med':>11} {'flush0 max':>11} "
        f"{'flush0 min':>11} {'stop med':>9} {'errors':>7} {'regions':>8}"
    )
    for label, rows in by_label.items():
        firsts = [r.flush_ms[0] for r in rows if r.flush_ms]
        stops = [r.stop_ms for r in rows if r.stop_ms is not None]
        errs = sum(len(r.save_errors) for r in rows)
        regions = [r.region_files for r in rows if r.region_files is not None]
        region_med = f"{statistics.median(regions):.0f}" if regions else "0"
        print(
            f"{label:<20} {len(rows):>7} {ms(firsts):>11} "
            f"{f'{max(firsts):.0f}' if firsts else 'n/a':>11} "
            f"{f'{min(firsts):.0f}' if firsts else 'n/a':>11} "
            f"{secs(stops):>9} {errs:>7} {region_med:>8}"
        )
        print(
            f"{'':<20}   per-trial flush0 (ms): "
            + "; ".join(
                f"t{r.trial}={r.flush_ms[0]:.0f}" for r in rows if r.flush_ms
            )
            + "   | later flushes: "
            + "; ".join(
                f"t{r.trial}=[{' '.join(f'{x:.0f}' for x in r.flush_ms[1:])}]"
                for r in rows
                if len(r.flush_ms) > 1
            )
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--configs",
        default="all,none,smoothchunk_only,fastasync_only,c2me_only",
        help="comma separated: all, none, smoothchunk_only, fastasync_only, c2me_only",
    )
    parser.add_argument("--trials", type=int, default=DEFAULT_TRIALS)
    parser.add_argument("--flushes", type=int, default=DEFAULT_FLUSHES)
    parser.add_argument("--memory-mb", type=int, default=DEFAULT_MEMORY_MB)
    parser.add_argument(
        "--radius",
        type=int,
        default=32,
        help="pregen radius for the shared baseline world. 32 = ~4200 chunks, "
        "large enough that a flush takes seconds and differences are visible. "
        "Smaller radii make every config look identical.",
    )
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--json-out", type=Path, default=None)
    args = parser.parse_args()

    pack = read_pack(PACK_TOML)
    java = find_java()

    combos = {
        "all": set(SAVE_STACK.values()),
        "none": set(),
        "smoothchunk_only": {SAVE_STACK["smoothchunk"]},
        "fastasync_only": {SAVE_STACK["fastasyncworldsave"]},
        "c2me_only": {SAVE_STACK["c2me"]},
    }

    BENCH_ROOT.mkdir(parents=True, exist_ok=True)
    template = BENCH_ROOT / "template"
    if not (template / "libraries" / "net" / "neoforged" / "neoforge").is_dir():
        print("assembling server template")
        assemble_server(pack, template)
    install_neoforge(template, pack, java)
    apply_config(template, ROOT / "pack" / "config")

    generate_baseline_world(template, java, args.memory_mb, args.radius, args.timeout)

    results: list[TrialResult] = []
    for name in [c.strip() for c in args.configs.split(",") if c.strip()]:
        if name not in combos:
            raise SystemExit(f"unknown config {name!r}; choose from {sorted(combos)}")
        keep = combos[name]
        print(f"\n=== config {name}: keeping {sorted(Path(j).stem for j in keep) or 'nothing'} ===")
        for trial in range(1, args.trials + 1):
            results.append(
                run_trial(
                    name,
                    trial,
                    template,
                    keep,
                    pack,
                    java,
                    args.memory_mb,
                    args.flushes,
                    args.timeout,
                )
            )

    summarize(results)
    if args.json_out:
        args.json_out.write_text(
            json.dumps([r.to_json() for r in results], indent=2), encoding="utf-8"
        )
        print(f"wrote {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
