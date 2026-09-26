# Performance

Tick, memory, and chunk-saving work that runs on the server and in singleplayer. Render-only mods are in [Rendering](rendering.md). Placebo and Cupboard are in [Libraries](libraries.md).

Each mod is listed once. Decision notes stay in [`docs/mods/`](../mods/manifest.md).

## Tick and memory

| Mod | File | Side | Tags | What it adds |
|---|---|---|---|---|
| Lithium (Fabric/NeoForge) | `lithium-neoforge-0.15.4+mc1.21.1.jar` | both | `core`, `optimizer` | Gameplay and tick optimizer. |
| FerriteCore ((Neo)Forge) | `ferritecore-7.0.3-neoforge.jar` | both | `core`, `optimizer` | Lower memory use. |
| ModernFix | `modernfix-neoforge-5.27.24+mc1.21.1.jar` | both | `core`, `optimizer` | Launch and mixin fixes. |
| Concurrent Chunk Management Engine | `c2me-neoforge-mc1.21.1-0.4.0-alpha.0.122.jar` | both | `core`, `optimizer` | Threaded chunk generation. |
| Bye?Pregen! | `byepregen-1.21.1-1.1.2.5.jar` | both | `core`, `optimizer` | Faster chunk generation. Do not add Noisium beside it. |
| Server Performance - Smooth Chunk Save | `smoothchunk-1.21-4.1.jar` | both | `core`, `optimizer` | Spreads chunk saves out. |
| Ksyxis | `Ksyxis-1.4.5.jar` | both | `addon`, `optimizer` | Faster world join. |
| Let Me Despawn | `letmedespawn-1.21.x-neoforge-1.5.0.jar` | both | `core`, `optimizer` | Lets persistent mobs despawn. |
| Almanac Lib | `Almanac-1.21.1-2-neoforge-1.5.2.jar` | both | `library`, `optimizer` | Library Let Me Despawn needs. |
| Clumps | `Clumps-neoforge-1.21.1-19.0.0.1.jar` | both | `core`, `optimizer` | Merges XP orbs. |
| FastWorkbench | `FastWorkbench-1.21.1-9.1.3.jar` | both | `core`, `optimizer` | Faster crafting lookup. |
| FastFurnace | `FastFurnace-1.21.1-9.0.1.jar` | both | `addon`, `optimizer` | Faster furnaces. |
| FastSuite | `FastSuite-1.21.1-6.0.7.jar` | both | `addon`, `optimizer` | Faster recipe manager. |
| Cerulean | `cerulean-neoforge-1.0.0-1.21.1.jar` | both | `addon`, `optimizer` | Cheaper advancement checks. |
| TxniLib | `txnilib-neoforge-1.0.24-1.21.1.jar` | both | `library`, `optimizer` | Library Cerulean needs. |
| Fluidium | `fluidium-1.21.1-1.4.0.jar` | both | `addon`, `optimizer` | Delays fluid ticks far from players. Claimed chunks stay full speed. |
| Duplicationless | `duplicationless-1.21.1-1.2.1.jar` | both | `library`, `optimizer` | Library Fluidium needs. Also blocks a few dupe paths. |
| Observable | `observable-5.4.4.jar` | both | `addon`, `optimizer` | In-game lag profiler. |
