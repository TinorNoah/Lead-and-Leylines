---
name: test-server
description: Restart the panel-hosted test server, wait for boot, pull recent console output, and flag crash or error patterns. Use when testing the pack on the dedicated server.
---

# Test dedicated server

Until a CurseForge file exists, deploy the current `pack/` tree with `python scripts/deploy_server.py --from-local`. That uses the Forge Minecraft egg plus Wings file upload. Do not invent a GitHub raw pack.toml fallback. After CurseForge is public, `--curseforge --reinstall` tracks the last published store file. See `server/README.md`.

## Steps

1. Confirm `.env` exists at the repo root (never commit it). Required: `PANEL_URL`, `PANEL_API_KEY`, `PANEL_NODE_FQDN`. For the CurseForge Generic egg also `CURSEFORGE_PROJECT_ID`. The CurseForge console `API_KEY` can be copied from another CurseForge Generic server on the panel.
2. From the repo root, run `python scripts/deploy_server.py --status` to find the server.
3. Push the current pack (default while CurseForge is unpublished):

   `python scripts/deploy_server.py --from-local`

   Friends: `python scripts/deploy_server.py --share-only`, then send `dist/*.mrpack` (ATLauncher Instances → Import → Browse).
4. Wait until the panel console shows a boot-complete pattern (Forge "Done" / "For help, type") or a crash. Application API keys cannot read live console output; use the panel console (or a `pacc_` client key later).
5. Flag:
   - `Exception`, `Error`, crash reports
   - egg message that the file is not a server pack (CurseForge Generic only; expected until a distinct server pack exists; still report it)
   - missing overlay after reinstall (`ops.json`, `user_jvm_args.txt` not re-copied)
   - HTTP 401 from the script: wrong `PANEL_URL` or key in `.env` (not the Dokploy host)
