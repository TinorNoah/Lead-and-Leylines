# Contributing

## Install packwiz

Follow current docs: https://packwiz.infra.link/tutorials/creating/getting-started/

Confirm with `packwiz help`. Work inside `pack/` for packwiz commands.

## Add a mod

Prefer the `minecraft-modding` skill (research and approval), then `add-mod` (packwiz install), or by hand:

1. Read Minecraft version and loader from `pack/pack.toml`.
2. Confirm the mod supports that Minecraft version and loader on CurseForge or Modrinth.
3. `packwiz curseforge install <slug-or-url>` or `packwiz modrinth install <slug-or-url>`.
4. `packwiz refresh`.
5. Commit the new `*.pw.toml`, `index.toml` / `pack.toml`, and `docs/mods/` updates. Never commit jars.

## Test on Prism

1. Create a Prism instance whose Minecraft version and loader match `pack/pack.toml`.
2. Download `packwiz-installer-bootstrap.jar` from https://github.com/packwiz/packwiz-installer-bootstrap/releases/download/v0.0.3/packwiz-installer-bootstrap.jar into the instance `.minecraft` folder (same folder as `options.txt`).
3. From `pack/` run `packwiz serve` and leave it running (`http://localhost:8080/pack.toml`).
4. Instance settings → Custom commands → enable Custom Commands. Paste this **exactly** (no extra quotes around `$INST_JAVA`; Prism's INI parser will smash those into `javaw.exe-jar`):

   `$INST_JAVA -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml`

   Pre-launch runs in the instance `.minecraft` folder, where the bootstrap jar lives. If you edit `instance.cfg` by hand, quote the **whole** value:

   `PreLaunchCommand="$INST_JAVA -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml"`

5. Launch. The installer syncs the instance to the current pack. If serve is down, pre-launch fails.

The Prism instance is local only. Do not commit it.

## Release

Policy: [docs/RELEASING.md](docs/RELEASING.md). Keep `CHANGELOG.md` `[Unreleased]` current as you work (player-facing bullets), not an ad hoc `notes.md` at the last minute.

The Pelican test server address is shared with testers out of band (Discord/DM/etc.), never in the repo or GitHub Release text.

1. Set `pack.toml` `version` to `X.Y.Z` (no `v`) and keep the README Pack details table in sync.
2. Promote `[Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` and re-scaffold an empty `[Unreleased]` (see docs/RELEASING.md). Merge to `main` with a clean working tree.
3. From the repo root:

   ```text
   python scripts/release.py vX.Y.Z --channel alpha
   ```

   Default notes are the `## [X.Y.Z]` section in `CHANGELOG.md`. `--changelog FILE` or `--notes "..."` override. `--channel release` is the only channel that uploads CurseForge/Modrinth (default `alpha`). `--dry-run` prints the plan. The script exports zip + mrpack, tags `vX.Y.Z`, and creates the GitHub Release from that changelog.

Secrets (gitignored `.env` at the repo root; never commit):

- `GH_TOKEN` — GitHub token that can create releases and upload assets
- `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID` (the 8-character id from the Modrinth dashboard, not the slug `lead-and-leylines`; token must be able to read unpublished projects)

Missing CurseForge or Modrinth values skip that store with a log line. A missing `GH_TOKEN` fails the run. Copy `.env.example` to `.env`.
