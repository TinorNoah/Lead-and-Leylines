# Performance mods — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** first 1.21.1 NeoForge wave installed (2026-09-17). Official Sodium / Iris / Lithium replace the 1.20.1 Embeddium / Oculus / Radium stack. Shader packs and Colorwheel are not in this wave.

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
| FastWorkbench | `FastWorkbench-1.21.1-9.1.3.jar` | both | Crafting screen / recipe lookup. Requires Placebo. |
| FastFurnace | `FastFurnace-1.21.1-9.0.1.jar` | both | Furnace tick. Requires Placebo. |
| FastSuite | `FastSuite-1.21.1-6.0.7.jar` | both | Recipe manager. Requires Placebo. |
| Placebo | `Placebo-1.21.1-9.9.2.jar` | both | Library for the Fast* mods. |
| Let Me Despawn | `letmedespawn-1.21.x-neoforge-1.5.0.jar` | both | Persistent pickup-mobs despawn. Requires Almanac Lib. Server logic, so `both` for singleplayer. |
| Almanac Lib | `Almanac-1.21.1-2-neoforge-1.5.2.jar` | both | Required by Let Me Despawn. |
| Neruina | `neruina-3.3.3+1.21.1-neoforge.jar` | both | Isolates ticking entity crashes. Requires Configurable. |
| Configurable | `configurable-3.5.2+1.21.1-neoforge.jar` | both | Required by Neruina. |
| Clumps | `Clumps-neoforge-1.21.1-19.0.0.1.jar` | both | XP orb merge. |
| Noisium | `noisium-neoforge-2.3.0+mc1.21-1.21.1.jar` | both | Worldgen noise. Archived on CurseForge; 2.3.0 is the 1.21.1 file. |
| AllTheLeaks | `alltheleaks-1.1.12+1.21.1-neoforge.jar` | both | Known leak patches. |
| Smooth Chunk Save | `smoothchunk-1.21-4.1.jar` | both | Spreads chunk saves. Requires Cupboard. |
| Cupboard | `cupboard-1.21.1-4.2.jar` | both | Required by Smooth Chunk Save. |
| BadOptimizations | `BadOptimizations-2.4.1-1.21.1.jar` | client | Client-side rendering skip work. |
| Dynamic FPS | `dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar` | client | Lowers FPS when unfocused. File lists 1.21.1. |
| Crash Assistant | `CrashAssistant-neoforge-1.20.6-1.21.4-1.11.12.jar` | client | Crash dump helper. Dedicated boot log: client-only, no-op on server. |
| Entity Culling | `entityculling-neoforge-1.10.5-mc1.21.1.jar` | client | Occlusion culling. Custom tr7zw license; referenced via CurseForge, not bundled. |

No pack config overrides yet; defaults only. See [configs.md](configs.md).

## Considered / held / dropped

Full named-list skip reasons and the remaining 1.20.1 Forge mods: [deferred.md](deferred.md).

| Mod | Status | Why |
|---|---|---|
| Embeddium / Oculus / Radium | Dropped | No 1.21.1 NeoForge ports we will ship. Official Sodium / Iris / Lithium instead. |
| Sodium Extra | Held | 0.9.4 now has a 1.21.1 NeoForge file for Sodium 0.8.13. Not installed; pick Extra or Chloride, not both. |
| Chloride | Held | Overlaps Extra. ARR. |
| Shader packs (BSL, Complementary, …) | Deferred | Separate wave after the renderer boots cleanly. |
| Colorwheel / Colorwheel Patcher | Deferred | Shader companion; wait for shader wave. |
| Rubidium Extra | Dropped | Embeddium-era. |
