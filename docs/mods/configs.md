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
| FTB Essentials `/rtp` | Pack override | `/rtp` calls `getChunk` on the server thread. Ship `pack/defaultconfigs/ftbessentials-server.snbt`: `max_distance` 2000 (default 25000), `max_tries` 3 (default 100), blacklist End / Nether / Aquamirae Maelstrom. Existing worlds already have `world/serverconfig/ftbessentials.snbt` — copy those rtp keys there, or delete that file so the default is copied on next start. Do not use `/rtp` as a substitute for Chunky pregen. |
| Dedicated `server.properties` | Dedicated only | `max-tick-time=600000` (vanilla 60000). One Tectonic + Streams chunk can exceed 60s; the watchdog then kills the process. Not a packwiz file — set on the dedicated world. Do not set `-1` unless a true hang is confirmed. |
| FTB Chunks large map key | Pack default | `key.ftbchunks.map` defaults to **M**, same as Xaero World Map. Ship `pack/config/defaultoptions/keybindings.txt` (unbind Open Map). New installs get that default. Existing instances that already saved **M** keep it — unbind once in Controls → FTB Chunks → **Open Map**. Claim manager stays unbound. The FTB sidebar still opens claim/map screens on purpose. Leave Xaero World Map on **M**. |
| Distant Horizons | Pack override | Client only. `pack/config/DistantHorizons.toml`: `rendererMode = "DISABLED"`, `enableDistantGeneration = false`. Floor quality if the player turns it on in Options → DH. Auto-updater off. Do not put DH on the dedicated server. |
| Crash Assistant | Pack override | Client only. `pack/config/crash_assistant/config.toml`: `help_link` is the Lead and Leylines Discord invite, `modpack_name` / `support_name` / `support_place` match the pack, piracy notice on. Change `#support` in that file if the Discord channel is named something else. |
| Colorwheel | Version pair only | Beta. Pair with Colorwheel Patcher. Do not add Iris/Oculus Flywheel Compat. |
| Create | World data | Back up existing worlds before first boot. Contraptions and kinetic blocks stay in the save if Create is removed. |
| Sophisticated Backpacks | Keybind | Open defaults to **B**. Forge stores binds in `options.txt`; do not ship that file. Unbind in Controls if it fights something later. |
| Functional Storage / Sophisticated Storage | World data | Drawer and chest blocks stay in the save if those mods are removed. |
| Amplified Nether / BetterNether / Bygone / Infernal Redux / YUNG fortresses / MMR / Stalwart / Awesome Dungeon | Worldgen | Existing chunks stay old-gen. New world. Do not add Incendium. Do not add YUNG Better Mineshafts. |
| Infernal Expansion Redux | Optional lights | Leave LambDynamicLights out; Oculus is the light path. Cloth Config is shipped for the GUI. |
| Farmer's Delight / My Nether's Delight | World data | Crops, blocks, and kitchen pieces stay in the save if removed. Keep MND `1.10.4-backport.1` with Farmer's Delight 1.3.x. |
| Terralith / RU / BWG / Tectonic / YUNG caves / structures | Worldgen | New world. Do not add Expanded Ecosphere or Lithosphere. Do not re-add StructureOverlapless. |
| Tectonic | Pack override | `pack/config/tectonic.json`: Continents Scale `0.11`, Ocean Offset `-0.92`, temperature/vegetation scale `0.125` (larger biomes). Do not raise Ocean Offset toward `0`. |
| TerraBlender | Pack override | `pack/config/terrablender.toml`: `overworld_region_size` 6, `nether_region_size` 4. |
| Sparse Structures | Pack override | `pack/config/sparsestructures.json5`: `spreadFactor` 1, `idBasedSalt` true. |
| Structurify | Pack override | `pack/config/structurify.json`: global spacing modifier **off**. |
| Create: Sky Village | Pack override | `pack/config/create_sky_village-common.toml`: spacing 32 / separation 16, height offset 64. `/locate` still uses ground Y. |
| YUNG's Bridges | Baked rate | 4.0.3 uses `rarity_filter` chance `3` in the jar. Tectonic/Terralith make bridges rarer. No pack toml to raise that. |
| Chunky | Pregen | Writes chunks. Run a radius on purpose; do not leave a huge job unattended. Pregen around spawn before relying on `/rtp`. |
| Countered's Terrain Slabs | Beta | Defaults. |

FerriteCore, FastWorkbench, FastFurnace, FastSuite, BadOptimizations, Radium, AllTheLeaks, Entity Culling, Dynamic FPS, Clumps, Noisium, Smooth Chunk Save, Cupboard, Neruina, EMI, TMRV, Jade, FTB Library/Teams/Quests/Ultimine/Essentials/XMod/Filter System, Architectury, Kotlin for Forge, Create Ultimine, Accelerated Decay, Xaero, Titanium, Sophisticated Core, Curios, the Sophisticated Create integrations, Cloth Config, GeckoLib, YUNG's API, BCLib, WunderLib, Library Ferret, Moog's Structure Lib, YACL, CorgiLib, Citadel, Fragmentum, Ars Nouveau, Patchouli, AE2, GuideME, Twilight Forest, Supplementaries, Moonlight, Waystones, Lootr, MmmMmmMmmMmm, Polymorph, Crafting Tweaks, NetherPortalFix, TrashSlot, Balm, Controlling, Searchables, Mouse Tweaks, Better Advancements, FancyMenu, Drippy, Konkrete, Melody, and Too Fast: no extra pack overrides. Dynamic FPS can use Cloth Config's in-game screen. Do not add EMI Loot or JEI.
