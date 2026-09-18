#!/usr/bin/env python3
"""Unit tests for smoke-test metric parsers and report writers."""

from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

import smoke_metrics as metrics
import smoke_test


TICK_QUERY = """\
[12:00:00] [Server thread/INFO]: Target tick rate: 20.0 per second.
[12:00:00] [Server thread/INFO]: Average time per tick: 80.0ms (Target: 50.0ms)
[12:00:00] [Server thread/INFO]: Percentiles: P50: 44.1ms P95: 92.6ms P99: 210.3ms. Sample: 100
"""

TICK_QUERY_IDLE = """\
Target tick rate: 20.0 per second.
Average time per tick: 12.5ms (Target: 50.0ms)
Percentiles: P50: 11.0ms P95: 18.0ms P99: 22.0ms. Sample: 100
"""


class ParseTickQueryTests(unittest.TestCase):
    def test_parses_mspt_and_derives_tps_below_cap(self) -> None:
        sample = metrics.parse_tick_query(TICK_QUERY)
        self.assertIsNotNone(sample)
        assert sample is not None
        self.assertEqual(sample.mspt, 80.0)
        self.assertEqual(sample.target_tps, 20.0)
        self.assertEqual(sample.tps, 12.5)
        self.assertEqual(sample.p50_ms, 44.1)
        self.assertEqual(sample.p95_ms, 92.6)
        self.assertEqual(sample.p99_ms, 210.3)

    def test_caps_derived_tps_at_target_when_idle(self) -> None:
        sample = metrics.parse_tick_query(TICK_QUERY_IDLE)
        self.assertIsNotNone(sample)
        assert sample is not None
        self.assertEqual(sample.mspt, 12.5)
        self.assertEqual(sample.tps, 20.0)

    def test_parses_real_1_21_1_percentiles_line(self) -> None:
        sample = metrics.parse_tick_query(
            "Target tick rate: 20.0 per second.\n"
            "Average time per tick: 0.4ms (Target: 50.0ms)\n"
            "Percentiles: P50: 0.2ms P95: 1.2ms P99: 3.3ms, sample: 100\n"
        )
        self.assertIsNotNone(sample)
        assert sample is not None
        self.assertEqual(sample.p50_ms, 0.2)
        self.assertEqual(sample.p95_ms, 1.2)
        self.assertEqual(sample.p99_ms, 3.3)

    def test_returns_none_when_output_missing(self) -> None:
        self.assertIsNone(metrics.parse_tick_query("server starting"))


class ParseSpawnElapsedTests(unittest.TestCase):
    def test_parses_time_elapsed_ms(self) -> None:
        lines = [
            "Preparing spawn area: 100%\n",
            "[Server thread/INFO]: Time elapsed: 4321 ms\n",
        ]
        self.assertEqual(metrics.parse_spawn_elapsed_ms(lines), 4321)

    def test_returns_none_when_absent(self) -> None:
        self.assertIsNone(metrics.parse_spawn_elapsed_ms(["Done (12.3s)!"]))


class ParseCantKeepUpTests(unittest.TestCase):
    def test_counts_vanilla_and_keeps_worst(self) -> None:
        lines = [
            "Can't keep up! Is the server overloaded? Running 2000ms or 40 ticks behind\n",
            "unrelated\n",
            "Can't keep up! Is the server overloaded? Running 5120ms or 102 ticks behind\n",
            "Can't keep up! Is the server overloaded? Running 1500ms or 1500ms behind, skipping 30 ticks\n",
        ]
        summary = metrics.summarize_cant_keep_up(lines)
        self.assertEqual(summary.count, 3)
        self.assertIsNotNone(summary.worst)
        assert summary.worst is not None
        self.assertEqual(summary.worst.behind_ms, 5120)
        self.assertEqual(summary.worst.skipped_ticks, 102)

    def test_zero_when_none(self) -> None:
        summary = metrics.summarize_cant_keep_up(["all good\n"])
        self.assertEqual(summary.count, 0)
        self.assertIsNone(summary.worst)


class ParsePregenTests(unittest.TestCase):
    def test_progress_line_done_and_total(self) -> None:
        progress = metrics.parse_pregen_progress(
            "[Server] 12/289 Chunks <1, 0> (Average/t: 2,7), Ram: 798MB"
        )
        self.assertIsNotNone(progress)
        assert progress is not None
        self.assertEqual(progress.done, 12)
        self.assertEqual(progress.total, 289)

    def test_progress_current_total_from_chunk_pregenerator_4_5(self) -> None:
        progress = metrics.parse_pregen_progress(
            "[Task: Current/Total: 137/256]"
        )
        self.assertIsNotNone(progress)
        assert progress is not None
        self.assertEqual(progress.done, 137)
        self.assertEqual(progress.total, 256)

    def test_does_not_invent_a_chunk_count(self) -> None:
        self.assertIsNone(metrics.parse_pregen_progress("starting task smoketest"))

    def test_finished_typo_and_corrected_spellings(self) -> None:
        finished = metrics.parse_pregen_finished(
            "Pregenation Finished: [Time=00:01:13, Chunks=289]"
        )
        self.assertIsNotNone(finished)
        assert finished is not None
        self.assertEqual(finished.chunks, 289)

        fixed = metrics.parse_pregen_finished(
            "Pregeneration Finished: [Time=00:00:08, Chunks=9]"
        )
        self.assertIsNotNone(fixed)
        assert fixed is not None
        self.assertEqual(fixed.chunks, 9)

    def test_average_cps_from_real_count_and_duration(self) -> None:
        self.assertAlmostEqual(metrics.average_cps(289, 28.9), 10.0)
        self.assertIsNone(metrics.average_cps(289, 0))
        self.assertIsNone(metrics.average_cps(None, 10))


class ReportTests(unittest.TestCase):
    def test_filesystem_safe_utc_stem(self) -> None:
        when = datetime(2026, 9, 18, 6, 30, 5, tzinfo=timezone.utc)
        self.assertEqual(metrics.report_stem(when), "2026-09-18T063005Z")

    def test_report_includes_metrics_change_note_and_partial_tail(self) -> None:
        idle = metrics.parse_tick_query(TICK_QUERY_IDLE)
        mid = metrics.parse_tick_query(TICK_QUERY)
        body = metrics.render_report(
            metrics.SmokeReport(
                timestamp="2026-09-18T063005Z",
                passed=False,
                change_note="HEAD abc123 fix widgets\nstatus: M pack/mods/foo.pw.toml",
                note="testing the parser",
                boot_s=41.2,
                spawn_elapsed_ms=4321,
                idle=idle,
                mid=mid,
                post=None,
                pregen_s=12.0,
                chunks=None,
                cps=None,
                cant_keep_up=metrics.CantKeepUpSummary(count=0, worst=None),
                rss_idle_kb=1000,
                rss_mid_kb=2000,
                rss_post_kb=None,
                world_bytes=None,
                sparkprofile_path=None,
                log_tail="crash here",
            )
        )
        self.assertIn("fail", body.lower())
        self.assertIn("HEAD abc123", body)
        self.assertIn("testing the parser", body)
        self.assertIn("| Idle | 20.0 | 12.5 |", body)
        self.assertNotIn("| Idle | — | — | — | |", body)
        self.assertNotIn("| Idle | 20.0 | 12.5 | — | |", body)
        self.assertIn("41.2", body)
        self.assertIn("4321", body)
        self.assertIn("12.5", body)
        self.assertIn("80.0", body)
        self.assertIn("crash here", body)
        self.assertNotIn("17×17", body)
        self.assertNotIn("17x17", body)

    def test_index_inserts_newest_first_without_rewriting_prior_rows(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            index = Path(tmp) / "index.md"
            metrics.ensure_index(index)
            metrics.insert_index_row(
                index,
                metrics.IndexRow(
                    timestamp="2026-09-18T060000Z",
                    commit="aaa1111",
                    passed=True,
                    tps_summary="20.0 / 12.5 / 19.0",
                    cps_summary="10.0",
                    report_rel="2026-09-18T060000Z.md",
                ),
            )
            metrics.insert_index_row(
                index,
                metrics.IndexRow(
                    timestamp="2026-09-18T070000Z",
                    commit="bbb2222",
                    passed=False,
                    tps_summary="20.0 / — / —",
                    cps_summary="—",
                    report_rel="2026-09-18T070000Z.md",
                ),
            )
            text = index.read_text(encoding="utf-8")
            first = text.index("2026-09-18T070000Z")
            second = text.index("2026-09-18T060000Z")
            self.assertLess(first, second)
            self.assertIn("aaa1111", text)
            self.assertIn("bbb2222", text)
            self.assertEqual(text.count("| 2026-09-18T060000Z |"), 1)

    def test_previous_run_comes_from_existing_index_not_current_head(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            index = Path(tmp) / "index.md"
            metrics.ensure_index(index)
            self.assertIsNone(metrics.previous_index_run(index))
            metrics.insert_index_row(
                index,
                metrics.IndexRow(
                    timestamp="2026-09-18T060000Z",
                    commit="aaa1111",
                    passed=True,
                    tps_summary="20 / 12 / 19",
                    cps_summary="8.1",
                    report_rel="2026-09-18T060000Z.md",
                ),
            )
            prev = metrics.previous_index_run(index)
            self.assertIsNotNone(prev)
            assert prev is not None
            self.assertEqual(prev.commit, "aaa1111")
            self.assertEqual(prev.timestamp, "2026-09-18T060000Z")


class ArgParseTests(unittest.TestCase):
    def test_benchmark_is_default(self) -> None:
        args = smoke_test.parse_args([])
        self.assertFalse(args.skip_bench)
        self.assertEqual(args.radius, 8)
        self.assertFalse(args.profile)

    def test_skip_bench_flag(self) -> None:
        args = smoke_test.parse_args(["--skip-bench"])
        self.assertTrue(args.skip_bench)


class SparkAndSizeTests(unittest.TestCase):
    def test_spark_cache_path_is_under_dev_tools(self) -> None:
        cache = Path("/tmp/repo/.cache/dev-tools")
        path = metrics.spark_cache_path(cache)
        self.assertEqual(path.name, "spark-1.10.124-neoforge.jar")
        self.assertEqual(path.parent, cache)

    def test_parses_spark_written_path(self) -> None:
        path = metrics.parse_spark_written(
            "[⚡] Data has been written to: /tmp/config/spark/profile-2026-09-18_12.38.03.sparkprofile"
        )
        self.assertEqual(
            path,
            Path("/tmp/config/spark/profile-2026-09-18_12.38.03.sparkprofile"),
        )

    def test_find_sparkprofile_ignores_files_already_seen(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            spark = work / "config" / "spark"
            spark.mkdir(parents=True)
            old = spark / "old.sparkprofile"
            new = spark / "new.sparkprofile"
            old.write_bytes(b"old")
            new.write_bytes(b"new")
            found = metrics.find_sparkprofile(work, after={old})
            self.assertEqual(found, new)

    def test_find_sparkprofile_prefers_newest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            older = work / "config" / "spark" / "old.sparkprofile"
            newer = work / "config" / "spark" / "new.sparkprofile"
            older.parent.mkdir(parents=True)
            older.write_bytes(b"old")
            newer.write_bytes(b"new")
            found = metrics.find_sparkprofile(work)
            self.assertEqual(found, newer)

    def test_world_size_sums_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            world = Path(tmp) / "world"
            (world / "region").mkdir(parents=True)
            (world / "region" / "r.0.0.mca").write_bytes(b"abcd")
            (world / "level.dat").write_bytes(b"xy")
            self.assertEqual(metrics.dir_size_bytes(world), 6)


if __name__ == "__main__":
    unittest.main()
