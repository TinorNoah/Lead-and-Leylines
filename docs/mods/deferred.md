# Deferred and not-yet-ported mods

Not an install list. Each row still needs a fresh 1.21.1 NeoForge research pass and explicit file approval. Minecraft / loader: [`pack/pack.toml`](../../pack/pack.toml). What is already in the pack: [manifest.md](manifest.md). History of the old pack: branch `forge-1.20.1`.

This file lists **only mods that are not in `pack/mods/`**.

## Held — file exists but not a fit yet

| Named as | Why not |
|---|---|
| sodium lights + Sodium Options API + Options Mod Compat | Matching jars are from 2025-01 / 2025-04, before Sodium 0.8. Extra 0.9.4 does not need Options API. Wait for 0.8-era files. |
| Particle Core | Incompatible with AsyncParticles. |
| Redirected | 1.21.1 files exist (2025-02). Stale vs current NeoForge; enum intern is a tiny gain. |
| ServerCore 1.5.19 | Entity Activation Range is a distant-entity freezer. Pack policy: do not add those. |
| Gnetum | HUD-over-frames. Overlaps ImmediatelyFast. |
| LightSpeedRe | Launch shortcut. Overlaps ModernFix. |
| Put A Plug In it! (PAPI) | Same leak-patch niche as AllTheLeaks. |
| Fast Noise | 1.21.1 NF file exists. Exclusive Tectonic smoke 7.62 CPS vs 7.73 Tectonic-only baseline. No CPS gain. |
| TaCZ / Sophisticated Backpacks ammo | 1.21.1 NeoForge file requires modid `tacz-1-21-1`. Unofficial port 1353462 registers as `tacz`. |
| TaCZ: Immersive Ballistic (+ TaCZ Tweaks) | Alpha. Duplicate VertexFormatElement registration with Iris on boot. |
| ScalableLux | 1.21.1 NF file exists. Exclusive Tectonic smoke 4.89 CPS vs 7.73; BlockState lighting errors. Combo with Fast Noise 6.33. |
| AdventureZ | Project 390991's 1.21.1 file is Fabric only. |
| ANARCHY Minibosses | Requires Spell Engine, Spell Power, AzureLib, and Accessories beside Curios. |
| Myths of the Sea | Requires GeckoLib 4.7.4. The pack is on 4.9.3. |
| Somake Spells | Apothic Attributes is in. Still requires Cataclysm. |
| Weapons of Legendary Monsters | Forge 1.20.1 only. Project 1169738. |
| Eternal Hunts | Requires Cataclysm, Mowzie's Mobs, and Born in Chaos. Cataclysm is not in the pack. |
| Neo Vitae | Dropped from the pack (and BMAddon with it). World-data / demon dungeon. Revisit only with explicit approval. |
| Chunk Pregenerator (+ Carbon Config) | Removed 2026-09-26. Hang on dedicated-server stop (`Pregen Chunk Task Queue`). Operator pregen is `/neoforge generate`. Do not re-add without fixing that shutdown hang. |
| JEI / REI / EMI WorldGen | Removed 2026-09-26. Worldgen pages in JEI. Do not re-add; JER stays for mob/dungeon loot. |

## Overlaps something already in the pack

| Named as | Why not |
|---|---|
| (Sodium) Chloride | Same Extra job (leaves, fog, FPS overlay, entity distance). ARR. Extra is the license we want. |
| Sodium Extras (Txni) | Third Extra. Last 1.21.1 file 2025-04; needs old Options API. Official Extra 0.9.4 covers this. |
| Sodium Leaf Culling | Extra / Chloride already do leaves. 2025-04 Sodium-era file. |
| OptiLeaves | Same leaf-culling niche. ARR. |
| Despawn Tweaks | Let Me Despawn already covers this. |
| NoisiumForked 2.7.0 | Do not stack on ByePregen. Noisium itself was removed as incompatible. |
| Idle Boost | Dynamic FPS already lowers unfocused FPS. 2024-09 file. |
| Better Block Entities | Same draw-cost space as Flerovium. Pick one. |
| Performance Tweaks | Same project as Adaptive Performance Tweaks (listed twice in the original doc). |
| Better Sparse Structures | Same structure-spacing job as Structurify. Do not stack. |
| Structure Compass | Same structure-finding job as Explorer's Compass. Dropped 2026-09-24. Do not re-add. |

## Needs a parent mod we have not ported

| Named as | Missing parent / file |
|---|---|
| Vanillin (`flw-vanillin`) | Shader-incompatible with Iris. |
| TwilightForest Thread Safety Addon | No 1.21.1 NeoForge file. |

## Wrong renderer, missing file, or not a single pack mod

| Named as | Why not |
|---|---|
| Bocchium | No 1.21.1 NeoForge project found. Old Embeddium/Rubidium bedrock-face cull. |
| DarkTimer - RPG Clear Entity Lag | No 1.21.1 NeoForge file. Entity-delete lag clear. ARR. |
| Delightful | No 1.21.1 NeoForge file (last 1.20.1). |
| Refined Polymorphism | No 1.21.1 NeoForge file. |
| Polymorphic Energistics | July 2024 `0.4.1` vs current AE2 19.2.17 / RS 2.0.9. |
| RS Addons | Replaced by Quartz Arsenal on 1.21.1; no 1.21.1 file. |
| C2ME OpenCL | 1.21.1 NeoForge file exists (`1563823` / `8896938`) but is Java 25 (class file 69). Pack stays on Java 21. Author also lists TerraBlender biome-placement failure; Apple OpenCL unsupported. |
| Continuity | `3.0.0+1.21.neoforge` (531351 / 5981335) requires Connector and Forgified Fabric API, and it was built for Sodium 0.6. Pack is Sodium 0.8.13. Do not re-add. |

## Gameplay-changing, crashy, or too much library for the gain

| Named as | Correction |
|---|---|
| DoesPotatoTick? | Distant-entity freeze. Do not add on top of Fluidium/Duplicationless. |
| Immersive Optimization | Same entity-scheduler idea. Skip. |
| Adaptive Performance Tweaks | Auto-cuts view distance / spawns / items. Skip. |
| TCT ClearLag | Deletes entities. ARR + TCT Core. Skip. |
| Dimensional Threading Reforked | One world per thread. Skip. |
| Invasive Optimizations | Author: disable this first if anything breaks. Optional Create / Pipez patches on a mixed pack. Skip. |
| Ixeris | Moves input off-thread. Skip. Asked again 2026-09-26. Still skip. |
| Nolijium | Fog, sky, particles, and darkness overlap Sodium / Iris. Last 1.21.1 file is 2025-03. Optional Embeddium. Skip. |
| Inventory Essentials | Installed 2026-09-26 beside Inventory Profiles Next (user override). |
| Modern Dynamics | Installed 2026-09-26 after Pipez removal. |
| Pretty X Smart Pipez, Pretty X Smart Pipez Mekanism Edition | Resource packs, not mods. `allowModDistribution` is false, so they cannot ship. Skip. |
| Rechiseled (+ Chipped / Create / AE2) | Installed 2026-09-26 beside Chipped (user override). |
| Mob Grinding Utils (+ Vanillafied) | Installed 2026-09-26. |
| Create: Copper & Zinc | Skipped 2026-09-26; Create: Alloyed is the metal addon. |
| Modern Industrialization Extentended Integrations | Dropped 2026-09-26. Crashes MI 2.5.8: `Machine casing model "modern_industrialization:iv" does not exist` in `miei` stress hatches. Do not re-add until a build matches current MI casings. |
| Krypton Reno | Real project is `krypton-fnp` (`krypton_fnp-neoforge-1.21.1-0.2.28.1`). File exists. Still hold: network mixins next to Lithium / NeoForge. |
| Fast Item Frames | Installed 2026-09-26. World data + Puzzles Lib (already in). |
| BetterGrassify | Required Forgified Fabric API. Skip. |
| Roxy | Translation layer for Fabric Voxy `0.2.16-beta` (1.21.11 jar). Voxy is out. Skip. |
| Ecliptic Seasons : Fabricated | Fabric rewrite. Bundles listed it as a required dep; packwiz skipped it on NeoForge. Skip. |
| Serene Seasons | Replaced by Ecliptic Seasons + Serene Seasons API Stub. Do not stack. |
| voxy-forged | Dropped. ARR; no GitHub release jars. Do not build it into Prism. |
| Voxy Server Side, Forgified Fabric API | Dropped with Voxy on 2026-09-24. Forgified Fabric API had no other user in the pack. |
| Ecliptic Seasons : Voxy Compact | Dropped. Crashes without Voxy. Do not re-add. |
| Voxy - Make it compatible | Dropped. Voxy client companion. Do not re-add. |
| EpicFight-Nightfall (+ Invincible Lib) | Dedicated server crash: `EffekUnits.VFXENABLE` reads client config before load (e.g. Sophisticated Backpacks spawn potions). Do not re-add without a proven dedicated-server fix. AAA Particles stays in the pack. |
| Vic's Point Blank - Interaction | Dropped 2026-09-24. `InteractionManager` is marked client-only and crashes a dedicated server during config load. Do not re-add. |
| Mekanism Covers | Client join crash vs Sodium 0.8.13 (`SodiumBlockRendererMixin.putTranslucentVertexColor`, 0 targets). Latest 1.21.1 file is still 1.3-BETA (2025-01-10). Do not re-add until a Sodium 0.8-compatible build ships. |
| JEI++ (JEI Plus) | Client join crash on JEI 19.57: `BookmarkOverlayMixin` needs `mezz.jei.gui.input.IUserInputHandler`, which that JEI build moved to `mezz.jei.common.input`. Latest file is still 1.0.5 for JEI 19.56 (2026-09-13). Do not re-add until a 19.57 build ships. |
| Loading Backgrounds | Cosmetic + Architectury + ARR. Skip. |
| Too Many Entities | Client limiter + Architectury + Cloth. Skip. |
| GPUTape | ToadLib. Modest vs Sodium/Iris/ImmediatelyFast. Skip. |

## 1.20.1 Forge pack — not on 1.21.1 NeoForge yet

Source: `pack/mods/*.pw.toml` on branch `forge-1.20.1`. Do not dump-install. Replaced names that must not come back as-is: Embeddium, Oculus, Radium, Rubidium Extra.

### Create

Slice & Dice; Alex's Caves Compat. Central Kitchen and Applied Kinetics are installed.

### Applied Energistics 2

Polymorphic Energistics.

### Refined Storage

Refined Polymorphism.

### Combat / guns / movement

Simply Swords; Simply More. Remaining TaCZ content not in the pack: Labs, Gucci & Vuitton. Daffa's Arsenal and CS+ are in `pack/tacz/`. Warzone 1.1.8B is dropped (encrypted `taczpack.dat`; this port never unpacks the textures). MCS2Gun-addon `1285238` stays out (1.20.1 encrypted Forge jar; Pack Upgrader does not register it). The MCS2 gun pack zip is in [content.md](content.md). Epic Fight, ParCool, Ice and Fire CE, the unofficial 1.21.1 TaCZ port, and Vic's Point Blank are in [content.md](content.md). Point Blank: Recipe stays out (no 1.21.1 NeoForge CurseForge file; declined). Do not add Pointblank: Jelly beside official Point Blank. Official Doom, Destiny, and Blue Archive packs are not in.

### Worldgen / structures / dimensions

Stalwart Dungeons; Bygone Nether; Awesome Dungeon Nether.

### Farmer's Delight cluster

Delightful.

### Maps / compasses / QoL

Inventory Tweaks ReFoxed; No trampling on farmland (no 1.21.1 NF); NetherPortalFix; MmmMmmMmmMmm; Model Gap Fix; Perfect Graves; Dyenamics; Dyenamics and Friends. Construction Sticks, Tempad, Inventory Essentials, and Observable are installed. Fusion and its connected-glass pack are in [content.md](content.md).

### UI / loading / shaders

FancyMenu; Drippy Loading Screen; Konkrete; Melody.

### Libraries (only with a consumer)

Resourceful Lib (already in for Variants&Ventures, Chipped, and Handcrafted); BCLib Forge (old); WunderLib Forge (old). New Dawn BCLib/WunderLib, Ice and Fire Jupiter/Uranus, and Patchouli are in [manifest.md](manifest.md).

### Other Forge leftovers

Chunky. Any other slug on `forge-1.20.1` `pack/mods/` not named above and not in [manifest.md](manifest.md) is still not ported.
