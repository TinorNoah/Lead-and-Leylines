# Utility / QoL — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Jade + EMI recipe/tooltip stack.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. |
| `both` | Must run in singleplayer and on the dedicated server. |

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Jade | `Jade-1.21.1-NeoForge-15.10.6.jar` | both | Block/entity tooltip. WTHIT not added. |
| Jade Addons (Neo/Forge) | `JadeAddons-1.21.1-NeoForge-6.1.1.jar` | both | Extra Jade integrations (Create, etc.). ARR. |
| EMI | `emi-1.1.24+1.21.1+neoforge.jar` | client | Recipe viewer. JEI not added. |
| EMI QoL Tweaks | `emi-qol-tweaks-neoforge-1.2.jar` | client | EMI convenience. |
| JEI / REI / EMI WorldGen | `jeiworldgen-neoforge-1.21.1-1.4.5.jar` | client | Worldgen recipe pages. Optional JEI/REI; EMI is enough. |

## Considered / held / dropped

| Mod | Status | Why |
|---|---|---|
| EMI Enchants | Held | Last file is 1.20.4. No 1.21.1 NeoForge build. |
| TooManyRecipeViewers | Dropped | Not in the 1.20.1 pack tree. Incompatible with JEI; EMI already covers recipes. |
| JEI | Dropped | Pack uses EMI. JEI WorldGen works as an EMI addon without JEI. |
| WTHIT | Dropped | Overlaps Jade. |
