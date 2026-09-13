# Lead and Leylines

A Minecraft Forge modpack for a long campaign: late-game progression, exploration, and a world that still has somewhere to go.

This repository is the source of truth. The pack is [packwiz](https://packwiz.infra.link/) TOML under `pack/`. Jars, launcher instances, and tokens are never committed.

## Pack details

Copied from [`pack/pack.toml`](pack/pack.toml). Change that file when bumping; do not leave this table behind.

| | |
|---|---|
| Pack | Lead and Leylines |
| Author | TinorNoah |
| Pack version | 0.0.2 |
| Minecraft | 1.20.1 |
| Mod loader | Forge 47.4.23 |
| Java | 17 |
| Packwiz format | packwiz:1.1.0 |
| Mods | Performance/shader first cut plus QoL, FTB, Xaero, and Create (see [docs/mods/manifest.md](docs/mods/manifest.md)) |

A git tag `vX.Y.Z` must match pack version `X.Y.Z` (currently `v0.0.2`).

## Play

The pack is in early development. The current cut is performance mods, Oculus (shader loader), FTB/EMI/Jade/Xaero QoL, and Create. Shader packs come later. CurseForge and Modrinth listings are not public yet.

**Testers (ATLauncher):** download the `.mrpack` (or `.zip`) from the [GitHub Release](https://github.com/TinorNoah/Lead-and-Leylines/releases). Instances → **Import** → **Browse** → that file → **Install**. After store listings exist, install from [Modrinth](https://modrinth.com/modpack/lead-and-leylines) or CurseForge instead.

Prism developers: [CONTRIBUTING.md](CONTRIBUTING.md).

Prism and other launchers must use Minecraft **1.20.1** and Forge **47.4.23**.

## License

Pack files in this repo (TOML, configs, docs) are [MIT](LICENSE). The Minecraft mods the pack downloads stay under each author’s own license.


## Repository layout

| Path | Role |
|---|---|
| `pack/` | Packwiz root. This tree is what gets exported. |
| `server/` | Dedicated-server overlay. Never indexed or exported. |
| `scripts/` | Pack export and `release.py` (tag, GitHub Release, CurseForge, Modrinth). |
| `.agents/skills/` | Shared agent skills (`minecraft-modding`, `add-mod`, `test-server`, `publish-release`). |
| `docs/mods/` | Manifest, decision logs, and config notes (not exported). |

One pack, not two roots. Client vs server files use packwiz `side` (`client` / `server` / `both`).

## Develop

See [CONTRIBUTING.md](CONTRIBUTING.md) for packwiz, adding mods, the Prism + `packwiz serve` loop, and publishing a release.

Installed mods: [docs/mods/manifest.md](docs/mods/manifest.md). Performance decisions: [docs/mods/performance.md](docs/mods/performance.md). QoL / FTB / Create: [docs/mods/utility.md](docs/mods/utility.md). Config notes: [docs/mods/configs.md](docs/mods/configs.md).

Agent conventions: [AGENTS.md](AGENTS.md).

Short version:

1. Work in a feature branch. Run packwiz from `pack/`.
2. After any manual file change, `packwiz refresh`. Commit TOML, never jars.
3. Test locally: Prism instance matching `pack.toml`, `packwiz serve`, installer bootstrap as in CONTRIBUTING.md.
4. Merge to `main`. Set `pack.toml` `version` to `X.Y.Z`, then `python scripts/release.py vX.Y.Z --changelog notes.md`.
