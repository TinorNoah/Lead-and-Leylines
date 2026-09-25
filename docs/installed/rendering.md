# Rendering

Shaders, entity models, and client render optimizers. Server tick optimizers are in [Performance](performance.md).

Each mod is listed once. Decision notes stay in [`docs/mods/`](../mods/manifest.md).

## Sodium and Iris

| Mod | File | Side | Tags | What it adds |
|---|---|---|---|---|
| Sodium | `sodium-neoforge-0.8.13+mc1.21.1.jar` | client | `core`, `rendering`, `optimizer` | Renderer. |
| Iris Shaders | `iris-neoforge-1.8.14-beta.1+mc1.21.1.jar` | client | `core`, `rendering`, `optimizer` | Shader loader for Sodium. |
| Euphoria Patches | `EuphoriaPatcher-1.10.5-r5.9.3-neoforge.jar` | client | `core`, `rendering` | Shader patch set for Iris. |
| Sodium Extra | `sodium-extra-neoforge-0.9.4+mc1.21.1.jar` | client | `core`, `rendering`, `optimizer` | Extra Sodium options. |
| Colorwheel | `colorwheel-neoforge-1.3.0-beta3+mc1.21.1.jar` | client | `addon`, `rendering`, `optimizer` | Create rendering path for Iris. |
| Colorwheel Patcher | `colorwheel_patcher-neoforge-1.0.5+mc1.21.1.jar` | client | `addon`, `rendering`, `optimizer` | Patcher Colorwheel needs. |
| ImmediatelyFast | `ImmediatelyFast-NeoForge-1.6.14+1.21.1.jar` | client | `core`, `rendering`, `optimizer` | Faster immediate-mode rendering. |
| Entity Culling Fabric/Forge | `entityculling-neoforge-1.11.2-mc1.21.1.jar` | client | `core`, `rendering`, `optimizer` | Skips entities you cannot see. |
| MoreCulling | `moreculling-neoforge-1.21.1-1.0.10.jar` | client | `addon`, `rendering`, `optimizer` | Extra block-face culling. |
| Flerovium | `flerovium-neoforge-1.21.1-1.1.3-all.jar` | client | `addon`, `rendering`, `optimizer` | Cheaper block-entity rendering. |
| BadOptimizations | `BadOptimizations-2.4.1-1.21.1.jar` | client | `addon`, `rendering`, `optimizer` | Skips client work that does not change. |
| AsyncParticles | `AsyncParticles-21.1.4.4+1.21.1.jar` | client | `addon`, `rendering`, `optimizer` | Particle rendering off the main thread. |
| GeckolibBetterFPS | `gbf-1.21.1-1.0.2.jar` | client | `library`, `rendering`, `optimizer` | Cheaper GeckoLib animations. |

## Entity models

| Mod | File | Side | Tags | What it adds |
|---|---|---|---|---|
| [EMF] Entity Model Features [Fabric & Forge] | `entity_model_features-3.3.9-1.21-neoforge.jar` | client | `core`, `rendering` | Custom entity models. Some mobs stay on vanilla models while Epic Fight is in. |
| [ETF] Entity Texture Features - [Fabric & Forge] | `entity_texture_features-7.2.4-1.21-neoforge.jar` | client | `core`, `rendering` | Custom entity textures. EMF needs this. |
| EMF Compat: Core | `emf_compat_core_1.21.1_2.0.0.jar` | client | `library`, `compat`, `rendering` | EMF compat library. |
| Fresh Animations | `FreshAnimations_v1.10.4.zip` | client | `core`, `resource-pack`, `rendering` | Resource pack. Fresh Animations. |
| Fresh Animations: Extensions | `FA+All_Extensions-v1.8.1.zip` | client | `resource-pack`, `rendering` | Resource pack. Fresh Animations extensions. |
| Darkest Ages Mobs | `Darkest_Ages_Mobs-1.21.1_1.2.1.zip` | client | `resource-pack`, `rendering` | Resource pack. Darkest Ages mobs. |
| Darkest Ages Mobs + Fresh Animations | `Darkest_Ages_Mobs+FA-1.21.1_1.2.1.zip` | client | `resource-pack`, `rendering` | Resource pack. Darkest Ages plus Fresh Animations. |
| Boss Refreshed | `boss-refreshed-v2-1.19-1.21.zip` | client | `resource-pack`, `rendering` | Resource pack. Dragon, wither, warden, and elder guardian models. |
