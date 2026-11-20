# Lead and Leylines

Long-lived Minecraft NeoForge modpack. Source of truth is git + packwiz TOML under `pack/`. Mod bans, pins, required sides, and must-keep configs live in [`docs/mods/rules.md`](docs/mods/rules.md) — read it before adding, removing, updating, or configuring any mod.

## Versions

- Minecraft, loader, and loader version live only in `pack/pack.toml`. Do not copy those numbers into docs, skills, or workflow inputs. When bumping, check current loader docs and update the README Pack details table in the same change.
- Pack `version` matches git tag `vX.Y.Z` without the `v`. Never retag or re-upload a shipped version; cut a new one. The 1.20.1 Forge pack (`v0.0.1`–`v0.0.9`) is archived on `forge-1.20.1`; do not copy it onto `main`.

## Layout

- `pack/` — packwiz root, the only exported tree. `server/` — dedicated-server overlay (`run.sh`), never indexed. `docs/`, `.agents/`, `site/` stay at the repo root. `dist/` is gitignored (search it with `rg --no-ignore`).
- One pack: set packwiz `side` (`client` / `server` / `both`) on every mod and config. Server-logic mods are `both` so singleplayer matches the server.
- Shipped server-config defaults go in `pack/config/` (the server zip never includes `defaultconfigs/`). CurseForge resource packs and datapacks ship as packwiz metadata, not committed zips; force-enable client packs in `pack/config/global_packs.toml`. TaCZ packs: `pack/tacz/`. Point Blank: `pack/pointblank/`. KubeJS: `pack/kubejs/`.
- `leylines_patches` (the pack's own compatibility mod) lives in [Lead-and-Leylines-Patches](https://github.com/TinorNoah/Lead-and-Leylines-Patches); its README is the fix ledger and regression checklist. Read it before changing the patch or the MI / EI / Armaments versions it pins. Update `pack/mods/leylines-patches.pw.toml` from its `patches-vX.Y.Z` prereleases. The smoke test never loads its client Mixins, so client fixes need a manual client test.
- JVM flags: `pack/user_jvm_args.txt`, copied to Prism and the server by the scripts.

## Commands

From `pack/`:

- `packwiz curseforge install <mod>` first; confirm the `.pw.toml` has `[update.curseforge]`. `packwiz modrinth install` only when the mod is not on CurseForge (pin with `--project-id <id> --version-id <id> -y`, no slug).
- `packwiz refresh` after any manual file change. `packwiz serve` → `http://localhost:8080/pack.toml`.

From the repo root:

- After every mod add or remove: hand-edit `docs/installed/catalog.toml` (see `docs/installed/MAINTENANCE.md`), then `python3 scripts/installed_catalog.py` and `--check`.
- After a mod or config change: `python scripts/smoke_test.py` (`--skip-bench` boot-only, `--keep` keeps logs) before `test-server`. After a big content add, also boot a client.
- Local Prism sync: `python scripts/update_prism.py` (setup in CONTRIBUTING.md). Fully quit the game first after removing a `both` worldgen or fluid mod.

Never commit `.jar` files, launcher instances, `.env`, tokens, or panel hostnames.

## Releasing and the server

- `python scripts/release.py vX.Y.Z` on `main` does GitHub Release (notes from `CHANGELOG.md` `## [X.Y.Z]`), then the Pelican server (pulls that Release's server zip), then local Prism. Policy: `docs/RELEASING.md`. Run the `publish-release` skill only on an explicit `/publish-release`.
- Every Pelican deploy (`release.py` or `scripts/deploy_server.py`) deletes the world. Pass `--keep-world` only when the user explicitly says to keep it. Use `--skip-server` only when the user asks for a GitHub-only release. CurseForge only when asked (`--curseforge` via Actions, `--upload-stores` locally). Never upload the server zip to Pelican directly.
- Never mention the test server, panel, or join address in GitHub-facing copy (Release notes, CHANGELOG, commits, PRs).
- Secrets live in gitignored `.env` only: `GH_TOKEN` (without it there is no Release and the Pelican pull fails), panel URL, node FQDN, `papp_` key, optional `CURSEFORGE_*`. Site icons need `CURSEFORGE_API_KEY` in the site env.
- Server details: `server/README.md`. Pin the egg's `NEOFORGE_VERSION` to the exact `pack.toml` loader version. Do not wipe the packwiz cache or `.cache/mod-files`.

## Skills

Under `.agents/skills/` (not `.cursor/skills/`). Pack-authored skills stay short checklists that link to `docs/`. Third-party skills (installed with `npx skills add <repo> -s <skill> -a cursor --copy -y`, pinned in `skills-lock.json`) stay as upstream wrote them; this file and `docs/mods/rules.md` win on conflicts.

- `minecraft-modding` → `add-mod` — research and approval, then install
- `update-changelog` — player-facing `[Unreleased]` bullet
- `local-smoke-test` → `test-server` — local boot, then the dedicated server
- `publish-release` — explicit `/publish-release` only
- `modpack-audit`, `stitch-screen` — reference-pack audits; site screens
- Third-party: `kubejs-modding`, `minecraft-datapack`, `minecraft-resource-pack`, `minecraft-modpack-authoring`

## Working preferences

- Verify on the web and in the jars (`javap`, `neoforge.mods.toml`, `*.mixins.json`, logs) before acting; do not treat this file or `docs/` as proof. State player-visible trade-offs before removing a mod.
- Install a mod only after research and explicit approval, never from a list or `docs/mods/deferred.md` alone. When asked to update mods, never silently hold or revert a breaking update: ask whether to write a `leylines_patches` fix (preferred), pin, or update anyway.
- Ask before structural decisions (repo layout, branching, side split). Favor maintainability. Agent work uses GitHub Flow (feature branch + PR).
- Record mod decisions in `docs/mods/` and open work in `docs/TODO.md`. Do not commit every mod's generated config defaults. Keep helper scripts single-purpose; add at most a one-line hook to `release.py` or `pack_artifacts.py`.
- FTB Quests (`pack/config/ftbquests/`): teach the whole pack in GregTech / ATM10-style chapters with tech (Modern Industrialization first) as the gated spine. Moderate item and XP rewards; mod chapters roll random same-mod items. Tone: Gate / Demon Lord 2077 / Witcher mashup building toward a leyline-confluence endgame.
- Site (`site/`, Bun, Dokploy): player-first mod browser reading `docs/installed/catalog.json` from `main` at runtime. Earthy adventure look from the Stitch mocks, not a SaaS dashboard; pack emblem favicon; header shows the latest release and prerelease.
