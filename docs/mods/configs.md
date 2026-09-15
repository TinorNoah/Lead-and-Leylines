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
| Sophisticated Backpacks | Keybind | Open defaults to **B**. Forge stores binds in `options.txt`; do not ship that file. Unbind in Controls if it fights something later. |
| Functional Storage / Sophisticated Storage | World data | Drawer and chest blocks stay in the save if those mods are removed. |
| Amplified Nether / BetterNether / Bygone / Infernal Redux / YUNG fortresses / MMR / Stalwart / Awesome Dungeon | Worldgen | Existing chunks stay old-gen. New world. Do not add Incendium. Do not add YUNG Better Mineshafts. |
| Infernal Expansion Redux | Optional lights | Leave LambDynamicLights out; Oculus is the light path. Cloth Config is shipped for the GUI. |
| Farmer's Delight / My Nether's Delight | World data | Crops, blocks, and kitchen pieces stay in the save if removed. Keep MND `1.10.4-backport.1` with Farmer's Delight 1.3.x. |
| Terralith / RU / BWG / Tectonic / YUNG caves / structures | Worldgen | New world. Terralith biomes get smaller next to RU+BWG. Do not add Expanded Ecosphere or Lithosphere. |
| Tectonic | Spacing | After first launch, Mods → Tectonic: Continents Scale `0.11` (default `0.13`), Ocean Offset `-0.92` (default `-0.8`). Land stays large; more ocean between continents. Do not raise Ocean Offset toward `0`. |
| YUNG's Bridges | Baked rate | 4.0.3 uses `rarity_filter` chance `3` in the jar. Tectonic/Terralith make bridges rarer. No pack toml to raise that. |
| Chunky | Pregen | Writes chunks. Run a radius on purpose; do not leave a huge job unattended. |
| Countered's Terrain Slabs | Beta | Defaults. |

FerriteCore, FastWorkbench, FastFurnace, FastSuite, BadOptimizations, Crash Assistant, Radium, AllTheLeaks, Entity Culling, Dynamic FPS, Clumps, Noisium, Smooth Chunk Save, Cupboard, Neruina, EMI, TMRV, Jade, FTB Library/Teams/Quests/Ultimine/Essentials/XMod/Filter System, Architectury, Kotlin for Forge, Create Ultimine, Accelerated Decay, Xaero, Titanium, Sophisticated Core, Curios, the Sophisticated Create integrations, Cloth Config, GeckoLib, YUNG's API, BCLib, WunderLib, Library Ferret, Moog's Structure Lib, YACL, TerraBlender, CorgiLib, Citadel, Fragmentum, Sparse Structures, StructureOverlapless, and the WDA sparse compat packs: no extra pack overrides. Dynamic FPS can use Cloth Config's in-game screen.
