# Lead and Leylines

Long-lived Minecraft Forge modpack. Source of truth is git + packwiz TOML under `pack/`.

## Versions

Read Minecraft version, loader name, and loader version from `pack/pack.toml` (`version`, `[versions]`). Do not copy those numbers into docs, skills, or workflow inputs. Bump by editing `pack.toml` after checking current loader docs.

Pack `version` must match git tag `vX.Y.Z` without the `v`.

## Commands

Run packwiz from `pack/`:

- `packwiz refresh` after any manual file change
- `packwiz curseforge install <mod>` / `packwiz modrinth install <mod>` (aliases `cf add` / `mr add`)
- Pin a Modrinth file with `packwiz modrinth install --project-id <id> --version-id <id> -y` (do not pass a slug together with `--version-id`)
- `packwiz update --all`
- `packwiz curseforge export` / `packwiz modrinth export`
- `packwiz serve` → `http://localhost:8080/pack.toml`
- From repo root: `python scripts/release.py vX.Y.Z --changelog notes.md` — GitHub Release; then dedicated test server; then GitHub Actions for CurseForge + Modrinth (client and server packs; default alpha); then local Prism (`scripts/update_prism.py`). Changelog is the public notes only.

Never commit `.jar` files, launcher instance folders, `.env`, or tokens.

## Layout

- `pack/` — packwiz root (only this tree is exported)
- `server/` — dedicated-server overlay; never indexed
- `.agents/skills/` — shared agent skills (not `.cursor/skills/`)
- `scripts/release.py` — tag + GitHub Release + local server update + Prism sync
- `.github/workflows/publish-stores.yml` — CurseForge + Modrinth after Wings (default alpha; client + server files)

Use packwiz `side` (`client` / `server` / `both`) on mods and configs. One pack, not two roots.

## Local test (Prism)

1. Set the Prism instance Minecraft and loader to the values in `pack/pack.toml`.
2. From `pack/`, run `packwiz serve`.
3. Put `packwiz-installer-bootstrap.jar` in the instance `.minecraft`.
4. Pre-launch: `$INST_JAVA -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml` (do not quote `$INST_JAVA` in instance.cfg; see CONTRIBUTING.md)

See CONTRIBUTING.md for the full loop. `python scripts/release.py` also runs `python scripts/update_prism.py` unless `--skip-prism`.

## Publishing

`python scripts/release.py vX.Y.Z --changelog notes.md` on `main` after `pack.toml` `version` is `X.Y.Z`. The changelog is the GitHub Release body and the CurseForge/Modrinth notes. Do not mention the test server, panel, or join address there. Operator tokens live in gitignored `.env`, never in git:

- `GH_TOKEN` (GitHub Release + Wings pull)
- Optional `CURSEFORGE_*` / `MODRINTH_*` only with `--upload-stores` (`MODRINTH_PROJECT_ID` is the 8-character dashboard id, not the slug)

Store publish tokens live as GitHub Actions secrets.

Never hardcode those values. CurseForge and Modrinth publish from GitHub Actions secrets after the live instance update (default alpha). Official `--channel release` is GitHub Latest plus store release. Local `.env` store keys are optional (`--upload-stores`). Missing `GH_TOKEN` skips the GitHub Release but still updates the test server and local Prism.

## Dedicated server

CurseForge Generic egg tracks the last published CurseForge file, not git. Until that listing is public, `python scripts/deploy_server.py` (default `--from-local`) installs the Forge Minecraft egg and has Wings pull the GitHub Release server-mods zip when `GH_TOKEN` is set, otherwise the local zip. `--share-only` writes ATLauncher zip/mrpack under `dist/`. See `server/README.md`. Application API `papp_` key, panel URL, and node FQDN live in gitignored `.env` — never commit those hostnames. `test-server` skill: local deploy until CF is public; then `--curseforge --reinstall`.

## Skills

- `minecraft-modding` — research, compatibility, approval, manifest (read before any install)
- `add-mod` — packwiz install after `minecraft-modding` approval; then refresh
- `update-changelog` — player-facing `[Unreleased]` bullet when a change is noticeable
- `test-server` — dedicated server via `scripts/deploy_server.py` (`--from-local` until CurseForge is public); console still from the panel until a client API key exists
- `publish-release` — only on explicit `/publish-release`; runs `python scripts/release.py`

## Learned User Preferences

- Verify current versions, docs, and API behavior on the web before implementing; do not assume file structures, tool defaults, or mod compatibility.
- Favor maintainability over speed-of-first-commit on this long-lived pack.
- Ask clarifying questions before structural decisions (repo layout, branching, client/server split) rather than picking silently.
- Never hardcode API tokens, platform project IDs, panel URLs, or node FQDNs; store them in gitignored `.env` (not in `mcp.json`). Missing `GH_TOKEN` in `.env` skips the GitHub Release attach; the test server still updates.
- Keep agent skills under `.agents/skills/` (not `.cursor/skills/`) so any agent tool reads the same files.
- Run the `publish-release` skill only on an explicit `/publish-release` invocation (`disable-model-invocation: true`).
- Research each candidate mod in detail (compatibility first, including planned content mods), ask why it belongs, and compare alternatives before installing. Get explicit install approval after that research; do not install from a named list until then. Prefer client and server changes that make the pack smoother without reliability issues. Overworld height is Tectonic 3 (toned-down pack config + Lithostitched). Streams is out for `/rtp`. Do not treat Chunky as required for `/rtp`. Do not add Lithosphere as a second height line. When adding recipe-bearing mods, check in-jar EMI coverage; do not add JEI or extra EMI addon jars unless requested. Melee is Epic Fight + ParCool (not Better Combat). AE2 and Refined Storage both ship; AE2 expansion kits may be stacked when requested. Skip Gateways until Apotheosis/Apothic Attributes is an intentional combat change.
- Record mod decisions in `docs/mods/` (considered, chosen, held, or dropped; rationale; packwiz `side`); document only configs that need pack notes.
- Keep agent skills short and single-purpose (checklists that link out). Policy, rationale, and examples live in `docs/` (for example `docs/RELEASING.md`), not in SKILL.md files.
- Ship and deploy only through `python scripts/release.py` then `python scripts/deploy_server.py --from-local` (GitHub Release attach, then Wings `files/pull`), then `python scripts/update_prism.py`. Do not improvise local zip uploads or skip that sequence.

## Learned Workspace Facts

- Pack display name is **Lead and Leylines** (`pack/pack.toml` `name`). GitHub remote is `https://github.com/TinorNoah/Lead-and-Leylines.git`. Modrinth slug is `lead-and-leylines` (`https://modrinth.com/modpack/lead-and-leylines`). Pack files are MIT (`LICENSE`); third-party mods keep their own licenses. Modrinth listing: description from README pitch, license MIT, version environment client and server.
- This is a long-term Minecraft Forge modpack managed with packwiz; never commit jars.
- Packwiz root is `pack/`; docs (including `docs/mods/` decision logs) and `.agents/` stay at the repo root and are not exported. Shaders are a pack feature (Oculus + Embeddium); Colorwheel is the Create + Oculus path. Embeddium is the renderer — do not add OptiFine, Nvidium, VulkanMod, or Distant Horizons. Shader packs ship but none is enabled by default, so TACZ gun-muzzle/tracer lights (TaCZ x Guns Lights) are allowed; do not stack a second general dynamic-lights mod (LambDynamicLights, Embeddium Extra lights, Sodium/Embeddium Dynamic Lights). If a shader pack is later enabled, gun lights may flicker — turn them down or off. Default Options ships a two-line `options.txt` (`version` + `biomeBlendRadius:0`); do not ship a full video preset. Java 17 pack flags are `pack/user_jvm_args.txt` (`-XX:+UseZGC`); `scripts/update_prism.py` copies them into Prism `instance.cfg`. Dedicated Forge starts with `server/run.sh` (`bash run.sh` on the Forge egg) so `@user_jvm_args.txt` actually applies. Do not add `-XX:+ZGenerational` on this runtime. Mrpack cannot auto-apply launcher JVM args.
- Branching is GitHub Flow (`main`, feature branches, PRs); pack version `X.Y.Z` matches git tag `vX.Y.Z`. `python scripts/release.py vX.Y.Z` creates the GitHub Release from `CHANGELOG.md`, updates the live instance, then dispatches `.github/workflows/publish-stores.yml`.
- Minecraft, loader, and loader version live only in `pack/pack.toml`; bump that file and keep the README Pack details table in sync in the same change. Do not hardcode versions in skills.
- One pack uses packwiz `side` (`client` / `server` / `both`); server overlay lives in `server/` (`run.sh`) and is never exported. `scripts/deploy_server.py` copies `pack/user_jvm_args.txt` onto the Forge instance as `/user_jvm_args.txt`. Server-logic optimizers we ship use `both` so Prism singleplayer matches the dedicated server. Too Fast stays `server`.
- Local Prism testing uses `packwiz serve` plus packwiz-installer-bootstrap against `http://localhost:8080/pack.toml`. `python scripts/release.py` also runs `scripts/update_prism.py` (serve on a free port, installer `-g`) unless `--skip-prism`. Instance path is `PRISM_INSTANCE_DIR` in `.env`, or the PrismLauncher instance whose `name` matches `pack.toml`. After removing a both-side worldgen or fluid mod, sync Prism before joining (fully quit the game first so leftover locked jars can be deleted) or the client crashes on missing registry objects.
- Panel URL and Wings node FQDN come from gitignored `.env` (`PANEL_URL`, `PANEL_NODE_FQDN`). Deploy with `python scripts/deploy_server.py` (Forge egg; Wings `files/pull` of the GitHub Release `*-server-mods.zip` when `GH_TOKEN` is set, otherwise the local zip — not a GitHub raw pack.toml URL; Wings `files/write` of that zip is unreliable). Generic egg tracks the last published CurseForge file after that.
- `python scripts/release.py` exports zip + mrpack from `CHANGELOG.md` `## [X.Y.Z]` (the script is read-only on that file; promote `[Unreleased]` in the `publish-release` skill first). Default `--channel alpha` is a GitHub prerelease; after Wings, GitHub Actions uploads CurseForge/Modrinth as alpha (client pack + server-mods zip). `--channel release` is GitHub Latest plus store release. Do not later re-upload the same `X.Y.Z` as a store release — cut a new version. Then updates the panel locally. Do not mention the dedicated server, the panel, or the join address in GitHub Release notes, CHANGELOG.md, commit messages, or other GitHub-facing copy. `MODRINTH_PROJECT_ID` is the 8-character dashboard id, not the slug. Channel and changelog policy: `docs/RELEASING.md`. Every `release.py` run updates the test server unless `--skip-server`, and local Prism unless `--skip-prism`.
- Use `.gitattributes` `* -text` so Windows line endings do not break packwiz hashes.
- `CLAUDE.md` is a one-line `@AGENTS.md` pointer.
- Planned content to stay compatible with: TACZ, Superb Warfare, Apotheosis, Create, AE2, Refined Storage, Ars Nouveau, Modern Industrialization, Building Gadgets, Mining Gadgets, Mekanism (installed), Mob Grinding Utils, plus later magic / tech / utility mods. Skip TaCZ Ammo Query and No Mindless Shooting; hold TACZ Durability. Item storage is Functional Storage (drawers) + Sophisticated Storage (chests) + Sophisticated Backpacks with Curios (not Storage Drawers, Iron Chests, or Tom’s Simple Storage). AE2 is the primary item network; RS is also in. Overworld biomes are Terralith + Regions Unexplored + Oh The Biomes We’ve Gone (Terralith gets rarer in that stack). Overworld height is Tectonic 3.0.17 + Lithostitched 1.4.11 (Modrinth omits the Lithostitched dep; the jar still requires it; toned-down `pack/config/tectonic.json`: Vertical Scale 0.80, climate scale 0.16, extra caves/pillars/rivers/islands off). Do not add Lithosphere or Terratonic (Forge jars already blend Terralith). TerraBlender Overworld and Nether regions stay at max size (`overworld_region_size` 6, `nether_region_size` 6) so RU/BWG/Terralith slices are not postage stamps; do not lower region size. Streams Reflowing is out. Do not stack William Wythers’ Expanded Ecosphere with RU/BWG. Nether is Amplified Nether (height) + BetterNether Forge (biomes), not Incendium. End is Nullscape (Stardust Forge jar), not Better End. Fortresses are YUNG’s Better Nether Fortresses. Infernal content is Infernal Expansion Redux (no 1.20.1 original). Nether cooking is Farmer’s Delight + My Nether’s Delight (not the 2023 Nether’s Delight jar). Mineshafts are Moog’s Mineshafts Reimagined, not YUNG’s Better Mineshafts. Twilight Forest is the official CurseForge jar only (not the Modrinth Unofficial port). Structure spacing is Better Sparse Structures (`globalSpacingRadiusChunks` 4, overlap reject); whitelist `alexscaves:*` and `create_sky_village:*`. Do not re-add Sparse Structures next to it. Create sky villages use author spacing 80/40. Do not add StructureOverlapless (it skips placement so `/locate` points at empty spots; BSS overlap reject has the same skip class). `/rtp` and `/locate` stay short-range (or already-generated) or the dedicated-server watchdog can hang; do not `/locate` MMR biome-locked mineshafts over ungenerated land. Ice and Fire is Community Edition (not the official AlexThe666 jar; they cannot both load). Melee is Epic Fight + ParCool + Official Epic ParCool (not Better Combat). Official Epic ParCool mixins still need ParCool 3.4 (`com.alrex.parcool.common.action.Action`); do not pin ParCool 4.0 alpha until the bridge is rewritten. Do not add distant-tick freezers, a second Lithium port, a second claim mod, or a second map UI. FTB Chunks is the claim layer (minimap off; unbind Open Map); Xaero is the map UI. EMI is the recipe viewer (not JEI; extra EMI jars only when requested — Enchants, WorldGen, and QoL Tweaks are in). Too Many Recipe Viewers registers a fake `jei` id at 15.20, so keep Polymorph at 0.49.10 — 0.49.11+ version-gates JEI 15.57 and Forge aborts; do not add real JEI to satisfy it. Create + Oculus uses Colorwheel + Colorwheel Patcher (not Iris/Oculus Flywheel Compat). Complementary Euphoria Patches matches the r5.9.3 Complementary packs.
