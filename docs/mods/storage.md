# Storage — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Pipez only. Drawers/chests/backpacks from the 1.20.1 pack are not ported.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Pipez | `pipez-neoforge-1.21.1-1.2.31.jar` | both | Item/fluid/energy pipes. ARR. World data. |
| Pipez Lag Fix | `pipezlagfix-1.21.1-1.1.0.jar` | both | Eco mode when item-pipe destinations are full. ARR. |

## Considered / held / dropped

Sophisticated Storage / Backpacks, Functional Storage, and the rest of the 1.20.1 logistics list: [deferred.md](deferred.md).
