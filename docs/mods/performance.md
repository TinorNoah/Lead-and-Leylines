# Performance mods — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** first 1.21.1 NeoForge wave installed (2026-09-17). Extra/culling, ByePregen, C2ME (alpha, no OpenCL), Complementary/BSL + Euphoria.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. Dedicated server must not require it. |
| `server` | Dedicated server (and not needed on a pure client). Rare for this list. |
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. Use this for every “server optimizer” we actually ship, or singleplayer will not get the benefit. |

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Sodium | `sodium-neoforge-0.8.13+mc1.21.1.jar` | client | Official CaffeineMC renderer on NeoForge. Replaces Embeddium. |
| Iris Shaders | `iris-neoforge-1.8.14-beta.1+mc1.21.1.jar` | client | Official shaders for Sodium 0.8.x. Oculus has no 1.21.1 NeoForge file. Beta; known block-entity shadow quirk vs Iris 1.8.12+Sodium 0.6.13, which cannot pair with 0.8.13. |
| Lithium | `lithium-neoforge-0.15.4+mc1.21.1.jar` | both | Official server/gameplay optimizer. Replaces Radium. |
| FerriteCore | `ferritecore-7.0.3-neoforge.jar` | both | Memory. |
| ModernFix | `modernfix-neoforge-5.27.24+mc1.21.1.jar` | both | Launch and general mixins. Defaults. |
| ImmediatelyFast | `ImmediatelyFast-NeoForge-1.6.14+1.21.1.jar` | client | Immediate-mode / HUD rendering. |
| FastWorkbench | `FastWorkbench-1.21.1-9.1.3.jar` | both | Crafting screen / recipe lookup. Requires Placebo. Visual Workbench 21.1.2 is also in; its 21.0.2 release fixed the FastWorkbench crafting-menu crash. |
| FastFurnace | `FastFurnace-1.21.1-9.0.1.jar` | both | Furnace tick. Requires Placebo. |
| FastSuite | `FastSuite-1.21.1-6.0.7.jar` | both | Recipe manager. Requires Placebo. |
| Placebo | `Placebo-1.21.1-9.9.2.jar` | both | Library for the Fast* mods. |
| Let Me Despawn | `letmedespawn-1.21.x-neoforge-1.5.0.jar` | both | Persistent pickup-mobs despawn. Requires Almanac Lib. Server logic, so `both` for singleplayer. |
| Almanac Lib | `Almanac-1.21.1-2-neoforge-1.5.2.jar` | both | Required by Let Me Despawn. |
| Neruina | `neruina-3.3.3+1.21.1-neoforge.jar` | both | Isolates ticking entity crashes. Requires Configurable. |
| Configurable | `configurable-3.5.2+1.21.1-neoforge.jar` | both | Required by Neruina. |
| Clumps | `Clumps-neoforge-1.21.1-19.0.0.1.jar` | both | XP orb merge. |
| AllTheLeaks | `alltheleaks-1.1.13+1.21.1-neoforge.jar` | both | Known leak patches. |
| Smooth Chunk Save | `smoothchunk-1.21-4.1.jar` | both | Spreads chunk saves. Requires Cupboard. |
| Cupboard | `cupboard-1.21.1-4.2.jar` | both | Required by Smooth Chunk Save. |
| BadOptimizations | `BadOptimizations-2.4.1-1.21.1.jar` | client | Client-side rendering skip work. |
| Dynamic FPS | `dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar` | client | Lowers FPS when unfocused. File lists 1.21.1. |
| Crash Assistant | `CrashAssistant-neoforge-1.20.6-1.21.4-1.11.12.jar` | client | Crash dump helper. Dedicated boot log: client-only, no-op on server. |
| Entity Culling | `entityculling-neoforge-1.11.2-mc1.21.1.jar` | client | Occlusion culling. Custom tr7zw license; referenced via CurseForge, not bundled. |
| Sodium Extra | `sodium-extra-neoforge-0.9.4+mc1.21.1.jar` | client | Official Extra for Sodium 0.8.13 (fog, particles, FPS overlay). Not Chloride. |
| Flerovium | `flerovium-neoforge-1.21.1-1.1.3-all.jar` | client | Item/entity/particle draw. Not Better Block Entities. |
| AsyncParticles | `AsyncParticles-21.1.4.4+1.21.1.jar` | client | Particle thread. Not Particle Core. Coexists with AAA Particles (Effekseer). |
| Particle Rain | `particlerain-4.0.0-beta.11+1.21.1-neoforge.jar` | client | Weather particles. |
| Subtle Effects | `SubtleEffects-neoforge-1.21.1-1.14.3.jar` | client | Ambient particles and sounds. Fzzy Config. |
| More Culling | `moreculling-neoforge-1.21.1-1.0.10.jar` | client | Extra block/entity culling next to Entity Culling. Cloth Config required. See [configs.md](configs.md) for Extra leaf overlap. |
| Cloth Config | `cloth-config-15.0.140-neoforge.jar` | both | More Culling (and optional AsyncParticles) GUI. |
| Fzzy Config | `fzzy_config-0.7.7+1.21+neoforge.jar` | both | Required by Subtle Effects. |
| Structure Layout Optimizer | `structure_layout_optimizer-neoforge-1.0.12.jar` | both | Jigsaw/NBT structure gen. Resourceful Config required. |
| Resourceful Config | `resourcefulconfig-neoforge-1.21-3.0.11.jar` | both | SLO dependency. |
| Ksyxis | `Ksyxis-1.4.4.jar` | both | Unloads unused spawn chunks. |
| Disconnect Packet Fix | `disconnect-packet-fix-neoforge-2.0.1.jar` | both | MC-271325 disconnect packets. |
| quick pack | `quick-pack-neoforge-1.5.0+1.21.1.jar` | both | Faster zip datapack/resourcepack parse. Complements ModernFix. |
| CrashExploitFixer | `crashexploitfixer-neoforge-2.0.0+1.21.4.jar` | both | Crash-exploit filter; file tags 1.21.1–1.21.4. |
| Async Logger | `asynclogger-2.2.2+1.21.1-neoforge.jar` | client | Async log writes. |
| ResourcePackCached | `rpc-1.2.5+1.20.5-1.21.4-neoforge.jar` | client | Keeps server resource packs across rejoins. |
| Chunk Pregenerator | `Chunk-Pregenerator-Neoforge-1.21-4.5.4.jar` | both | Operator pregen. Carbon Config required. |
| Carbon Config | `CarbonConfig-Neoforge-1.21.1-2.0.2.1.jar` | both | Chunk Pregenerator dependency. |
| Create Better FPS | `createbetterfps-1.21.1-1.1.5.jar` | client | Create FPS with shader packs. Compatible with Colorwheel. |
| Create: Threaded Trains | `createthreadedtrains-neoforge-1.21.1-1.0.0.jar` | both | Train network off the server thread. See [configs.md](configs.md). |
| FTB Quests Optimizer | `FTBQuestsOptimizer-neoforge-3.2.0-1.21.1.jar` | both | Quest tick cost. Older than Quests 2101.1.36; see [configs.md](configs.md). |
| Bye?Pregen! | `byepregen-1.21.1-1.1.2.5.jar` | both | Chunk-gen MSPT / placement. Replaces Noisium (incompatible). Complements Chunk Pregenerator, does not replace it. |
| Cerulean | `cerulean-neoforge-1.0.0-1.21.1.jar` | both | Advancement InventoryChangeTrigger. Replaces Achievements Optimizer. TxniLib required. |
| TxniLib | `txnilib-neoforge-1.0.24-1.21.1.jar` | both | Cerulean dependency. |
| Pipez Lag Fix | `pipezlagfix-1.21.1-1.1.0.jar` | both | Item-pipe eco mode when the destination is full. |
| GeckolibBetterFPS | `gbf-1.21.1-1.0.2.jar` | client | Faster GeckoLib entity rendering. Alpha 1.0.2. Sodium and ImmediatelyFast already in. |
| FastBoot | `fastboot-1.21.x-v1.3neo.jar` | client | Early-load mixins. ARR. First to remove if launch breaks next to ModernFix / quick pack. |
| Fluidium | `fluidium-1.21.1-1.4.0.jar` | both | Distant fluid tick delay. Not a distant-entity freezer. Duplicationless required. |
| Duplicationless | `duplicationless-1.21.1-1.2.1.jar` | both | Fluidium hard dep. Same author. Do not treat as DoesPotatoTick. |
| MemGuard | `memguard-1.0.4.jar` | both | Heap monitor only in 1.0.4 (Create 6-unsafe mixins removed). Complements AllTheLeaks. |
| C2ME | `c2me-neoforge-mc1.21.1-0.4.0-alpha.0.122.jar` | both | Threaded chunk gen/IO. Alpha. OpenCL module not shipped. |
No pack config overlays yet; defaults only. Leaf overlap and Threaded Trains notes: [configs.md](configs.md).

## Considered / held / dropped

Full named-list skip reasons and the remaining 1.20.1 Forge mods: [deferred.md](deferred.md).

| Mod | Status | Why |
|---|---|---|
| Embeddium / Oculus / Radium | Dropped | No 1.21.1 NeoForge ports we will ship. Official Sodium / Iris / Lithium instead. |
| Chloride | Dropped | Overlaps Extra. ARR. Extra is the license we want. |
| Sodium Dynamic Lights / Options API | Held | 1.21.1 files exist but are 2025-era, before Sodium 0.8. Extra 0.9.4 does not need Options API. |
| Particle Core | Dropped | Incompatible with AsyncParticles (installed). Pulls Kotlin + Fzzy Config. |
| Better Block Entities | Dropped | Same draw-cost space as Flerovium. |
| Vanillin (`flw-vanillin`) | Dropped | Shader-incompatible; Iris is in. |
| Shader packs (BSL, Complementary, …) | Chosen | Complementary r5.9.3 + BSL v10.1.1 + Euphoria + Colorwheel. |
| Colorwheel / Colorwheel Patcher | Chosen | Shader companion; in with Euphoria. Replaces Iris Flywheel Compat for Create + Iris. |
| Iris Flywheel Compat | Dropped | Mixin conflict with Colorwheel (`irisflw` any); Colorwheel author will not fix it. |
| Voxy, Voxy Server Side, Forgified Fabric API | Dropped | Distant LOD removed on request. Forgified Fabric API was only required by the local Voxy renderer. Do not re-add. |
| Roxy | Dropped | Translation layer for Fabric Voxy `0.2.16-beta` (Minecraft 1.21.11 jar). Voxy is out. Do not add. |
| voxy-forged (GitHub) | Dropped | Unofficial NeoForge Voxy. ARR; no release jars; cannot go in packwiz. Do not build it into Prism. |
| Ecliptic Seasons : Voxy Compact | Dropped | Mixins fail hard without Voxy. Voxy is out. |
| Voxy - Make it compatible | Dropped | Voxy client companion. Voxy is out. |
| Rubidium Extra | Dropped | Embeddium-era. |
| Noisium | Dropped | Bye?Pregen! lists Noisium as incompatible. |
| Achievements Optimizer | Dropped | Overlaps Cerulean. |
| FastNoise | Dropped | Exclusive radius-8 smoke with Tectonic: 7.62 CPS vs 7.73 baseline (`121328Z` vs `120913Z`). No CPS gain. Do not stack with RTF. |
| C2ME OpenCL | Dropped | 1.21.1 file exists but is compiled for Java 25 (`UnsupportedClassVersionError` 69.0 on Java 21). Author: Java 25 even on pre-26.1. Also lists TerraBlender as biome-placement fail; Apple OpenCL unsupported. Do not bump the pack JVM. |
| ScalableLux | Dropped | Exclusive Tectonic smoke 4.89 CPS vs 7.73 baseline (`121800Z`); combo with Fast Noise 6.33 (`122255Z`). Logged BlockState lighting analysis errors. Not a CPS pick. |
