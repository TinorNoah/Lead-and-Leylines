# Server overlay

This directory is **not** part of the packwiz index. Do not put these files under `pack/`.

## Deploy

The panel URL and Wings node FQDN live in gitignored `.env` (`PANEL_URL`, `PANEL_NODE_FQDN`). Never commit real hostnames.

Copy [`.env.example`](../.env.example) to `.env` at the repo root. Set `PANEL_API_KEY` to an Application API key (`papp_`). Do not commit `.env`.

Until a CurseForge file exists, the default path is **GitHub, then Pelican**: export the current `pack/` tree, attach `Lead-and-Leylines-<version>-server-mods.zip` to the matching GitHub Release (`vX.Y.Z`), switch the test server to the **NeoForge** egg, install NeoForge from `pack.toml`, and have Pelican **pull** that Release asset. `GH_TOKEN` is required. Do not write the zip straight to the server, and do not fall back to a GitHub raw `pack.toml` URL. Pin `NEOFORGE_VERSION` to the exact loader version in `pack.toml`; do not install from `MC_VERSION` alone.

```text
python scripts/release.py vX.Y.Z --changelog notes.md
python scripts/deploy_server.py
python scripts/deploy_server.py --from-local
python scripts/deploy_server.py --share-only
python scripts/deploy_server.py --status
python scripts/deploy_server.py --dry-run
python scripts/deploy_server.py --curseforge --reinstall --wait 600
```

`python scripts/release.py vX.Y.Z --changelog notes.md` is the usual ship path: GitHub Release from the changelog, then `--from-local` on this Pelican server, then local Prism. CurseForge stays off unless you pass `--curseforge` or `--upload-stores`. Default `--channel alpha` is a GitHub prerelease. `--channel release` is GitHub Latest. Every release updates this server unless you pass `--skip-server`, and Prism unless `--skip-prism`. Do not put panel/join details in that changelog. Use `deploy_server.py` alone when you only need the server.

`--share-only` writes ATLauncher files under `dist/` (gitignored) and does not touch the panel. `--from-local` looks at GitHub Release `v{pack.toml version}` for the server-mods zip. When that asset is already there, Pelican pulls it and no new pack is built. When it is missing, the script exports, attaches the zip, then Pelican pulls it. That export reuses jars already in the packwiz cache or `.cache/mod-files` and downloads only files that are missing. Reinstalling the NeoForge egg **wipes the world**; later `--from-local` runs only replace `mods/` if Minecraft/NeoForge versions are unchanged.

The script owns the server as `PANEL_OWNER_USERNAME` and uses a free allocation on that node. Java image is chosen from the egg from `pack/pack.toml` Minecraft version.

### ATLauncher (friends)

Send them `dist/Lead-and-Leylines-<pack version>.mrpack` (or the `.zip`). In ATLauncher: **Instances → Import → Browse** → select the file → **Import** → name it → **Install**. Store search will not find this pack until the CurseForge listing is public. GitHub download URLs often fail ATLauncher's URL import; send the file.

### After CurseForge is public

Set `CURSEFORGE_PROJECT_ID` (numeric modpack id) in `.env`. `CURSEFORGE_API_KEY` is a CurseForge **console** key for the Generic egg (not the panel key). If the console key is omitted, the script copies one already stored on another CurseForge Generic server on the panel. Then:

```text
python scripts/deploy_server.py --curseforge --reinstall --wait 600
```

## Eggs

**Local testing (default):** NeoForge already on the panel (`MC_VERSION` and `NEOFORGE_VERSION` from `pack.toml`; `NEOFORGE_VERSION` is the exact loader version, not `{minecraft}-{loader}`). Mods come from the GitHub Release server-mods zip, not a Wings push of the zip from this machine.

**Store listing:** CurseForge Generic egg, imported via `EGG_IMPORT_URL` in `.env`.

| Panel env (CurseForge Generic) | Value |
|---|---|
| `PROJECT_ID` | CurseForge modpack project ID (set in `.env` / the panel, never in git) |
| `VERSION_ID` | `latest` on the test server |
| `API_KEY` | CurseForge console key (panel / `.env` only, never in git) |

Pick the egg Java docker image required by the Minecraft version in `pack/pack.toml`. Look up current Mojang/NeoForge Java requirements when that version changes.

The CurseForge Generic egg installs from the last published CurseForge file. It does not track git.

If the Generic egg warns that the file is not a server pack, it will use the client zip. That is expected until a distinct CurseForge server pack is uploaded.

## Overlay files

Re-copy these onto the server **after every egg reinstall** (the install script writes `/mnt/server`):

- `run.sh` — NeoForge start. Panel startup is `bash run.sh`. Uses Java 21 ZGC from `user_jvm_args.txt`. Sets `-Xmx` below the panel `SERVER_MEMORY` limit (about 1.5 GiB headroom) so ZGC and native memory do not trigger Linux OOM kill (exit 137). Do not add `-XX:+ZGenerational`.
- `user_jvm_args.txt` — copied from `pack/user_jvm_args.txt`
- `ops.json`
- `server-icon.png` — 64×64 leyline emblem shown beside the server name in the multiplayer list

The NeoForge egg’s default startup is `java … @unix_args.txt` and ignores `user_jvm_args.txt`. Local NeoForge deploys set startup to `bash run.sh` so ZGC actually applies. The CurseForge Generic egg keeps its own startup.
