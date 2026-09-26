#!/usr/bin/env python3
"""Parsers, reports, and Spark cache helpers for the local smoke test.

Imported by smoke_test.py. Never touches pack/mods or packwiz state.
"""

from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

USER_AGENT = "LeadAndLeylines-smoke/1.0 (local tooling)"

SPARK_FILENAME = "spark-1.10.124-neoforge.jar"
SPARK_URL = (
    "https://cdn.modrinth.com/data/l6YH9Als/versions/v5qtqRQi/"
    "spark-1.10.124-neoforge.jar"
)
SPARK_SHA1 = "9430cc2ab64ff89d698be593769fb9f9ee4efae6"

ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")
TICK_TARGET_RE = re.compile(r"Target tick rate:\s*([\d.]+)\s*per second", re.I)
TICK_MSPT_RE = re.compile(r"Average time per tick:\s*([\d.]+)\s*ms", re.I)
TICK_PCTL_RE = re.compile(
    r"Percentiles:\s*P50:\s*([\d.]+)ms\s*P95:\s*([\d.]+)ms\s*P99:\s*([\d.]+)ms",
    re.I,
)
SPAWN_ELAPSED_RE = re.compile(r"Time elapsed:\s*(\d+)\s*ms", re.I)
CANT_KEEP_UP_RE = re.compile(
    r"Can't keep up! Is the server overloaded\?\s*Running\s*(\d+)\s*ms"
    r"(?:\s*or\s*(\d+)\s*(?:ms|ticks)\s*behind)?"
    r"(?:.*?skipping\s*(\d+)\s*ticks?)?",
    re.I,
)
PREGEN_PROGRESS_RES = (
    re.compile(
        r"(?:Generation status!|Generation stopped!)\s*(\d+)\s+out of\s+(\d+)\s+chunks",
        re.I,
    ),
    re.compile(r"Current/Total:\s*(\d+)\s*/\s*(\d+)", re.I),
    re.compile(r"(\d+)\s*/\s*(\d+)\s+Chunks", re.I),
)
PREGEN_STARTED_RE = re.compile(r"Generating\s+(\d+)\s+chunks,\s+in an area of", re.I)
PREGEN_FINISHED_RE = re.compile(
    r"Generation Done!|"
    r"Pregen(?:er)?ation\s+Finished:.*?Chunks\s*=\s*(\d+)",
    re.I,
)
SPARK_WRITTEN_RE = re.compile(
    r"Data has been written to:\s*(.+\.sparkprofile)",
    re.I,
)
INDEX_ROW_RE = re.compile(
    r"^\|\s*(\d{4}-\d{2}-\d{2}T\d{6}Z)\s*\|\s*`?([0-9a-f]+)`?\s*\|",
    re.I,
)

INDEX_HEADER = """\
# Smoke-test runs

Local dedicated-server benchmark history from `python scripts/smoke_test.py`.
Newest first. `--skip-bench` does not write a row.

| Timestamp | Commit | Result | TPS (idle / mid / post) | CPS | Report |
| --- | --- | --- | --- | --- | --- |
"""


@dataclass(frozen=True)
class TickSample:
    mspt: float
    tps: float
    target_tps: float
    p50_ms: float | None = None
    p95_ms: float | None = None
    p99_ms: float | None = None


@dataclass(frozen=True)
class PregenProgress:
    done: int
    total: int


@dataclass(frozen=True)
class PregenFinished:
    chunks: int


@dataclass(frozen=True)
class CantKeepUpHit:
    behind_ms: int
    skipped_ticks: int | None
    line: str


@dataclass(frozen=True)
class CantKeepUpSummary:
    count: int
    worst: CantKeepUpHit | None


@dataclass(frozen=True)
class IndexRow:
    timestamp: str
    commit: str
    passed: bool
    tps_summary: str
    cps_summary: str
    report_rel: str


@dataclass
class SmokeReport:
    timestamp: str
    passed: bool
    change_note: str
    note: str | None
    boot_s: float | None
    spawn_elapsed_ms: int | None
    idle: TickSample | None
    mid: TickSample | None
    post: TickSample | None
    pregen_s: float | None
    chunks: int | None
    cps: float | None
    cant_keep_up: CantKeepUpSummary
    rss_idle_kb: int | None
    rss_mid_kb: int | None
    rss_post_kb: int | None
    world_bytes: int | None
    sparkprofile_path: str | None
    log_tail: str | None


def report_stem(when: datetime) -> str:
    utc = when.astimezone(timezone.utc)
    return utc.strftime("%Y-%m-%dT%H%M%SZ")


def strip_ansi(text: str) -> str:
    return ANSI_RE.sub("", text)


def parse_tick_query(text: str) -> TickSample | None:
    text = strip_ansi(text)
    target_match = TICK_TARGET_RE.search(text)
    mspt_match = TICK_MSPT_RE.search(text)
    if not target_match or not mspt_match:
        return None
    target = float(target_match.group(1))
    mspt = float(mspt_match.group(1))
    tps = target if mspt <= 0 else min(target, 1000.0 / mspt)
    pctl = TICK_PCTL_RE.search(text)
    return TickSample(
        mspt=mspt,
        tps=round(tps, 3),
        target_tps=target,
        p50_ms=float(pctl.group(1)) if pctl else None,
        p95_ms=float(pctl.group(2)) if pctl else None,
        p99_ms=float(pctl.group(3)) if pctl else None,
    )


def parse_spawn_elapsed_ms(lines: list[str]) -> int | None:
    found: int | None = None
    for line in lines:
        match = SPAWN_ELAPSED_RE.search(strip_ansi(line))
        if match:
            found = int(match.group(1))
    return found


def parse_cant_keep_up(line: str) -> CantKeepUpHit | None:
    line = strip_ansi(line)
    match = CANT_KEEP_UP_RE.search(line)
    if not match:
        return None
    behind_ms = int(match.group(1))
    skipped = None
    if match.group(3):
        skipped = int(match.group(3))
    elif match.group(2):
        skipped = int(match.group(2))
    return CantKeepUpHit(behind_ms=behind_ms, skipped_ticks=skipped, line=line.rstrip())


def summarize_cant_keep_up(lines: list[str]) -> CantKeepUpSummary:
    hits = [hit for hit in (parse_cant_keep_up(line) for line in lines) if hit]
    worst = max(hits, key=lambda hit: hit.behind_ms) if hits else None
    return CantKeepUpSummary(count=len(hits), worst=worst)


def parse_pregen_progress(line: str) -> PregenProgress | None:
    text = strip_ansi(line)
    for pattern in PREGEN_PROGRESS_RES:
        match = pattern.search(text)
        if match:
            return PregenProgress(done=int(match.group(1)), total=int(match.group(2)))
    return None


def parse_pregen_started(line: str) -> int | None:
    match = PREGEN_STARTED_RE.search(strip_ansi(line))
    return int(match.group(1)) if match else None


def parse_pregen_finished(line: str) -> PregenFinished | None:
    match = PREGEN_FINISHED_RE.search(strip_ansi(line))
    if not match:
        return None
    if match.group(1):
        return PregenFinished(chunks=int(match.group(1)))
    return PregenFinished(chunks=0)


def latest_pregen_total(lines: list[str]) -> tuple[int | None, int | None]:
    """Return (done, total) from progress lines, preferring a finished count."""
    done: int | None = None
    total: int | None = None
    started_total: int | None = None
    for line in lines:
        started = parse_pregen_started(line)
        if started is not None:
            started_total = started
        finished = parse_pregen_finished(line)
        if finished:
            if finished.chunks > 0:
                return finished.chunks, finished.chunks
            if started_total is not None:
                return started_total, started_total
            if total is not None:
                return total, total
            return None, None
        progress = parse_pregen_progress(line)
        if progress:
            done, total = progress.done, progress.total
    return done, total


def average_cps(chunks: int | None, duration_s: float | None) -> float | None:
    if chunks is None or duration_s is None or duration_s <= 0:
        return None
    return round(chunks / duration_s, 3)


def format_tick(sample: TickSample | None) -> str:
    if sample is None:
        return "—"
    return f"{sample.tps:.1f} TPS / {sample.mspt:.1f} mspt"


def tps_index_summary(
    idle: TickSample | None,
    mid: TickSample | None,
    post: TickSample | None,
) -> str:
    def part(sample: TickSample | None) -> str:
        return f"{sample.tps:.1f}" if sample else "—"

    return f"{part(idle)} / {part(mid)} / {part(post)}"


def format_bytes(size: int | None) -> str:
    if size is None:
        return "—"
    if size < 1024:
        return f"{size} B"
    mib = size / (1024 * 1024)
    if mib < 1024:
        return f"{mib:.1f} MiB"
    return f"{mib / 1024:.2f} GiB"


def format_rss(kb: int | None) -> str:
    if kb is None:
        return "—"
    return f"{kb / 1024:.1f} MiB ({kb} KiB)"


def render_report(report: SmokeReport) -> str:
    status = "pass" if report.passed else "fail"
    note = report.note.strip() if report.note else ""
    chunks = str(report.chunks) if report.chunks is not None else "—"
    cps = f"{report.cps:.3f}" if report.cps is not None else "—"
    pregen_s = f"{report.pregen_s:.1f}s" if report.pregen_s is not None else "—"
    boot_s = f"{report.boot_s:.1f}s" if report.boot_s is not None else "—"
    spawn = (
        f"{report.spawn_elapsed_ms} ms"
        if report.spawn_elapsed_ms is not None
        else "—"
    )
    worst = "—"
    if report.cant_keep_up.worst:
        hit = report.cant_keep_up.worst
        ticks = (
            f", {hit.skipped_ticks} ticks"
            if hit.skipped_ticks is not None
            else ""
        )
        worst = f"{hit.behind_ms} ms behind{ticks}"
    spark = report.sparkprofile_path or "—"
    tail = ""
    if report.log_tail:
        tail = "\n## Log tail\n\n```\n" + report.log_tail.rstrip() + "\n```\n"

    return f"""\
# Smoke run {report.timestamp}

**Result:** {status}

## Change note

```
{report.change_note.rstrip()}
```

{f"Runner note: {note}" if note else ""}

## Boot

- Boot time: {boot_s}
- Spawn "Time elapsed": {spawn}

## `/tick query`

Do not use `/neoforge tps`; it reports a static 20.000 on this pack.

| Point | TPS | MSPT | P50 / P95 / P99 |
| --- | --- | --- | --- |
| Idle | {_tick_cell(report.idle)} |
| Mid-gen | {_tick_cell(report.mid)} |
| Post-gen | {_tick_cell(report.post)} |

## Pregen

- Duration: {pregen_s}
- Chunks (from `/neoforge generate` output): {chunks}
- Average CPS: {cps}

## Can't keep up

- Count: {report.cant_keep_up.count}
- Worst: {worst}

## Memory and disk

- RSS idle: {format_rss(report.rss_idle_kb)}
- RSS mid-gen: {format_rss(report.rss_mid_kb)}
- RSS post-gen: {format_rss(report.rss_post_kb)}
- World folder: {format_bytes(report.world_bytes)}

## Spark

- Profile file: `{spark}`
{tail}"""


def _tick_cell(sample: TickSample | None) -> str:
    if sample is None:
        return "— | — | —"
    pctl = "—"
    if sample.p50_ms is not None:
        pctl = f"{sample.p50_ms:.1f} / {sample.p95_ms:.1f} / {sample.p99_ms:.1f}"
    return f"{sample.tps:.1f} | {sample.mspt:.1f} | {pctl}"


def ensure_index(path: Path) -> None:
    if path.is_file() and path.read_text(encoding="utf-8").strip():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(INDEX_HEADER, encoding="utf-8")


def _index_row_markdown(row: IndexRow) -> str:
    result = "pass" if row.passed else "fail"
    return (
        f"| {row.timestamp} | `{row.commit}` | {result} | "
        f"{row.tps_summary} | {row.cps_summary} | "
        f"[{row.report_rel}]({row.report_rel}) |"
    )


def insert_index_row(path: Path, row: IndexRow) -> None:
    ensure_index(path)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    marker = "| --- | --- | --- | --- | --- | --- |"
    insert_at = None
    for index, line in enumerate(lines):
        if line.strip() == marker:
            insert_at = index + 1
            break
    if insert_at is None:
        raise SystemExit(f"smoke-runs index missing table header: {path}")
    lines.insert(insert_at, _index_row_markdown(row) + "\n")
    path.write_text("".join(lines), encoding="utf-8")


def previous_index_run(path: Path) -> IndexRow | None:
    if not path.is_file():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        match = INDEX_ROW_RE.match(line.strip())
        if not match:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        return IndexRow(
            timestamp=cells[0],
            commit=cells[1].strip("`"),
            passed=cells[2].lower() == "pass",
            tps_summary=cells[3],
            cps_summary=cells[4],
            report_rel=cells[5],
        )
    return None


def git_output(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        err = (result.stderr or result.stdout or "").strip()
        return f"(git {' '.join(args)} failed: {err})"
    return result.stdout.rstrip()


def collect_change_note(
    root: Path,
    previous: IndexRow | None,
    note: str | None = None,
) -> tuple[str, str]:
    """Return (short_commit, markdown change-note body).

    `note` is stored separately in the report; this is the git snapshot only.
    """
    del note
    head = git_output(root, "rev-parse", "--short", "HEAD")
    subject = git_output(root, "log", "-1", "--format=%s")
    status = git_output(root, "status", "--porcelain")
    if previous:
        diff = git_output(
            root,
            "diff",
            "--stat",
            previous.commit,
            "--",
            "pack/mods/",
        )
        compared = (
            f"Compared to previous smoke run {previous.timestamp} "
            f"(`{previous.commit}`), `git diff --stat pack/mods/`:"
        )
    else:
        diff = "(no previous smoke run in docs/smoke-runs/index.md)"
        compared = "First recorded smoke run; no previous baseline."
    status_block = status if status.strip() else "(clean)"
    diff_block = diff if diff.strip() else "(no pack/mods diff)"
    body = (
        f"HEAD `{head}` {subject}\n"
        f"git status --porcelain:\n{status_block}\n"
        f"{compared}\n{diff_block}\n"
    )
    return head, body


def process_rss_kb(pid: int) -> int | None:
    if sys.platform == "win32":
        try:
            result = subprocess.run(
                [
                    "powershell",
                    "-NoProfile",
                    "-Command",
                    f"(Get-Process -Id {pid} -ErrorAction Stop).WorkingSet64",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        except OSError:
            return None
        if result.returncode != 0:
            return None
        text = result.stdout.strip()
        if not text:
            return None
        try:
            return int(text) // 1024
        except ValueError:
            return None

    try:
        result = subprocess.run(
            ["ps", "-o", "rss=", "-p", str(pid)],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    text = result.stdout.strip().split()
    if not text:
        return None
    try:
        return int(text[0])
    except ValueError:
        return None


def dir_size_bytes(path: Path) -> int | None:
    if not path.exists():
        return None
    total = 0
    if path.is_file():
        return path.stat().st_size
    for root, _dirs, files in os.walk(path):
        for name in files:
            file_path = Path(root) / name
            try:
                total += file_path.stat().st_size
            except OSError:
                continue
    return total


def spark_cache_path(cache_dir: Path) -> Path:
    return cache_dir / SPARK_FILENAME


def _sha1(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def ensure_spark_jar(cache_dir: Path) -> Path:
    dest = spark_cache_path(cache_dir)
    if dest.is_file() and _sha1(dest) == SPARK_SHA1:
        return dest
    cache_dir.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".jar.partial")
    print(f"downloading Spark (dev-only, not a pack mod) from {SPARK_URL}")
    request = urllib.request.Request(SPARK_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=180) as response:
        tmp.write_bytes(response.read())
    digest = _sha1(tmp)
    if digest != SPARK_SHA1:
        tmp.unlink(missing_ok=True)
        raise SystemExit(
            f"Spark jar sha1 mismatch: got {digest}, expected {SPARK_SHA1}"
        )
    tmp.replace(dest)
    return dest


def copy_spark_into_mods(jar: Path, mods_dir: Path) -> Path:
    mods_dir.mkdir(parents=True, exist_ok=True)
    dest = mods_dir / jar.name
    shutil.copy2(jar, dest)
    return dest


def parse_spark_written(line: str) -> Path | None:
    match = SPARK_WRITTEN_RE.search(strip_ansi(line))
    if not match:
        return None
    return Path(match.group(1).strip())


def find_sparkprofile(work: Path, *, after: set[Path] | None = None) -> Path | None:
    matches = [
        path
        for path in work.rglob("*.sparkprofile")
        if after is None or path not in after
    ]
    matches.sort(key=lambda path: path.stat().st_mtime)
    return matches[-1] if matches else None
