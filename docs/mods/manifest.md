# Lead and Leylines — mod manifest

Synced with `pack/mods/*.pw.toml` on 2026-09-18. Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml). Decision logs: [performance.md](performance.md), [utility.md](utility.md), [storage.md](storage.md), [nether.md](nether.md), [worldgen.md](worldgen.md), [content.md](content.md). Config notes: [configs.md](configs.md). Distribution: [distribution.md](distribution.md). Not-yet-added candidates and remaining Forge mods: [deferred.md](deferred.md).

First 1.21.1 NeoForge wave: performance and client smoothness. Second wave: Extra/culling/Create/FTB Quests/Pipez.

## Installed

| Mod | Pinned file | Source | `side` | Category | Why | Required deps | Config | Date added |
|---|---|---|---|---|---|---|---|---|
| Sodium | `sodium-neoforge-0.8.13+mc1.21.1.jar` | CurseForge 394468 / 8756580 | client | renderer | Official NeoForge Sodium. Replaces Embeddium. | none | defaults | 2026-09-17 |
| Iris Shaders | `iris-neoforge-1.8.14-beta.1+mc1.21.1.jar` | CurseForge 455508 / 8242804 | client | shaders | Official shaders for Sodium 0.8.x. Oculus has no 1.21.1 NeoForge file. | Sodium (client) | defaults | 2026-09-17 |
| Lithium | `lithium-neoforge-0.15.4+mc1.21.1.jar` | CurseForge 360438 / 8330365 | both | optimizer | Official gameplay/tick optimizer. Replaces Radium. | none | defaults | 2026-09-17 |
| FerriteCore | `ferritecore-7.0.3-neoforge.jar` | CurseForge 429235 / 7524151 | both | memory | Memory. | none | defaults | 2026-09-17 |
| ModernFix | `modernfix-neoforge-5.27.24+mc1.21.1.jar` | CurseForge 790626 / 8774737 | both | optimizer | Launch and mixin fixes. | none | defaults | 2026-09-17 |
| ImmediatelyFast | `ImmediatelyFast-NeoForge-1.6.14+1.21.1.jar` | CurseForge 686911 / 8875640 | client | renderer | Immediate-mode rendering. | none | defaults | 2026-09-17 |
| FastWorkbench | `FastWorkbench-1.21.1-9.1.3.jar` | CurseForge 288885 / 6751534 | both | optimizer | Crafting lookup. | Placebo | defaults | 2026-09-17 |
| FastFurnace | `FastFurnace-1.21.1-9.0.1.jar` | CurseForge 299540 / 6751551 | both | optimizer | Furnace tick. | Placebo | defaults | 2026-09-17 |
| FastSuite | `FastSuite-1.21.1-6.0.7.jar` | CurseForge 475117 / 7527945 | both | optimizer | Recipe manager. | Placebo | defaults | 2026-09-17 |
| Placebo | `Placebo-1.21.1-9.9.2.jar` | CurseForge 283644 / 8463693 | both | library | Fast* dependency. | none | defaults | 2026-09-17 |
| Let Me Despawn | `letmedespawn-1.21.x-neoforge-1.5.0.jar` | CurseForge 663477 / 6311236 | both | entities | Pickup-mobs despawn. | Almanac Lib | defaults | 2026-09-17 |
| Almanac Lib | `Almanac-1.21.1-2-neoforge-1.5.2.jar` | CurseForge 1115285 / 7489091 | both | library | Let Me Despawn dependency. | none | defaults | 2026-09-17 |
| Neruina | `neruina-3.3.3+1.21.1-neoforge.jar` | CurseForge 851046 / 8451084 | both | stability | Ticking-entity isolation. | Configurable | defaults | 2026-09-17 |
| Configurable | `configurable-3.5.2+1.21.1-neoforge.jar` | CurseForge 1092048 / 8438541 | both | library | Neruina dependency. | none | defaults | 2026-09-17 |
| Clumps | `Clumps-neoforge-1.21.1-19.0.0.1.jar` | CurseForge 256717 / 5623731 | both | entities | XP orb merge. | none | defaults | 2026-09-17 |
| AllTheLeaks | `alltheleaks-1.1.12+1.21.1-neoforge.jar` | CurseForge 1091339 / 8648639 | both | stability | Leak patches. | none | defaults | 2026-09-17 |
| Smooth Chunk Save | `smoothchunk-1.21-4.1.jar` | CurseForge 582327 / 6296628 | both | IO | Spreads chunk saves. | Cupboard | defaults | 2026-09-17 |
| Cupboard | `cupboard-1.21.1-4.2.jar` | CurseForge 326652 / 8889050 | both | library | Smooth Chunk Save dependency. | none | defaults | 2026-09-17 |
| BadOptimizations | `BadOptimizations-2.4.1-1.21.1.jar` | CurseForge 949555 / 7338300 | client | renderer | Client skip work. | none | defaults | 2026-09-17 |
| Dynamic FPS | `dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar` | CurseForge 335493 / 7546938 | client | client QoL | Lowers FPS when unfocused. | none | defaults | 2026-09-17 |
| Crash Assistant | `CrashAssistant-neoforge-1.20.6-1.21.4-1.11.12.jar` | CurseForge 1154099 / 8636685 | client | stability | Crash dump helper (client-only). | none | defaults | 2026-09-17 |
| Entity Culling | `entityculling-neoforge-1.10.5-mc1.21.1.jar` | CurseForge 448233 / 8287097 | client | renderer | Occlusion culling. | none | defaults | 2026-09-17 |
| Sodium Extra | `sodium-extra-neoforge-0.9.4+mc1.21.1.jar` | CurseForge 447673 / 8892306 | client | renderer | Official Sodium extras (fog, particles, FPS overlay). Not Chloride. | Sodium (client) | See [configs.md](configs.md) if leaves stack with More Culling | 2026-09-18 |
| Flerovium | `flerovium-neoforge-1.21.1-1.1.3-all.jar` | CurseForge 1142875 / 8862415 | client | renderer | Item/entity/particle draw. Not Better Block Entities. | Sodium (client) | defaults | 2026-09-18 |
| AsyncParticles | `AsyncParticles-21.1.4.4+1.21.1.jar` | CurseForge 1215753 / 8887358 | client | renderer | Particle thread. Not Particle Core. | none (Cloth optional) | defaults | 2026-09-18 |
| More Culling | `moreculling-neoforge-1.21.1-1.0.10.jar` | CurseForge 630104 / 8833217 | client | renderer | Extra culling next to Entity Culling. | Cloth Config | See [configs.md](configs.md) | 2026-09-18 |
| Cloth Config | `cloth-config-15.0.140-neoforge.jar` | CurseForge 348521 / 5729127 | both | library | More Culling dependency. | none | defaults | 2026-09-18 |
| Structure Layout Optimizer | `structure_layout_optimizer-neoforge-1.0.12.jar` | CurseForge 1087831 / 7439136 | both | worldgen | Jigsaw/NBT structure gen. | Resourceful Config | defaults | 2026-09-18 |
| Resourceful Config | `resourcefulconfig-neoforge-1.21-3.0.11.jar` | CurseForge 714059 / 6467772 | both | library | SLO dependency. | none | defaults | 2026-09-18 |
| Ksyxis | `Ksyxis-1.4.4.jar` | CurseForge 537533 / 8891330 | both | worldgen | Unloads unused spawn chunks. | none | defaults | 2026-09-18 |
| Disconnect Packet Fix | `disconnect-packet-fix-neoforge-2.0.1.jar` | CurseForge 1173964 / 6064142 | both | stability | MC-271325 disconnect packets. | none | defaults | 2026-09-18 |
| quick pack | `quick-pack-neoforge-1.5.0+1.21.1.jar` | CurseForge 1380888 / 8619206 | both | IO | Faster zip pack parse. | none | defaults | 2026-09-18 |
| CrashExploitFixer | `crashexploitfixer-neoforge-2.0.0+1.21.4.jar` | CurseForge 1079896 / 8071070 | both | stability | Server crash-exploit filter; file tags 1.21.1–1.21.4. | none | defaults | 2026-09-18 |
| Async Logger | `asynclogger-2.2.2+1.21.1-neoforge.jar` | CurseForge 1491426 / 8631010 | client | IO | Async log writes. | none | defaults | 2026-09-18 |
| ResourcePackCached | `rpc-1.2.5+1.20.5-1.21.4-neoforge.jar` | CurseForge 1125284 / 7602181 | client | client QoL | Keeps server resource packs across rejoins. | none | defaults | 2026-09-18 |
| Chunk Pregenerator | `Chunk-Pregenerator-Neoforge-1.21-4.5.3.jar` | CurseForge 267193 / 8312000 | both | worldgen | Operator pregen. | Carbon Config | defaults | 2026-09-18 |
| Carbon Config | `CarbonConfig-Neoforge-1.21.1-2.0.2.1.jar` | CurseForge 898104 / 8119979 | both | library | Chunk Pregenerator dependency. | none | defaults | 2026-09-18 |
| Create | `create-1.21.1-6.0.10.jar` | CurseForge 328085 / 7963363 | both | tech | Contraptions and kinetics. | none (Flywheel embedded) | defaults | 2026-09-18 |
| Iris Flywheel Compat | `iris-flywheel-compat-NeoForge-2.4.0.jar` | CurseForge 659897 / 8047971 | client | renderer | Create/Flywheel instancing with Iris shaders. | Iris, Sodium; Create optional | defaults | 2026-09-18 |
| Create Better FPS | `createbetterfps-1.21.1-1.1.4.jar` | CurseForge 1217518 / 7951368 | client | renderer | Create FPS with shader packs. | Create | defaults | 2026-09-18 |
| Create: Threaded Trains | `createthreadedtrains-neoforge-1.21.1-1.0.0.jar` | CurseForge 1381890 / 7208558 | both | optimizer | Train network off the server thread. | Create | See [configs.md](configs.md) | 2026-09-18 |
| Architectury API | `architectury-13.0.11-neoforge.jar` | CurseForge 419699 / 8492726 | both | library | FTB dependency. | none | defaults | 2026-09-18 |
| FTB Library | `ftb-library-neoforge-2101.1.36.jar` | CurseForge 404465 / 8858846 | both | library | FTB Quests/Teams. | Architectury | defaults | 2026-09-18 |
| FTB Teams | `ftb-teams-neoforge-2101.1.11.jar` | CurseForge 404468 / 8724782 | both | utility | Shared quest progress. | FTB Library, Architectury | defaults | 2026-09-18 |
| FTB Quests | `ftb-quests-neoforge-2101.1.36.jar` | CurseForge 289412 / 8885017 | both | quests | Quest book. | FTB Library, FTB Teams, Architectury | defaults | 2026-09-18 |
| FTB Quests Optimizer | `FTBQuestsOptimizer-neoforge-3.2.0-1.21.1.jar` | CurseForge 912469 / 7576461 | both | optimizer | Quest tick cost. | FTB Quests | See [configs.md](configs.md) | 2026-09-18 |
| Pipez | `pipez-neoforge-1.21.1-1.2.31.jar` | CurseForge 443900 / 8351631 | both | logistics | Item/fluid/energy pipes. | none | defaults | 2026-09-18 |
| Pipez Lag Fix | `pipezlagfix-1.21.1-1.1.0.jar` | CurseForge 1446489 / 8113984 | both | optimizer | Eco mode when item-pipe destinations are full. | Pipez | defaults | 2026-09-18 |
| TxniLib | `txnilib-neoforge-1.0.24-1.21.1.jar` | CurseForge 1104882 / 6533725 | both | library | Cerulean dependency. | none | defaults | 2026-09-18 |
| Cerulean | `cerulean-neoforge-1.0.0-1.21.1.jar` | CurseForge 1204890 / 6489711 | both | optimizer | Advancement checks (Icterine fork). Replaces Achievements Optimizer. | TxniLib | defaults | 2026-09-18 |
| Bye?Pregen! | `byepregen-1.21.1-1.1.2.4.jar` | CurseForge 1567378 / 8858794 | both | worldgen | Chunk-gen MSPT. Incompatible with Noisium (removed). Not operator pregen. | none | defaults | 2026-09-18 |
| The Twilight Forest | `twilightforest-1.21.1-4.8.3345-universal.jar` | CurseForge 227639 / 7797302 | both | dimension | Twilight Forest dimension. World data. | none | defaults | 2026-09-18 |
| The Lost Cities | `lostcities-1.21-8.4.4.jar` | CurseForge 269024 / 8862503 | both | worldgen | City world type / generation. World data. The One Probe optional. | none | defaults | 2026-09-18 |
| Lithostitched | `lithostitched-1.8.0+beta6-neoforge-21.1.jar` | CurseForge 936015 / 8819894 | both | worldgen | Required by Tectonic and Regions Unexplored. RU's `in_structure` features are overridden by the pack datapack. | none | defaults | 2026-09-18 |
| Tectonic | `tectonic-3.0.28-neoforge-21.1.jar` | CurseForge 686836 / 8855043 | both | worldgen | Terrain overhaul. World data. Tectonic 3.0.28 has no `in_structure` predicates. | Lithostitched | defaults | 2026-09-18 |
| TerraBlender (NeoForge) | `TerraBlender-neoforge-1.21.1-4.1.0.8.jar` | CurseForge 940057 / 6054947 | both | worldgen | Biome injection library. Not the Forge project 563928. | none | defaults | 2026-09-18 |
| GeckoLib | `geckolib-neoforge-1.21.1-4.9.3.jar` | CurseForge 388172 / 8893490 | both | library | Required by Oh The Biomes We've Gone, Aquamirae, and Infernal Expansion Redux. | none | defaults | 2026-09-18 |
| CorgiLib | `Corgilib-NeoForge-1.21.1-5.0.0.9.jar` | CurseForge 693313 / 7773534 | both | library | Required by Oh The Biomes We've Gone. | none | defaults | 2026-09-18 |
| Oh The Trees You'll Grow | `Oh-The-Trees-Youll-Grow-neoforge-1.21.1-5.3.2.jar` | CurseForge 962544 / 8096180 | both | worldgen | Required by Oh The Biomes We've Gone. | none | defaults | 2026-09-18 |
| Oh The Biomes We've Gone | `Oh-The-Biomes-Weve-Gone-NeoForge-2.6.0.jar` | CurseForge 1070751 / 8245253 | both | worldgen | Overworld biomes. World data. ARR. WTHIT optional, not added. | TerraBlender, GeckoLib, CorgiLib, Oh The Trees You'll Grow | defaults | 2026-09-18 |
| Regions Unexplored | `regions-unexplored-0.6.2-neoforge-21.1.jar` | CurseForge 659110 / 8419667 | both | worldgen | Overworld biomes. World data. Eight `lithostitched:in_structure` placed features overridden. | Lithostitched | datapack override | 2026-09-18 |
| Global Packs | `globalpacks-neoforge-1.21.1-21.0.6.jar` | CurseForge 317134 / 6634585 | both | utility | Loads the unpacked RU override datapack. ARR. | none | See [configs.md](configs.md) | 2026-09-18 |
| Jade | `Jade-1.21.1-NeoForge-15.10.6.jar` | CurseForge 324717 / 8591319 | both | utility | Block/entity tooltip. | none | defaults | 2026-09-18 |
| Jade Addons (Neo/Forge) | `JadeAddons-1.21.1-NeoForge-6.1.1.jar` | CurseForge 583345 / 8777229 | both | utility | Extra Jade integrations. ARR. | Jade | defaults | 2026-09-18 |
| EMI | `emi-1.1.24+1.21.1+neoforge.jar` | CurseForge 580555 / 8081408 | client | recipes | Recipe viewer. JEI not added. | none | defaults | 2026-09-18 |
| EMI QoL Tweaks | `emi-qol-tweaks-neoforge-1.2.jar` | CurseForge 1623482 / 8617689 | client | recipes | EMI convenience. | EMI | defaults | 2026-09-18 |
| JEI / REI / EMI WorldGen | `jeiworldgen-neoforge-1.21.1-1.4.5.jar` | CurseForge 1509527 / 8897773 | client | recipes | Worldgen pages in EMI. JEI optional, not installed. | EMI | defaults | 2026-09-18 |
| GeckolibBetterFPS | `gbf-1.21.1-1.0.2.jar` | CurseForge 1455983 / 8582640 | client | optimizer | Faster GeckoLib entity rendering. Alpha. | GeckoLib | defaults | 2026-09-18 |
| Terralith | `Terralith_1.21.x_v2.6.2.jar` | CurseForge 513688 / 8222737 | both | worldgen | Overworld biomes. World data. | Lithostitched | `pack/config/terralith.json` terrain slabs off | 2026-09-18 |
| Feature Recycler | `Feature-Recycler-neoforge-2.0.0.jar` | CurseForge 1077985 / 5829420 | both | worldgen | Reorders biome features so Terralith + OTBWG do not crash. ARR. | none | defaults | 2026-09-18 |
| Nullscape | `Nullscape_1.21.x_v1.2.14.jar` | CurseForge 570354 / 7078265 | both | worldgen | End overhaul. World data. | none | defaults | 2026-09-18 |
| YACL | `yet_another_config_lib_v3-3.8.2+1.21.1-neoforge.jar` | CurseForge 667299 / 7437845 | both | library | Required by Structurify. | none | defaults | 2026-09-18 |
| Structurify | `structurify-neoforge-2.0.37+mc1.21.1.jar` | CurseForge 1087551 / 8888619 | both | worldgen | Structure spacing. | YACL | defaults | 2026-09-18 |
| When Dungeons Arise | `DungeonsArise-1.21.1-2.1.68-release.jar` | CurseForge 442508 / 7150870 | both | worldgen | Extra dungeons. World data. ARR. | none | defaults | 2026-09-18 |
| When Dungeons Arise - Seven Seas | `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` | CurseForge 953637 / 7142896 | both | worldgen | Ocean structures. World data. ARR. | none | defaults | 2026-09-18 |
| Library Ferret | `libraryferret-neoforge-1.21.1-4.0.0.jar` | Modrinth DOB2l4oJ / AKcIMUil | both | library | Required by Awesome Dungeon. No CF NeoForge 1.21.1 file. ARR. | none | defaults | 2026-09-18 |
| Awesome Dungeon | `awesomedungeon-neoforge-1.21.1-3.2.0.jar` | Modrinth ptzsjBKT / 5vFWzKiI | both | worldgen | Extra dungeons. World data. ARR. | Library Ferret | defaults | 2026-09-18 |
| YUNG's API (NeoForge) | `YungsApi-1.21.1-NeoForge-5.1.9.jar` | CurseForge 1015100 / 8894736 | both | library | Required by YUNG's structure mods. | none | defaults | 2026-09-18 |
| YUNG's Better Caves | `YungsBetterCaves-1.21.1-NeoForge-3.1.6.jar` | CurseForge 340583 / 8806071 | both | worldgen | Cave overhaul. World data. | YUNG's API | defaults | 2026-09-18 |
| YUNG's Better Nether Fortresses | `YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar` | CurseForge 1015118 / 6606621 | both | worldgen | Fortress overhaul. World data. | YUNG's API | defaults | 2026-09-18 |
| YUNG's Bridges | `YungsBridges-1.21.1-NeoForge-5.1.1.jar` | CurseForge 1015149 / 5812553 | both | worldgen | River bridges. World data. | YUNG's API | defaults | 2026-09-18 |
| Moog's Structure Lib | `MoogsStructureLib-neoforge-1.21.1-3.3.1.jar` | CurseForge 1337167 / 8885814 | both | library | Required by Moog's Mineshafts. | none | defaults | 2026-09-18 |
| MMR - Moog's Mineshafts Reimagined | `MoogsMineshaftsReimagined-1.21-1.0.3.jar` | Modrinth z25hqseO / gQlqjs2o | both | worldgen | Mineshaft overhaul. World data. | Moog's Structure Lib | defaults | 2026-09-18 |
| Epic Structures: Villages | `epic-structures-villages-2.0.0.jar` | CurseForge 1308486 / 8830175 | both | worldgen | Village overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Epic Structures: Witch Huts | `Epic Witch Huts v1.3.1.jar` | CurseForge 1335768 / 8383193 | both | worldgen | Witch hut overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Epic Structures: Jungle Temples | `Epic Jungle Temples v1.0.2.jar` | CurseForge 1600197 / 8611815 | both | worldgen | Jungle temple overhaul. World data. ARR. | none | defaults | 2026-09-18 |
| Amplified Nether | `Amplified_Nether_26.2_v1.2.16.jar` | CurseForge 552176 / 8425271 | both | worldgen | Taller Nether. World data. | none | defaults | 2026-09-18 |
| Infernal Expansion Redux | `infernalexp-neoforge-1.21.1-0.3.15.jar` | CurseForge 1407992 / 8750501 | both | worldgen | Nether biomes. World data. | Lithostitched, GeckoLib | defaults | 2026-09-18 |
| Countered's Terrain Slabs | `terrain_slabs-neoforge-3.1.2.jar` | CurseForge 1125437 / 8216091 | both | worldgen | Terrain slabs. World data. | Architectury | defaults | 2026-09-18 |
| Fragmentum (NeoForge) | `fragmentum-neoforge-1.21.1-2.4.4.jar` | CurseForge 1123977 / 8707553 | both | library | Required by Aquamirae. | none | defaults | 2026-09-18 |
| Aquamirae | `aquamirae-neoforge-1.21.1-7.2.7.jar` | Modrinth k23mNPhZ / muWVnCSg | both | content | Ocean structures and boss. World data. | GeckoLib, Fragmentum | defaults | 2026-09-18 |

World-data: Create, Pipez, FTB Quests, Twilight Forest, Lost Cities, Tectonic, Regions Unexplored, Oh The Biomes We've Gone, Terralith, Nullscape, dungeon/structure mods, Amplified Nether, Infernal Expansion Redux, Terrain Slabs, and Aquamirae write blocks/items/dimensions/terrain/biomes. Those are not a clean uninstall. New world required for the 1.21.1 cutover.

## Credits / Attribution

| Mod | Author / project | License note | Required credit |
|---|---|---|---|
| Sodium | CaffeineMC | Polyform Shield 1.0.0 | Keep the CurseForge reference; do not rehost the jar. |
| Iris Shaders | IrisShaders | LGPL-3.0-only | CurseForge reference. |
| Lithium | CaffeineMC | LGPL-3.0-only | CurseForge reference. |
| FerriteCore | malte0811 | MIT | CurseForge reference. |
| ModernFix | embeddedt | LGPL-3.0-only | CurseForge reference. |
| ImmediatelyFast | RaphiMC | LGPL-3.0-or-later | CurseForge reference. |
| FastWorkbench, FastFurnace, FastSuite, Placebo | Shadows_of_Fire | See each CurseForge page | CurseForge reference. |
| Let Me Despawn, Almanac Lib | frikinjay | LGPL-3.0-only | CurseForge reference. |
| Neruina | bawnorton | See CurseForge page | CurseForge reference. |
| Configurable | See CurseForge project 1092048 | See CurseForge page | CurseForge reference. |
| Clumps | jaredlll08 | MIT | CurseForge reference. |
| AllTheLeaks | Uncandango | See CurseForge page | CurseForge reference. |
| Smooth Chunk Save, Cupboard | someaddon | See CurseForge pages | CurseForge reference. |
| BadOptimizations | thosea | See CurseForge page | CurseForge reference. |
| Dynamic FPS | juliand665 | See CurseForge page | CurseForge reference. |
| Crash Assistant | kr0stik | See CurseForge page | CurseForge reference. |
| Entity Culling | tr7zw | Custom protective license | CurseForge metadata only; do not bundle the jar. |
| Sodium Extra | FlashyReese | LGPL-3.0-only | CurseForge reference. |
| Flerovium, AsyncParticles | See CurseForge pages | LGPL-3.0-only | CurseForge reference. |
| More Culling | FxMorin | GPL-3.0-only | CurseForge reference. |
| Cloth Config | shedaniel | LGPL-3.0-only | CurseForge reference. |
| Structure Layout Optimizer, Resourceful Config | See CurseForge pages | MIT | CurseForge reference. |
| Ksyxis, Disconnect Packet Fix, quick pack | See CurseForge pages | MIT | CurseForge reference. |
| CrashExploitFixer | See CurseForge page | GPL-3.0-only | CurseForge reference. |
| Async Logger | See CurseForge page | LGPL-3.0-only | CurseForge reference. |
| ResourcePackCached | See CurseForge page | GPL-3.0-only | CurseForge reference. |
| Chunk Pregenerator | Speiger | See CurseForge page | CurseForge metadata only; do not embed the jar. |
| Carbon Config | Carbon Config Project | Apache-2.0 | CurseForge reference. |
| Create | simibubi / Creators of Create | Create Mod License | CurseForge reference; do not rehost the jar. |
| Iris Flywheel Compat | leon-o | CC0-1.0 | CurseForge reference. |
| Create Better FPS | See CurseForge page | MIT | CurseForge reference. |
| Create: Threaded Trains | See CurseForge page | GPL-3.0-or-later | CurseForge reference. |
| Architectury API | architectury | LGPL-3.0-only | CurseForge reference. |
| FTB Library, Teams, Quests | Feed The Beast | ARR | CurseForge metadata only; do not embed the jars. |
| FTB Quests Optimizer | See CurseForge page | MIT | CurseForge reference. |
| Pipez | henkelmax | ARR | CurseForge metadata only; do not embed the jar. |
| Pipez Lag Fix | Almana21 | ARR | CurseForge metadata only; do not embed the jar. |
| TxniLib | Txni | MIT | CurseForge reference. |
| Cerulean | Txni | GPL-3.0-only | CurseForge reference. |
| Bye?Pregen! | MoePus | LGPL-3.0-only | CurseForge reference. |
| The Twilight Forest | TeamTwilight | See CurseForge page | CurseForge reference. |
| The Lost Cities | McJty | MIT | CurseForge reference. |
| Lithostitched | Apollounknowndev | MIT | CurseForge reference. |
| Tectonic | Apollounknowndev | MIT | CurseForge reference. |
| TerraBlender (NeoForge) | Glitchfiend | LGPL-3.0-only | CurseForge reference. Use project 940057, not Forge 563928. |
| GeckoLib | Gecko | MIT | CurseForge reference. |
| CorgiLib | Corgi_Taco | See CurseForge page | CurseForge reference. |
| Oh The Trees You'll Grow | Corgi_Taco | See CurseForge page | CurseForge reference. |
| Oh The Biomes We've Gone | Potion Studios | ARR | CurseForge metadata only; do not embed the jar. |
| Regions Unexplored | UHQ_GAMES | See CurseForge page | CurseForge reference. |
| Global Packs | JTK222 | ARR | CurseForge metadata only; do not embed the jar. |
| Jade | Snownee | ARR | CurseForge metadata only; do not embed the jar. |
| Jade Addons | Snownee | ARR | CurseForge metadata only; do not embed the jar. |
| EMI | Emily | MIT | CurseForge reference. |
| EMI QoL Tweaks | See CurseForge page | See CurseForge page | CurseForge reference. |
| JEI / REI / EMI WorldGen | See CurseForge page | See CurseForge page | CurseForge reference. |
| GeckolibBetterFPS | MoePus | LGPL-3.0-or-later | CurseForge reference. |
| Terralith, Nullscape, Amplified Nether | Stardust Labs | See CurseForge pages | CurseForge reference. |
| Feature Recycler | Corgi_Taco | ARR | CurseForge metadata only; do not embed the jar. |
| YACL | isXander | LGPL-3.0-or-later | CurseForge reference. |
| Structurify | See CurseForge page | See CurseForge page | CurseForge reference. |
| When Dungeons Arise / Seven Seas | Aurelj | ARR | CurseForge metadata only; do not embed the jars. |
| Library Ferret, Awesome Dungeon | JTL | ARR | Modrinth metadata; do not embed the jars. |
| YUNG's API / Better Caves / Better Nether Fortresses / Bridges | YUNG | LGPL-3.0-only | CurseForge reference. |
| Moog's Structure Lib / Mineshafts | Moog | See project pages | CurseForge / Modrinth metadata. |
| Epic Structures | See CurseForge pages | ARR | CurseForge metadata only; do not embed the jars. |
| Infernal Expansion Redux | See CurseForge page | See CurseForge page | CurseForge reference. |
| Countered's Terrain Slabs | Countered | See CurseForge page | CurseForge reference. |
| Fragmentum, Aquamirae | Obscuria | Obscuria licenses | CurseForge / Modrinth metadata; do not embed the jars. |

## Future / Deferred Mods

Long lists: [deferred.md](deferred.md).

| Mod | Why not now | What would change that |
|---|---|---|
| Shader packs | Renderer extras are in; shader packs still a separate wave | After Extra + Iris boot cleanly. |
| Colorwheel | Shader companion; Iris Flywheel Compat covers Create+Iris for now | Shader-pack wave. |
| EMI Enchants | No 1.21.1 NeoForge file (last 1.20.4). | 1.21.1 NeoForge file. |
| LC²H / TF thread-safety addons | Still 1.20.1 Forge only | 1.21.1 NeoForge files. |

## Deferred Ecosystem Upgrades

| Proposed change | Why a candidate wanted it | Status |
|---|---|---|

## Removed

| Mod | Removed on | Why | Re-add? |
|---|---|---|---|
| Entire 1.20.1 Forge pack | 2026-09-17 | Loader and Minecraft cutover. History is on `forge-1.20.1`. | Research each mod again for 1.21.1 NeoForge. |
| Embeddium, Oculus, Radium | 2026-09-17 | No 1.21.1 NeoForge ports we will ship. | No; Sodium / Iris / Lithium are the replacements. |
| Noisium | 2026-09-18 | Bye?Pregen! marks Noisium incompatible. | No while ByePregen is in. |
| Achievements Optimizer | 2026-09-18 | Overlaps Cerulean (Icterine fork with the same every-few-ticks option). | No while Cerulean is in. |
