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
3. From the repo root:

   ```text
   python scripts/release.py
   ```

   That tags `vX.Y.Z`, pushes `main` and the tag, waits for the GitHub Release workflow, then deploys the panel (`--from-local` until CurseForge is public). `--dry-run`, `--no-panel`, and `--no-wait` are available. Do not upload zip/mrpack from your machine; CI does that.

4. GitHub Actions exports zip + mrpack and creates a GitHub Release. CurseForge/Modrinth upload if those secrets are set.

Secrets (repo Settings → Secrets; never commit):

- `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID`
- `MODRINTH_TOKEN`, `MODRINTH_PROJECT_ID`

## test server

See `server/README.md` for egg variables and overlay files. Copy `.env.example` to `.env` and set `PANEL_API_KEY`. Never commit `.env`.

Until CurseForge is public, the default command pushes the current `pack/` tree:

```text
python scripts/deploy_server.py
```

That installs the **Forge Minecraft** egg from `pack.toml`, uploads `side` `server`/`both` jars, and writes ATLauncher files under `dist/` (gitignored). Re-running replaces `mods/` only. `--reinstall` (or a Minecraft/Forge bump) wipes the world. `--status` prints the join address.

Friends on ATLauncher (no store listing yet):

```text
python scripts/deploy_server.py --share-only
```

Send them `dist/Lead-and-Leylines-<pack version>.mrpack` (or the `.zip`). They: **Instances → Import → Browse** → that file → **Import** → name it → **Install**. Send the file; URL import often fails for GitHub links.

After a CurseForge file exists, set `CURSEFORGE_PROJECT_ID` and run `python scripts/deploy_server.py --curseforge --reinstall`. Overlay files under `server/` must be re-copied after a full egg reinstall.
