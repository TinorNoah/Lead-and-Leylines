# Worldgen — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Tectonic 3 + Lithostitched, Terralith, Nullscape, Regions Unexplored, Oh The Biomes We've Gone, Feature Recycler, structure mods, Lost Cities, Bye?Pregen! for generation cost.

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Tectonic | `tectonic-3.0.28-neoforge-21.1.jar` | both | Terrain (mountains, underground rivers). World data. |
| Lithostitched | `lithostitched-1.8.0+beta6-neoforge-21.1.jar` | both | Required by Tectonic and Regions Unexplored. Tectonic 3.0.28 does not use `lithostitched:in_structure`. RU does; those placed features are overridden (see below). |
| TerraBlender (NeoForge) | `TerraBlender-neoforge-1.21.1-4.1.0.8.jar` | both | Required by Oh The Biomes We've Gone. Separate CurseForge project from TerraBlender (Forge). |
| GeckoLib | `geckolib-neoforge-1.21.1-4.9.3.jar` | both | Required by Oh The Biomes We've Gone. |
| CorgiLib | `Corgilib-NeoForge-1.21.1-5.0.0.9.jar` | both | Required by Oh The Biomes We've Gone. |
| Oh The Trees You'll Grow | `Oh-The-Trees-Youll-Grow-neoforge-1.21.1-5.3.2.jar` | both | Required by Oh The Biomes We've Gone. |
| Oh The Biomes We've Gone | `Oh-The-Biomes-Weve-Gone-NeoForge-2.6.0.jar` | both | Overworld biomes. World data. WTHIT optional; not added. |
| Regions Unexplored | `regions-unexplored-0.6.2-neoforge-21.1.jar` | both | Overworld biomes. World data. Eight placed features that used `lithostitched:in_structure` are overridden. |
| Global Packs | `globalpacks-neoforge-1.21.1-21.0.6.jar` | both | Loads `pack/global_packs/required_data/lead-leylines-ru-in-structure/` so dedicated and singleplayer both get the RU override. Unpacked folder (`.packwizignore` blocks `*.zip`). ARR. |
| Terralith | `Terralith_1.21.x_v2.6.2.jar` | both | Overworld biome datapack-as-mod. World data. Requires Lithostitched. Stacks with Tectonic, OTBWG, and RU. Built-in terrain slabs off (Countered's Terrain Slabs is the pack's slab layer). |
| Nullscape | `Nullscape_1.21.x_v1.2.14.jar` | both | End overhaul. World data. Stardust companion to Terralith. |
| YACL | `yet_another_config_lib_v3-3.8.2+1.21.1-neoforge.jar` | both | Required by Structurify. |
| Structurify | `structurify-neoforge-2.0.37+mc1.21.1.jar` | both | Structure spacing/control. Better Sparse Structures skipped (same job). |
| When Dungeons Arise | `DungeonsArise-1.21.1-2.1.68-release.jar` | both | Extra overworld dungeons. World data. ARR. |
| When Dungeons Arise - Seven Seas | `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` | both | Ocean structures. World data. ARR. |
| Library Ferret | `libraryferret-neoforge-1.21.1-4.0.0.jar` | both | Required by Awesome Dungeon. No CurseForge NeoForge 1.21.1 file; Modrinth pin. ARR. |
| Awesome Dungeon | `awesomedungeon-neoforge-1.21.1-3.2.0.jar` | both | Extra dungeons. World data. Modrinth pin. ARR. |
| YUNG's API (NeoForge) | `YungsApi-1.21.1-NeoForge-5.1.9.jar` | both | Required by YUNG's structure mods. Separate CF project from Forge 421850. |
| YUNG's Better Caves | `YungsBetterCaves-1.21.1-NeoForge-3.1.6.jar` | both | Cave overhaul. World data. |
| YUNG's Better Nether Fortresses | `YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar` | both | Nether fortress overhaul. World data. |
| YUNG's Bridges | `YungsBridges-1.21.1-NeoForge-5.1.1.jar` | both | River bridges. World data. |
| Moog's Structure Lib | `MoogsStructureLib-neoforge-1.21.1-3.3.1.jar` | both | Required by Moog's Mineshafts. |
| MMR - Moog's Mineshafts Reimagined | `MoogsMineshaftsReimagined-1.21-1.0.3.jar` | both | Mineshaft overhaul. World data. Modrinth pin. |
| Epic Structures: Villages | `epic-structures-villages-2.0.0.jar` | both | Village overhaul. World data. ARR. |
| Epic Structures: Witch Huts | `Epic Witch Huts v1.3.1.jar` | both | Witch hut overhaul. World data. ARR. |
| Epic Structures: Jungle Temples | `Epic Jungle Temples v1.0.2.jar` | both | Jungle temple overhaul. World data. ARR. |
| Amplified Nether | `Amplified_Nether_26.2_v1.2.16.jar` | both | Taller Nether terrain. World data. |
| Infernal Expansion Redux | `infernalexp-neoforge-1.21.1-0.3.15.jar` | both | Nether biomes/content. World data. Requires Lithostitched and GeckoLib. |
| Countered's Terrain Slabs | `terrain_slabs-neoforge-3.1.2.jar` | both | Smooth terrain slabs. World data. Architectury already in. |
| The Lost Cities | `lostcities-1.21-8.4.4.jar` | both | City worlds. World data. |
| Bye?Pregen! | `byepregen-1.21.1-1.1.2.4.jar` | both | Generation MSPT. See [performance.md](performance.md). |
| Chunk Pregenerator | `Chunk-Pregenerator-Neoforge-1.21-4.5.3.jar` | both | Operator pregen, not the same job as ByePregen. |
| Feature Recycler | `Feature-Recycler-neoforge-2.0.0.jar` | both | Breaks Minecraft feature-order cycles so Terralith + Oh The Biomes We've Gone can generate. ARR. Not a second structure-spacing mod. |

Twilight Forest: [content.md](content.md).

The RU override datapack drops `minecraft:block_predicate_filter` steps whose predicate is `lithostitched:in_structure` from: `patch/ash_vents_inferno`, `patch/cave_bioshrooms`, `patch/dropleaf`, `patch/prismarite_cluster`, `patch/redstone_bud`, `patch/redstone_bulb`, `special/lava_fall`, `special/overworld_lava_delta`. That predicate joins a chunk future on a worldgen worker; dedicated servers freeze in `ChunkMap.processUnloads` / “Saving worlds”. Reproduced **without** ByePregen or C2ME (ATM10 Aeronautics dump, Lithostitched beta4; same predicate in beta6). Those eight features can now place inside structures.

Terralith 2.6.2 + Oh The Biomes We've Gone 2.6.0 hit `IllegalStateException: Feature order cycle found` during Lithostitched biome injectors (`terralith:skylands_spring` with `biomeswevegone:coconino_meadow` / `sakura_grove` and vanilla plains/savanna). Feature Recycler 2.0.0 reorders placed features so that cycle does not crash chunk gen. Do not drop Terralith to “fix” it.

## Considered / held / dropped

| Mod | Status | Why |
|---|---|---|
| WTHIT | Dropped | Overlaps Jade. Optional OTBWG tooltip dep; not added. |
| Better Sparse Structures | Dropped | Same structure-spacing job as Structurify. Do not stack. |
| Sparse Structures | Dropped | Different project from Better Sparse Structures; also overlaps Structurify. |
| Alex's Caves + Citadel | Held | No 1.21.1 NeoForge file for Alex's Caves. Do not add Citadel without a consumer. |
| Stalwart Dungeons | Held | No 1.21.1 NeoForge file. |
| Bygone Nether | Held | No 1.21.1 NeoForge file. |
| BetterNether | Held | No 1.21.1 NeoForge file. |
| Awesome Dungeon Nether | Held | No 1.21.1 NeoForge file (later MC only). |
| YUNG's Better Dungeons | Held | Not in the 1.20.1 pack. |
| WWOO | Held | Chart companion for Tectonic + ByePregen; not in the 1.20.1 pack. |
| Noisium | Dropped | Incompatible with ByePregen. |
| LC²H | Held | 1.20.1 Forge only; 1.21.1 NeoForge port is later. |
| FastNoise | Held | Compatible with ByePregen unless RTF is also in. Not required. |
| Chunky | Dropped for now | Pack uses Chunk Pregenerator. Chunky was in the freeze report only as the pregen driver, not the root cause. |
