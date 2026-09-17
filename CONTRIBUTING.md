# Contributing

## Install packwiz

Follow current docs: https://packwiz.infra.link/tutorials/creating/getting-started/

Confirm with `packwiz help`. Work inside `pack/` for packwiz commands.

## Git

Agent-authored changes still go on a branch with a PR. That review pass is how you see what the agent actually wrote.

Your own direct, trivial edits (a config tweak, a one-line doc fix) can go straight to `main`. A branch and PR are not required for those.

### Optional pre-commit hook

Once per clone:

```text
git config core.hooksPath .githooks
```

That runs `scripts/pre_commit_check.py` on commit: it **blocks** staged `.jar` files, and **warns** (does not block) if `pack/mods/*.pw.toml` is staged without `CHANGELOG.md`. Do not copy hooks into `.git/hooks/` by hand.

## Add a mod

Prefer the `minecraft-modding` skill (research and approval), then `add-mod` (packwiz install), or by hand:

1. Read Minecraft version and loader from `pack/pack.toml`.
2. Confirm the mod supports that Minecraft version and loader on CurseForge or Modrinth.
3. `packwiz curseforge install <slug-or-url>` first. Use `packwiz modrinth install` only if the mod is not on CurseForge. See `docs/mods/distribution.md`.
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

5. JVM args live in `pack/user_jvm_args.txt` (`-XX:+UseZGC` on Java 21). `python scripts/update_prism.py` writes those flags into the instance. If you are not using that script, Instance settings → Java → enable **Custom JVM arguments** and paste the same flags. Do not add `-XX:+ZGenerational`. Memory (`-Xmx`) stays in Prism's Memory tab. Use a Java 21 runtime; do not reuse a 1.20.1 Forge instance.

6. Launch. The installer syncs the instance to the current pack. If serve is down, pre-launch fails.

`python scripts/release.py` also runs `python scripts/update_prism.py` after GitHub (packwiz serve on a free port, then installer `-g`, then pack JVM args). Use `--skip-prism` to opt out. Set `PRISM_INSTANCE_DIR` in `.env` if discovery cannot find the instance. The Prism instance is local only. Do not commit it.

After a mod or config change, `python scripts/smoke_test.py` is the fast local dedicated-server boot check. Use the remote test server only when you need friends to join.

## Release

Policy: [docs/RELEASING.md](docs/RELEASING.md). Keep `CHANGELOG.md` `[Unreleased]` current as you work (player-facing bullets), not an ad hoc `notes.md` at the last minute.

The Pelican test server address is shared with testers out of band (Discord/DM/etc.), never in the repo or GitHub Release text.

1. Set `pack.toml` `version` to `X.Y.Z` (no `v`) and keep the README Pack details table in sync.
2. Promote `[Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` and re-scaffold an empty `[Unreleased]` (see docs/RELEASING.md). Merge to `main` with a clean working tree.
3. From the repo root:

   ```text
   python scripts/release.py vX.Y.Z --channel alpha
   ```

   Default notes are the `## [X.Y.Z]` section in `CHANGELOG.md`. `--changelog FILE` or `--notes "..."` override. Default `--channel alpha` is a GitHub prerelease; after Wings, GitHub Actions uploads CurseForge as alpha (client pack + server-mods zip). `--channel release` is GitHub Latest plus CurseForge release. `--dry-run` prints the plan. The script exports zip + mrpack, tags `vX.Y.Z`, creates the GitHub Release, updates the live instance, publishes CurseForge, then syncs local Prism.

Secrets (gitignored `.env` at the repo root; never commit):

- `GH_TOKEN` — GitHub token that can create releases and upload assets
- Optional local `CURSEFORGE_TOKEN`, `CURSEFORGE_PROJECT_ID` (only with `--upload-stores`)

CurseForge tokens and project ids for the default path live as GitHub Actions secrets. A missing `GH_TOKEN` fails the GitHub Release. Copy `.env.example` to `.env`.
