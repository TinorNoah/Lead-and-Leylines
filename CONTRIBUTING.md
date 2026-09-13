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

1. Set `pack.toml` `version` to `X.Y.Z` (no `v`) and keep the README Pack details table in sync.
2. Merge to `main` with a clean working tree.
3. Write markdown notes for this version (GitHub Release body, CurseForge changelog, and Modrinth changelog). Do not put private server or hosting details in those notes.
4. From the repo root:

   ```text
   python scripts/release.py vX.Y.Z --changelog notes.md
   ```

   `--notes "..."` works instead of a file. `--channel alpha|beta|release` (default `alpha`). `--dry-run` prints the plan. The script exports zip + mrpack, tags `vX.Y.Z`, creates the GitHub Release from that changelog, and uploads CurseForge/Modrinth when those values are set.

Secrets (gitignored `.env` at the repo root; never commit):

- `GH_TOKEN` — GitHub token that can create releases and upload assets
- `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID` (the 8-character id from the Modrinth dashboard, not the slug `lead-and-leylines`; token must be able to read unpublished projects)

Missing CurseForge or Modrinth values skip that store with a log line. A missing `GH_TOKEN` fails the run. Copy `.env.example` to `.env`.
