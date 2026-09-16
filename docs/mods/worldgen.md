# Overworld biomes, terrain, structures — considered, chosen, dropped

Research snapshot: 2026-09-16. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** this cut **installed** (2026-09-16) with the later Nether/mineshaft calls applied (Amplified Nether + BetterNether, not Incendium; MMR, not YUNG mineshafts). packwiz `side` is `both` for all of these.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. |

## Decision rules

1. One Overworld *height/noise* mod. Tectonic, not Lithosphere, not both.
2. Terratonic only if Terralith and Tectonic are datapacks. This pack uses the Forge **mod** jars; Tectonic already blends with Terralith.
3. Do not stack William Wythers’ Expanded Ecosphere with Regions Unexplored / Oh The Biomes We’ve Gone (Feature Order Cycle).
4. Terralith + RU + BWG is three surface biome injectors. Terralith would become postage stamps at TerraBlender defaults. Pack ships `overworld_region_size` 6 and Tectonic climate scale 0.125.
5. One mineshaft line: MMR (already in). Do not add YUNG’s Better Mineshafts.
6. YUNG Better Caves is Overworld-only (`#minecraft:is_overworld`). Leave the Nether to Amplified Nether + BetterNether.

---

## Chosen

| Mod | Project | `side` | Why add |
|---|---|---|---|
| Aquamirae | [modrinth.com/mod/aquamirae](https://modrinth.com/mod/aquamirae) `7.1.13` (`72GwOBcB`) | both | Ice/ocean dungeon + sea mobs |
| Fragmentum | [modrinth.com/mod/fragmentum](https://modrinth.com/mod/fragmentum) `1.5.2` (`1nysmgB4`) | both | Required by Aquamirae |
| Regions Unexplored | [modrinth.com/mod/regions-unexplored](https://modrinth.com/mod/regions-unexplored) `F-0.5.6+1.20.1` (`XTrgsfIB`) | both | Extra Overworld/Nether biomes |
| Oh The Biomes We've Gone | [modrinth.com/mod/oh-the-biomes-weve-gone](https://modrinth.com/mod/oh-the-biomes-weve-gone) `1.8.0-Forge` (`8L5cwpjz`) | both | BYG sequel |
| CorgiLib | [modrinth.com/mod/corgilib](https://modrinth.com/mod/corgilib) `4.0.3.5` (`HXTB2EAy`) | both | Required by BWG |
| Oh The Trees You'll Grow | [modrinth.com/mod/oh-the-trees-youll-grow](https://modrinth.com/mod/oh-the-trees-youll-grow) `1.20.1-1.7.0` (`AAp1NdQX`) | both | Required by BWG |
| TerraBlender | [modrinth.com/mod/terrablender](https://modrinth.com/mod/terrablender) `3.0.1.10` (`zGconCHG`) | both | Shared by RU and BWG. Pack `overworld_region_size` 6 |
| Alex's Caves | [modrinth.com/mod/alexs-caves](https://modrinth.com/mod/alexs-caves) `2.0.2` (`lC8HHXOF`) | both | Six rare cave biomes |
| Citadel | [modrinth.com/mod/citadel](https://modrinth.com/mod/citadel) `2.6.3` (`lTAAe4sZ`) | both | Required by Alex's Caves |
| Terralith | [modrinth.com/mod/terralith](https://modrinth.com/mod/terralith) `2.5.4` (`WeYhEb5d`) | both | Extra Overworld biomes |
| Tectonic | [modrinth.com/mod/tectonic](https://modrinth.com/mod/tectonic) `3.0.17` (`KLmvRxwh`) | both | Big terrain. Continent + climate scales and Vertical Scale `0.80` in [configs.md](configs.md) |
| Lithostitched | [modrinth.com/mod/lithostitched](https://modrinth.com/mod/lithostitched) `1.4.11-forge-1.20` (`srPoHKt8`) | both | Required by Tectonic 3.0.17. Modrinth does not list the dep; the jar still requires it. |
| YUNG's Bridges | [modrinth.com/mod/yungs-bridges](https://modrinth.com/mod/yungs-bridges) `1.20-Forge-4.0.3` (`KgO1gfM2`) | both | River bridges. Rate is baked into the jar (`rarity_filter` chance 3) |
| YUNG's Better Caves | [modrinth.com/mod/yungs-better-caves](https://modrinth.com/mod/yungs-better-caves) `1.20.1-Forge-2.0.7` (`BO1vVvun`) | both | Overworld caves only |
| Structurify | [modrinth.com/mod/structurify](https://modrinth.com/mod/structurify) `2.0.37` (`FMlB4OQ1`) | both | Structure Control. Global spacing modifier **off** |
| YetAnotherConfigLib | [modrinth.com/mod/yacl](https://modrinth.com/mod/yacl) `3.6.6+1.20.1-forge` (`sCWgXDYQ`) | both | Required by Structurify |
| Sparse Structures | [modrinth.com/mod/sparsestructures](https://modrinth.com/mod/sparsestructures) `3.0` (`oqEnX6AN`) | both | `idBasedSalt` only. `spreadFactor` 1 (vanilla density) |
| Epic Structures: Villages / Dungeons / Witch Huts / Jungle Temples | Modrinth `hCRa4eFr` / `fMMms6dF` (dungeons **1.0**) / `WAWShTQy` / `aN4PmOt6` | both | Vanilla-structure overhauls. Dungeons stay on 1.0 — later jars use 1.21 item NBT |
| When Dungeons Arise | [modrinth.com/mod/when-dungeons-arise](https://modrinth.com/mod/when-dungeons-arise) `2.1.58` (`6hQpx5Tc`) | both | Extra dungeons |
| When Dungeons Arise: Seven Seas | `DungeonsAriseSevenSeas-1.20.x-1.0.2-forge.jar` (`Ak226ElN`) | both | Ocean dungeons. Not the 1.19.2-named jar |
| Create: Sky Village | [modrinth.com/mod/create-sky-village](https://modrinth.com/mod/create-sky-village) `0.0.38` (`630wzTP1`) | both | Create is already in. Spacing 32 / height offset 64 |
| Streams Reflowing | [modrinth.com/mod/streams-reflowing](https://modrinth.com/mod/streams-reflowing) `2.13.7` (`OZN2NMml`) | both | Real rivers. 2.13.7 is the dedicated spawn/current stall fix (not Ksyxis, not C2ME) |
| Countered's Terrain Slabs | [modrinth.com/mod/countereds-terrain-slabs](https://modrinth.com/mod/countereds-terrain-slabs) `4.0.3-beta` (`fhdOSK5I`) | both | Smooth terrain steps. **Beta** |
| Nature's Compass | [modrinth.com/mod/natures-compass](https://modrinth.com/mod/natures-compass) `1.12.0` (`eRSDvCjN`) | both | Find biomes |
| Explorer's Compass | [modrinth.com/mod/explorers-compass](https://modrinth.com/mod/explorers-compass) `1.4.0` (`7ZdJbCOx`) | both | Find structures |
| Chunky | [modrinth.com/mod/chunky](https://modrinth.com/mod/chunky) `1.3.146` (`4FTDk9wv`) | both | Pregen. Writes chunks |

GeckoLib was already in from Infernal Expansion Redux.

## Dropped / skipped this cut

| Asked as | Outcome |
|---|---|
| Incendium | **Skipped.** Incompatible with Amplified Nether (already in). |
| Expanded Ecosphere | **Skipped.** Feature Order Cycle with RU + BWG. |
| Terratonic | **Skipped.** Datapack-only blend. Forge mods use Tectonic + Terralith jars. |
| Lithosphere | **Skipped.** Same noise job as Tectonic. |
| YUNG’s Better Mineshafts | **Skipped.** MMR is the mineshaft line. |
| Sodium / Enhanced Block Entities | **Skipped.** Embeddium + Oculus is the renderer. |
| Larion / Atmospherics / Wet Sand / Luki’s Ancient Cities / Voxy | **Skipped.** No usable Forge 1.20.1 file. |
| Fast Item Frames | **Skipped.** Requires Forge Config API Port; that project has no Forge 1.20.1 jar (Fabric only). |
| StructureOverlapless | **Removed 2026-09-16.** Skips placement when a chunk section is “occupied,” including by the same structure start. `/locate` and Explorer’s Compass still report that start. Dedicated logs skipped `create_sky_village:skyvillage` and `dungeons_arise:bandit_towers` at the locate coords. Do not re-add unless a relocate-not-skip tool exists. |
| WDA Sparse Structures compat | **Removed 2026-09-16.** Extra thinning on top of Sparse made WDA unfindable. |

## Configs worth documenting

| Mod | Why a pack note |
|---|---|
| All of this cut | New world. Old chunks stay old-gen. |
| Tectonic | `pack/config/tectonic.json`: Continents Scale `0.11`, Ocean Offset `-0.92`, temperature/vegetation scale `0.125` (default `0.25` — smaller scale = larger biomes). Vertical Scale `0.80` (was `1.125`) so surface above sea is ~40 blocks lower on typical highlands. Do not use Elevation Boost for this — that value is a mountain multiplier, not blocks. Do not raise Ocean Offset toward `0`. New chunks; 1.20 restart. |
| TerraBlender | `pack/config/terrablender.toml`: `overworld_region_size` 6 (max), `nether_region_size` 4. |
| Sparse Structures | `pack/config/sparsestructures.json5`: `spreadFactor` 1, `idBasedSalt` true. Do not set 2; that doubles rarity and locates still report starts. |
| Structurify | `pack/config/structurify.json`: global spacing modifier **off**. |
| Create: Sky Village | `pack/config/create_sky_village-common.toml`: spacing 32 / separation 16 (was 80/40), height offset 64 so Tectonic peaks are less likely to eat islands. `/locate` still teleports to ground Y — look up. |
| YUNG’s Bridges | 4.0.3 has `rarity_filter` chance `3` baked into the jar. Tectonic/Terralith make bridges rarer. No pack toml to turn that up without a datapack overlay. |
| YUNG’s Better Caves | Already Overworld-only. |
| Chunky | Pregen writes the world. Use on purpose; do not leave a huge radius running unattended. Pregen around spawn before relying on `/rtp`. |
| Streams Reflowing | Pin `2.13.7`. Pack `pack/config/streamsreflowing-common.toml`: `terrainAccuracyLevel = "LOW"` (default MEDIUM). Tectonic makes MEDIUM spawn-chunk gen stall; LOW is coarser rivers, cheaper watersheds. Network change in **new chunks** after a restart. Do not drop to POTATO unless LOW is still too slow. Do not add Ksyxis/C2ME. Use Chunky if you want HIGH quality without hitching. |
| Terrain Slabs | Beta. |
