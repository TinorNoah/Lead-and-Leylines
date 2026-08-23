---
name: test-server
description: Restart the panel-hosted test server (CurseForge Generic egg), wait for boot, pull recent console output, and flag crash or error patterns. Use when testing the pack on the dedicated server.
---

# Test dedicated server

The test server uses the CurseForge Generic egg and tracks the last published CurseForge file, not live git. See `server/README.md`.

If no CurseForge project/file exists yet, report **blocked-on-publish** and stop. Do not invent a GitHub raw pack.toml fallback.

## Steps

1. Confirm egg vars in the panel (do not print secret values):
   - `PROJECT_ID` — CurseForge modpack id
   - `VERSION_ID` — `latest` on the test box
   - `API_KEY` — present in the panel, never in git
2. Reinstall or restart so the egg pulls the current CurseForge file.
3. Wait until the console shows a boot-complete pattern (Forge "Done" / "For help, type") or a crash.
4. Pull recent console output.
5. Flag:
   - `Exception`, `Error`, crash reports
   - egg message that the file is not a server pack (expected until a distinct server pack exists; still report it)
   - missing overlay after reinstall (`ops.json`, `user_jvm_args.txt` not re-copied)

## Dedicated server API (placeholder)

Replace these when an MCP or API client exists. Do not guess URLs, keys, or server UUIDs.

```text
# TODO panel API: authenticate (panel URL + API key from user/MCP, never commit)
# TODO panel API: POST reinstall or power restart for the test server
# TODO panel API: GET websocket/console log since restart
# TODO panel API: map HTTP errors (401/404) to a clear operator message
```

Until those exist, ask the user to reinstall/restart in the panel and paste console output, then apply the flag rules above.
