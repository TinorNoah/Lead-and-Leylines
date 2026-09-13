# Server overlay

This directory is **not** part of the packwiz index. Do not put these files under `pack/`.

## Deploy

The panel is [example.invalid](https://example.invalid). Wings for this pack defaults to node `node` (`example.invalid`).

Copy [`.env.example`](../.env.example) to `.env` at the repo root (gitignored). Set `PANEL_API_KEY` to an Application API key (`papp_`). Do not commit it.

```text
python scripts/deploy_server.py
python scripts/deploy_server.py --reinstall --wait 600
python scripts/deploy_server.py --status
python scripts/deploy_server.py --dry-run
```

The script finds the CurseForge Generic egg (imports it only if missing), owns the server as `PANEL_OWNER_USERNAME`, and uses a free allocation on that node. Java image is chosen from the egg from `pack/pack.toml` Minecraft version.

`CURSEFORGE_PROJECT_ID` is the numeric CurseForge modpack id. `CURSEFORGE_API_KEY` is a CurseForge **console** key for the egg (not the panel key). If the console key is omitted, the script copies one already stored on another CurseForge Generic server on the panel.

Until a CurseForge file exists, deploy reports **blocked-on-publish**: the panel server can still be created, but the egg install is skipped. Set `CURSEFORGE_PROJECT_ID` and rerun with `--reinstall`. Do not fall back to a GitHub raw `pack.toml` URL.

## panel egg

Use the [CurseForge Generic]() egg.

| panel env | Value |
|---|---|
| `PROJECT_ID` | CurseForge modpack project ID (set in `.env` / the panel, never in git) |
| `VERSION_ID` | `latest` on the test server |
| `API_KEY` | CurseForge console key (panel / `.env` only, never in git) |

Pick the egg Java docker image required by the Minecraft version in `pack/pack.toml`. Look up current Mojang/Forge Java requirements when that version changes.

The egg installs from the last published CurseForge file. It does not track git. Until the first CurseForge upload exists, this pack cannot be installed on the dedicated server.

If the egg warns that the file is not a server pack, it will use the client zip. That is expected until a distinct CurseForge server pack is uploaded.

## Overlay files (not created in Phase 1)

After they exist, re-copy these onto the server **after every egg reinstall** (the install script writes `/mnt/server`):

- `user_jvm_args.txt`
- `ops.json`
- host-specific scripts
