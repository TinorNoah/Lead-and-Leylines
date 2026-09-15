# Nether, dungeons, cooking, mineshafts — considered, chosen, dropped

Research snapshot: 2026-09-16. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** this cut **installed** (2026-09-16). Incendium is out. Amplified Nether is terrain height; BetterNether is biomes/plants. Mineshafts are Moog’s Mineshafts Reimagined, not YUNG’s Better Mineshafts. packwiz `side` is `both` for all of these.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

Structure mods that Modrinth tags as server-only still use `both` here so Prism matches the dedicated server.

## Decision rules

1. One Nether *height* datapack. Amplified Nether, not Incendium. Stardust lists those two as incompatible.
2. BetterNether (unofficial Forge port) is the biome/plant layer. Amplified Nether’s page says it is often compatible with BetterNether.
3. One fortress rewrite. YUNG’s Better Nether Fortresses. They replace Bygone Nether’s enhanced vanilla fortress; Bygone citadels/manors still generate.
4. Infernal Expansion has no 1.20.1 file. Infernal Expansion Redux is the official 1.20.1 pointer (in-development rebuild, not a 1:1 port).
5. One Farmer’s Delight nether addon. My Nether’s Delight (maintained), not the 2023 Nether’s Delight jar, and not both.
6. One mineshaft rewrite family. MMR adds shafts beside vanilla. Do not also add YUNG’s Better Mineshafts.
7. Awesome Dungeon End/Ocean stay out of this cut. Overworld + Nether editions ship with Library Ferret.

---

## Chosen

| Mod | Project | `side` | Why add |
|---|---|---|---|
| Amplified Nether | [modrinth.com/mod/amplified-nether](https://modrinth.com/mod/amplified-nether) `1.2.15` (`ctnhVAao`) | both | Nether height 256, vanilla biomes only |
| BetterNether Forge | [modrinth.com/mod/betternether-forge](https://modrinth.com/mod/betternether-forge) `20.0.12` (`BEw6Aggq`) | both | Nether biomes, plants, structures. Unofficial Forge port |
| WunderLib Forge | [modrinth.com/mod/wunderlib-forge](https://modrinth.com/mod/wunderlib-forge) `20.0.1` (`FFIJ4Ioj`) | both | Required by BetterNether / BCLib |
| BCLib Forge | [modrinth.com/mod/bclib-forge](https://modrinth.com/mod/bclib-forge) `20.0.13` (`TIteCm8O`) | both | Required by BetterNether |
| YUNG’s Better Nether Fortresses | [modrinth.com/mod/yungs-better-nether-fortresses](https://modrinth.com/mod/yungs-better-nether-fortresses) `1.20-Forge-2.0.6` (`2nUEz0zq`) | both | Fortress rewrite. Create pieces optional if Create is present |
| YUNG’s API | [modrinth.com/mod/yungs-api](https://modrinth.com/mod/yungs-api) `1.20-Forge-4.0.6` (`PJOYAmAs`) | both | Required by YUNG fortresses |
| Infernal Expansion Redux | [modrinth.com/mod/infernal-expansion-redux](https://modrinth.com/mod/infernal-expansion-redux) `0.3.8` (`cMVA7QBk`) | both | 1.20.1 Infernal content. 0.x rebuild |
| GeckoLib | [modrinth.com/mod/geckolib](https://modrinth.com/mod/geckolib) `4.8.4` (`aC5KMoNg`) | both | Required by Infernal Expansion Redux |
| Cloth Config API | [modrinth.com/mod/cloth-config](https://modrinth.com/mod/cloth-config) `11.1.136+forge` (`t8TXrZvZ`) | both | Optional GUI for Infernal Redux and Dynamic FPS |
| Stalwart Dungeons | [modrinth.com/mod/stalwart-dungeons](https://modrinth.com/mod/stalwart-dungeons) `1.2.8` (`vgD645b7`) | both | Unique overworld / Nether / End dungeons |
| Bygone Nether | [modrinth.com/mod/bygone-nether](https://modrinth.com/mod/bygone-nether) `1.3.2-1.20.x` (`RA38ax2z`) | both | Piglin manors, citadels, Wither |
| Farmer’s Delight | [modrinth.com/mod/farmers-delight](https://modrinth.com/mod/farmers-delight) `1.20.1-1.3.4` (`SiIpcZzM`) | both | Cooking / farming pillar |
| My Nether’s Delight | [modrinth.com/mod/my-nethers-delight](https://modrinth.com/mod/my-nethers-delight) `1.10.4-backport.1` (`pOBasFQT`) | both | Nether cooking on Farmer’s Delight 1.3.x |
| Awesome Dungeon | [modrinth.com/mod/awesome-dungeon](https://modrinth.com/mod/awesome-dungeon) `3.2.0` (`GRFhAaFE`) | both | Extra overworld dungeons |
| Awesome Dungeon Nether | [modrinth.com/mod/awesome-dungeon-nether](https://modrinth.com/mod/awesome-dungeon-nether) `3.1.1` (`x2mdkok9`) | both | Extra Nether dungeons |
| Library Ferret | [modrinth.com/mod/library-ferret](https://modrinth.com/mod/library-ferret) `4.0.0` (`wl68oCTb`) | both | Required by Awesome Dungeon |
| MMR - Moog’s Mineshafts Reimagined | [modrinth.com/mod/mmr-moogs-mineshafts-reimagined](https://modrinth.com/mod/mmr-moogs-mineshafts-reimagined) `1.0.2` (`fjkyFY5g`) | both | Extra mineshafts beside vanilla |
| Moog’s Structure Lib | [modrinth.com/mod/moogs-structure-lib](https://modrinth.com/mod/moogs-structure-lib) `3.3.1` (`Xe7AFvDZ`) | both | Required by MMR |

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| Incendium | **Skipped.** Incompatible with Amplified Nether. |
| Infernal Expansion (original) | **Skipped.** No 1.20.1 file. Redux is the official pointer. |
| Nether’s Delight (`nethers-delight` 4.0, 2023) | **Skipped.** Unmaintained. My Nether’s Delight is the 1.20.1 addon. Do not ship both. |
| YUNG’s Better Mineshafts | **Skipped.** MMR is the mineshaft line. |
| Awesome Dungeon End / Ocean | **Held.** Overworld + Nether only this cut. |
| LambDynamicLights (optional on Infernal Redux) | **Skipped.** Oculus is the light path. No extra dynamic-lights mod. |

## Held

| Mod | Why not now | What would change that |
|---|---|---|
| Create: Farmer’s Delight | Create is in; this addon was not in this approval | After a cooking-Create research pass |
| Awesome Dungeon End / Ocean | Structure density | If overworld + Nether dungeons feel sparse |

## Incompatibility (this set)

Do not add Incendium next to Amplified Nether. Do not add YUNG’s Better Mineshafts next to MMR. Do not add original Nether’s Delight next to My Nether’s Delight.

YUNG fortresses replace Bygone’s enhanced vanilla fortress (author-intended). Infernal Redux + BetterNether + Bygone + Amplified stacks Nether biomes next to Terralith / RU / BWG. New world only.

Stalwart + Awesome Dungeon is two extra dungeon families (different designs, more density), not a hard crash.

## Configs worth documenting

| Mod | Why a pack note |
|---|---|
| Amplified Nether / BetterNether / Bygone / Infernal Redux / YUNG fortresses / MMR / dungeons | Worldgen. Existing Nether/overworld chunks stay old. New world. |
| Infernal Expansion Redux | 0.x rebuild. Optional LambDynamicLights stays out. Cloth Config is shipped for its GUI. |
| Farmer’s Delight / My Nether’s Delight | Blocks and crops stay in the save if removed. Pin MND `1.10.4-backport.1` on Farmer’s Delight 1.3.x (older MND `1.8` crashed on 1.3). |
