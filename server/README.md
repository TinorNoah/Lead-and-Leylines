# Server overlay

This directory is **not** part of the packwiz index. Do not put these files under `pack/`.

## Deploy

The panel URL and Wings node FQDN live in gitignored `.env` (`PANEL_URL`, `PANEL_NODE_FQDN`). Never commit real hostnames.

Copy [`.env.example`](../.env.example) to `.env` at the repo root. Set `PANEL_API_KEY` to an Application API key (`papp_`). Do not commit `.env`.

Until a CurseForge file exists, the default path is **GitHub + Forge Minecraft**: export the current `pack/` tree, attach `Lead-and-Leylines-<version>-server-mods.zip` to the matching GitHub Release (`vX.Y.Z`) when `GH_TOKEN` is set, switch the test server to the **Forge Minecraft** egg, install Forge from `pack.toml`, and have Wings **pull** that public Release asset (or take the local zip if GitHub is skipped). Do not fall back to a GitHub raw `pack.toml` URL.

```text
python scripts/release.py vX.Y.Z --changelog notes.md
python scripts/deploy_server.py
python scripts/deploy_server.py --from-local
python scripts/deploy_server.py --share-only
python scripts/deploy_server.py --status
python scripts/deploy_server.py --dry-run
python scripts/deploy_server.py --curseforge --reinstall --wait 600
```

`python scripts/release.py vX.Y.Z --changelog notes.md` is the usual ship path: GitHub Release from the changelog, then `--from-local` on this test server, then CurseForge/Modrinth (client + server packs), then local Prism. Default is GitHub prerelease + store alpha. `--channel release` is official on GitHub and both stores. Every release updates the test server unless you pass `--skip-server`, stores unless `--skip-stores`, and Prism unless `--skip-prism`. Do not put panel/join details in that changelog. Use `deploy_server.py` alone when you only need the test server.

`--share-only` writes ATLauncher files under `dist/` (gitignored) and does not touch the panel. `--from-local` does that export, attaches the server-mods zip to the GitHub Release when `GH_TOKEN` is set, and has Wings pull it (or writes the local zip if GitHub is skipped). Reinstalling the Forge egg **wipes the world**; later `--from-local` runs only replace `mods/` if Minecraft/Forge versions are unchanged.

The script owns the server as `PANEL_OWNER_USERNAME` and uses a free allocation on that node. Java image is chosen from the egg from `pack/pack.toml` Minecraft version.

### ATLauncher (friends)

Send them `dist/Lead-and-Leylines-<pack version>.mrpack` (or the `.zip`). In ATLauncher: **Instances → Import → Browse** → select the file → **Import** → name it → **Install**. Store search will not find this pack until CurseForge/Modrinth listings are public. GitHub download URLs often fail ATLauncher's URL import; send the file.

### After CurseForge is public

Set `CURSEFORGE_PROJECT_ID` (numeric modpack id) in `.env`. `CURSEFORGE_API_KEY` is a CurseForge **console** key for the Generic egg (not the panel key). If the console key is omitted, the script copies one already stored on another CurseForge Generic server on the panel. Then:

```text
python scripts/deploy_server.py --curseforge --reinstall --wait 600
```

## Eggs

**Local testing (default):** Forge Minecraft already on the panel (`MC_VERSION` and `FORGE_VERSION` from `pack.toml`; `FORGE_VERSION` is `{minecraft}-{forge}`). Mods come from the GitHub Release server-mods zip, not a Wings push of the zip from this machine.

**Store listing:** CurseForge Generic egg, imported via `EGG_IMPORT_URL` in `.env`.

| Panel env (CurseForge Generic) | Value |
|---|---|
| `PROJECT_ID` | CurseForge modpack project ID (set in `.env` / the panel, never in git) |
| `VERSION_ID` | `latest` on the test server |
| `API_KEY` | CurseForge console key (panel / `.env` only, never in git) |

Pick the egg Java docker image required by the Minecraft version in `pack/pack.toml`. Look up current Mojang/Forge Java requirements when that version changes.

The CurseForge Generic egg installs from the last published CurseForge file. It does not track git.

If the Generic egg warns that the file is not a server pack, it will use the client zip. That is expected until a distinct CurseForge server pack is uploaded.

## Overlay files

`python scripts/deploy_server.py --from-local` copies these after every mods zip (re-copy after an egg reinstall; the install script writes `/mnt/server`):

- `run.sh` — Forge start. Panel startup is `bash run.sh`. Uses Java 17 ZGC from `user_jvm_args.txt`. Do not add `-XX:+ZGenerational`.
- `user_jvm_args.txt` — copied from `pack/user_jvm_args.txt` (`-XX:+UseZGC`)
- `ops.json` — only if present under `server/`

The Forge Minecraft egg’s default startup is `java … @unix_args.txt` and ignores `user_jvm_args.txt`. Local Forge deploys set startup to `bash run.sh` so ZGC actually applies. The CurseForge Generic egg keeps its own startup.
