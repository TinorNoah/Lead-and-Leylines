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
| FTB Chunks | Pack override | Xaero is the map UI. Ship `pack/defaultconfigs/ftbchunks/client-config.snbt` (`minimap.enabled: false`) and `pack/defaultconfigs/ftbchunks/ftbchunks-world.snbt` (`force_disable_minimap: true`). FTB also auto-disables its minimap when `xaerominimap` is loaded. Existing worlds already have `world/serverconfig/ftbchunks-world.snbt` — set `force_disable_minimap: true` there, or delete that file so the default is copied on next start. |
| FTB Chunks large map key | Cannot pack | `key.ftbchunks.map` defaults to **M**, same as Xaero World Map. Forge stores binds in `options.txt`; shipping that file would overwrite player settings, and Default Options is not in the pack. In Controls → FTB Chunks → **Open Map**, unbind (None). Claim manager is already unbound. The FTB sidebar still opens the claim/map screens on purpose. Leave Xaero World Map on **M**. |
| Colorwheel | Version pair only | Beta. Pair with Colorwheel Patcher. Do not add Iris/Oculus Flywheel Compat. |
| Create | World data | Back up existing worlds before first boot. Contraptions and kinetic blocks stay in the save if Create is removed. |

FerriteCore, FastWorkbench, FastFurnace, FastSuite, BadOptimizations, Crash Assistant, Radium, AllTheLeaks, Entity Culling, Dynamic FPS, Clumps, Noisium, Smooth Chunk Save, Cupboard, Neruina, EMI, TMRV, Jade, FTB Library/Teams/Quests/Ultimine/Essentials/XMod/Filter System, Architectury, Kotlin for Forge, Create Ultimine, Accelerated Decay, and Xaero: no extra pack overrides. Cloth Config is not shipped; Dynamic FPS uses defaults without its optional config screen.
