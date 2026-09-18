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
| FastBoot | `fastboot-1.21.x-v1.3neo.jar` | CurseForge 1030285 / 6998687 | client | optimizer | Early-load mixins; skips per-version data conversion on boot. ARR. | none | defaults | 2026-09-18 |
| Fluidium | `fluidium-1.21.1-1.4.0.jar` | CurseForge 1306029 / 7481400 | both | optimizer | Distant fluid ticks delayed (default 32 blocks, 50% skip). Claimed/force-loaded chunks stay full-speed. | Duplicationless | defaults | 2026-09-18 |
| Duplicationless | `duplicationless-1.21.1-1.2.1.jar` | CurseForge 1380105 / 8646414 | both | library | Required by Fluidium (`mandatory=true` `[1.1.5,)`). Not DoesPotatoTick. | none | defaults | 2026-09-18 |
| LC²H [Lost Cities: Multithreaded] | `lc2h-omni-4.2.3-LTS.jar` | CurseForge 1325431 / 8889302 | both | worldgen | Async Lost Cities gen. Omni jar tags 1.21.1 NeoForge. BRSSLA V2.0.0. | Lost Cities, Quantified API | defaults | 2026-09-18 |
| Quantified API | `quantified api-omni-2.2.3.jar` | CurseForge 1397967 / 8830709 | both | library | Required by LC²H (`quantified` `[2.2.2,)`). Omni jar tags 1.21.1 NeoForge. | none | defaults | 2026-09-18 |
| BiomeSpy | `biomespy-neoforge-1.21.1-1.3.3.jar` | CurseForge 1376024 / 7488072 | both | worldgen | Faster `/locate` biome/structure search. No worldgen change. | none | defaults | 2026-09-18 |
| DarkSleep - RPG Sleep Percentage | `darksleep-neoforge-1.21.1-1.0.1.jar` | CurseForge 1106281 / 5741536 | both | QoL | Sets `playersSleepingPercentage` to 50 on load. ARR. | none | defaults | 2026-09-18 |
| MemGuard | `memguard-1.0.4.jar` | CurseForge 1468440 / 8192435 | both | stability | Lightweight heap-usage log after Create 6 mixin strip. Complements AllTheLeaks. | none | defaults | 2026-09-18 |
| Balm | `balm-neoforge-1.21.1-21.0.65.jar` | CurseForge 531761 / 8645517 | both | library | Waystones, Crafting Tweaks, TrashSlot, Default Options. | none | defaults | 2026-09-18 |
| Iceberg | `Iceberg-1.21.1-neoforge-1.3.2.jar` | CurseForge 520110 / 6423863 | both | library | Equipment Compare, Legendary Tooltips, Item Borders. | none | defaults | 2026-09-18 |
| Prism | `Prism-1.21.1-neoforge-1.0.11.jar` | CurseForge 638111 / 6372979 | both | library | Legendary Tooltips, Item Borders. | none | defaults | 2026-09-18 |
| Curios API | `curios-neoforge-9.5.1+1.21.1.jar` | CurseForge 309927 / 6529130 | both | library | Elytra Slot (and later Ars). | none | defaults | 2026-09-18 |
| Caelus API | `caelus-neoforge-7.0.1+1.21.1.jar` | CurseForge 308989 / 5694215 | both | library | Elytra Slot. | none | defaults | 2026-09-18 |
| Bookshelf | `bookshelf-neoforge-1.21.1-21.1.81.jar` | CurseForge 228525 / 7606240 | both | library | Botany Pots/Trees. | none | defaults | 2026-09-18 |
| Prickle | `prickle-neoforge-1.21.1-21.1.11.jar` | CurseForge 1023259 / 6961457 | both | library | Botany Pots/Trees. | none | defaults | 2026-09-18 |
| Moonlight Lib | `moonlight-1.21.1-3.6.5-neoforge.jar` | CurseForge 499980 / 8905916 | both | library | Supplementaries, Amendments. | none | defaults | 2026-09-18 |
| SuperMartijn642's Core Lib | `supermartijn642corelib-1.1.24-neoforge-mc1.21.jar` | CurseForge 454372 / 8623666 | both | library | Trash Cans. | none | defaults | 2026-09-18 |
| SuperMartijn642's Config Lib | `supermartijn642configlib-1.1.8-neoforge-mc1.21.jar` | CurseForge 438332 / 5546996 | both | library | Trash Cans, Durability Tooltip. | none | defaults | 2026-09-18 |
| Titanium | `titanium-1.21-4.0.50.jar` | CurseForge 287342 / 8760562 | both | library | Functional Storage. | none | defaults | 2026-09-18 |
| Cobweb | `cobweb-neoforge-1.21-1.4.0.jar` | CurseForge 968456 / 7186943 | both | library | Harvest with ease. | none | defaults | 2026-09-18 |
| Fzzy Config | `fzzy_config-0.7.7+1.21+neoforge.jar` | CurseForge 1005914 / 8883390 | both | library | Simply Tooltips. | none | defaults | 2026-09-18 |
| Kotlin for Forge | `kotlinforforge-5.12.0-all.jar` | CurseForge 351264 / 8335665 | both | library | Simply Tooltips. | none | defaults | 2026-09-18 |
| Searchables | `Searchables-neoforge-1.21.1-1.0.2.jar` | CurseForge 858542 / 5831692 | client | library | Controlling. | none | defaults | 2026-09-18 |
| Xaero's Minimap | `xaerominimap-neoforge-1.21.1-26.5.0.jar` | CurseForge 263420 / 8849842 | client | map | Minimap. | none | defaults | 2026-09-18 |
| Xaero's World Map | `xaeroworldmap-neoforge-1.21.1-1.46.0.jar` | CurseForge 317780 / 8849973 | client | map | World map. | none | defaults | 2026-09-18 |
| Nature's Compass | `NaturesCompass-1.21.1-3.4.0-neoforge.jar` | CurseForge 252848 / 7892954 | both | utility | Locate biomes. | none | defaults | 2026-09-18 |
| Explorer's Compass | `ExplorersCompass-1.21.1-3.4.0-neoforge.jar` | CurseForge 491794 / 7892943 | both | utility | Locate structures. | none | defaults | 2026-09-18 |
| Structure Compass | `StructureCompass-1.21.1-4.2.1.jar` | CurseForge 319598 / 8439673 | both | utility | Locate structures. | none | defaults | 2026-09-18 |
| Waystones | `waystones-neoforge-1.21.1-21.1.45.jar` | CurseForge 245755 / 8873000 | both | utility | Teleport stones. World data. | Balm | defaults | 2026-09-18 |
| AppleSkin | `appleskin-neoforge-mc1.21-3.0.9.jar` | CurseForge 248787 / 7854442 | both | QoL | Hunger/saturation HUD. | none | defaults | 2026-09-18 |
| Mouse Tweaks | `MouseTweaks-neoforge-mc1.21-2.26.1.jar` | CurseForge 60089 / 5637846 | client | QoL | Inventory drag-transfer. | none | defaults | 2026-09-18 |
| ETF | `entity_texture_features-7.2.4-1.21-neoforge.jar` | CurseForge 568563 / 8908931 | client | renderer | Entity texture variants. | none | defaults | 2026-09-18 |
| EMF | `entity_model_features-3.3.9-1.21-neoforge.jar` | CurseForge 844662 / 8909425 | client | renderer | Entity model variants. | ETF | defaults | 2026-09-18 |
| Athena | `athena-neoforge-1.21.1-4.0.6.jar` | CurseForge 841890 / 8061947 | both | library | Connected textures. | none | defaults | 2026-09-18 |
| Crafting Tweaks | `craftingtweaks-neoforge-1.21.1-21.1.11.jar` | CurseForge 233071 / 8697050 | both | QoL | Crafting grid buttons. | Balm | defaults | 2026-09-18 |
| Controlling | `Controlling-neoforge-1.21.1-19.0.5.jar` | CurseForge 250398 / 6368976 | client | QoL | Keybind search. | Searchables | defaults | 2026-09-18 |
| Harvest with ease | `harvest-with-ease-neoforge-1.21-9.4.0.jar` | CurseForge 602171 / 5968872 | both | QoL | Right-click harvest. | Cobweb | defaults | 2026-09-18 |
| Clean Swing Through Grass | `cleanswing-1.10-1.21.jar` | CurseForge 915308 / 8746293 | both | QoL | Swing through plants. | none | defaults | 2026-09-18 |
| Cosmetic Armor Reworked | `cosmeticarmorreworked-1.21.1-v1-neoforge.jar` | CurseForge 237307 / 5610814 | both | QoL | Cosmetic armor slots. | none | defaults | 2026-09-18 |
| Elytra Slot | `elytraslot-neoforge-9.0.2+1.21.1.jar` | CurseForge 317716 / 5778461 | both | QoL | Elytra in Curios. | Curios, Caelus | defaults | 2026-09-18 |
| Durability Tooltip | `durabilitytooltip-1.2.0-neoforge-mc1.21.jar` | CurseForge 511040 / 8830219 | client | QoL | Durability numbers. | SuperMartijn642 Config | defaults | 2026-09-18 |
| Equipment Compare | `EquipmentCompare-1.21.1-neoforge-1.3.13.jar` | CurseForge 502561 / 6375501 | client | QoL | Shift-compare gear. | Iceberg | defaults | 2026-09-18 |
| Legendary Tooltips | `LegendaryTooltips-1.21.1-neoforge-1.5.5.jar` | CurseForge 532127 / 6400660 | client | QoL | Rarity tooltip frames. | Iceberg, Prism | defaults | 2026-09-18 |
| Item Borders | `ItemBorders-1.21-neoforge-1.2.5.jar` | CurseForge 513769 / 5591010 | client | QoL | Rarity item borders. | Iceberg, Prism | defaults | 2026-09-18 |
| Colorful Hearts | `colorfulhearts-neoforge-1.21.1-10.5.9.jar` | CurseForge 854213 / 6830399 | client | QoL | Colored heart rows. | none | defaults | 2026-09-18 |
| Simply Tooltips | `SimplyTooltips-neoforge-0.1.5.jar` | CurseForge 1475755 / 8715141 | client | QoL | Extra item tooltip lines. | Fzzy Config, Kotlin for Forge | defaults | 2026-09-18 |
| Better Advanced Tooltips | `better-advanced-tooltips-2101.1.0-build.5.jar` | CurseForge 1637623 / 8576077 | both | QoL | F3+H tag/component tooltips. Same jar as the Modrinth pin. | none | defaults | 2026-09-18 |
| Better Advancements | `BetterAdvancements-NeoForge-1.21.1-0.4.3.21.jar` | CurseForge 272515 / 5850587 | client | QoL | Advancement GUI. | none | defaults | 2026-09-18 |
| Clickable advancements | `clickadv-1.21-3.8.jar` | CurseForge 511733 / 5551404 | both | QoL | Click toast to open advancement. | none | defaults | 2026-09-18 |
| Toast Control | `ToastControl-1.21.1-9.0.1.jar` | CurseForge 271740 / 6751464 | client | QoL | Toast spam filter. | Placebo | defaults | 2026-09-18 |
| Default Options | `defaultoptions-neoforge-1.21.1-21.1.8.jar` | CurseForge 232131 / 8498229 | client | QoL | Pack default options. | Balm | defaults | 2026-09-18 |
| Login Protection | `logprot-1.21.1-3.6.jar` | CurseForge 358304 / 8824987 | both | QoL | Invuln after join. | none | defaults | 2026-09-18 |
| Packet Fixer | `packetfixer-3.3.1-1.20.5-1.21.X-merged.jar` | CurseForge 689467 / 7221528 | both | stability | Oversized packets. Not Disconnect Packet Fix. | none | defaults | 2026-09-18 |
| Too Fast | `toofast-1.21.0-0.4.3.6.jar` | CurseForge 550678 / 6819714 | both | QoL | Movement packet speed. | none | defaults | 2026-09-18 |
| Accelerated Decay | `accelerated-decay-neoforge-21.0.0.jar` | CurseForge 699872 / 5433036 | both | QoL | Faster leaf decay. | none | defaults | 2026-09-18 |
| WITS | `wits-neoforge-1.3.1.jar` | CurseForge 909375 / 8412915 | both | utility | Structure name overlay. | none | defaults | 2026-09-18 |
| Lootr | `lootr-neoforge-1.21.1-1.11.38.125.jar` | CurseForge 361276 / 8811105 | both | utility | Per-player loot chests. World data. | none | defaults | 2026-09-18 |
| Polymorph | `polymorph-neoforge-1.2.0+1.21.1.jar` | CurseForge 388800 / 8849478 | both | recipes | Duplicate recipe picker. | none | defaults | 2026-09-18 |
| Almost Unified | `almostunified-neoforge-1.21.1-1.4.2.jar` | CurseForge 633823 / 8127603 | both | recipes | Ore unification. | none | defaults | 2026-09-18 |
| ATO - All the Ores | `alltheores-3.2.0_neoforge_1.21.1.jar` | CurseForge 405593 / 7825464 | both | worldgen | Extra ores. World data. | none | defaults | 2026-09-18 |
| Supplementaries | `supplementaries-1.21.1-3.9.9-neoforge.jar` | CurseForge 412082 / 8852720 | both | content | Decor and utility blocks. World data. | Moonlight | defaults | 2026-09-18 |
| Amendments | `amendments-1.21-2.1.10-neoforge.jar` | CurseForge 896746 / 8825641 | both | content | Vanilla block tweaks. World data. | Moonlight | defaults | 2026-09-18 |
| NeoAuth | `NeoAuth-1.21.1-1.0.1.jar` | CurseForge 1140741 / 7069504 | client | auth | Microsoft auth helper. | none | defaults | 2026-09-18 |
| Better Compatibility Checker | `better-compatability-checker-neoforge-21.1.8.jar` | CurseForge 551894 / 7404415 | both | utility | Join-time modlist check. | none | defaults | 2026-09-18 |
| Crash Utilities | `crashutilities-9.0.4.jar` | CurseForge 371813 / 5993450 | both | stability | Extra crash helpers. | none | defaults | 2026-09-18 |
| Sophisticated Core | `sophisticatedcore-1.21.1-1.5.1.2341.jar` | CurseForge 618298 / 8838842 | both | library | Sophisticated storage/backpacks. | none | defaults | 2026-09-18 |
| Sophisticated Backpacks | `sophisticatedbackpacks-1.21.1-3.26.3.2158.jar` | CurseForge 422301 / 8845926 | both | storage | Backpacks. World data. | Sophisticated Core | defaults | 2026-09-18 |
| Sophisticated Storage | `sophisticatedstorage-1.21.1-1.5.91.2127.jar` | CurseForge 619320 / 8687896 | both | storage | Barrels/chests. World data. | Sophisticated Core | defaults | 2026-09-18 |
| Functional Storage | `functionalstorage-1.21.1-1.5.8.jar` | CurseForge 556861 / 8459097 | both | storage | Drawers. World data. | Titanium | defaults | 2026-09-18 |
| Botany Pots | `botanypots-neoforge-1.21.1-21.1.44.jar` | CurseForge 353928 / 8243851 | both | farming | Crop pots. World data. | Bookshelf, Prickle | defaults | 2026-09-18 |
| Botany Trees | `botanytrees-neoforge-1.21.1-21.1.7.jar` | CurseForge 411357 / 8188485 | both | farming | Tree pots. World data. | Bookshelf, Prickle | defaults | 2026-09-18 |
| Trash Cans | `trashcans-1.1.0-neoforge-mc1.21.jar` | CurseForge 394535 / 8646611 | both | storage | Trash blocks. World data. | SuperMartijn642 Core + Config | defaults | 2026-09-18 |
| TrashSlot | `trashslot-neoforge-1.21.1-21.1.11.jar` | CurseForge 235577 / 8163135 | both | QoL | Inventory trash slot. | Balm | defaults | 2026-09-18 |
| Packing Tape | `PackingTape-1.21.1-0.15.6.jar` | CurseForge 238659 / 6667874 | both | storage | Pickup tile entities. | none | defaults | 2026-09-18 |
| FTB Chunks | `ftb-chunks-neoforge-2101.1.22.jar` | CurseForge 314906 / 8791113 | both | utility | Chunk claims. World data. ARR. | FTB Library, Architectury | defaults | 2026-09-18 |
| FTB Essentials | `ftb-essentials-neoforge-2101.1.10.jar` | CurseForge 410811 / 8442866 | both | utility | `/home` and related commands. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB Ultimine | `ftb-ultimine-neoforge-2101.1.15.jar` | CurseForge 386134 / 8231400 | both | utility | Vein mine. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB Filter System | `ftb-filter-system-neoforge-21.1.4.jar` | CurseForge 943925 / 7429011 | both | library | Item filters. ARR. | FTB Library | defaults | 2026-09-18 |
| FTB XMod Compat | `ftb-xmod-compat-neoforge-21.1.11.jar` | CurseForge 889915 / 8653466 | both | utility | FTB cross-mod hooks. ARR. | FTB Library | defaults | 2026-09-18 |
| Create Ultimine | `createultimine-1.21.1-neoforge-1.3.2.jar` | CurseForge 1231381 / 8086425 | both | optimizer | Create-aware vein mine. | Create | defaults | 2026-09-18 |
| Create: Sky Village | `create_sky_village-0.0.38 NeoForge 1.21.1.jar` | CurseForge 1104939 / 8004708 | both | worldgen | Create village structure. World data. | Create | defaults | 2026-09-18 |
| Sophisticated Backpacks Create Integration | `sophisticatedbackpackscreateintegration-1.21.1-0.2.0.168.jar` | CurseForge 1238567 / 8833933 | both | storage | Create + backpacks. | Create, Backpacks, Core | defaults | 2026-09-18 |
| Sophisticated Storage Create Integration | `sophisticatedstoragecreateintegration-1.21.1-0.1.21.209.jar` | CurseForge 1226755 / 8503147 | both | storage | Create + storage. | Create, Storage, Core | defaults | 2026-09-18 |
| C2ME | `c2me-neoforge-mc1.21.1-0.4.0-alpha.0.122.jar` | CurseForge 533097 / 8896937 | both | optimizer | Threaded chunk gen/IO. Alpha. ByePregen disables C2ME FluidPostProcessingFilter. OpenCL module not shipped (Java 25). | none | defaults | 2026-09-18 |
| Applied Energistics 2 | `appliedenergistics2-19.2.17.jar` | CurseForge 223794 / 7027323 | both | storage | ME network. World data. | GuideME | defaults | 2026-09-18 |
| GuideME | `guideme-21.1.19.jar` | CurseForge 1173950 / 8897145 | both | library | AE2 guidebook. | none | defaults | 2026-09-18 |
| AE2 Things | `AE2-Things-1.4.2-beta.jar` | CurseForge 609977 / 5637783 | both | storage | AE2 disks. Beta 1.4.2. World data. | AE2, GuideME | defaults | 2026-09-18 |
| Ars Énergistique | `arseng-2.1.1-beta.jar` | CurseForge 905641 / 6203425 | both | magic | Ars + AE2 bridge. Beta. | Ars Nouveau, AE2 | defaults | 2026-09-18 |
| Refined Storage | `refinedstorage-neoforge-2.0.9.jar` | CurseForge 243076 / 8211701 | both | storage | RS 2. World data. | none | defaults | 2026-09-18 |
| Quartz Arsenal | `refinedstorage-quartz-arsenal-neoforge-1.0.8.jar` | CurseForge 1230483 / 8103101 | both | storage | RS wireless crafting grid (replaces RS Addons). | RS | defaults | 2026-09-18 |
| Cable Tiers | `cabletiers-neoforge-1.21.1-0.6.14.jar` | CurseForge 454382 / 8705433 | both | storage | Faster RS cables. | RS | defaults | 2026-09-18 |
| Extra Disks | `ExtraDisks-1.21.1-4.0.15.jar` | CurseForge 351491 / 8031115 | both | storage | Larger RS disks. Beta. | RS | defaults | 2026-09-18 |
| ExtraStorage | `ExtraStorage-1.21.1-5.0.10.jar` | CurseForge 410168 / 8330353 | both | storage | Extra RS storage. | RS, EdivadLib | defaults | 2026-09-18 |
| Farmer's Delight | `FarmersDelight-1.21.1-1.3.4.jar` | CurseForge 398521 / 8765184 | both | farming | Kitchen. World data. | none | defaults | 2026-09-18 |
| Spice of Life: Carrot Edition | `solcarrot-1.21.1-1.16.6.jar` | CurseForge 277616 / 7374098 | both | food | Food diversity. | none | defaults | 2026-09-18 |
| Mekanism | `Mekanism-1.21.1-10.7.19.85.jar` | CurseForge 268560 / 7904058 | both | tech | Machines. World data. | none | defaults | 2026-09-18 |
| Ars Nouveau | `ars_nouveau-1.21.1-5.13.1.jar` | CurseForge 401955 / 8721482 | both | magic | Spellcrafting. World data. | none | defaults | 2026-09-18 |
| Spectrum | `spectrum-1.12.7-1.21.1-neo.jar` | CurseForge 556967 / 8866762 | both | magic | Progression magic. World data. | Revelationary, Modonomicon, Curios | defaults | 2026-09-18 |
| TMRV | `toomanyrecipeviewers-0.9.0+mc.21.1.jar` | CurseForge 1194921 / 8336857 | client | recipes | JEI plugins on EMI without JEI. | EMI | defaults | 2026-09-18 |
| EMI Ores | `emi_ores-1.3+1.21.1+neoforge.jar` | CurseForge 974009 / 8254306 | client | recipes | Ore pages in EMI. | EMI | defaults | 2026-09-18 |
| EMI Enchanting | `emi_enchanting-0.1.2+1.21+neoforge.jar` | CurseForge 936713 / 5733125 | client | recipes | Enchantment pages in EMI. 2024 file. | EMI | defaults | 2026-09-18 |
| Complementary Reimagined | `ComplementaryReimagined_r5.9.3.zip` | CurseForge 627557 / 8884654 | client | shader | Matches Euphoria r5.9.3. | Iris | defaults | 2026-09-18 |
| Complementary Unbound | `ComplementaryUnbound_r5.9.3.zip` | CurseForge 385587 / 8884656 | client | shader | Matches Euphoria r5.9.3. | Iris | defaults | 2026-09-18 |
| BSL Shaders | `BSL_v10.1.1.zip` | CurseForge 322506 / 7588844 | client | shader | Latest CF 1.21.1-tagged BSL. | Iris | defaults | 2026-09-18 |
| Euphoria Patches | `EuphoriaPatcher-1.10.5-r5.9.3-neoforge.jar` | CurseForge 915902 / 8884680 | client | shader | Complementary extras. | Colorwheel | defaults | 2026-09-18 |
| Colorwheel | `colorwheel-neoforge-1.3.0-beta3+mc1.21.1.jar` | CurseForge 1254143 / 8845482 | client | renderer | Iris shader extras. Beta. | none | defaults | 2026-09-18 |
| Colorwheel Patcher | `colorwheel_patcher-neoforge-1.0.5+mc1.21.1.jar` | CurseForge 1285475 / 7924942 | client | renderer | Colorwheel companion. | Colorwheel | defaults | 2026-09-18 |

World-data: Create, Pipez, FTB Quests/Chunks, Twilight Forest, Lost Cities, Tectonic, Regions Unexplored, Oh The Biomes We've Gone, Terralith, Nullscape, dungeon/structure mods, Amplified Nether, Infernal Expansion Redux, Terrain Slabs, Aquamirae, Waystones, Lootr, ATO, Supplementaries, Amendments, Sophisticated/Functional storage, Botany, Trash Cans, Create Sky Village, AE2, Refined Storage, Mekanism, Ars Nouveau, Farmer's Delight cluster, Alchemistry, and Spectrum write blocks/items/dimensions/terrain/biomes. Those are not a clean uninstall. New world required for the 1.21.1 cutover.

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
| FastBoot | dnlayu | ARR | CurseForge metadata only; do not embed the jar. |
| Fluidium, Duplicationless | Kall | MIT | CurseForge reference. |
| LC²H | Admany | BRSSLA V2.0.0 | CurseForge metadata only; do not embed the jar. |
| Quantified API | Admany | See CurseForge page | CurseForge metadata only; do not embed the jar. |
| BiomeSpy | MoePus | LGPL-3.0-only | CurseForge reference. |
| DarkSleep | GamerPotion | ARR | CurseForge metadata only; do not embed the jar. |
| MemGuard | See CurseForge project 1468440 | MIT (in-jar) | CurseForge reference. |
| Wave 1 QoL/storage/FTB (Xaero, Waystones, Sophisticated, etc.) | See each CurseForge page | Mix of MIT/ARR/LGPL | CurseForge metadata; do not embed ARR jars. |
| Better Advanced Tooltips | Lat / latvian-dev | MIT | CurseForge reference. |

## Future / Deferred Mods

Long lists: [deferred.md](deferred.md).

| Mod | Why not now | What would change that |
|---|---|---|
| TwilightForest Thread Safety Addon | Still 1.20.1 Forge only | 1.21.1 NeoForge file. |
| C2ME OpenCL | Java 25 even on 1.21.1; TerraBlender biome fail; Apple OpenCL unsupported | Pack JVM 25 (separate upgrade) plus TerraBlender-safe OpenCL, or skip. |

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
| C2ME OpenCL | 2026-09-18 | Java 25 class files on a Java 21 pack; TerraBlender listed as biome-placement fail. | No while Java 21. |
| ScalableLux | 2026-09-18 | Lighting companion for C2ME OpenCL only. | Only with OpenCL. |
