---
name: local-smoke-test
description: Use when a mod, config, or pack change needs a local dedicated-server boot check, after add-mod or a config edit, and before using the remote test-server skill.
---

# Local smoke test

Run `python scripts/smoke_test.py` from the repo root after a mod or config change. The default 8 GiB allocation runs a full benchmark: boot, `/neoforge generate` with chunkRadius 8, `/tick query` samples, then a report under `docs/smoke-runs/` (see `index.md`). Timeout is 900 seconds. The server zip this script builds reuses cached jars (packwiz cache, then `.cache/mod-files`) and downloads only missing files. Do not clear those caches or download the jars by hand.

`--skip-bench` is the original boot-only check (300s, no generate, no report). Use it for a quick "did world load break?" pass.

`--radius` is an occasional heavier stress pass, not routine. `--profile` copies a gitignored Spark jar into the throwaway server only — use it after a report already looks worse than a recent `docs/smoke-runs/` baseline, not as a normal step. Spark is never a pack mod.

This script never uses panel credentials. Non-zero exit means crash or timeout; a benchmark still writes a (possibly partial) report.

## Join-sync measurement (Mineflayer bot)

`smoke_test.py` never logs a player in, so for join sync use `scripts/join-test/` (Node, `npm install` once; pack-external, never a pack mod). Start the server manually from `dist/_smoke-test` (`bash run.sh`, needs Java 21 on PATH), wait for `Done`, then `node scripts/join-test/join-test.mjs 127.0.0.1 <server-port>` — it prints one JSON line with `loginMs`/`spawnMs`, exit 0 on spawn, 1 with kick reason otherwise. HeadlessMc (real client under Xvfb) is the documented heavier alternative for client-side join costs; it needs Linux and is not set up here. 2026-10-10 spike: vanilla-protocol bots are rejected at NeoForge negotiation (`vanilla.client.not_supported`), so the bot is connection-check only — it cannot time joins.

## Presence/load spike (Stressmark, throwaway)

2026-10-10: Stressmark 1.1.0 (NeoForge, server-only) dropped directly into `dist/_smoke-test/mods/` — never via packwiz, removed afterwards — driven over RCON (`scripts/join-test/rcon.py`). Idle: 20 TPS / 0.4ms / Exceptional. 10 spectator bots flying chunk-load patterns (4410 tracked chunks): TPS 7.3, MSPT 136, grade Poor, capacity 1. Expected, not a defect — no 10 real players generate terrain in 10 directions at once. Method proven; repeat with Spark `--profile` for tick-level attribution. This measures presence/load, never login sync.
