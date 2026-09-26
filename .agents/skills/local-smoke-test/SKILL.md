---
name: local-smoke-test
description: Use when a mod, config, or pack change needs a local dedicated-server boot check, after add-mod or a config edit, and before using the remote test-server skill.
---

# Local smoke test

Run `python scripts/smoke_test.py` from the repo root after a mod or config change. Default is a full benchmark: boot, `/neoforge generate` with chunkRadius 8, `/tick query` samples, then a report under `docs/smoke-runs/` (see `index.md`). Timeout is 900 seconds. The server zip this script builds reuses cached jars (packwiz cache, then `.cache/mod-files`) and downloads only missing files. Do not clear those caches or download the jars by hand.

`--skip-bench` is the original boot-only check (300s, no generate, no report). Use it for a quick "did world load break?" pass.

`--radius` is an occasional heavier stress pass, not routine. `--profile` copies a gitignored Spark jar into the throwaway server only — use it after a report already looks worse than a recent `docs/smoke-runs/` baseline, not as a normal step. Spark is never a pack mod.

This script never uses panel credentials. Non-zero exit means crash or timeout; a benchmark still writes a (possibly partial) report.
