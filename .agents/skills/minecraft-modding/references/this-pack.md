# Lead and Leylines — pack mapping

Read this after Step 0. This repository is one Forge pack managed with packwiz, not a loose `mods/` folder.

## Instance context

Read Minecraft version, loader name, and loader version from `pack/pack.toml` (`[versions]`). Do not copy those numbers into skills or invent a second pack.

| Fact | Where |
|---|---|
| Pack display name | `pack/pack.toml` `name` (Lead and Leylines) |
| Pack version | `pack/pack.toml` `version` (must match git tag `vX.Y.Z` without the `v`) |
| Source of truth | `pack/mods/*.pw.toml` + `pack/index.toml` |
| Live manifest | `docs/mods/manifest.md` |
| Decision logs | `docs/mods/` (e.g. `performance.md`) |
| Config notes | `docs/mods/configs.md` — only settings that need pack notes |
| Local test | Prism + `packwiz serve` (see CONTRIBUTING.md). Friends: ATLauncher Import of `dist/*.mrpack` from `python scripts/deploy_server.py --share-only` |
| Dedicated server | `python scripts/deploy_server.py` (Forge egg + local mods until CurseForge is public). Overlay in `server/` is not exported; same pack, packwiz `side` |

GitHub remote is `https://github.com/TinorNoah/Lead-and-Leylines.git`. Do not change remotes or store project slugs as a side effect of adding a mod.

## Never drop a jar in

Install only with packwiz from `pack/`:

- `packwiz curseforge install <slug-or-url>` / `packwiz modrinth install <slug-or-url>`
- Pin a Modrinth file with `packwiz modrinth install --project-id <id> --version-id <id> -y` (do not pass a slug together with `--version-id`)
- After any manual TOML edit: `packwiz refresh`
- Set packwiz `side` to `client`, `server`, or `both`. Server-logic mods that should work in singleplayer must be `both`.
- Stage TOML only. Never commit `.jar` files, launcher instances, `.env`, or tokens.

The installer after Steps 1–4 approval is the `add-mod` skill. Do not run `add-mod` until the user approved the recommendation.

## Step 5 on this pack

The git tree (TOML + `docs/mods/`) is the reproducible backup. The Prism `mods/` folder is a local download cache and is not committed.

- Note `pack.toml` `version` and `git status` before installing.
- Do not copy jars into the repo as a “backup.”
- World saves live in the Prism instance; back those up only when Step 2 flagged persistent world data.

## Step 6 on this pack

1. Re-verify the store file still lists this pack’s Minecraft + Forge from `pack.toml`.
2. Install with packwiz (required deps only). Do not bump Minecraft, Forge, or shared libraries in `pack.toml` to make a mod fit.
3. `packwiz refresh`.
4. Sync Prism with `packwiz serve` + installer bootstrap, then confirm a clean boot (log + intended feature), not just that a TOML file appeared. For a dedicated-server check, `python scripts/deploy_server.py --from-local` and watch the panel console.
5. Update `docs/mods/manifest.md` and the relevant `docs/mods/` decision log. Confirm the manifest matches `pack/mods/*.pw.toml`.

Shaders: Oculus is the loader. Do not add a separate dynamic-lights mod while Oculus is in. Shader packs are a later pack feature, not a silent add.

## Rollback on this pack

`packwiz remove` (or delete the `*.pw.toml`), then `packwiz refresh`. Check the manifest before removing a shared library (Placebo, Almanac, and similar). Update `docs/mods/manifest.md`.
