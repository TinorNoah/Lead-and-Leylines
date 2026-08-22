# Server overlay

This directory is **not** part of the packwiz index. Do not put these files under `pack/`.

## Pelican egg

Use the [CurseForge Generic](https://raw.githubusercontent.com/pelican-eggs/minecraft/refs/heads/main/java/curseforge/egg-curse-forge-generic.json) egg.

| Pelican env | Value |
|---|---|
| `PROJECT_ID` | CurseForge modpack project ID (set in the panel, never in git) |
| `VERSION_ID` | `latest` on the test server |
| `API_KEY` | CurseForge console key (panel only, never in git) |

Pick the egg Java docker image required by the Minecraft version in `pack/pack.toml`. Look up current Mojang/Forge Java requirements when that version changes.

The egg installs from the last published CurseForge file. It does not track git. Until the first CurseForge upload exists, this pack cannot be installed on Pelican. Do not fall back to a GitHub raw `pack.toml` URL.

If the egg warns that the file is not a server pack, it will use the client zip. That is expected until a distinct CurseForge server pack is uploaded.

## Overlay files (not created in Phase 1)

After they exist, re-copy these onto the server **after every egg reinstall** (the install script writes `/mnt/server`):

- `user_jvm_args.txt`
- `ops.json`
- host-specific scripts
