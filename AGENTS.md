# Lead and Leylines

Long-lived Minecraft NeoForge modpack. Source of truth is git + packwiz TOML under `pack/`.

## Versions

Read Minecraft version, loader name, and loader version from `pack/pack.toml` (`version`, `[versions]`). Do not copy those numbers into docs, skills, or workflow inputs. Bump by editing `pack.toml` after checking current loader docs.

Pack `version` must match git tag `vX.Y.Z` without the `v`.

Tags `v0.0.1`–`v0.0.9` already shipped as Minecraft 1.20.1 Forge. Do not retag or re-upload those versions. The empty 1.21.1 NeoForge working tree may use pack version `0.0.1`; the first NeoForge GitHub/store ship is `v0.1.0`.

## Commands

Run packwiz from `pack/`:

- `packwiz refresh` after any manual file change
- `packwiz curseforge install <mod>` / `packwiz modrinth install <mod>` (aliases `cf add` / `mr add`)
- Pin a Modrinth file with `packwiz modrinth install --project-id <id> --version-id <id> -y` (do not pass a slug together with `--version-id`)
- `packwiz update --all`
- `packwiz curseforge export` / `packwiz modrinth export`
- `packwiz serve` → `http://localhost:8080/pack.toml`
- From repo root: `python scripts/release.py vX.Y.Z --changelog notes.md` — GitHub Release; then dedicated test server; then GitHub Actions for CurseForge (client and server packs; default alpha); then local Prism (`scripts/update_prism.py`). Changelog is the public notes only.

Never commit `.jar` files, launcher instance folders, `.env`, or tokens.

## Layout

- `pack/` — packwiz root (only this tree is exported)
- `server/` — dedicated-server overlay; never indexed
- `.agents/skills/` — shared agent skills (not `.cursor/skills/`)
- `scripts/release.py` — tag + GitHub Release + local server update + Prism sync
- `.github/workflows/publish-stores.yml` — CurseForge after Wings (default alpha; client + server files)

Use packwiz `side` (`client` / `server` / `both`) on mods and configs. One pack, not two roots.

## Local test (Prism)

1. Set the Prism instance Minecraft and loader to the values in `pack/pack.toml`. Use Java 21.
2. From `pack/`, run `packwiz serve`.
3. Put `packwiz-installer-bootstrap.jar` in the instance `.minecraft`.
4. Pre-launch: `$INST_JAVA -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml` (do not quote `$INST_JAVA` in instance.cfg; see CONTRIBUTING.md)

See CONTRIBUTING.md for the full loop. `python scripts/release.py` also runs `python scripts/update_prism.py` unless `--skip-prism`. Do not mix leftover 1.20.1 Forge jars into a 1.21.1 NeoForge instance.

## Publishing

`python scripts/release.py vX.Y.Z --changelog notes.md` on `main` after `pack.toml` `version` is `X.Y.Z`. The changelog is the GitHub Release body and the CurseForge notes. Do not mention the test server, panel, or join address there. Operator tokens live in gitignored `.env`, never in git:

- `GH_TOKEN` (GitHub Release + Wings pull)
- Optional `CURSEFORGE_*` only with `--upload-stores`

Store publish tokens live as GitHub Actions secrets.

Never hardcode those values. CurseForge publishes from GitHub Actions secrets after the live instance update (default alpha). Official `--channel release` is GitHub Latest plus store release. Local `.env` store keys are optional (`--upload-stores`). Missing `GH_TOKEN` skips the GitHub Release but still updates the test server and local Prism.

## Dedicated server

CurseForge Generic egg tracks the last published CurseForge file, not git. Until that listing is public, `python scripts/deploy_server.py` (default `--from-local`) installs the NeoForge egg and has Wings pull the GitHub Release server-mods zip when `GH_TOKEN` is set, otherwise the local zip. `--share-only` writes ATLauncher zip/mrpack under `dist/`. See `server/README.md`. Application API `papp_` key, panel URL, and node FQDN live in gitignored `.env` — never commit those hostnames. `test-server` skill: local deploy until CF is public; then `--curseforge --reinstall`.

## Skills

- `minecraft-modding` — research, compatibility, approval, manifest (read before any install)
- `add-mod` — packwiz install after `minecraft-modding` approval; then refresh
- `update-changelog` — player-facing `[Unreleased]` bullet when a change is noticeable
- `local-smoke-test` — local dedicated-server boot via `scripts/smoke_test.py` before `test-server`
- `test-server` — dedicated server via `scripts/deploy_server.py` (`--from-local` until CurseForge is public); console still from the panel until a client API key exists
- `publish-release` — only on an explicit `/publish-release`; runs `python scripts/release.py`

## Learned User Preferences

- Verify current versions, docs, and API behavior on the web before implementing; do not assume file structures, tool defaults, or mod compatibility.
- Favor maintainability over speed-of-first-commit on this long-lived pack.
- Ask clarifying questions before structural decisions (repo layout, branching, client/server split) rather than picking silently.
- Never hardcode API tokens, platform project IDs, panel URLs, or node FQDNs; store them in gitignored `.env` (not in `mcp.json`). Missing `GH_TOKEN` in `.env` skips the GitHub Release attach; the test server still updates.
- Keep agent skills under `.agents/skills/` (not `.cursor/skills/`) so any agent tool reads the same files. Track `.cursor/` in git except `hooks/state`; keep `.env` local per machine.
- Run the `publish-release` skill only on an explicit `/publish-release` invocation (`disable-model-invocation: true`).
- Research each candidate mod in detail (compatibility first), ask why it belongs, and compare alternatives before installing. Get explicit install approval after that research; do not install from a named list or from `docs/mods/deferred.md` until then. Re-verify deferred notes against the current loader and renderer rather than trusting old add/skip buckets. Prefer client and server changes that make the pack smoother without reliability issues. Do not stack overlapping optimizers or renderer extras, do not add distant-entity freezers, do not re-add Noisium (or NoisiumForked) while Bye?Pregen! is in, do not re-add Tectonic, do not re-add Iris Flywheel Compat while Colorwheel is in, do not re-add Immersive Ballistic (or TaCZ Tweaks) while Iris is in (vertex-format conflict), do not add Serene Seasons while Ecliptic Seasons is in, do not re-add Mekanism Covers while Sodium 0.8.x is in (Sodium mixin hard-fail), do not re-add JEI++ while JEI 19.57 is in (bookmark mixin still calls the old `IUserInputHandler`), and do not re-add Ecliptic Seasons Voxy Compact or Voxy Make-it-compatible without a shippable Voxy client jar (`voxy-forged` is ARR/local-only; Voxy Server Side may stay). When adding recipe-bearing mods, check in-jar JEI coverage; do not add EMI, TMRV, or extra JEI addon jars unless requested. JEI QuickCraft and JEI Stuff stay packwiz `both` (required network channels).
- Install with `packwiz curseforge install` first and confirm the new `.pw.toml` has `[update.curseforge]` (retry `--addon-id` / `--file-id` on a slug miss). Use `packwiz modrinth install` only when the mod is not on CurseForge; that fallback is a mod source, not a store listing. After a mod or config change, run `python scripts/smoke_test.py` before `test-server` (default appends a Chunk Pregenerator + `/tick query` report under `docs/smoke-runs/`; `--skip-bench` is the fast boot-only check).
- Record mod decisions in `docs/mods/` (considered, chosen, held, or dropped; rationale; packwiz `side`); document only configs that need pack notes. `docs/mods/deferred.md` is the not-yet-ported 1.20.1 list plus researched skip/hold reasons, not an install queue; keep it to mods that are not in `pack/mods/`.
- Keep agent skills short and single-purpose (checklists that link out). Policy, rationale, and examples live in `docs/` (for example `docs/RELEASING.md` and `docs/mods/distribution.md`), not in SKILL.md files. Helper scripts stay single-purpose; do not fold new checks into `release.py` or `pack_artifacts.py` beyond a one-line hook.
- Ship and deploy only through `python scripts/release.py` then `python scripts/deploy_server.py --from-local` (GitHub Release attach, then Wings `files/pull`), then `python scripts/update_prism.py`. Do not improvise local zip uploads or skip that sequence.
- When porting combat and storage from the old pack, use Epic Fight + ParCool (not Better Combat), the unofficial 1.21.1 TaCZ port for guns (not 1.20.1 TaCZ worlds), and Ice and Fire Community Edition (not original Ice and Fire). Do not re-add Epic Fight Nightfall (or Invincible Lib for it) — Nightfall crashes dedicated servers reading client VFX config. AAA Particles stays for Effekseer. Epic Fight × Curios Compat stays packwiz `client` (loads client classes on dedicated servers). Keep both Applied Energistics 2 and Refined Storage. Create vehicles are Create Aeronautics with Sable. Ice and Fire pixie villages generate in the Nether, not overworld forests.

## Learned Workspace Facts

- Pack display name is **Lead and Leylines** (`pack/pack.toml` `name`). GitHub remote is `https://github.com/TinorNoah/Lead-and-Leylines.git`. Pack files are MIT (`LICENSE`); third-party mods keep their own licenses. CurseForge is the sole public store listing. The `.mrpack` is still built for ATLauncher testers.
- This is a long-term Minecraft NeoForge modpack managed with packwiz; never commit jars. `main` is the 1.21.1 NeoForge pack (official Sodium / Iris / Lithium, not Embeddium / Oculus / Radium). Colorwheel (plus Colorwheel Patcher) is the Create + Iris / Euphoria path; Iris Flywheel Compat is out (mixin conflict). The recipe viewer is JEI with MezzConfig, not EMI or TMRV. Seasons are Ecliptic Seasons (plus the Serene Seasons API stub), not Serene Seasons. Tectonic is out; Overworld biomes stay large and less mixed via TerraBlender region size 6 plus the large-climate datapack (do not use the Large Biomes world type). Pack config skips the BetterX / WorldWeaver first-run welcome and does not force the BetterX world type (Terralith / TerraBlender stay the create-world path). The 1.20.1 Forge pack is archived on `forge-1.20.1` (tag `archive/forge-1.20.1`); do not copy that content onto `main`.
- Packwiz root is `pack/`; docs (including `docs/mods/` decision logs) and `.agents/` stay at the repo root and are not exported. Java 21 pack flags are `pack/user_jvm_args.txt` (`-XX:+UseZGC`); `scripts/update_prism.py` copies them into Prism `instance.cfg`. Dedicated NeoForge starts with `server/run.sh` (`bash run.sh` on the NeoForge egg) so `@user_jvm_args.txt` actually applies; leave heap headroom below the panel RAM limit for ZGC/native (do not set `-Xmx` to the full container memory). Do not add `-XX:+ZGenerational`. The C2ME OpenCL Acceleration Module needs Java 25 and stays out. Mrpack cannot auto-apply launcher JVM args. Orphan Evolved Mekanism / soft-dep loot tables are emptied by datapack `lead-leylines-orphan-loot`.
- Branching is GitHub Flow for agent-authored work (`main`, feature branches, PRs). Direct trivial human edits may go to `main`. Pack version `X.Y.Z` matches git tag `vX.Y.Z`. `python scripts/release.py vX.Y.Z` creates the GitHub Release from `CHANGELOG.md`, updates the live instance, then dispatches `.github/workflows/publish-stores.yml`.
- Minecraft, loader, and loader version live only in `pack/pack.toml`; bump that file and keep the README Pack details table in sync in the same change. Do not hardcode versions in skills.
- One pack uses packwiz `side` (`client` / `server` / `both`); server overlay lives in `server/` (`run.sh`) and is never exported. `scripts/deploy_server.py` copies `pack/user_jvm_args.txt` onto the NeoForge instance as `/user_jvm_args.txt`. Pin `NEOFORGE_VERSION` to the exact `pack.toml` loader version; do not let the egg resolve 1.21.1 from `MC_VERSION` alone (it can pick 1.21.10 / 1.21.11). Server-logic optimizers we ship use `both` so Prism singleplayer matches the dedicated server.
- Local Prism testing uses `packwiz serve` plus packwiz-installer-bootstrap against `http://localhost:8080/pack.toml`. `python scripts/release.py` also runs `scripts/update_prism.py` (serve on a free port, installer `-g`) unless `--skip-prism`. Instance path is `PRISM_INSTANCE_DIR` in `.env`, or the PrismLauncher instance whose `name` matches `pack.toml`. After removing a both-side worldgen or fluid mod, sync Prism before joining (fully quit the game first so leftover locked jars can be deleted) or the client crashes on missing registry objects.
- Panel URL and Wings node FQDN come from gitignored `.env` (`PANEL_URL`, `PANEL_NODE_FQDN`). Deploy with `python scripts/deploy_server.py` (NeoForge egg; Wings `files/pull` of the GitHub Release `*-server-mods.zip` when `GH_TOKEN` is set, otherwise the local zip — not a GitHub raw pack.toml URL; Wings `files/write` of that zip is unreliable). Generic egg tracks the last published CurseForge file after that. Switching Minecraft or loader versions reinstalls the egg and wipes the test world.
- `python scripts/release.py` exports zip + mrpack from `CHANGELOG.md` `## [X.Y.Z]` (the script is read-only on that file; promote `[Unreleased]` in the `publish-release` skill first). Default `--channel alpha` is a GitHub prerelease; after Wings, GitHub Actions uploads CurseForge as alpha (client pack + server-mods zip). `--channel release` is GitHub Latest plus store release. Do not later re-upload the same `X.Y.Z` as a store release — cut a new version. Then updates the panel locally. Do not mention the dedicated server, the panel, or the join address in GitHub Release notes, CHANGELOG.md, commit messages, or other GitHub-facing copy. Channel and changelog policy: `docs/RELEASING.md`. Every `release.py` run updates the test server unless `--skip-server`, and local Prism unless `--skip-prism`.
- Use `.gitattributes` `* -text` so Windows line endings do not break packwiz hashes.
- CurseForge-first metadata keeps export zips from embedding jars: `scripts/check_exports.py` reports `overrides/mods/` jars after export; `scripts/detect_curseforge.py` is a manual `packwiz curseforge detect` pass, not a release step. Local helpers: `scripts/smoke_test.py` (default benches with Chunk Pregenerator and `/tick query`, never `/neoforge tps`; append-only `docs/smoke-runs/`; Spark is not a pack mod), `scripts/lookup_mod.py`, `scripts/check_outdated.py` (report-only), `scripts/draft_changelog.py`. Optional `.githooks/pre-commit` (`git config core.hooksPath .githooks`) blocks staged jars and warns if mod TOML is staged without CHANGELOG.md.
- `CLAUDE.md` is a one-line `@AGENTS.md` pointer.
