# Pack mod rules

Hard rules for adding, removing, updating, or configuring mods. Read before any mod change (`minecraft-modding` skill). Rationale and history live in the other `docs/mods/` files; this page is the short list. Recheck a rule against the current jars before relying on it — remove a line when its reason is gone.

## Chosen paths (do not add a second one)

| Role | In the pack | Keep out |
|---|---|---|
| Renderer | Sodium / Iris / Lithium (official) | Embeddium, Oculus, Radium, Nolijium |
| Create + shaders | Colorwheel + Colorwheel Patcher | Iris Flywheel Compat |
| Connected textures | Fusion (+ Fusion packs) | Continuity (needs Sinytra / Forgified Fabric API) |
| GUI restyle | Colourful Everywhere | OptiGUI, Colourful Containers |
| Recipe viewer | JEI + MezzConfig | EMI, TMRV, JEI / REI / EMI WorldGen, extra JEI addons unless requested |
| JEI startup | Just Enough Threads 0.14.9 (`client`) | JEIOptimizer, JEI++ |
| Loot in JEI | JEI Stuff (`both`) + Just Enough Resources | Advanced Loot Info |
| Network fixes | Connectivity (+ Cupboard) | Packet Fixer, Disconnect Packet Fix |
| Seasons | Ecliptic Seasons (+ Serene Seasons API stub) | Serene Seasons |
| Item tooltips | Tooltip Overhaul (Tag Tooltips OK; Better Advanced Tooltips only as a KubeJS dep) | Legendary Tooltips, Simply Tooltips (so no Simply Swords) |
| Structure / biome finder | Explorer's Compass / Nature's Compass | Structure Compass |
| Trinkets | Curios | Accessories (and Spell Engine stacks needing it) |
| Logistics | Modern Dynamics, XNet (+ McJtyLib / RFTools Base), Simple Conveyor Belts, Modular Routers | Pipez, Pipez Lag Fix |
| Storage | AE2 **and** Refined Storage (keep both); Flux Networks beside Applied Flux | — |
| Pregen | `/neoforge generate` + Bye?Pregen! | Chunk Pregenerator, Carbon Config, Noisium / NoisiumForked |
| Melee / movement | Epic Fight + ParCool | Better Combat, Epic Fight Nightfall (+ Invincible Lib), Fresh Moves, Fresh Animations Player Extension |
| Guns | Official 1.21.1 TaCZ (CF 1028108) + Vic's Point Blank | Warzone pack (encrypted), TaCZ Blueprints Reforged, TaCZ Gunslights / lights, Immersive Ballistic, TaCZ Tweaks, Point Blank: Recipe / Jelly / Interaction |
| Dragons | Ice and Fire Community Edition | original Ice and Fire |
| Alex's mobs | Alex's Mobs Continued (Codxlib) | Alex's Caves Continued (+ Delight / Spellbooks), unofficial Alex's ports, Citadel |
| End | BetterEnd: New Dawn (+ Farmer's Cutting: BetterEnd), Nullscape, Unusual End | BetterEnd Remastered |
| Mob loot | DarkLoot datapack in `pack/global_packs/required_data/darkloot/` | DarkLoot mod |
| Affix tuning | Apotheosis Balance Configurator | Apothic Nerf |
| Create alloys | Create: Alloyed | Create: Copper & Zinc |
| Blocks | Chipped + Rechiseled (+ bridges) | — |
| Worldgen shape | TerraBlender region size 6 + large-climate datapack | Tectonic, Large Biomes world type |

## Other mods kept out

- Optimizer stacking: Recipe Essentials, FastBoot, MemGuard, AI Improvements, Structure Essentials, distant-entity freezers, Ixeris. C2ME OpenCL module (needs Java 25).
- Mixin Helper (no fixes, wrong priority can corrupt worlds), Golden Tweaks (PolyForm-Noncommercial mixin pile).
- Quark / Zeta, Integrated BOMD / Mowzie's / API / Patches, Gambling Craft.
- Voxy and every Voxy port/compat (client jar is ARR).
- Mekanism Covers while Sodium 0.8.x is in (mixin hard-fail).
- Legendary Monsters (+ Box of Structures: Legendary Monsters) until a NeoForge build registers default entity attributes.
- Create Aeronautics, Sable, and Aeronautics addons without a fresh research pass. Create trains + Create: Threaded Trains stay.
- Nautec 2, or any mod whose `assets/minecraft/atlases/blocks.json` adds a bare `"source": "entity"` directory — the blocks atlas is already at the GPU ceiling. Check a new content mod's atlas json first.
- KubeJS addons and In Control: none installed; add one through normal research and approval when a script or rule file needs it.

## Pins and holds

- JEI stays on 19.57.0.450: 19.69+ breaks Reinhardt's HBM `JeiFluidHelperMixin` (client crash). Recheck HBM before moving JEI. JEI Structures needs 19.70+, so it waits too.
- Ars Elemental 0.7.10.4: 0.7.11.2 bundles Sauce that crashes dedicated servers.
- Berezka's library on the 1.2.9.5 fix, not the beta.
- Apotheosis 8.9.0 travels with Apokinetics 1.0.12, Compats 0.2.6, irons_apothic 2.2.8.
- Tesseract API 1.12.21 + MI 2.5.13 + EI 1.16.5 + BK's Armaments `5.0.0-neoforge`: exact-pinned by `leylines_patches`.
- Building Gadgets 21.1.1 with Logistics Networks 1.18.0.
- Projects with `allowModDistribution = false` (Simply More, Overgeared: Universal Compatibility, Farmer's Spell 'n Spell Book, Fresh Animations Extensions) use a direct CurseForge CDN `[download] url`, not `metadata:curseforge`, or `packwiz-installer` aborts.

## Sides that matter

- `both`: JEI, MezzConfig, JEI QuickCraft, JEI Stuff, Connectivity, `leylines_patches`, KubeJS, server-logic optimizers.
- `client`: Epic Fight × Curios Compat (loads client classes on servers), Inventory Essentials, Just Enough Threads.

## Configs to keep

- MoreCulling: `leavesCullingMode = "DEFAULT"` (FAST hides Ecliptic Seasons snowy leaves), `useCustomItemFrameRenderer = true`.
- BadOptimizations `enable_sky_color_caching: false`; FTBQuestsOptimizer `consume.aggregate: false`; Leaky full 10-key `leaky.json` with thresholds `1000000`.
- EMF `modelsNamesDisabled` lists every mob Epic Fight animates (Darkest Ages + Fresh Animations otherwise break them).
- Ice and Fire `dragon.generate.skeletons` off; fire dragons and pixie villages generate in the Nether.
- SKY ACES `generateAirbase = false` (first-join stall); `kubejs:deployable_airbase` deploys it on demand.
- Inventory Essentials shift-drag, bulk transfer, and sort disabled (Mouse Tweaks family owns container clicks).
- Structurify spacing 2.0. BetterX / WorldWeaver welcome skipped, BetterX world type not forced.
- Content-mod first-join guidebooks off (Welcome's Akashic Tome stores guides); keep the FTB Quests book and the starting-kit backpack.
- `pack/config/defaultoptions/keybindings.txt` only applies to a fresh `options.txt`.
- `config/justenoughthreads-client.toml` `enabled = false` is the JET escape hatch.

## Pack datapacks and resource packs

Under `pack/global_packs/`. Edit these instead of adding a mod or a KubeJS script for the same job.

- `lead-leylines-starting-kit`: the only first-join give (one iron backpack per world).
- `lead-leylines-load-fixes`: broken-data repairs (see `docs/mods/load-fixes-inventory.md`).
- `lead-leylines-orphan-loot`, `-nether-fire-dragons`, `-nether-pixies`, `-no-vanilla-stone` (not ore dedup; Almost Unified does recipes/tags only), `-large-climate`, `-compat-recipes`, `-oritech-create-compat`, `-ru-in-structure`.
- Resource packs `lead-leylines-armageddon-models` and `lead-leylines-item-atlas-fixes`.

## Not overlap

- Create Ultimine is an FTB Ultimine addon, not a second vein miner.
- Epic Fight × Punchy Neo hides Punchy arms in Epic Fight mode. AAA Particles stays for Effekseer.
