---
name: local-smoke-test
description: Use when a mod, config, or pack change needs a local dedicated-server boot check, after add-mod or a config edit, and before using the remote test-server skill.
---

# Local smoke test

Run `python scripts/smoke_test.py` from the repo root after any mod install or config change. Default timeout is 300 seconds. This is the first sanity check: did the dedicated server reach "Done" / "For help, type" without a crash-report?

It replaces the first, slowest iteration of the old "deploy to Pelican and watch" loop. `test-server` is for the friends-can-actually-join check, not this first boot.

This script never uses panel credentials. Watch its own stdout. Non-zero exit means crash or timeout — read the printed log tail before deploying remotely.
