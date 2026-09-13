# Lead and Leylines

A Minecraft Forge modpack for a long campaign: late-game progression, exploration, and a world that still has somewhere to go.

This repository is the source of truth. The pack is [packwiz](https://packwiz.infra.link/) TOML under `pack/`. Jars, launcher instances, and tokens are never committed.

## Pack details

Copied from [`pack/pack.toml`](pack/pack.toml). Change that file when bumping; do not leave this table behind.

| | |
|---|---|
| Pack | Lead and Leylines |
| Author | TinorNoah |
| Pack version | 0.0.1 |
| Minecraft | 1.20.1 |
| Mod loader | Forge 47.4.23 |
| Java | 17 |
| Packwiz format | packwiz:1.1.0 |
| Mods | Performance/shader first cut (see [docs/mods/manifest.md](docs/mods/manifest.md)) |

A git tag `vX.Y.Z` must match pack version `X.Y.Z` (currently `v0.0.1`).

## Play

The pack is in early development. The current cut is performance mods plus Oculus (shader loader). Shader packs come later. CurseForge and Modrinth listings are not public yet.

**Testers (ATLauncher):** have someone run `python scripts/deploy_server.py --share-only` and send you `dist/Lead-and-Leylines-<pack version>.mrpack` (or the `.zip`). Instances → **Import** → **Browse** → that file → **Install**. Join the panel address printed by `python scripts/deploy_server.py --status`. Send the file; ATLauncher URL import often rejects GitHub links.

Prism developers: [CONTRIBUTING.md](CONTRIBUTING.md). After store listings exist, install from [Modrinth](https://modrinth.com/modpack/lead-and-leylines), CurseForge, or the [GitHub Release](https://github.com/TinorNoah/Lead-and-Leylines/releases) zip / `.mrpack`.

Prism and other launchers must use Minecraft **1.20.1** and Forge **47.4.23**.

## License

Pack files in this repo (TOML, configs, docs, CI) are [MIT](LICENSE). The Minecraft mods the pack downloads stay under each author’s own license.


## Repository layout

| Path | Role |
|---|---|
| `pack/` | Packwiz root. This tree is what gets exported. |
| `server/` | server overlay overlay. Never indexed or exported. |
| `scripts/` | Local panel deploy and ATLauncher zip/mrpack export. |
| `.github/workflows/release.yml` | Tag pipeline: export, GitHub Release, optional store upload. |
| `.agents/skills/` | Shared agent skills (`minecraft-modding`, `add-mod`, `test-server`, `publish-release`). |
| `docs/mods/` | Manifest, decision logs, and config notes (not exported). |

One pack, not two roots. Client vs server files use packwiz `side` (`client` / `server` / `both`).

## Develop

See [CONTRIBUTING.md](CONTRIBUTING.md) for packwiz, adding mods, the Prism + `packwiz serve` loop, and tagging a release.

Installed mods: [docs/mods/manifest.md](docs/mods/manifest.md). Performance decisions: [docs/mods/performance.md](docs/mods/performance.md). Config notes: [docs/mods/configs.md](docs/mods/configs.md).

Agent conventions: [AGENTS.md](AGENTS.md). test server: [server/README.md](server/README.md).

Short version:

1. Work in a feature branch. Run packwiz from `pack/`.
2. After any manual file change, `packwiz refresh`. Commit TOML, never jars.
3. Test locally: Prism instance matching `pack.toml`, `packwiz serve`, installer bootstrap as in CONTRIBUTING.md.
4. Test on the dedicated server / share with ATLauncher: `python scripts/deploy_server.py` (see [server/README.md](server/README.md)).
5. Merge to `main`. Set `pack.toml` `version` to `X.Y.Z`, then tag `vX.Y.Z`. GitHub Actions exports the pack and creates the Release.
