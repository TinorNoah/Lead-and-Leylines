# Lead and Leylines

A Minecraft NeoForge modpack for a long campaign: late-game progression, exploration, and a world that still has somewhere to go.

This repository is the source of truth. The pack is [packwiz](https://packwiz.infra.link/) TOML under `pack/`. Jars, launcher instances, and tokens are never committed.

## Pack details

Copied from [`pack/pack.toml`](pack/pack.toml). Change that file when bumping; do not leave this table behind.

| | |
|---|---|
| Pack | Lead and Leylines |
| Author | TinorNoah |
| Pack version | 0.0.1 |
| Minecraft | 1.21.1 |
| Mod loader | NeoForge 21.1.250 |
| Java | 21 (`pack/user_jvm_args.txt`: `-XX:+UseZGC`) |
| Packwiz format | packwiz:1.1.0 |
| Mods | Performance stack plus Create, FTB Quests, Pipez, biomes, Jade, EMI, and worldgen (see [docs/mods/manifest.md](docs/mods/manifest.md)) |

A git tag `vX.Y.Z` must match pack version `X.Y.Z`. Tags `v0.0.1`–`v0.0.9` already shipped as 1.20.1 Forge; do not reuse them. The first 1.21.1 NeoForge GitHub/store ship is `v0.1.0`.

## Play

The pack is in early development on Minecraft 1.21.1 NeoForge. This cut has the performance stack plus Create, FTB Quests, Pipez, biomes, Jade, EMI, and the ported worldgen set. New world required. The CurseForge listing is not public yet.

**Testers (ATLauncher):** download the `.mrpack` (or `.zip`) from the [GitHub Release](https://github.com/TinorNoah/Lead-and-Leylines/releases). Instances → **Import** → **Browse** → that file → **Install**. Then set that instance's Java arguments to `-XX:+UseZGC` (same flags as `user_jvm_args.txt` in the instance folder) and use **Java 21**. After the store listing exists, install from CurseForge instead.

Prism developers: [CONTRIBUTING.md](CONTRIBUTING.md).

Prism and other launchers must use the Minecraft version and NeoForge version in [`pack/pack.toml`](pack/pack.toml), on Java 21. Do not reuse a 1.20.1 Forge instance.

## License

Pack files in this repo (TOML, configs, docs) are [MIT](LICENSE). The Minecraft mods the pack downloads stay under each author’s own license.


## Repository layout

| Path | Role |
|---|---|
| `pack/` | Packwiz root. This tree is what gets exported. |
| `server/` | Dedicated-server overlay. Never indexed or exported. |
| `scripts/` | Pack export, `release.py`, `deploy_server.py`, and `update_prism.py`. |
| `.agents/skills/` | Shared agent skills (`minecraft-modding`, `add-mod`, `local-smoke-test`, `test-server`, `publish-release`). |
| `docs/mods/` | Manifest, decision logs, and config notes (not exported). |

One pack, not two roots. Client vs server files use packwiz `side` (`client` / `server` / `both`).

## Develop

See [CONTRIBUTING.md](CONTRIBUTING.md) for packwiz, adding mods, the Prism + `packwiz serve` loop, and publishing a release.

Installed mods: [docs/mods/manifest.md](docs/mods/manifest.md). Performance decisions: [docs/mods/performance.md](docs/mods/performance.md). QoL: [docs/mods/utility.md](docs/mods/utility.md). Config notes: [docs/mods/configs.md](docs/mods/configs.md).

Agent conventions: [AGENTS.md](AGENTS.md).

Short version:

1. Work in a feature branch. Run packwiz from `pack/`.
2. After any manual file change, `packwiz refresh`. Commit TOML, never jars.
3. Test locally: Prism instance matching `pack.toml` (Java 21), `packwiz serve`, installer bootstrap as in CONTRIBUTING.md.
4. Merge to `main`. Set `pack.toml` `version` to `X.Y.Z`, then `python scripts/release.py vX.Y.Z --changelog notes.md`.
