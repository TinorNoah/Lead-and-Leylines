---
name: test-server
description: Restart the panel-hosted test server (CurseForge Generic egg), wait for boot, pull recent console output, and flag crash or error patterns. Use when testing the pack on the dedicated server.
---

# Test dedicated server

The test server uses the CurseForge Generic egg and tracks the last published CurseForge file, not live git. See `server/README.md`.

If no CurseForge project/file exists yet, report **blocked-on-publish** and stop. Do not invent a GitHub raw pack.toml fallback.

## Steps

1. Confirm `.env` exists at the repo root (never commit it). Required: `PANEL_API_KEY`. For a real egg install also `CURSEFORGE_PROJECT_ID`. The CurseForge console `API_KEY` can be copied from another CurseForge Generic server on the panel.
2. From the repo root, run `python scripts/deploy_server.py --status` to find the server, or without `--status` to create/update it.
3. Reinstall so the egg pulls the current CurseForge file:

   `python scripts/deploy_server.py --reinstall --wait 600`

4. Wait until the panel console shows a boot-complete pattern (Forge "Done" / "For help, type") or a crash. Application API keys cannot read live console output; use the panel console (or a `pacc_` client key later).
5. Flag:
   - `Exception`, `Error`, crash reports
   - egg message that the file is not a server pack (expected until a distinct server pack exists; still report it)
   - missing overlay after reinstall (`ops.json`, `user_jvm_args.txt` not re-copied)
   - HTTP 401 from the script: wrong panel URL or key (panel is `https://example.invalid`, not Dokploy at `example.invalid`)
