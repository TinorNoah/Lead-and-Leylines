# Config notes (necessary only)

Defaults are the pack unless a row below says otherwise. Do not dump every mod’s full config into git.

Shaders are a pack feature. Oculus is the loader. Ten Iris packs ship in `pack/shaderpacks/` for in-game testing; **none is enabled by default**. Dynamic lights mods stay out. Create + Oculus uses Colorwheel (beta), not iris-flw-compat.

| Mod | Touch? | Note |
|---|---|---|
| Embeddium + Oculus | Version pair only | Keep the Forge 1.20.1 files that match each other. Do not mix random Embeddium/Oculus builds. No extra dynamic-lights mod. Shader list is `pack/shaderpacks/*.pw.toml`. Do not ship an Oculus default-pack option until one pack is chosen. |
| Embeddium Extra | Only if a leaf or DL mod is added later | Turn off Extra’s leaf culling / dynamic lights so they do not stack. With Oculus in, leave Extra lights off. |
| Let Me Despawn | Gameplay | Equipped-mob despawn. After first launch, if raid/named mobs vanish unexpectedly, tighten the equipment whitelist. Do not change until that happens. |
| ImmediatelyFast | Later HUD mods only | If Legendary Tooltips / Equipment Compare / Simply Tooltips / AppleSkin glitch, disable `hud_batching`. Otherwise leave default. |
| ModernFix | No | Mixin defaults stay. Change only if a crash log names a mixin. |
| ServerCore | N/A until added | Activation range is gameplay; do not add silently. |
| FTB Chunks | Pack override | Xaero is the map UI. Ship `pack/defaultconfigs/ftbchunks/client-config.snbt` (`minimap.enabled: false`) and `pack/defaultconfigs/ftbchunks/ftbchunks-world.snbt` (`force_disable_minimap: true`). FTB also auto-disables its minimap when `xaerominimap` is loaded. Existing worlds already have `world/serverconfig/ftbchunks-world.snbt` — set `force_disable_minimap: true` there, or delete that file so the default is copied on next start. |
| FTB Essentials `/rtp` | Pack override | `/rtp` calls `getChunk` on the server thread. Ship `pack/defaultconfigs/ftbessentials-server.snbt`: `max_distance` 2000 (default 25000), `max_tries` 3 (default 100), blacklist End / Nether / Aquamirae Maelstrom. Existing worlds already have `world/serverconfig/ftbessentials.snbt` — copy those rtp keys there, or delete that file so the default is copied on next start. Do not use `/rtp` as a substitute for Chunky pregen. |
| Dedicated `server.properties` | Dedicated only | `max-tick-time=600000` (vanilla 60000). Heavy first-chunk gen can still exceed 60s. Not a packwiz file — set on the dedicated world. Do not set `-1` unless a true hang is confirmed. |
| Epic Structures: Dungeons | Removed | No 1.20.1-safe file: 1.0 (`fMMms6dF`) uses uppercase loot IDs that abort chunk gen; 1.1+ tagged 1.20 still bake 1.21 `components` on item frames. Villages / witch huts / jungle temples stay. Do not pin 1.2.5 (`tcsK0UPh`) or other unified jars. |
| FTB Chunks large map key | Pack default | `key.ftbchunks.map` defaults to **M**, same as Xaero World Map. Ship `pack/config/defaultoptions/keybindings.txt` (unbind Open Map). New installs get that default. Existing instances that already saved **M** keep it — unbind once in Controls → FTB Chunks → **Open Map**. Claim manager stays unbound. The FTB sidebar still opens claim/map screens on purpose. Leave Xaero World Map on **M**. |
| Epic Fight battle/mining | Pack default | Defaults to **R**, same as TACZ reload. Same `keybindings.txt` sets `key.epicfight.switch_mode` to **V**. Existing instances that already saved **R** keep it — rebind once in Controls → Epic Fight → **Toggle Battle/Mining Mode**. |
| Oculus Reload Shaders | Pack default | Defaults to **R**, same as TACZ reload. Same `keybindings.txt` unbinds `iris.keybind.reload`. New installs get that default. Existing instances that already saved **R** keep it — unbind once in Controls → Oculus → **Reload Shaders**. |
| Java 17 JVM flags | Pack overlay | `pack/user_jvm_args.txt` (`-XX:+UseZGC`). `python scripts/update_prism.py` copies those flags into Prism `instance.cfg`. Mrpack/CurseForge cannot auto-apply launcher JVM args — ATLauncher/store installs paste the same flags. Do not add `-XX:+ZGenerational` (Java 21+). |
| Crash Assistant | Pack override | Client only. `pack/config/crash_assistant/config.toml`: `help_link` is the Lead and Leylines Discord invite, `modpack_name` / `support_name` / `support_place` match the pack, piracy notice on. Change `#support` in that file if the Discord channel is named something else. |
| Colorwheel | Version pair only | Beta. Pair with Colorwheel Patcher. Do not add Iris/Oculus Flywheel Compat. |
| Euphoria Patches | Shader extra | Client. Matches Complementary Reimagined/Unbound `r5.9.3`. Options off until a Complementary pack is enabled. |
| Create | World data | Back up existing worlds before first boot. Contraptions and kinetic blocks stay in the save if Create is removed. |
| Sophisticated Backpacks | Keybind | Open defaults to **B**. Forge stores binds in `options.txt`; do not ship that file. Unbind in Controls if it fights something later. |
| Functional Storage / Sophisticated Storage | World data | Drawer and chest blocks stay in the save if those mods are removed. |
| Amplified Nether / BetterNether / Bygone / Infernal Redux / YUNG fortresses / MMR / Stalwart / Awesome Dungeon | Worldgen | Existing chunks stay old-gen. New world. Do not add Incendium. Do not add YUNG Better Mineshafts. |
| Infernal Expansion Redux | Optional lights | Leave LambDynamicLights out; Oculus is the light path. Cloth Config is shipped for the GUI. |
| Farmer's Delight / My Nether's Delight | World data | Crops, blocks, and kitchen pieces stay in the save if removed. Keep MND `1.10.4-backport.1` with Farmer's Delight 1.3.x. |
| Terralith / RU / BWG / YUNG caves / structures | Worldgen | New world. Do not add Expanded Ecosphere or Lithosphere. Do not re-add StructureOverlapless or Tectonic 3. |
| TerraBlender | Pack override | `pack/config/terrablender.toml`: `overworld_region_size` 6, `nether_region_size` 4. |
| Sparse Structures | Pack override | `pack/config/sparsestructures.json5`: `spreadFactor` 1, `idBasedSalt` true. |
| Structurify | Pack override | `pack/config/structurify.json`: global spacing modifier **off**. |
| Create: Sky Village | Pack override | `pack/config/create_sky_village-common.toml`: spacing 32 / separation 16, height offset 64. `/locate` still uses ground Y. |
| Nullscape | End worldgen | Forge jar `1.2.8`. New End chunks. Does not change Overworld/Nether. Do not add Incendium. |
| YUNG's Bridges | Baked rate | 4.0.3 uses `rarity_filter` chance `3` in the jar. Terralith can make bridges rarer. No pack toml to raise that. |
| Chunky | Pregen | Writes chunks. Run a radius on purpose; do not leave a huge job unattended. Pregen around spawn before relying on `/rtp`. |
| Countered's Terrain Slabs | Beta | Defaults. |
| IceAndFire Community Edition | Worldgen + entities | Defaults. Tune spawn/structure rates in the Jupiter GUI if TPS drops. Do not also install original Ice and Fire. |
| TACZ / Simply Swords / Ars Elemental / Amendments / Trash Cans | World data | Defaults. Guns, weapons, elemental blocks, lanterns, and trash cans stay in the save if removed. |
| Epic Fight / ParCool | Combat | Melee is Epic Fight, not Better Combat. Official Epic × ParCool needs ParCool 3.4.3.3, not 4.0. Epic Fight stays 20.14.17. |
| Dyenamics and Friends | Extra dyes | Pin 1.9.3 with Connected Glass 1.1.14. 1.6.0 still registers `CGPaneBakedModel`, which Fusion-era Connected Glass removed. |
| Mekanism / Alchemistry | World data | Ores, machines, and chem blocks stay in the save if removed. Almost Unified writes `unify.json` on first launch. |
| ATO - All the Ores | Worldgen | Extra ores on top of Mekanism. New chunks. After first launch, tune `config/alltheores-common.toml` if veins overlap Mek/Terralith too hard. |
| Mekanism: More Machine | World data | Beta extra factories. Blocks stay in the save if removed. |
| Better Compatibility Checker | Join check | Last 1.20.1 file Sep 2023. Mismatched client/server mod lists fail to join. Do not leave a lone extra jar in Prism. |
| AE2 kits + Refined Storage | Dual network | Extended AE, AdvancedAE, Applied Flux, MEGA, and AE Additions are stacked on purpose. RS is a second network. AE2 Things `1.2.1` is Jun 2023 vs AE2 15.4.10. |
| The Lost Cities | Worldgen | New chunks. Existing land stays empty of cities. |

FerriteCore, FastWorkbench, FastFurnace, FastSuite, BadOptimizations, Radium, AllTheLeaks, Entity Culling, Dynamic FPS, Clumps, Noisium, Smooth Chunk Save, Cupboard, Neruina, EMI, TMRV, Jade, FTB Library/Teams/Quests/Ultimine/Essentials/XMod/Filter System, Architectury, Kotlin for Forge, Create Ultimine, Accelerated Decay, Xaero, Titanium, Sophisticated Core, Curios, the Sophisticated Create integrations, Cloth Config, GeckoLib, YUNG's API, BCLib, WunderLib, Library Ferret, Moog's Structure Lib, YACL, CorgiLib, Citadel, Fragmentum, Ars Nouveau, Patchouli, AE2, GuideME, Twilight Forest, Supplementaries, Moonlight, Waystones, Lootr, MmmMmmMmmMmm, Polymorph, Crafting Tweaks, NetherPortalFix, TrashSlot, Balm, Controlling, Searchables, Mouse Tweaks, Better Advancements, FancyMenu, Drippy, Konkrete, Melody, Too Fast, Fzzy Config, Iceberg, Prism, Jupiter, Uranus, SuperMartijn642 Core/Config Lib, Epic Fight, ParCool, Official Epic × ParCool, Simply Swords, Simply More, Simply Tooltips, Legendary Tooltips, Equipment Compare, TACZ and extra gun packs, IceAndFire CE, Ars Elemental, Amendments, Trash Cans, Mekanism, Almost Unified, Refined Storage, and the 2026-09-16 kitchen-sink QoL set: no extra pack overrides unless a row above says otherwise. Dynamic FPS can use Cloth Config's in-game screen. Do not add EMI Loot or JEI.
