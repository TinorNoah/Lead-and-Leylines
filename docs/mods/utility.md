# Utility / QoL — considered, chosen, dropped

Target is whatever Minecraft + NeoForge are in [`pack/pack.toml`](../../pack/pack.toml). Re-check store pages before a file bump.

**Status:** Jade + JEI, maps/compasses, FTB extras, advancement/tooltip QoL. Remaining 1.20.1 leftovers: [deferred.md](deferred.md).

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. |
| `both` | Must run in singleplayer and on the dedicated server. |

## Chosen

| Mod | Pinned file | `side` | Why |
|---|---|---|---|
| Jade | `Jade-1.21.1-NeoForge-15.10.6.jar` | both | Block/entity tooltip. WTHIT not added. |
| Jade Addons (Neo/Forge) | `JadeAddons-1.21.1-NeoForge-6.1.1.jar` | both | Extra Jade integrations (Create, etc.). ARR. |
| Just Enough Items (JEI) | `jei-1.21.1-neoforge-19.57.0.447.jar` | both | Recipe viewer. Replaces EMI + TMRV. File 19.57 satisfies Polymorph and Sophisticated. Server side is what lets Move Items fill a crafting grid. |
| MezzConfig | `mezz_config-1.21.1-neoforge-0.6.3.jar` | both | Required by current JEI on both sides. |
| AE2 JEI Integration | `ae2jeiintegration-1.2.1.jar` | client | Extra AE2 JEI pages. |
| Refined Storage - JEI Integration | `refinedstorage-jei-integration-neoforge-1.0.0.jar` | client | RS recipe transfer. Pinned 1.0.0; 2.0.x is Minecraft 26.1.2. |
| JEIOptimizer | `jeioptimizer-1.21.1-1.2.0-19.56.jar` | client | Faster JEI ingredient filter on world join. ARR. |
| Sophisticated JEI Index | `sophisticated_jei_index-1.2.3+1.21.1.jar` | client | Backpack recipe transfer. |
| Smithing Template Viewer | `smithingtemplateviewer-1.0.4.jar` | client | Armor trim preview in JEI. 1.1.0 is 26.1.2-only. |
| Create JEI Compat | `createjeicompat-1.0.3.jar` | client | Paginated sequenced-assembly recipes with 7+ steps. |
| JEI Stuff | `jeistuff-1.21.1-1.2.1.jar` | both | Extra JEI helpers. Required network channel. |
| JEI QuickCraft | `jei-quickcraft-1.21.1-neoforge-1.0.jar` | both | Craft from JEI using inventory. ARR. Required network channel. |
| SpectrumJEI | `SpectrumJEI-21.1.11.1+neoforge.jar` | client | Spectrum recipe pages in JEI. |
| FTB JEI Extras | `ftb-jei-extras-21.1.7.jar` | client | FTB quest/filter pages in JEI. |
| MekaGenJei | `mekagenjei-1.2.jar` | client | Mekanism Generators JEI pages. |
| Just Enough Mekanism Multiblocks | `JustEnoughMekanismMultiblocks-1.21.1-7.21.jar` | client | Multiblock overlays in JEI. |
| Mekanism: Ponders | `mekanism_ponders-1.0.3-1.21.1.jar` | client | Create ponder scenes for Mekanism. |
| Just Enough TaCZ | `just_enough_tacz-1.2.0.jar` | client | TaCZ recipes in JEI. Berezka's library required. |
| Just Enough Resources (JER) | `JustEnoughResources-NeoForge-1.21.1-1.6.0.17.jar` | client | Ore gen and mob drops in JEI. Pinned 1.21.1 NeoForge; later files are Fabric 26.x. |
| Patchouli | `Patchouli-1.21.1-93-NEOFORGE.jar` | both | Guidebooks. Required by Mekanism Elements. |
| MekaJadeUpgrades | `mekajadeupgrade-1.3.jar` | both | Mekanism upgrade info on Jade. |
| TACZ / Jade Compatibility | `tacz-jade-1.21.1-neoforge-1.0.0.jar` | client | Gun info on Jade. |
| Spice of Life: Carrot Edition | `solcarrot-1.21.1-1.16.6.jar` | both | Food diversity. |
| JEI / REI / EMI WorldGen | `jeiworldgen-neoforge-1.21.1-1.4.5.jar` | both | Worldgen recipe pages in JEI. Server jar supplies the data when you join. |
| DarkSleep - RPG Sleep Percentage | `darksleep-neoforge-1.21.1-1.0.1.jar` | both | Sets `playersSleepingPercentage` to 50 on world load. ARR. |
| Xaero's Minimap | `xaerominimap-neoforge-1.21.1-26.5.0.jar` | client | Minimap. |
| Xaero's World Map | `xaeroworldmap-neoforge-1.21.1-1.46.0.jar` | client | Full world map. |
| Icon Xaero's | `Icon Xaero's 1.22.zip` | client | Map icons for Xaero's. CurseForge metadata. Force-enabled by Global Packs. |
| Enhanced Boss Bars | `[1.6] Enhanced Boss Bars.zip` | client | Boss bar textures. Resource pack format 34. Force-enabled by Global Packs. |
| Fresh Animations | `FreshAnimations_v1.10.4.zip` | client | Animated mobs. EMF + ETF. Beta 1.10.4. Force-enabled by Global Packs. |
| Fresh Animations: Extensions | `FA+All_Extensions-v1.8.1.zip` | client | Official Fresh Animations extension bundle. Force-enabled above the base pack. |
| Darkest Ages Mobs | `Darkest_Ages_Mobs-1.21.1_1.2.1.zip` | client | Medieval mob look. EMF + ETF. Force-enabled by Global Packs. |
| Darkest Ages Mobs + Fresh Animations | `Darkest_Ages_Mobs+FA-1.21.1_1.2.1.zip` | client | Lets both mob packs apply together. Force-enabled last among the mob packs. |
| Nature's Compass | `NaturesCompass-1.21.1-3.4.0-neoforge.jar` | both | Locate biomes. |
| Explorer's Compass | `ExplorersCompass-1.21.1-3.4.0-neoforge.jar` | both | Locate structures. |
| Waystones | `waystones-neoforge-1.21.1-21.1.45.jar` | both | Teleport stones. World data. Balm. |
| AppleSkin | `appleskin-neoforge-mc1.21-3.0.9.jar` | both | Hunger/saturation HUD. |
| Mouse Tweaks | `MouseTweaks-neoforge-mc1.21-2.26.1.jar` | client | Inventory drag-transfer. |
| Crafting Tweaks | `craftingtweaks-neoforge-1.21.1-21.1.11.jar` | both | Crafting grid buttons. Balm. |
| Controlling | `Controlling-neoforge-1.21.1-19.0.5.jar` | client | Keybind search. Searchables. |
| Harvest with ease | `harvest-with-ease-neoforge-1.21-9.4.0.jar` | both | Right-click harvest. Cobweb. |
| Clean Swing Through Grass | `cleanswing-1.10-1.21.jar` | both | Swing through plants. |
| Cosmetic Armor Reworked | `cosmeticarmorreworked-1.21.1-v1-neoforge.jar` | both | Cosmetic armor slots. |
| Elytra Slot | `elytraslot-neoforge-9.0.2+1.21.1.jar` | both | Elytra in Curios. Caelus. |
| Durability Tooltip | `durabilitytooltip-1.2.0-neoforge-mc1.21.jar` | client | Durability numbers. |
| Equipment Compare | `EquipmentCompare-1.21.1-neoforge-1.3.13.jar` | client | Shift-compare gear. Iceberg. Tooltip Overhaul's own compare key is unbound so the two do not stack. |
| Item Borders | `ItemBorders-1.21-neoforge-1.2.5.jar` | client | Rarity item borders. Iceberg + Prism. |
| Tooltip Overhaul | `tooltipoverhaul-neoforge-1.21.1-2.0.2.jar` | client | Only item-tooltip skin. Frames by type, then mod namespace, then rarity. GPL-3.0-only; CurseForge metadata. |
| Tag Tooltips | `tagtooltips-neoforge-1.21.1-1.2.0.jar` | client | Hold semicolon to list tags inside the Tooltip Overhaul frame. CC-BY-SA-4.0; modpack use allowed. |
| Colorful Hearts | `colorfulhearts-neoforge-1.21.1-10.5.9.jar` | client | Colored heart rows. |
| Better Advancements | `BetterAdvancements-NeoForge-1.21.1-0.4.3.21.jar` | client | Advancement GUI. |
| Clickable advancements | `clickadv-1.21-3.8.jar` | both | Click toast to open advancement. |
| Toast Control | `ToastControl-1.21.1-9.0.1.jar` | client | Toast spam filter. Placebo. |
| Default Options | `defaultoptions-neoforge-1.21.1-21.1.8.jar` | client | Pack default options. Balm. |
| Login Protection | `logprot-1.21.1-3.6.jar` | both | Invulnerability after join. |
| Packet Fixer | `packetfixer-3.3.1-1.20.5-1.21.X-merged.jar` | both | Larger network packets. Not Disconnect Packet Fix. |
| Too Fast | `toofast-1.21.0-0.4.3.6.jar` | both | Movement packet speed (singleplayer too). |
| Accelerated Decay | `accelerated-decay-neoforge-21.0.0.jar` | both | Faster leaf decay. |
| WITS | `wits-neoforge-1.3.1.jar` | both | Structure name overlay. |
| Lootr | `lootr-neoforge-1.21.1-1.11.38.126.jar` | both | Per-player loot chests. World data. |
| Polymorph | `polymorph-neoforge-1.2.0+1.21.1.jar` | both | Duplicate recipe picker. |
| Almost Unified | `almostunified-neoforge-1.21.1-1.4.2.jar` | both | Ore unification. |
| TrashSlot | `trashslot-neoforge-1.21.1-21.1.11.jar` | both | Inventory trash slot. Balm. |
| FTB Chunks | `ftb-chunks-neoforge-2101.1.22.jar` | both | Chunk claims. World data. ARR. |
| FTB Essentials | `ftb-essentials-neoforge-2101.1.10.jar` | both | `/home` and related commands. ARR. |
| FTB Ultimine | `ftb-ultimine-neoforge-2101.1.15.jar` | both | Vein mine. ARR. |
| FTB Filter System | `ftb-filter-system-neoforge-21.1.4.jar` | both | Item filters. ARR. |
| FTB XMod Compat | `ftb-xmod-compat-neoforge-21.1.12.jar` | both | FTB cross-mod hooks. ARR. |
| NeoAuth | `NeoAuth-1.21.1-1.0.1.jar` | client | Microsoft auth helper. |
| Better Compatibility Checker | `better-compatability-checker-neoforge-21.1.8.jar` | both | Join-time modlist check. |
| Crash Utilities | `crashutilities-9.0.4.jar` | both | Extra crash helpers. |
| ETF | `entity_texture_features-7.2.4-1.21-neoforge.jar` | client | Entity texture variants. |
| EMF | `entity_model_features-3.3.9-1.21-neoforge.jar` | client | Entity model variants. |
| Athena | `athena-neoforge-1.21.1-4.0.6.jar` | both | Connected textures. Chipped. |
| Enchantment Descriptions | `enchdesc-neoforge-1.21.1-21.1.11.jar` | client | Enchantment tooltip lines. Bookshelf + Prickle. Apothic inlined descriptions are on. |
| Beautiful Enchanted Books | `BEB-NeoForge-1.21-6.0.0.jar` | client | Enchanted book textures. |
| Enchant Icons | `enchant icons 1.21 v1.3.zip` | client | Resource pack. Enchantment name icons. Global Packs required. |
| Loot Journal (NeoForge) | `loot_journal-neoforge-1.21.1-6.2.2.jar` | client | Pickup notifier. Fragmentum. |
| BetterF3 | `BetterF3-11.0.3-NeoForge-1.21.1.jar` | client | Debug HUD. Cloth Config. |
| Colourful Everywhere | `colourfuleverywhere-1.21-1.3.6.jar` | client | Shader GUI recolor. NeoForge stand-in for Colourful Containers + OptiGUI. |
| Fast Item Frames | `FastItemFrames-v21.1.6-1.21.1-NeoForge.jar` | both | Faster item frames. World data. Puzzles Lib. |
| Visual Workbench | `VisualWorkbench-v21.1.2-1.21.1-NeoForge.jar` | both | Items stay in crafting tables. World data. Puzzles Lib. FastWorkbench 9.1.3 stays; the crafting-menu crash was fixed in Visual Workbench 21.0.2. |
| Better Modlist | `better_modlist-21.1.1.jar` | client | Mods screen. |
| Bridging Mod | `BridgingMod-2.6.2+1.21.1.neoforge-release.jar` | client | Bridge assist. YACL. |
| Client Tweaks | `clienttweaks-neoforge-1.21.1-21.1.15.jar` | both | Client annoyance toggles. Required on the server. ARR. Balm. |
| AttributeFix | `attributefix-neoforge-1.21.1-21.1.3.jar` | both | Attribute id fixes. Bookshelf + Prickle. |
| Akashic Tome | `AkashicTome-1.8-30.jar` | both | Holds other guide books. |
| CreativeCore | `CreativeCore_NEOFORGE_v2.13.48_mc1.21.1.jar` | both | Required by AmbientSounds. |
| AmbientSounds 6 | `AmbientSounds_NEOFORGE_v6.3.8_mc1.21.1.jar` | both | Ambient audio. |
| Create - Xaero's map | `sablexaeromaps-1.21.1-1.4.0.jar` | client | Aeronautics contraptions on Xaero's maps. |
| Bad Wither No Cookie - Reloaded | `bwncr-neoforge-1.21.1-3.20.4.jar` | client | Mutes wither/dragon/raid music. |
| SeasonHud | `seasonhud-neoforge-1.21.1-2.0.10.jar` | client | Season text on the HUD / Xaero map. Works with Ecliptic Seasons. |

## Considered / held / dropped

| Mod | Status | Why |
|---|---|---|
| EMI / EMI Ores / EMI Enchanting / EMI QoL Tweaks | Dropped | Replaced by JEI so Create and Sophisticated plugins get a real JEI version. |
| Continuity | Held | Needs Connector and Forgified Fabric API, and it targets Sodium 0.6. Fusion is the connected-texture mod. |
| TooManyRecipeViewers | Dropped | Incompatible with real JEI; its stub reported JEI 19.27.0.343. |
| JEI | Chosen | Installed as `238222` / `8946440` (`jei-1.21.1-neoforge-19.57.0.447.jar`). |
| JEI++ (JEI Plus) | Dropped | Latest file `1.0.5` (`1645653` / `8870206`, 2026-09-13) targets JEI 19.56. On JEI 19.57, `jei_plus_plus.mixins.json:BookmarkOverlayMixin` crashes looking for `mezz.jei.gui.input.IUserInputHandler` (moved to `mezz.jei.common.input`). Do not re-add until a build for JEI 19.57 exists. |
| WTHIT | Dropped | Overlaps Jade. |
| Inventory Management Deluxe | Dropped | Fabric-only; no 1.21.1 NeoForge file. |
| No trampling on farmland | Held | Last CurseForge file is 1.20.1. |
| Fresh Moves / Fresh Animations: Player Extension | Held | Both replace the player model. Epic Fight already owns player combat animation. |
| The Rename Compat Project | Dropped | Latest zip is resource pack format 42 (1.21.2). 1.21.1 only accepts format 34 unless the pack declares a range that includes 34. |
| Legendary Tooltips, Simply Tooltips, Better Advanced Tooltips | Dropped | Tooltip Overhaul is the only item-tooltip skin. Fzzy Config left with Simply Tooltips. Kotlin for Forge stays; AE Additions, Better P2P, and Create Ultimine still need it. Tag Tooltips shows tags while its key is held. |
