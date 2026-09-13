# Config notes (necessary only)

Defaults are the pack unless a row below says otherwise. Do not dump every mod’s full config into git.

Shaders are a pack feature. Players drop shader packs into the Oculus/Iris shader folder; this repo does not ship a default pack until one is chosen on purpose.

| Mod | Touch? | Note |
|---|---|---|
| Embeddium + Oculus | Version pair only | Keep the Forge 1.20.1 files that match each other. Do not mix random Embeddium/Oculus builds. No extra dynamic-lights mod. |
| Embeddium Extra | Only if a leaf or DL mod is added later | Turn off Extra’s leaf culling / dynamic lights so they do not stack. With Oculus in, leave Extra lights off. |
| Let Me Despawn | Gameplay | Equipped-mob despawn. After first launch, if raid/named mobs vanish unexpectedly, tighten the equipment whitelist. Do not change until that happens. |
| ImmediatelyFast | Later HUD mods only | If tooltips/HUD glitch, disable `hud_batching`. Otherwise leave default. |
| ModernFix | No | Mixin defaults stay. Change only if a crash log names a mixin. |
| ServerCore | N/A until added | Activation range is gameplay; do not add silently. |

FerriteCore, FastWorkbench, FastFurnace, FastSuite, BadOptimizations, Crash Assistant, Radium, AllTheLeaks, Entity Culling, Dynamic FPS, Clumps, Noisium, Smooth Chunk Save, Cupboard, and Neruina: no pack overrides. Cloth Config is not shipped; Dynamic FPS uses defaults without its optional config screen.
