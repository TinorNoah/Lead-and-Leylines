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
- From repo root: `python scripts/release.py vX.Y.Z --changelog notes.md` — GitHub Release + CurseForge + Modrinth; then dedicated test server. Changelog is the public notes only.

Never commit `.jar` files, launcher instance folders, `.env`, or tokens.

## Layout

- `pack/` — packwiz root (only this tree is exported)
- `server/` — dedicated-server overlay; never indexed
- `.agents/skills/` — shared agent skills (not `.cursor/skills/`)
- `scripts/release.py` — tag + GitHub Release + CurseForge/Modrinth + local server update

Use packwiz `side` (`client` / `server` / `both`) on mods and configs. One pack, not two roots.

## Local test (Prism)

1. Set the Prism instance Minecraft and loader to the values in `pack/pack.toml`.
2. From `pack/`, run `packwiz serve`.
3. Put `packwiz-installer-bootstrap.jar` in the instance `.minecraft`.
4. Pre-launch: `$INST_JAVA -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml` (do not quote `$INST_JAVA` in instance.cfg; see CONTRIBUTING.md)

See CONTRIBUTING.md for the full loop.

## Publishing

`python scripts/release.py vX.Y.Z --changelog notes.md` on `main` after `pack.toml` `version` is `X.Y.Z`. The changelog is the GitHub Release body and the CurseForge/Modrinth notes. Do not mention the test server, panel, or join address there. Tokens live in gitignored `.env`, never in git:

- `GH_TOKEN`
- `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID` (8-character dashboard id, not the slug)

Never hardcode those values. Missing CurseForge or Modrinth values skip that store with an explicit log. Missing `GH_TOKEN` fails. There is no tag GitHub Actions publish job.

## Dedicated server

CurseForge Generic egg tracks the last published CurseForge file, not git. Until that listing is public, `python scripts/deploy_server.py` (default `--from-local`) installs the Forge Minecraft egg and uploads the current pack’s server-side mods via Wings. `--share-only` writes ATLauncher zip/mrpack under `dist/`. See `server/README.md`. Application API `papp_` key, panel URL, and node FQDN live in gitignored `.env` — never commit those hostnames. `test-server` skill: local deploy until CF is public; then `--curseforge --reinstall`.

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
- Never hardcode API tokens, platform project IDs, panel URLs, or node FQDNs; store them in gitignored `.env`.
- Keep agent skills under `.agents/skills/` (not `.cursor/skills/`) so any agent tool reads the same files.
- Run the `publish-release` skill only on an explicit `/publish-release` invocation (`disable-model-invocation: true`).
- Research each candidate mod in detail (compatibility first, including planned content mods), ask why it belongs, and compare alternatives before installing. Get explicit install approval after that research; do not install from a named list until then. Prefer client and server changes that make the pack smoother without reliability issues.
- Record mod decisions in `docs/mods/` (considered, chosen, held, or dropped; rationale; packwiz `side`); document only configs that need pack notes.
- Keep agent skills short and single-purpose (checklists that link out). Policy, rationale, and examples live in `docs/` (for example `docs/RELEASING.md`), not in SKILL.md files.

## Learned Workspace Facts

- Pack display name is **Lead and Leylines** (`pack/pack.toml` `name`). GitHub remote is `https://github.com/TinorNoah/Lead-and-Leylines.git`. Modrinth slug is `lead-and-leylines` (`https://modrinth.com/modpack/lead-and-leylines`). Pack files are MIT (`LICENSE`); third-party mods keep their own licenses. Modrinth listing: description from README pitch, license MIT, version environment client and server.
- This is a long-term Minecraft Forge modpack managed with packwiz; never commit jars.
- Packwiz root is `pack/`; docs (including `docs/mods/` decision logs) and `.agents/` stay at the repo root and are not exported. Shaders are a pack feature (Oculus + Embeddium); Colorwheel is the Create + Oculus path. Embeddium is the renderer — do not add OptiFine, Nvidium, VulkanMod, or a separate dynamic-lights mod while Oculus is in.
- Branching is GitHub Flow (`main`, feature branches, PRs); pack version `X.Y.Z` matches git tag `vX.Y.Z`. `python scripts/release.py vX.Y.Z` creates the GitHub Release from `CHANGELOG.md` (no tag Actions job).
- Minecraft, loader, and loader version live only in `pack/pack.toml`; bump that file and keep the README Pack details table in sync in the same change. Do not hardcode versions in skills.
- One pack uses packwiz `side` (`client` / `server` / `both`); server overlay/JVM overlay lives in `server/` and is never exported. Server-logic optimizers we ship use `both` so Prism singleplayer matches the dedicated server.
- Local Prism testing uses `packwiz serve` plus packwiz-installer-bootstrap against `http://localhost:8080/pack.toml`.
- Panel URL and Wings node FQDN come from gitignored `.env` (`PANEL_URL`, `PANEL_NODE_FQDN`). Deploy with `python scripts/deploy_server.py` (local pack tree via Forge egg + Wings until CurseForge is public; Generic egg tracks the last published CurseForge file after that).
- `python scripts/release.py` exports zip + mrpack from `CHANGELOG.md` `## [X.Y.Z]` (the script is read-only on that file; promote `[Unreleased]` in the `publish-release` skill first). Only `--channel release` uploads to CurseForge/Modrinth; `alpha`/`beta` are GitHub prerelease plus local test-server update and are never promoted — cut a new version for the stores. Then updates the panel locally. Do not mention the dedicated server, the panel, or the join address in GitHub Release notes, CHANGELOG.md, commit messages, or other GitHub-facing copy. `MODRINTH_PROJECT_ID` is the 8-character dashboard id, not the slug. Channel and changelog policy: `docs/RELEASING.md`.
- Use `.gitattributes` `* -text` so Windows line endings do not break packwiz hashes.
- `CLAUDE.md` is a one-line `@AGENTS.md` pointer.
- Planned content to stay compatible with: TACZ, Superb Warfare, Apotheosis, Create, AE2, Ars Nouveau, Modern Industrialization, Building Gadgets, Mining Gadgets, Mekanism, Mob Grinding Utils, plus later magic / tech / utility mods. Item storage is Functional Storage (drawers) + Sophisticated Storage (chests) + Sophisticated Backpacks with Curios (not Storage Drawers, Iron Chests, or Tom’s Simple Storage). Overworld biomes are Terralith + Regions Unexplored + Oh The Biomes We’ve Gone (Terralith gets rarer in that stack). Terrain is Tectonic, not Lithosphere, not Terratonic. Do not stack William Wythers’ Expanded Ecosphere with RU/BWG. Nether is Amplified Nether (height) + BetterNether Forge (biomes), not Incendium. Fortresses are YUNG’s Better Nether Fortresses. Infernal content is Infernal Expansion Redux (no 1.20.1 original). Nether cooking is Farmer’s Delight + My Nether’s Delight (not the 2023 Nether’s Delight jar). Mineshafts are Moog’s Mineshafts Reimagined, not YUNG’s Better Mineshafts. Do not add distant-tick freezers, a second Lithium port, a second claim mod, or a second map UI. FTB Chunks is the claim layer (minimap off; unbind Open Map); Xaero is the map UI. EMI is the recipe viewer (not JEI). Create + Oculus uses Colorwheel + Colorwheel Patcher (not Iris/Oculus Flywheel Compat).
