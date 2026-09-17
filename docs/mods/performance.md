# Performance mods — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** empty pack. No performance mods installed.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. Dedicated server must not require it. |
| `server` | Dedicated server (and not needed on a pure client). Rare for this list. |
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. Use this for every “server optimizer” we actually ship, or singleplayer will not get the benefit. |

## Chosen

None.

## Considered / held / dropped

None yet. Do not port 1.20.1 Forge choices without a fresh 1.21.1 NeoForge research pass.
