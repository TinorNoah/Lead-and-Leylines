# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Git tags are `vX.Y.Z`. Headers here are `## [X.Y.Z]` with no `v`.

Minecraft 1.20.1 Forge history lives on branch `forge-1.20.1` (tag `archive/forge-1.20.1`). Do not reuse tags `v0.0.1`–`v0.0.9`. The first 1.21.1 NeoForge GitHub/store ship is `v0.1.0`.

## [Unreleased]

### Added

### Changed

### Fixed

### Removed

## [0.1.26] - 2026-10-10

### Added

### Changed

- Switched the Java 21 garbage collector from ZGC to G1GC, using All the Mods 10's server tuning block. ZGC's extra native memory kept getting the dedicated server OOM-killed (exit 137) on tight boxes, and a return trip into fresh terrain chunk generation was enough to trigger it. Heap size rules are unchanged in the launcher; the dedicated server now reserves 2 GB below its container limit instead of 1.5 GB.

### Fixed

- Silenced the boot-time tag errors (`minecraft:rabbit_food`, `farmersdelight:pies`, `apothic_pointblank:gun/small_arms` and their `c:animal_foods` / `create:brittle` cascades, plus `blueprint:generates_overrides`) with pack tag snapshots that drop the unregistered entries, an empty stub for NetherExp's missing `soul_has_feature/ecto_soul_sand` biome tag, and a disabled stand-in for Tempad's missing loot-modifier file.
- Repaired three unloadable advancements (Dungeons Arise fishing hut / thornborn towers reparented to the mod root; Jaden's `big_brain_time` repointed at the real `brain_food`) and stubbed three missing registry tags (`netherexp:fossil_ore_convertible`, Forbidden Arcanus `soulbound_incompatible`, Iron's Jewelry `nether_findable`).

### Removed

## [0.1.25] - 2026-10-09

### Added

- Neapolitan, a food mod of flavored ice creams, milkshakes, and cakes, each flavor with its own effect, plus the strawberry fields biome and chimpanzees and plantain spiders that live in it.
- Twilight's Flavors & Delight now has all of its food. Aurora, glacier, phytochemical, and torchberry cake slices, and the ice creams and milkshakes built on them, were missing because that mod only creates them when Neapolitan is installed. They are craftable now, and the flavored cakes drop their slices again.

### Changed

- Shaders now have a fixed starting configuration instead of whatever your launcher happens to write on first run. They are still off until you turn them on, and you still pick which pack to use from the four included.
- The readme now says how much memory to give the game, and explains where that number comes from.
- Model and texture loading now happens off the main thread while the game starts, so entering the world is less likely to stutter on this pack's resource packs. Every other performance setting stays on its mod default; this only pins the ones that were already tuned, so a mod update can no longer quietly change them.

### Fixed

- Three of the seven broken tags behind the "some tags are a bit cooked" startup error are fixed. Twilight's Flavors & Delight was shipping recipes and tag entries for foods it only registers when Neapolitan is installed, so `farmersdelight:snacks`, `farmersdelight:sweets`, and `diet:sugars` never resolved. The warning still names four other tags, all upstream bugs in other mods, so the chat error can still appear on join until those are handled separately.
- Global Packs no longer loads the `resourcepacks/` folder as a data pack. Those are client resource pack zips, so the entry did nothing except make Global Packs re-resolve the whole client pack folder on every data sync.
- Dropped two dead `alexsmobs` entries from the Apotheosis bow loot-category overrides. Alex's Mobs is not in the pack, so each one logged a data-map ERROR on every boot.

### Removed

- Inventory Profiles Next, and its helper library. Slot sorting, locked slots and saved gear sets are gone from the inventory screen.
- Smooth Chunk Save. Timed against the rest of the save stack it made chunk saves slower rather than faster, and did nothing to reduce lag spikes, so it was costing a little performance for no benefit.
- Pattern Converter. Its Integrated Dynamics converter style pointed at `integrateddynamics` textures the pack does not have, which logged missing-texture warnings on every resource reload.
- Modern Industrialization Extended Integrations. It added MI-style hatches to Mekanism, PneumaticCraft and Create machines, but shipped 23 block loot tables for hatch items that Modern Industrialization does not register, so every boot logged a loot-table parse error and those hatch blocks dropped nothing when broken.

## [0.1.24] - 2026-10-03

### Added

- Oritech, a new tech tree with animated factory multiblocks, ore processing, item and fluid pipes, drones, nuclear reactors, and particle accelerators. It runs on the same Forge Energy as Mekanism and Modern Industrialization, so you can power it from generators you already have.
- Applied Oritech, so Oritech machines can sit on an ME network: an ME Dock, a pattern provider, and an interface for handing Oritech items to Applied Energistics.
- Oritech Things, the main Oritech addon: tiered Speed, Processing, Capacitor, and Acceptor addons that push machines further, plus particle-accelerator controls, a frame placer, and Amethyst Fish that swim out of infested geodes.
- Eighteen new Create recipes for working with Oritech materials: crushing hay, packed wheat, and other plant matter into biomass, crushing uranium crystals, splashing crushed nickel, platinum, and uranium, mixing the high-tier metals, and blasting or smelting crushed nickel and platinum straight into Oritech ingots.

### Changed

- Seven fewer mods to install and keep up to date. The Farmer's Delight cutting-board recipes for BetterNether, Twilight Forest, BetterEnd, Oh The Biomes We've Gone and Regions Unexplored, plus Create crushing recipes for Regions Unexplored, now ship inside the pack as ordinary data instead of as separate mods. All 567 recipes are unchanged, so nothing about crafting differs.
- Two more mods gone, same idea. Create's milling recipes for Oh The Biomes We've Gone blocks and for Sophisticated Backpacks upgrades are now part of the pack, so those two addons no longer need installing. All 143 recipes are unchanged. As a bonus this clears a packaging problem: CurseForge marks both projects as not available for automatic download, so a fresh install could previously have refused them.
- The sleep rule is now the pack's own. Half your players still need to be in bed to skip the night, exactly as before.

### Fixed

- Diamond armor is craftable again. Overgeared was overwriting 44 vanilla recipes with placeholder versions, and the ones for all nine pieces of diamond armor were failing to load entirely, which left them with no recipe at all.
- Gold, iron, and stone tools and armor, buckets, cauldrons, shears, flint and steel, and arrows all have their normal recipes again. Netherite ingots are unaffected either way, since Create: Alloyed supplies its own recipe for those.

### Removed

- Overgeared and its five addons, temporarily. This is the tool and armor forging overhaul, so tool and armor upgrading is back to the pack's other sources until it returns. Simply Swords and Ice and Fire stay; they only lose their Overgeared variants.

## [0.1.23] - 2026-10-01

### Added

- Just Enough Threads 0.14.2, which moves JEI's startup indexing off the main thread so joining a world stops freezing. The previous 0.14.1 build was pulled because it broke JEI entirely on JEI 19.57; 0.14.2 skips that mixin when the JEI constructor it targets is absent.
- Connectivity 7.7, which fixes login timeouts, oversized payloads, decoder errors, and ghostblocks.
- NeoForge 21.1.252 (was 21.1.250).
- Awesome Dungeon gets two more editions: ocean dungeons in the Overworld oceans, and a dungeon set in the End.
- Epic Structures: Dungeons and Igloo, joining the Villages, Jungle Temples, and Witch Huts already in the pack.
- Yggdrasils, a pack of very large Norse dungeon structures, with a Loot Integrations addon so those chests roll modded loot.
- Simply Swords 1.70.2 (katanas, spears, glaives, rapiers, and more), Simply More for extra weapon types, and Simply Swords Create Lines for Create production lines. Simply Swords needs Simply Tooltips from 1.63.0 onward, so that is installed too; it only draws its own tooltips over Simply Swords weapons and leaves every other item's tooltip to Tooltip Overhaul.
- Overgeared, which rebuilds tool and armor crafting around forging, and Overgeared JEI Compat so its items show up in the recipe viewer.
- Just Enough Professions (JEP): profession workstations and skills in JEI. Client-side.
- Steve's Carts (plus its PolyLib library) for customizable minecart automation, and Logistics Network for item, fluid, and energy routing.
- Applied Industrialization (AE2 blocks for Modern Industrialization), Industrialization Overdrive (extra MI machines), Modern Industrialization Extended Integrations (MI hatches that draw on Create stress), and AE2 Network Analyser for inspecting ME networks.
- Ars Polymorphia (Polymorph support for Ars storage lecterns) and Ars Unification (Ars Nouveau can craft from other mods' recipes).
- Creeper Overhaul, Enderman Overhaul, and AI Improvements for mob behaviour.
- Structure Essentials for faster structure locating and a nearby-structure command.
- In Control! for deciding what spawns where.
- Gravitational Modulating Additional Unit, extra Mekanism-side features.
- A batch of server/client fixes and optimizers: I'm Fast (stops movement desync kicks and log spam), Connectivity's neighbours Chunk Sending, Fast Async World Save and Structure Essentials, Leaky (cleans item piles and broken farms), Invasive Optimizations, Better Fps - Render Distance, and fix GPU memory leak.
- Macaw's Paths and Pavings, joining the other Macaw's decoration mods.
- Overgeared's companion addons: Overgearium (broad cross-mod compatibility), OvergearedXSimplySwords, Overgeared x Ice and Fire, and Overgeared: Universal Compatibility for per-metal tool heads.
- ATi Structures, an overworld structure pack, with a Loot Integrations addon for its chests. ATi also authors the Epic Structures mods already in the pack.
- Gateways to Eternity: giant portals, monster hordes, and large rewards.
- Loot Integrations addons for Awesome Dungeon, Born in Chaos, Ice and Fire, vanilla chests, and YUNG's structures, so those chests roll modded loot.
- Macaw's Lights and Lamps, and Macaw's Stairs (stairs, handrails, and balconies).
- FTB Ranks, so server ranks and permissions sit next to FTB Teams.
- Additional Lights (lantern, torch, and lamp variants) and FramedBlocks (picture frames for any block).
- Iris & Oculus Search, a search bar for Iris shader settings.
- Fuel Goes Here, so fuel goes to the fuel slot even when it is also smeltable.
- Get It Together, Drops! for merging dropped stacks, and Hey Berry! SHUT UP so villagers stop dying to berry bushes.
- Client comfort: KeyBind Bundles, KeybindsPurger, Borderless Window, and FlickerFix for night vision flicker.
- MmmMmmMmmMmm target dummies, so you can place one, equip it with armor, and read the damage numbers off it.
- More Overlays Updated: F7 shows a light-level and mob-spawn overlay, F9 draws chunk borders, and a double-click in the JEI search field greys out everything that does not match.
- Refined Storage - Curios Integration, so Refined Storage network items can be worn in Curios slots.
- No Chat Reports, so your chat cannot be reported to Mojang.

### Changed

- NeoForge moved from 21.1.250 to 21.1.252.
- Packet Fixer and Disconnect Packet Fix are gone: Connectivity covers the same oversized-packet and login-timeout problems, and all three patched the same networking internals.

### Fixed

### Removed

- Packet Fixer and Disconnect Packet Fix, replaced by Connectivity.

## [0.1.22] - 2026-09-30

### Added

- Sophisticated Storage 1.6.0: linked storage. Link barrels, chests, and shulker boxes with an Ender Linker to share one inventory across several blocks.
- Colorwheel 1.3.0 final, with a new `indirect` backend that skips geometry hidden behind other blocks. Create-heavy scenes can gain roughly 30% more FPS.

### Changed

- Updated 29 mods to their latest 1.21.1 NeoForge builds, including Applied Energistics 2, Ars Nouveau and Ars Elemental, Spectrum, the four Sophisticated mods, and Create: Metalwork 3.0.0.
- Apothic Attributes now caps Protection Shred at 90% instead of 100%.
- Applied Energistics 2 crafting CPUs list storage amounts more readably.

### Fixed

- Fixed an Applied Energistics 2 item duplication bug that could trigger when a large extract operation was split up.
- Fixed Sophisticated Backpacks losing their contents after a chunk reload, and rendering white after a chunk load.
- Fixed Ars Nouveau deleting waystones and iron doors with its Break spell instead of treating them as breakable.
- Fixed a crash when Moog's Structure Lib structures were wrapped by another mod such as Lithostitched.
- Fixed Infernal Expansion's Lashing, Leaping, Disarming, and Illuminating spells being unobtainable, and its Blindsight Tongue Whip wrongly accepting Sharpness and Looting.
- Fixed items in Spectrum's fluid-logged blocks not floating to the surface, and several Spectrum items being unobtainable outside DD biomes.
- Fixed non-stackable items stuck in Ars Nouveau lecterns when read through a repository.
- Fixed Moog's Structure Lib leaving floating lumps of ground above structures with deep tunnels.

### Removed

## [0.1.21] - 2026-09-30

### Changed

- JEI may take noticeably longer to finish loading its recipe list after entering a world, now that its startup work runs on the main thread again.

### Fixed

- Fixed a crash when searching Creative Search for Modern Industrialization and Extended Industrialization electric tools on a multiplayer server.
- Fixed the recipe viewer (JEI) failing to open. Just Enough Threads was patching a JEI search class whose constructor changed in JEI 19.57, which stopped JEI from starting at all.

### Removed

- Removed Just Enough Threads, which was breaking JEI. Its startup optimization can come back in a build that supports the current JEI.

## [0.1.20] - 2026-09-30

### Added

- A project-owned compatibility patch for the Weapons of Miracles × Modern Industrialization drill enchantment crash.

### Changed

- Updated Just Enough Items (JEI) to the latest compatible 1.21.1 NeoForge beta.

### Fixed

### Removed

- Create Aeronautics and its Sable physics library, plus every addon that existed only to teach another mod about them: Climbable Ropes, Curios API Compat, Mekanism Compatibility, the Sable Xaero's map overlay, Jade Sable Compat, TACZ, Point Blank, and Iron's Spells compat. Create trains and Create: Threaded Trains are unchanged. Existing vehicles in a world stay in the save and must be removed by hand.

## [0.1.19] - 2026-09-28

### Changed

- Login timeout increased from 30 s to 150 s (5×) via `-Dfml.loginTimeout=150 -Dfml.readTimeout=150` in `user_jvm_args.txt` — prevents "Timed Out" kicks during registry sync on join for players on slow connections or lower-end hardware.

## [0.1.18] - 2026-09-28

### Added

- Just Enough Threads: moves JEI's startup indexing off the main thread so joining a world is less likely to freeze.

### Fixed

### Removed

- JEIOptimizer: replaced by Just Enough Threads (same role; both mods target the same JEI routines).

## [0.1.17] - 2026-09-27

### Fixed

- Mod list site: search updates as you type, pages stop waiting on store APIs, and the card grid loads in chunks so browsing stays responsive.

### Removed

- Alex's Mobs Continued, Alex's Mobs: Tweaks, Alex's Mobs Continued Delight, and Codxlib. Old worlds may have leftover entity data from those creatures.

## [0.1.16] - 2026-09-27

### Fixed

- Cleared boot recipe and loot parse spam from soft-deps and broken bridges (empty orphan loot for Create Connected Dye Depot catalysts, Create Encased slicers, Ars Delight / Twilight Delight cake blocks, and related tables; disabled the matching bad recipes; fixed Agritech Evolved BWG pale pumpkin and Japanese orchid planter typos).
- Removed Apothic Category Compat (data map pointed at Alex's Caves / Cataclysm / Undergarden items we do not ship); kept the in-pack Apotheosis bow loot-category overrides in the load-fixes datapack.

## [0.1.15] - 2026-09-27

### Removed

- Legendary Monsters and Box of Structures: Legendary Monsters (bosses never registered default attributes on NeoForge, so arenas and summons were broken). Old worlds may keep missing LM blocks or structures.

## [0.1.14] - 2026-09-27

### Fixed

- Spawn Clams no longer try to natural-spawn (constructor crash with Spectrum and Forbidden Arcanus was spamming the server and contributing to join timeouts). Other Spawn mobs stay.

## [0.1.13] - 2026-09-27

### Changed

- Updated Archaion to 1.4.4 (Ancient Keep structure fixes) plus 32 other mods to their latest 1.21.1 NeoForge builds, including Ecliptic Seasons 0.15.2.1, JEI 19.57.0.449, Structurify 2.0.41, and Moonlight 3.7.0.

## [0.1.12] - 2026-09-27

### Removed

- Quark (and Zeta), plus Integrated Bosses of Mass Destruction, Integrated Mowzie's Mobs, Integrated API, and Integrated Patches. BOMD and Mowzie's base mods stay. Old worlds may keep missing Quark or Integrated structure pieces.
- Alex's Caves Continued (and its Delight cooking recipes and Iron's Spells cave spellbooks). Codxlib stays for Alex's Mobs Continued. Old cave chunks may keep missing blocks.

## [0.1.11] - 2026-09-26

### Removed

- JEI / REI / EMI WorldGen. Worldgen pages are gone from JEI; Just Enough Resources still covers mob and dungeon loot.
- Chunk Pregenerator (and Carbon Config). Operator pregen uses NeoForge `/neoforge generate` instead. Existing worlds keep their chunks.
- Neo Vitae blood magic (and its Applied Energistics blood automation addon). Existing Neo Vitae items or the demon dungeon in old worlds will not load cleanly.

## [0.1.10] - 2026-09-26

### Added

- Sort inventories, lock slots, save gear sets, and move items with more mouse gestures.
- Mute chosen sounds, add more sound effects, and hear reverb through blocks.
- More glass, a tape measure, laser mining gadgets, elevators, and one-click multiblock building.
- Programmable routers, including Mekanism parts and Modern Industrialization energy.
- Modern Industrialization and Just Dire Things, as extra automation beside Create and Mekanism.
- Request stock in Applied Energistics, and wear a portable QIO on a Curios slot.
- Iron's jewelry, more Ars Nouveau glyphs, and Neo Vitae blood magic.
- Compact redstone, and modded loot in When Dungeons Arise chests.
- The vanilla recipe book is gone. JEI stays.
- KubeJS can script recipes and loot. No scripts ship with this yet.
- Modern Dynamics pipes, XNet channels, and simple conveyor belts for logistics.
- Rechiseled (with Chipped, Create, and Applied Energistics bridges) beside Chipped.
- A large Create factory wave: Enchantment Industry, Central Kitchen, New Age, Big Cannons, TFMG, Alloyed, Diesel Generators, Ore Excavation, and related addons.
- Extended and Solar Industrialization, Flux Networks, DimStorage, Construction Sticks, Tempad, Mob Grinding Utils, Agritech, and BuffMobs.
- Inventory Essentials beside Inventory Profiles Next.
- Better Advanced Tooltips so the latest KubeJS can load.

### Changed

- KubeJS is on build 377 (needs Better Advanced Tooltips).

### Fixed

- Dropped Modern Industrialization Extentended Integrations: it crashes MI 2.5.8 looking for casing `modern_industrialization:iv`.

### Removed

- Pipez and Pipez Lag Fix. Use Modern Dynamics, XNet, and conveyors instead.

## [0.1.9] - 2026-09-26

### Added

- Chipped block variants, Handcrafted and Macaw's furniture, and Macaw's doors, windows, and fences.
- Glass connects, and many items use 3D models.
- Enchantment tooltips say what each enchantment does.
- Items stay visible on crafting tables.
- Twilight Forest boss respawns, villages, and dungeons.
- BetterEnd: New Dawn (with Farmer's Cutting), beside Nullscape and Unusual End.
- YUNG rebuilt dungeons, strongholds, desert temples, ocean monuments, and the End island; Luki's ancient cities and woodland mansions.
- Particle rain, subtle ambient effects, Colourful Everywhere GUI recolor, BetterF3, loot pickup toasts, prettier enchanted books, and enchantment icons.
- Cross-dimension Refined Storage wireless, Fast Item Frames, and DarkLoot mob loot (editable datapack).

### Changed

### Fixed

### Removed

- Gun lights and gun blueprints are gone from Timeless and Classics Zero.

## [0.1.8] - 2026-09-25

### Added

- The leyline emblem is the pack icon.

### Changed

### Fixed

- The loading screen no longer crashes while Armageddon models load.

### Removed

## [0.1.7] - 2026-09-25

### Added

- New mobs and bosses: a desert illager arena, Qliphoth Awakening, Bosses of Mass Destruction (including integrated structures), Spawn, Critters and Companions, Companions, Armageddon, and Born in Chaos.
- Alex's Mobs Continued, with tweaks and cooking recipes. Alex's Caves animals can be cooked too.
- Iron's Spells, with Twilight Forest spells, Create spell tools, Farmer's Delight spells, Alex's Caves spells, and teleport spells that still work on Aeronautics ships.
- Quark's small vanilla tweaks. Armageddon tools show their tier, and Jade names Born in Chaos infected diamond ore as diamond ore.
- Apotheosis affixes and gems, including enchanting, movable spawners, Iron's Spells gear, Point Blank and TaCZ guns, and Create machines. Flight potions and charms are off. Affix numbers can be changed in the balance config. Affix tooltips are shorter.
- More bosses and places: Mutant Monsters, Illager Invasion, Mowzie's Mobs, Myths & Legends, Legendary Monsters, an expanded End, Forbidden and Arcanus, and extra dungeons.
- Pam's HarvestCraft foods, crops, and fruit trees, beside Farmer's Delight.

### Changed

- The installed-mod browser uses a leyline restyle with clearer filters, card and list views, and a mod detail drawer.

### Fixed

### Removed

## [0.1.6] - 2026-09-24

### Added

- AE2 extras: crafting tree, schematic cannon link, mega disks, pattern-provider compat, infinite water/lava/cobblestone drives, machine pulling, an AE2/Refined Storage pattern converter, and one universal processor press.
- Create extras: electric motor and alternator, decoration blocks, encased parts, climbable Aeronautics ropes, aviator goggles in a Curios slot, and Aeronautics vehicles drawn on Xaero's maps.
- Ars extras: spell control, dual-element gear, Create glyphs and tools, Ars foods, and refreshed item textures.
- Crystalix colored glass, Artifacts curios, player graves, sleeping bags and hammocks, Building Gadgets, Autochef's Delight, and Barbeque's Delight.
- Ambient sounds, a book that holds other books, attribute fixes, bridge assist, a clearer mods screen, and client annoyance toggles.
- Backpack upgrade icons, and new models for the ender dragon, wither, warden, and elder guardian.

### Removed

- Vic's Point Blank Interaction. Holding a Point Blank gun no longer opens or uses the block or mob you are looking at.
- Structure Compass. Explorer's Compass still finds structures.

## [0.1.5] - 2026-09-24

### Fixed

- Vic's Point Blank Interaction no longer stops multiplayer from starting. Using blocks and mobs while holding a Point Blank gun still works.
- Point Blank no longer writes a log line for every normal block and mob interaction.
- Distant TaCZ gunshot echoes stay on. The per-shot debug trace is off.
- Bastion hoglin-stable and treasure chests include My Nether's Delight loot again.
- Terralith caves, gravel deserts, and savannas use Ecliptic Seasons' current rain tags.
- Ocelots in Regions Unexplored forests count as creatures, and sand snappers in Lost Caves count as monsters.
- Nether Expansion recipes for items that are not in this version no longer fail to load.

### Removed

- Call of Duty Warzone guns. Their models and textures do not load on this version, so those items were missing-texture blocks.
- Distant terrain LOD. Voxy, Voxy Server Side, and Forgified Fabric API are gone.

## [0.1.4] - 2026-09-23

### Changed

- Structures that use normal structure spacing are about twice as far apart.
- Fire dragons live in the Nether. Dragon skeletons no longer generate on their own; a dragon you kill still leaves a corpse.

### Fixed

- Boot no longer warns about Terralith's disabled andesite, diorite, and granite blobs. Those stones still generate from Terralith.
- You can join with Vic's Point Blank Interaction installed. The server now has the `pointblank_passthrough:interaction` channel.
- JEI's Move Items button can fill a crafting grid in multiplayer. JEI and MezzConfig ship on both sides.
- Skeletons and the other Epic Fight mobs render as Epic Fight models again. Fresh Animations and Darkest Ages no longer replace those mobs.

## [0.1.3] - 2026-09-23

### Added

- Archaion (the Ancient Keep) and Olympus! (Greek artifacts, mobs, and structures).
- Fresh Animations with its extensions, Darkest Ages mob looks, restyled boss bars, and Xaero's map icons.
- Hold the tag key (semicolon, rebindable) to list an item's tags inside its tooltip.
- Vic's Point Blank, with Extended Edition, Gun Gale, Half-Life, and Cyberpunk 2077 guns. You can use blocks while holding one, and the shots hit Aeronautics vehicles.
- MCS2 guns for Timeless and Classics Zero.
- Daffa's Arsenal, CS+, and Call of Duty Warzone guns for Timeless and Classics Zero.

### Changed

- Item tooltips are framed by item type, and untagged items from each major mod get that mod's frame.
- Parkour, Epic Fight, and both gun mods no longer share keys. M opens Xaero's world map only. Reload stays R. Epic Fight mode is the tilde key, dodge is C, and lock-on is T. ParCool dodges are left Alt, TaCZ zoom is middle mouse, and prone is Z. Shader reload and the shader toggle are unbound. Ultimine is Tab.

### Fixed

- Epic Fight combat no longer leaves the normal first-person hand floating. Punchy hides its arms while Epic Fight mode is on.

### Removed

- Legendary Tooltips, Simply Tooltips, and Better Advanced Tooltips. Fzzy Config left with Simply Tooltips.

## [0.1.2] - 2026-09-23

### Fixed

- Epic Fight × Curios Compat is client-only again, so dedicated servers no longer crash loading `ClientCuriosCompat`.
- Empty-override datapack clears orphan Mekanism More Machine / Extras / ExtendedAE loot tables that pointed at unregistered items (boot parse spam).
- JEI QuickCraft and JEI Stuff ship on both sides so their required network channels exist on dedicated servers.
- JEI WorldGen ships on both sides, so world-gen pages can load when you join instead of asking for the mod on the server.

### Removed

- JEI++ (client crash on join: its bookmark mixin still calls JEI's old `mezz.jei.gui.input.IUserInputHandler`, which JEI 19.57 moved).
- Ecliptic Seasons : Voxy Compact and Voxy - Make it compatible (client crash applying mixins when unofficial Voxy is not installed; Voxy cannot ship in the pack).
- Epic Fight Nightfall and Invincible Lib (Nightfall reads client VFX config on dedicated servers and crashes when mobs gain effects). AAA Particles stays.
- Mekanism Covers (beta Sodium mixin fails on join with Sodium 0.8.13; no newer 1.21.1 build).

## [0.1.1] - 2026-09-23

### Added

- Just Enough Items (JEI) 19.57, with MezzConfig, as the recipe viewer.
- JEI companions: JEI++, AE2 JEI Integration, Refined Storage JEI Integration, JEIOptimizer, Sophisticated JEI Index, Smithing Template Viewer, Create JEI Compat, JEI Stuff, JEI QuickCraft, and SpectrumJEI. JEI WorldGen was already in.
- Create Aeronautics 1.3.2 (planes, airships, vehicles) with Sable 2.0.5. Shaders may look wrong on those contraptions.
- Mekanism extras: generator/multiblock JEI pages, Jade upgrades, covers (beta), Extras, Elements, Refined Storage chemicals, Aeronautics compat, Create ponders, and chemical tanks in Sophisticated backpacks.
- Sophisticated backpacks/storage companions: Ars Nouveau, Create recipes, tactical backpacks (beta), item actions, inventory helpers, Yukami tab, chest renderer (NeoForge pin), Jade, Refined Storage quick-deposit, and Demagnetizer (beta, NeoForge pin).
- Patchouli (guidebooks; required by Mekanism Elements).
- Timeless and Classics Zero (unofficial 1.21.1 port) with Pack Upgrader, gun packs, ammo, turrets, armed mobs, Aeronautics/Create/AE2 bridges, and JEI/Jade helpers. Guns Lights is 2.8.2 (2.9.0 is 1.20.x).
- Create crushing/compat for Regions Unexplored and Oh The Biomes We've Gone, plus Block Variants for OTBWG.
- Just Enough Resources (ore/mob pages in JEI), YUNG's Cave Biomes, and Variants & Ventures.
- Nether extras: Jaden's Nether Expansion (and Delight), BetterNether: New Dawn, Eternal Nether, Nether Remastered, Just-In Nether, Nether Villager Trader, and Netherite Tweaks. Farmer's Cutting for BetterNether is in; Cutting for RU and OTBWG was already in.
- Epic Fight with ParCool, Nightfall (AAA Particles), Twilight Forest / TaCZ / Curios / Ice and Fire compat, Bosses' Rise, and related helpers. Ice and Fire: Community Edition is in so that armor compat works.
- Alex's Caves Continued (Codxlib, not Citadel), Compat Structure, and Bad Wither No Cookie Reloaded (quiets boss-fight music).
- Ecliptic Seasons (solar-term weather, snow, and crops) with SeasonHUD, crop bundles, multimod patches, and a Serene Seasons API bridge. Do not add Serene Seasons itself.
- Distant terrain LOD streaming (Voxy Server Side) and Voxy compatibility patches. The Voxy renderer jar is All Rights Reserved and is not redistributed; build the unofficial NeoForge port locally.

### Changed

- Updated sixteen other 1.21.1 NeoForge mods, including Chunk Pregenerator, Entity Culling, Create Better FPS, ExtendedAE, Aquamirae, and Lithostitched.
- Overworld, Nether, and End biome regions are as large as TerraBlender allows, so Terralith, Oh The Biomes We've Gone, Regions Unexplored, and vanilla sit in big continents instead of mixed patches. Individual biomes inside those continents use Large Biomes climate scale, with a bit less speckle at the edges. Alex's Caves biomes are larger and farther apart. New world required. Do not pick the Large Biomes world type.
- Ice and Fire pixie villages generate in the Nether instead of overworld forests. New Nether chunks required.
- BetterNether / WorldWeaver no longer opens the BetterX welcome setup screen on launch.

### Fixed

- Create, Sophisticated, and Polymorph recipe pages load under real JEI instead of TooManyRecipeViewers' fake 19.27 stub.

### Removed

- TaCZ: Immersive Ballistic and TaCZ Tweaks (alpha; Iris vertex-format conflict on load).
- TaCZ / Sophisticated Backpacks ammo addon (it requires a different TaCZ mod id than the unofficial 1.21.1 port).
- EMI, EMI Ores, EMI Enchanting, EMI QoL Tweaks, and TooManyRecipeViewers.
- Iris Flywheel Compat (mixin conflict with Colorwheel; Colorwheel stays for Create + shaders).
- Tectonic. New chunks use vanilla-height terrain plus the remaining biome and structure mods; already-generated Tectonic land stays until those chunks are regenerated.

## [0.1.0] - 2026-09-18

### Changed

- The pack is rebuilt for Minecraft 1.21.1 NeoForge. New world required.
- Discontinued Modrinth as a publishing target; CurseForge is now the sole public store listing.

### Added

- First performance and smoothness stack: Sodium and Iris (replacing Embeddium and Oculus), Lithium, FerriteCore, ModernFix, ImmediatelyFast, FastWorkbench / FastFurnace / FastSuite, and related leak, crash, and entity helpers.
- Extra renderer and smoothness mods: Sodium Extra, Flerovium, AsyncParticles, More Culling, Structure Layout Optimizer, Ksyxis, Disconnect Packet Fix, quick pack, CrashExploitFixer, Async Logger, ResourcePackCached, and Chunk Pregenerator.
- Create (with Iris Flywheel Compat, Create Better FPS, and Threaded Trains), FTB Quests (Library, Teams, Optimizer), and Pipez.
- Pipez Lag Fix, Cerulean (with TxniLib), Bye?Pregen!, The Twilight Forest, The Lost Cities, and Tectonic (with Lithostitched).
- Regions Unexplored and Oh The Biomes We've Gone, with TerraBlender, GeckoLib, CorgiLib, and Oh The Trees You'll Grow. A pack datapack drops Regions Unexplored's Lithostitched structure checks so world generation does not freeze.
- Jade, EMI (with QoL Tweaks and WorldGen pages), Terralith, GeckolibBetterFPS, Nullscape, Structurify, When Dungeons Arise, YUNG's caves/fortresses/bridges, Moog's mineshafts, Epic Structures, Amplified Nether, Infernal Expansion Redux, Terrain Slabs, Awesome Dungeon, and Aquamirae.
- Feature Recycler, so Terralith and Oh The Biomes We've Gone can generate in the same world.
- FastBoot (faster client load), Fluidium (distant fluids tick less), LC²H (multithreaded Lost Cities), BiomeSpy (faster `/locate`), DarkSleep (half the players can skip the night), and MemGuard (heap monitor next to AllTheLeaks).
- Maps, storage, and QoL: Xaero's maps, compasses, Waystones, Sophisticated Backpacks/Storage, Functional Storage, Botany Pots/Trees, FTB Chunks/Essentials/Ultimine, Lootr, Supplementaries, and Better Advanced Tooltips (F3+H item tags).
- Applied Energistics 2 (including AE2 Things), Refined Storage (with Quartz Arsenal and Cable Tiers), Mekanism, Ars Nouveau (including Ars Énergistique), Farmer's Delight, Spectrum, Complementary/BSL shaders with Euphoria Patches, and C2ME. The C2ME OpenCL module is not included: it requires Java 25.

### Fixed

- New worlds no longer crash during generation when Terralith biomes share decoration order with Oh The Biomes We've Gone.

### Removed

- Noisium (incompatible with Bye?Pregen!) and Achievements Optimizer (replaced by Cerulean).
