# Lead and Leylines — mod manifest

Synced with `pack/mods/*.pw.toml` on 2026-09-16. Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml). Decision logs: [performance.md](performance.md), [utility.md](utility.md), [storage.md](storage.md), [nether.md](nether.md), [worldgen.md](worldgen.md), [content.md](content.md). Config notes: [configs.md](configs.md).

## Installed

### Embeddium

- Pinned file / version: `embeddium-0.3.31+mc1.20.1.jar` (Modrinth version `UTbfe5d1`)
- Download source: https://modrinth.com/mod/embeddium/version/UTbfe5d1
- packwiz `side`: client
- Category: optimization (renderer)
- Why chosen: Forge Sodium. Rubidium is abandoned; this is the renderer the rest of the client stack expects.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Oculus (shaders), Embeddium Extra
- Config changes: none — defaults. Pair with Oculus `1.8.0`.
- World-data / removability: client renderer; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Oculus

- Pinned file / version: `oculus-mc1.20.1-1.8.0.jar` (Modrinth version `iQ1SwGc3`)
- Download source: https://modrinth.com/mod/oculus/version/iQ1SwGc3
- packwiz `side`: client
- Category: shaders (loader)
- Why chosen: Iris for Forge. Shaders are a pack feature. No separate dynamic-lights mod.
- Required dependencies: Embeddium (paired `0.3.31`)
- Optional dependencies: none
- Recommended companions: shader packs (not shipped yet)
- Config changes: none — no default shader pack until one is chosen on purpose
- World-data / removability: client; clean to remove (shader packs are files, not world data)
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### FerriteCore

- Pinned file / version: `ferritecore-6.0.1-forge.jar`
- Download source: https://modrinth.com/mod/ferrite-core
- packwiz `side`: both
- Category: optimization (memory)
- Why chosen: Blockstate/model memory. No real alternative.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### ImmediatelyFast

- Pinned file / version: `ImmediatelyFast-Forge-1.5.5+1.20.4.jar` (Modrinth version `rvsLEEZU`; file lists 1.20.1)
- Download source: https://modrinth.com/mod/immediatelyfast/version/rvsLEEZU
- packwiz `side`: client
- Category: optimization (HUD / immediate-mode GL)
- Why chosen: Different layer from Embeddium. Do not let packwiz pick older `1.2.7`.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. If a later HUD/tooltip mod glitches, disable `hud_batching`.
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### ModernFix

- Pinned file / version: `modernfix-forge-5.27.83+mc1.20.1.jar`
- Download source: https://modrinth.com/mod/modernfix
- packwiz `side`: both
- Category: optimization (launch, memory, vanilla fixes)
- Why chosen: Author intends it next to other perf mods.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — mixin defaults stay
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### FastWorkbench

- Pinned file / version: `FastWorkbench-1.20.1-8.0.4.jar`
- Download source: https://modrinth.com/mod/fastworkbench
- packwiz `side`: both
- Category: optimization (crafting)
- Why chosen: Crafting-table recipe scan. Must match on client and server.
- Required dependencies: Placebo
- Optional dependencies: none
- Recommended companions: FastFurnace (same author)
- Config changes: none — defaults
- World-data / removability: clean to remove (no new blocks)
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Placebo

- Pinned file / version: `Placebo-1.20.1-8.6.3.jar`
- Download source: https://modrinth.com/mod/placebo
- packwiz `side`: both
- Category: library
- Why chosen: Required by FastWorkbench and FastSuite.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while FastWorkbench or FastSuite is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### FastFurnace

- Pinned file / version: `FastFurnace-1.20.1-8.0.2.jar`
- Download source: https://modrinth.com/mod/fastfurnace
- packwiz `side`: both
- Category: optimization (furnaces)
- Why chosen: Furnace tick shortcut. Same both-sides rule as FastWorkbench.
- Required dependencies: none (Placebo is present via FastWorkbench)
- Optional dependencies: none
- Recommended companions: FastWorkbench
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### BadOptimizations

- Pinned file / version: `BadOptimizations-2.4.1-1.20.1.jar`
- Download source: https://modrinth.com/mod/badoptimizations
- packwiz `side`: client
- Category: optimization (CPU, non-meshing)
- Why chosen: Complements Embeddium (toasts, sky, etc.).
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Embeddium Extra

- Pinned file / version: `rubidium-extra-0.5.4.4+mc1.20.1-build.131.jar`
- Download source: https://modrinth.com/mod/rubidium-extra
- packwiz `side`: client
- Category: optimization (Sodium Extra port)
- Why chosen: Fog, particles, animation, leaf settings. One extras mod only.
- Required dependencies: Embeddium
- Optional dependencies: none
- Recommended companions: none
- Config changes: leave Extra lights off while Oculus is in. If another leaf mod is added later, turn Extra leaf culling off.
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Crash Assistant

- Pinned file / version: `CrashAssistant-forge-1.19-1.20.1-1.11.12.jar`
- Download source: https://modrinth.com/mod/crash-assistant
- packwiz `side`: client
- Category: QoL (crash UI)
- Why chosen: Crash GUI and log analysis. Better default than Not Enough Crashes.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: `pack/config/crash_assistant/config.toml` — Request Help → `https://discord.gg/Ck7TP4btRy`; pack name / Discord placeholders; piracy notice on ([configs.md](configs.md))
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Radium

- Pinned file / version: `radium-mc1.20.1-0.12.4+git.26c9d8e.jar`
- Download source: https://modrinth.com/mod/radium (Reforged-Hub; not CurseForge “Radium Reforged” as a second jar)
- packwiz `side`: both
- Category: optimization (Lithium port)
- Why chosen: AI, block updates, ticking. Chosen instead of Canary.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. FerriteCore disables Radium’s blockstate alloc mixin (expected).
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Let Me Despawn

- Pinned file / version: `letmedespawn-1.20.x-forge-1.5.0.jar`
- Download source: https://modrinth.com/mod/lmd
- packwiz `side`: both
- Category: optimization (entity / despawn)
- Why chosen: Despawn for mobs that picked up gear and would otherwise live forever.
- Required dependencies: Almanac
- Optional dependencies: none
- Recommended companions: none
- Config changes: none until raid/named mobs vanish unexpectedly; then tighten equipment whitelist (`docs/mods/configs.md`)
- World-data / removability: gameplay (despawn rules); no new blocks
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Almanac

- Pinned file / version: `almanac-1.20.x-forge-1.0.2.jar`
- Download source: https://modrinth.com/mod/almanac
- packwiz `side`: both
- Category: library
- Why chosen: Required by Let Me Despawn. `both` so singleplayer gets it.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Let Me Despawn is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### AllTheLeaks

- Pinned file / version: `alltheleaks-1.1.3+1.20.1-forge.jar` (CurseForge file id `8779054`, project `1091339`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/alltheleaks
- packwiz `side`: both
- Category: optimization (leak patches)
- Why chosen: Leak patches for vanilla and popular mods. CurseForge only.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: see CurseForge project page
- Date added: 2026-09-13

### Entity Culling

- Pinned file / version: `entityculling-forge-1.10.5-mc1.20.1.jar` (Modrinth version `MloBcsQQ`)
- Download source: https://modrinth.com/mod/entityculling/version/MloBcsQQ
- packwiz `side`: client
- Category: optimization (entity / block-entity visibility)
- Why chosen: Async line-of-sight hide. Official Forge. Different layer from Embeddium Extra (not leaf culling).
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client; clean to remove
- License / attribution: tr7zw Protective License — CurseForge/Modrinth packs allowed; do not rehost the jar elsewhere
- Date added: 2026-09-13

### Dynamic FPS

- Pinned file / version: `dynamic-fps-3.11.4+minecraft-1.20.0-forge.jar` (Modrinth version `EjdIWWqG`; file lists 1.20 / 1.20.1)
- Download source: https://modrinth.com/mod/dynamic-fps/version/EjdIWWqG
- packwiz `side`: client
- Category: optimization (background CPU)
- Why chosen: Lowers resource use when Minecraft is unfocused. Official Forge. Not in-game FPS.
- Required dependencies: none
- Optional dependencies: Cloth Config (shipped; in-game screen)
- Recommended companions: none
- Config changes: none — defaults. Cloth Config is now in for the optional GUI.
- World-data / removability: client; clean to remove
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-13

### FastSuite

- Pinned file / version: `FastSuite-1.20.1-5.1.2.jar` (Modrinth version `nhk4VpGm`)
- Download source: https://modrinth.com/mod/fastsuite/version/nhk4VpGm
- packwiz `side`: both
- Category: optimization (recipes)
- Why chosen: Indexes all JSON recipes. Same author as FastWorkbench. Helps Apotheosis / AE2 / MI / magic / utility recipes. Does not replace FastWorkbench or FastFurnace.
- Required dependencies: Placebo (already in)
- Optional dependencies: none
- Recommended companions: FastWorkbench, FastFurnace
- Config changes: none — defaults
- World-data / removability: clean to remove (no new blocks)
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-13

### Noisium

- Pinned file / version: `noisium-forge-2.3.0+mc1.20-1.20.1.jar` (Modrinth version `gbYUKrDP`)
- Download source: https://modrinth.com/mod/noisium/version/gbYUKrDP
- packwiz `side`: both
- Category: optimization (worldgen CPU)
- Why chosen: Faster vanilla-parity chunk generation. For exploration hitch and planned biome mods. Does not change terrain.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove; worlds stay vanilla-shaped
- License / attribution: LGPL-3.0-only; see Modrinth project page
- Date added: 2026-09-13

### Clumps

- Pinned file / version: `Clumps-forge-1.20.1-12.0.0.4.jar` (Modrinth version `nAHGB5ls`)
- Download source: https://modrinth.com/mod/clumps/version/nAHGB5ls
- packwiz `side`: both
- Category: optimization (XP orbs)
- Why chosen: Merges XP orbs. Needed when Mob Grinding Utils and other farms spawn orb spam.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove (orbs are entities, not world blocks)
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-13

### Smooth Chunk Save

- Pinned file / version: `smoothchunk-1.20.1-4.1.jar` (CurseForge file id `6296598`, project `582327`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/smooth-chunk-save
- packwiz `side`: both
- Category: optimization (chunk autosave)
- Why chosen: Spreads disk writes so autosave does not hitch in singleplayer or on the dedicated server.
- Required dependencies: Cupboard
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: All Rights Reserved on CurseForge; allowed in CurseForge/Modrinth packs via store distribution of this pack
- Date added: 2026-09-13

### Cupboard

- Pinned file / version: `cupboard-1.20.1-4.1.jar` (CurseForge file id `8746423`, project `326652`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/cupboard
- packwiz `side`: both
- Category: library
- Why chosen: Required by Smooth Chunk Save. Keep for later Connectivity if needed.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Smooth Chunk Save is installed
- License / attribution: All Rights Reserved on CurseForge; store pack distribution
- Date added: 2026-09-13

### Neruina

- Pinned file / version: `neruina-3.3.3+1.20.1-forge.jar` (Modrinth version `7Pn5jnNB`)
- Download source: https://modrinth.com/mod/neruina/version/7Pn5jnNB
- packwiz `side`: both
- Category: reliability (ticking crash isolation)
- Why chosen: Prevents a broken entity/block tick from bricking the world as farms, magic, and tech land.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Crash Assistant (client crash UI)
- Config changes: none — defaults
- World-data / removability: clean to remove; does not add blocks
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-13

### Architectury API

- Pinned file / version: `architectury-9.2.14-forge.jar` (Modrinth version `1MKTLiiG`)
- Download source: https://modrinth.com/mod/architectury-api/version/1MKTLiiG
- packwiz `side`: both
- Category: library
- Why chosen: Required by the FTB suite, EMI, and Countered's Terrain Slabs.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while FTB mods, EMI, or Terrain Slabs are installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Kotlin for Forge

- Pinned file / version: `kotlinforforge-4.12.0-all.jar` (Modrinth version `Zsh14XeQ`)
- Download source: https://modrinth.com/mod/kotlin-for-forge/version/Zsh14XeQ
- packwiz `side`: both
- Category: library
- Why chosen: Required by Create Ultimine.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Create Ultimine is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### FTB Library

- Pinned file / version: `ftb-library-forge-2001.2.13.jar` (CurseForge file `8226927`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ftb-library-forge/files/8226927
- packwiz `side`: both
- Category: library
- Why chosen: Shared UI/config for the FTB suite.
- Required dependencies: Architectury API
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while other FTB mods are installed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-13

### FTB Teams

- Pinned file / version: `ftb-teams-forge-2001.3.2.jar` (CurseForge file `7499810`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ftb-teams-forge/files/7499810
- packwiz `side`: both
- Category: multiplayer (parties)
- Why chosen: Parties for FTB Chunks claims and FTB Quests.
- Required dependencies: FTB Library, Architectury API
- Optional dependencies: none
- Recommended companions: FTB Chunks, FTB Quests
- Config changes: none — defaults
- World-data / removability: writes team data; removing drops parties
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-13

### FTB Chunks

- Pinned file / version: `ftb-chunks-forge-2001.3.8.jar` (CurseForge file `8216874`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ftb-chunks-forge/files/8216874
- packwiz `side`: both
- Category: claims / forceload
- Why chosen: One claim system. Map HUD is Xaero, not FTB’s minimap.
- Required dependencies: FTB Library, FTB Teams, Architectury API
- Optional dependencies: none
- Recommended companions: Xaero’s Minimap / World Map (map UI)
- Config changes: minimap disabled; see [configs.md](configs.md). Unbind FTB **Open Map** in Controls (defaults to M, same as Xaero World Map).
- World-data / removability: claims and forceload tickets live in the world; removing drops protection
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-13

### FTB Quests

- Pinned file / version: `ftb-quests-forge-2001.4.22.jar` (CurseForge file `8078538`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ftb-quests-forge/files/8078538
- packwiz `side`: both
- Category: quests
- Why chosen: Quest book for the long campaign.
- Required dependencies: FTB Library, FTB Teams, FTB Filter System, Architectury API
- Optional dependencies: none
- Recommended companions: FTB XMod Compat (EMI bridge)
- Config changes: none — defaults (no quest chapter shipped yet)
- World-data / removability: player quest progress is world data
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-13

### FTB Ultimine

- Pinned file / version: `ftb-ultimine-forge-2001.1.8.jar` (CurseForge file `7880472`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ftb-ultimine-forge/files/7880472
- packwiz `side`: both
- Category: mining QoL
- Why chosen: Vein-style mining. Pair with Create Ultimine for Create blocks.
- Required dependencies: FTB Library, Architectury API
- Optional dependencies: none
- Recommended companions: Create Ultimine
- Config changes: none — defaults
- World-data / removability: client/server logic; clean to remove
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-13

### FTB Essentials

- Pinned file / version: `ftb-essentials-forge-2001.2.4.jar` (CurseForge file `7609948`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ftb-essentials/files/7609948
- packwiz `side`: both
- Category: commands
- Why chosen: Light `/home`, `/spawn`, and related commands without a full essentials suite.
- Required dependencies: Architectury API
- Optional dependencies: none
- Recommended companions: none
- Config changes: `pack/defaultconfigs/ftbessentials-server.snbt` — `/rtp` `max_distance` 2000, `max_tries` 3, dimension blacklist End/Nether/Maelstrom. Stops the server-thread chunk search from tripping the 60s watchdog on ungenerated Tectonic terrain.
- World-data / removability: homes/warps are world data
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-13

### FTB XMod Compat

- Pinned file / version: `ftb-xmod-compat-forge-2.1.3.jar` (CurseForge file `6402486`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ftb-xmod-compat/files/6402486
- packwiz `side`: both
- Category: compatibility
- Why chosen: Bridges FTB Quests to EMI (and other FTB integrations).
- Required dependencies: FTB Library
- Optional dependencies: EMI, FTB Quests (present)
- Recommended companions: EMI
- Config changes: none — defaults
- World-data / removability: clean to remove; quests still work without EMI integration
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-13

### FTB Filter System

- Pinned file / version: `ftb-filter-system-forge-20.0.1.jar` (CurseForge file `6466153`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ftb-filter-system/files/6466153
- packwiz `side`: both
- Category: library (item filters)
- Why chosen: FTB Quests item filters on 1.20.1. Item Filters was skipped.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: FTB Quests
- Config changes: none — defaults
- World-data / removability: do not remove while FTB Quests is installed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-13

### Jade

- Pinned file / version: `Jade-1.20.1-Forge-11.13.3.jar` (Modrinth version `xJQHCmWJ`)
- Download source: https://modrinth.com/mod/jade/version/xJQHCmWJ
- packwiz `side`: both
- Category: HUD (block/entity info)
- Why chosen: Overlay for what you are looking at. `both` so server-synced info matches Prism and the dedicated server.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### EMI

- Pinned file / version: `emi-1.1.24+1.20.1+forge.jar` (Modrinth version `Axuu9I9R`)
- Download source: https://modrinth.com/mod/emi/version/Axuu9I9R
- packwiz `side`: both
- Category: recipe browser
- Why chosen: One recipe viewer. JEI skipped because TMRV cannot sit next to it.
- Required dependencies: Architectury API
- Optional dependencies: none
- Recommended companions: Too Many Recipe Viewers, FTB XMod Compat
- Config changes: none — defaults
- World-data / removability: clean to remove (recipe index is not world data)
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Too Many Recipe Viewers

- Pinned file / version: `toomanyrecipeviewers-0.9.0+mc.20.1.jar` (Modrinth version `PSC3dlCl`)
- Download source: https://modrinth.com/mod/tmrv/version/PSC3dlCl
- packwiz `side`: client
- Category: recipe browser (EMI layout)
- Why chosen: EMI list/UI helper. Ships a `jei` stub at 15.20.0.132 so JEI plugins can run on EMI. Incompatible with a real JEI jar, and with mods that require a newer JEI version (Polymorph 0.49.11+).
- Required dependencies: EMI
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Accelerated Decay

- Pinned file / version: `accelerated-decay-forge-3.0.1+mc1.20.1.jar` (CurseForge file `4863307`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/accelerated-decay/files/4863307
- packwiz `side`: both
- Category: world (leaf/decay catch-up)
- Why chosen: Speeds leaf decay catch-up after chopping. Last Forge 1.20.1 file (Nov 2023); still lists this pair.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: changes decay timing only; clean to remove
- License / attribution: see CurseForge project page
- Date added: 2026-09-13

### Create

- Pinned file / version: `create-1.20.1-6.0.8.jar` (Modrinth version `8amzvn9x`)
- Download source: https://modrinth.com/mod/create/version/8amzvn9x
- packwiz `side`: both
- Category: content (kinetics)
- Why chosen: Planned tech pillar. Create 6 bundles Flywheel.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Colorwheel + Patcher (Oculus), Create Ultimine
- Config changes: none — defaults. Back up existing worlds before first boot.
- World-data / removability: kinetic blocks and contraptions stay in the save if Create is removed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-13

### Create Ultimine

- Pinned file / version: `createultimine-1.20.1-forge-1.3.1.jar` (Modrinth version `v1WWGazc`)
- Download source: https://modrinth.com/mod/create-ultimine/version/v1WWGazc
- packwiz `side`: both
- Category: mining QoL (Create)
- Why chosen: Lets FTB Ultimine vein-mine Create blocks.
- Required dependencies: Create, FTB Ultimine, Kotlin for Forge
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Colorwheel

- Pinned file / version: `colorwheel-forge-1.3.0-beta3+mc1.20.1.jar` (Modrinth version `RwUrKFGe`)
- Download source: https://modrinth.com/mod/colorwheel/version/RwUrKFGe
- packwiz `side`: client
- Category: shaders (Create + Oculus)
- Why chosen: Flywheel under Oculus. Replaces Iris/Oculus Flywheel Compat (incompatible with Colorwheel). **Beta**.
- Required dependencies: Oculus, Colorwheel Patcher, Create (Flywheel)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — pair with Patcher; do not add iris-flw-compat
- World-data / removability: client; clean to remove (Create still runs without shaders)
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Colorwheel Patcher

- Pinned file / version: `colorwheel_patcher-forge-1.0.5+mc1.20.1.jar` (Modrinth version `REyG66M8`)
- Download source: https://modrinth.com/mod/colorwheel-patcher/version/REyG66M8
- packwiz `side`: client
- Category: shaders (Colorwheel companion)
- Why chosen: Required patcher for Colorwheel on this stack.
- Required dependencies: Colorwheel
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Colorwheel is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Xaero's Minimap

- Pinned file / version: `xaerominimap-forge-1.20.1-26.5.0.jar` (Modrinth version `Juh6inLY`)
- Download source: https://modrinth.com/mod/xaeros-minimap/version/Juh6inLY
- packwiz `side`: client
- Category: map (HUD)
- Why chosen: One minimap. FTB Chunks minimap is disabled.
- Required dependencies: none
- Optional dependencies: Xaero’s World Map (shipped)
- Recommended companions: Xaero’s World Map
- Config changes: none — FTB minimap off is on the FTB side ([configs.md](configs.md))
- World-data / removability: client waypoints live in the instance; not server claims
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Xaero's World Map

- Pinned file / version: `xaeroworldmap-forge-1.20.1-1.46.0.jar` (Modrinth version `rlPmwaQX`)
- Download source: https://modrinth.com/mod/xaeros-world-map/version/rlPmwaQX
- packwiz `side`: client
- Category: map (fullscreen)
- Why chosen: One fullscreen map. Keep **M** for Xaero; unbind FTB Open Map.
- Required dependencies: none
- Optional dependencies: Xaero’s Minimap (shipped)
- Recommended companions: Xaero’s Minimap
- Config changes: none on Xaero. Unbind FTB Chunks Open Map so **M** is not a double bind ([configs.md](configs.md)).
- World-data / removability: client map cache in the instance
- License / attribution: see Modrinth project page
- Date added: 2026-09-13

### Titanium

- Pinned file / version: `titanium-1.20.1-3.8.35.jar` (Modrinth version `LMqbm4db`)
- Download source: https://modrinth.com/mod/titanium/version/LMqbm4db
- packwiz `side`: both
- Category: library
- Why chosen: Required by Functional Storage.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Functional Storage is installed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-15

### Functional Storage

- Pinned file / version: `functionalstorage-1.20.1-1.2.14.jar` (Modrinth version `XJ0p2eID`)
- Download source: https://modrinth.com/mod/functional-storage/version/XJ0p2eID
- packwiz `side`: both
- Category: storage (drawers)
- Why chosen: Same-item drawers. Not Storage Drawers.
- Required dependencies: Titanium
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: drawer blocks stay in the save if removed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-15

### Sophisticated Core

- Pinned file / version: `sophisticatedcore-1.20.1-1.5.1.2335.jar` (Modrinth version `1Xl7lP0L`)
- Download source: https://modrinth.com/mod/sophisticated-core/version/1Xl7lP0L
- packwiz `side`: both
- Category: library
- Why chosen: Required by Sophisticated Storage and Sophisticated Backpacks.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Sophisticated Storage or Backpacks is installed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-15

### Curios API

- Pinned file / version: `curios-forge-5.14.1+1.20.1.jar` (Modrinth version `IPQlZkz1`)
- Download source: https://modrinth.com/mod/curios/version/IPQlZkz1
- packwiz `side`: both
- Category: library (equipment slots)
- Why chosen: Back slot so Sophisticated Backpacks do not occupy chest armor.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Sophisticated Backpacks
- Config changes: none — defaults
- World-data / removability: do not remove while backpacks use the Curios back slot
- License / attribution: LGPL-3.0-or-later; see Modrinth project page
- Date added: 2026-09-15

### Sophisticated Storage

- Pinned file / version: `sophisticatedstorage-1.20.1-1.4.86.2131.jar` (Modrinth version `JCxeJIsN`)
- Download source: https://modrinth.com/mod/sophisticated-storage/version/JCxeJIsN
- packwiz `side`: both
- Category: storage (chests / barrels)
- Why chosen: Upgradeable chests, barrels, and shulkers. Not Iron Chests.
- Required dependencies: Sophisticated Core
- Optional dependencies: JEI (skipped; EMI is the viewer), Quark, Crafting Tweaks, Chipped, TrashSlot, Item Borders
- Recommended companions: Sophisticated Storage Create Integration (shipped)
- Config changes: none — defaults
- World-data / removability: chests and barrels stay in the save if removed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-15

### Sophisticated Backpacks

- Pinned file / version: `sophisticatedbackpacks-1.20.1-3.26.3.2157.jar` (Modrinth version `XxOZuQnU`)
- Download source: https://modrinth.com/mod/sophisticated-backpacks/version/XxOZuQnU
- packwiz `side`: both
- Category: storage (backpacks)
- Why chosen: One backpack mod. Wearable, placeable, upgradeable.
- Required dependencies: Sophisticated Core
- Optional dependencies: Curios (shipped), JEI (skipped), Crafting Tweaks, Chipped, TrashSlot, Item Borders
- Recommended companions: Curios, Sophisticated Backpacks Create Integration (both shipped)
- Config changes: open defaults to **B**; unbind in Controls if needed ([configs.md](configs.md))
- World-data / removability: backpack items and placed backpacks stay in the save if removed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-15

### Sophisticated Storage Create Integration

- Pinned file / version: `sophisticatedstoragecreateintegration-1.20.1-0.1.24.221.jar` (Modrinth version `o8dwHKKj`)
- Download source: https://modrinth.com/mod/sophisticated-storage-create-integration/version/o8dwHKKj
- packwiz `side`: both
- Category: compatibility (Create)
- Why chosen: Create is already in. Without this, Sophisticated Storage on moving contraptions can dupe.
- Required dependencies: Sophisticated Storage, Sophisticated Core, Create (present)
- Optional dependencies: JEI (skipped)
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Create + Sophisticated Storage are installed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-15

### Sophisticated Backpacks Create Integration

- Pinned file / version: `sophisticatedbackpackscreateintegration-1.20.1-0.1.10.167.jar` (Modrinth version `gzpoJdRt`)
- Download source: https://modrinth.com/mod/sophisticated-backpacks-create-integration/version/gzpoJdRt
- packwiz `side`: both
- Category: compatibility (Create)
- Why chosen: Same contraption safety for backpacks.
- Required dependencies: Sophisticated Backpacks, Sophisticated Core, Create (present)
- Optional dependencies: JEI (skipped)
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Create + Sophisticated Backpacks are installed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-15

### Amplified Nether

- Pinned file / version: `Amplified_Nether_26.2_v1.2.15.jar` (Modrinth version `ctnhVAao`)
- Download source: https://modrinth.com/mod/amplified-nether/version/ctnhVAao
- packwiz `side`: both
- Category: worldgen (Nether height)
- Why chosen: Taller Nether. Incompatible with Incendium; often compatible with BetterNether.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: BetterNether Forge (shipped)
- Config changes: none — defaults. New world for Nether terrain.
- World-data / removability: changes Nether generation; old chunks stay old
- License / attribution: Stardust Labs License; store pack distribution
- Date added: 2026-09-16

### WunderLib Forge

- Pinned file / version: `WunderLib-20.0.1.jar` (Modrinth version `FFIJ4Ioj`)
- Download source: https://modrinth.com/mod/wunderlib-forge/version/FFIJ4Ioj
- packwiz `side`: both
- Category: library
- Why chosen: Required by BetterNether Forge and BCLib Forge.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while BetterNether or BCLib is installed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### BCLib Forge

- Pinned file / version: `BCLib-20.0.13.jar` (Modrinth version `TIteCm8O`)
- Download source: https://modrinth.com/mod/bclib-forge/version/TIteCm8O
- packwiz `side`: both
- Category: library
- Why chosen: Required by BetterNether Forge.
- Required dependencies: WunderLib Forge
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while BetterNether is installed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### BetterNether Forge

- Pinned file / version: `BetterNether-20.0.12.jar` (Modrinth version `BEw6Aggq`)
- Download source: https://modrinth.com/mod/betternether-forge/version/BEw6Aggq
- packwiz `side`: both
- Category: worldgen (Nether biomes)
- Why chosen: Nether biomes, plants, and structures. Unofficial Forge port of BetterNether.
- Required dependencies: BCLib Forge, WunderLib Forge
- Optional dependencies: none
- Recommended companions: Amplified Nether (shipped)
- Config changes: none — defaults. New world.
- World-data / removability: biomes, blocks, and items stay in the save if removed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### YUNG's API

- Pinned file / version: `YungsApi-1.20-Forge-4.0.6.jar` (Modrinth version `PJOYAmAs`)
- Download source: https://modrinth.com/mod/yungs-api/version/PJOYAmAs
- packwiz `side`: both
- Category: library
- Why chosen: Required by YUNG’s Better Nether Fortresses.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while YUNG fortresses are installed
- License / attribution: LGPL-3.0-only; see Modrinth project page
- Date added: 2026-09-16

### YUNG's Better Nether Fortresses

- Pinned file / version: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` (Modrinth version `2nUEz0zq`)
- Download source: https://modrinth.com/mod/yungs-better-nether-fortresses/version/2nUEz0zq
- packwiz `side`: both
- Category: worldgen (structures)
- Why chosen: Fortress rewrite. Replaces Bygone Nether’s enhanced vanilla fortress (intended).
- Required dependencies: YUNG’s API
- Optional dependencies: Create (present; optional fortress pieces)
- Recommended companions: none
- Config changes: none on YUNG’s toml. `/locate` reports `~` for Y; in Amplified Nether the fortress is often far above or below the player. New world.
- World-data / removability: generated structures stay in chunks
- License / attribution: LGPL-3.0-only; see Modrinth project page
- Date added: 2026-09-16

### GeckoLib

- Pinned file / version: `geckolib-forge-1.20.1-4.8.4.jar` (Modrinth version `aC5KMoNg`)
- Download source: https://modrinth.com/mod/geckolib/version/aC5KMoNg
- packwiz `side`: both
- Category: library (entity animation)
- Why chosen: Required by Infernal Expansion Redux.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Infernal Expansion Redux is installed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### Cloth Config API

- Pinned file / version: `cloth-config-11.1.136-forge.jar` (Modrinth version `t8TXrZvZ`)
- Download source: https://modrinth.com/mod/cloth-config/version/t8TXrZvZ
- packwiz `side`: both
- Category: library (config GUI)
- Why chosen: Optional GUI for Infernal Expansion Redux and Dynamic FPS.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove (mods still load without the GUI)
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Infernal Expansion Redux

- Pinned file / version: `infernalexp-forge-1.20.1-0.3.8.jar` (Modrinth version `cMVA7QBk`)
- Download source: https://modrinth.com/mod/infernal-expansion-redux/version/cMVA7QBk
- packwiz `side`: both
- Category: content (Nether)
- Why chosen: Official 1.20.1 pointer from Infernal Expansion. In-development rebuild, not a 1:1 port.
- Required dependencies: GeckoLib
- Optional dependencies: Cloth Config (shipped), LambDynamicLights (skipped; Oculus is the light path), Afterimages (skipped)
- Recommended companions: none
- Config changes: none — defaults. New world.
- World-data / removability: biomes, blocks, and mobs stay in the save if removed
- License / attribution: AGPL-3.0-only; see Modrinth project page
- Date added: 2026-09-16

### Stalwart Dungeons

- Pinned file / version: `stalwart-dungeons-1.20.1-1.2.8.jar` (Modrinth version `vgD645b7`)
- Download source: https://modrinth.com/mod/stalwart-dungeons/version/vgD645b7
- packwiz `side`: both
- Category: worldgen (dungeons)
- Why chosen: Unique dungeon types (including Nether). Last 1.20.1 file 2023; still lists this pair.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. Density stacks with Awesome Dungeon.
- World-data / removability: generated structures stay in chunks
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### Bygone Nether

- Pinned file / version: `bygonenether-1.3.2-1.20.x.jar` (Modrinth version `RA38ax2z`)
- Download source: https://modrinth.com/mod/bygone-nether/version/RA38ax2z
- packwiz `side`: both
- Category: content (Nether)
- Why chosen: Piglin manors, citadels, Wither. Fortress rewrite is YUNG’s, not Bygone’s.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world.
- World-data / removability: structures, blocks, and mobs stay in the save if removed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### Farmer's Delight

- Pinned file / version: `FarmersDelight-1.20.1-1.3.4.jar` (Modrinth version `SiIpcZzM`)
- Download source: https://modrinth.com/mod/farmers-delight/version/SiIpcZzM
- packwiz `side`: both
- Category: content (cooking / farming)
- Why chosen: Cooking pillar. Paired with My Nether’s Delight, not the 2023 Nether’s Delight jar.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: My Nether’s Delight (shipped)
- Config changes: none — defaults
- World-data / removability: crops, blocks, and items stay in the save if removed
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### My Nether's Delight

- Pinned file / version: `MyNethersDelight-1.20.1-1.10.4-backport.1.jar` (Modrinth version `pOBasFQT`)
- Download source: https://modrinth.com/mod/my-nethers-delight/version/pOBasFQT
- packwiz `side`: both
- Category: content (Nether cooking)
- Why chosen: Maintained Nether addon for Farmer’s Delight 1.3.x. Do not also install original Nether’s Delight.
- Required dependencies: Farmer’s Delight
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — pin this backport on Farmer’s Delight 1.3.x (MND `1.8` crashed on 1.3)
- World-data / removability: crops and blocks stay in the save if removed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-16

### Library Ferret

- Pinned file / version: `libraryferret-forge-1.20.1-4.0.0.jar` (Modrinth version `wl68oCTb`)
- Download source: https://modrinth.com/mod/library-ferret/version/wl68oCTb
- packwiz `side`: both
- Category: library
- Why chosen: Required by Awesome Dungeon and Awesome Dungeon Nether.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Awesome Dungeon mods are installed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-16

### Awesome Dungeon

- Pinned file / version: `awesomedungeon-forge-1.20.1-3.2.0.jar` (Modrinth version `GRFhAaFE`)
- Download source: https://modrinth.com/mod/awesome-dungeon/version/GRFhAaFE
- packwiz `side`: both
- Category: worldgen (dungeons)
- Why chosen: Extra overworld dungeons. End/Ocean editions held.
- Required dependencies: Library Ferret
- Optional dependencies: none
- Recommended companions: Awesome Dungeon Nether (shipped)
- Config changes: none — defaults
- World-data / removability: generated structures stay in chunks
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-16

### Awesome Dungeon Nether

- Pinned file / version: `awesomedungeonnether-forge-1.20.1-3.1.1.jar` (Modrinth version `x2mdkok9`)
- Download source: https://modrinth.com/mod/awesome-dungeon-nether/version/x2mdkok9
- packwiz `side`: both
- Category: worldgen (Nether dungeons)
- Why chosen: Extra Nether dungeons.
- Required dependencies: Library Ferret
- Optional dependencies: none
- Recommended companions: Awesome Dungeon (shipped)
- Config changes: none — defaults
- World-data / removability: generated structures stay in chunks
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-16

### Moog's Structure Lib

- Pinned file / version: `MoogsStructureLib-forge-1.20-3.3.1.jar` (Modrinth version `Xe7AFvDZ`)
- Download source: https://modrinth.com/mod/moogs-structure-lib/version/Xe7AFvDZ
- packwiz `side`: both
- Category: library
- Why chosen: Required by Moog’s Mineshafts Reimagined.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while MMR is installed
- License / attribution: LGPL-3.0-only; see Modrinth project page
- Date added: 2026-09-16

### MMR - Moog's Mineshafts Reimagined

- Pinned file / version: `MoogsMineshaftsReimagined-1.20-1.0.2.jar` (Modrinth version `fjkyFY5g`)
- Download source: https://modrinth.com/mod/mmr-moogs-mineshafts-reimagined/version/fjkyFY5g
- packwiz `side`: both
- Category: worldgen (mineshafts)
- Why chosen: Extra mineshafts beside vanilla. Not YUNG’s Better Mineshafts.
- Required dependencies: Moog’s Structure Lib
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world for shaft placement.
- World-data / removability: generated structures stay in chunks
- License / attribution: GPL-3.0-only; see Modrinth project page
- Date added: 2026-09-16

### TerraBlender

- Pinned file / version: `TerraBlender-forge-1.20.1-3.0.1.10.jar` (Modrinth version `zGconCHG`)
- Download source: https://modrinth.com/mod/terrablender/version/zGconCHG
- packwiz `side`: both
- Category: library (biomes)
- Why chosen: Required by Regions Unexplored and Oh The Biomes We've Gone.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: `pack/config/terrablender.toml` — `overworld_region_size` 6, `nether_region_size` 4 ([configs.md](configs.md))
- World-data / removability: do not remove while RU or BWG is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Fragmentum

- Pinned file / version: `fragmentum-forge-1.20.1-1.5.2.jar` (Modrinth version `1nysmgB4`)
- Download source: https://modrinth.com/mod/fragmentum/version/1nysmgB4
- packwiz `side`: both
- Category: library
- Why chosen: Required by Aquamirae.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Aquamirae is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Aquamirae

- Pinned file / version: `aquamirae-forge-1.20.1-7.1.13.jar` (Modrinth version `72GwOBcB`)
- Download source: https://modrinth.com/mod/aquamirae/version/72GwOBcB
- packwiz `side`: both
- Category: content (ocean)
- Why chosen: Ice/ocean dungeon and sea mobs. Not a biome pack.
- Required dependencies: Fragmentum, GeckoLib (present)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world.
- World-data / removability: structures, blocks, and mobs stay in the save if removed
- License / attribution: Obscuria license; unmodified store files in CurseForge/Modrinth packs only
- Date added: 2026-09-16

### Regions Unexplored

- Pinned file / version: `RegionsUnexploredForge-0.5.6+1.20.1.jar` (Modrinth version `XTrgsfIB`)
- Download source: https://modrinth.com/mod/regions-unexplored/version/XTrgsfIB
- packwiz `side`: both
- Category: worldgen (biomes)
- Why chosen: Extra Overworld/Nether biomes via TerraBlender. Not Expanded Ecosphere.
- Required dependencies: TerraBlender
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world. Terralith biomes get rarer next to this.
- World-data / removability: biomes and blocks stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### CorgiLib

- Pinned file / version: `Corgilib-Forge-1.20.1-4.0.3.5.jar` (Modrinth version `HXTB2EAy`)
- Download source: https://modrinth.com/mod/corgilib/version/HXTB2EAy
- packwiz `side`: both
- Category: library
- Why chosen: Required by Oh The Biomes We've Gone.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while BWG is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Oh The Trees You'll Grow

- Pinned file / version: `Oh-The-Trees-Youll-Grow-forge-1.20.1-1.7.0.jar` (Modrinth version `AAp1NdQX`)
- Download source: https://modrinth.com/mod/oh-the-trees-youll-grow/version/AAp1NdQX
- packwiz `side`: both
- Category: library (trees)
- Why chosen: Required by Oh The Biomes We've Gone.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while BWG is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Oh The Biomes We've Gone

- Pinned file / version: `Oh-The-Biomes-Weve-Gone-Forge-1.8.0.jar` (Modrinth version `8L5cwpjz`)
- Download source: https://modrinth.com/mod/oh-the-biomes-weve-gone/version/8L5cwpjz
- packwiz `side`: both
- Category: worldgen (biomes)
- Why chosen: BYG sequel. TerraBlender stack with Regions Unexplored.
- Required dependencies: CorgiLib, Oh The Trees You'll Grow, TerraBlender, GeckoLib (present)
- Optional dependencies: WTHIT (skipped; Jade is the overlay)
- Recommended companions: none
- Config changes: none — defaults. New world.
- World-data / removability: biomes and blocks stay in the save if removed
- License / attribution: All Rights Reserved; store pack distribution
- Date added: 2026-09-16

### Citadel

- Pinned file / version: `citadel-2.6.3-1.20.1.jar` (Modrinth version `lTAAe4sZ`)
- Download source: https://modrinth.com/mod/citadel/version/lTAAe4sZ
- packwiz `side`: both
- Category: library
- Why chosen: Required by Alex's Caves.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Alex's Caves is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Alex's Caves

- Pinned file / version: `alexscaves-2.0.2.jar` (Modrinth version `lC8HHXOF`)
- Download source: https://modrinth.com/mod/alexs-caves/version/lC8HHXOF
- packwiz `side`: both
- Category: worldgen (cave biomes)
- Why chosen: Six rare underground biomes. Not a second surface overhaul.
- Required dependencies: Citadel
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world. Tectonic can hide some cave biomes; best-effort.
- World-data / removability: biomes, blocks, and mobs stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Terralith

- Pinned file / version: `Terralith_1.20.x_v2.5.4.jar` (Modrinth version `WeYhEb5d`)
- Download source: https://modrinth.com/mod/terralith/version/WeYhEb5d
- packwiz `side`: both
- Category: worldgen (biomes)
- Why chosen: Extra Overworld biomes. Next to RU+BWG they generate rarer and smaller (author-documented).
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Tectonic (shipped)
- Config changes: none — defaults. New world.
- World-data / removability: biomes stay in chunks if removed
- License / attribution: Stardust Labs License; store pack distribution
- Date added: 2026-09-16

### Tectonic

- Pinned file / version: `tectonic-3.0.17-forge-1.20.1.jar` (Modrinth version `KLmvRxwh`)
- Download source: https://modrinth.com/mod/tectonic/version/KLmvRxwh
- packwiz `side`: both
- Category: worldgen (terrain)
- Why chosen: Big continents and mountains. Not Lithosphere. Forge jar already blends with Terralith (not Terratonic).
- Required dependencies: Lithostitched 1.4.11+ (Modrinth version metadata lists none; the jar still fails without it)
- Optional dependencies: none
- Recommended companions: Terralith (shipped)
- Config changes: `pack/config/tectonic.json` — Continents Scale `0.11`, Ocean Offset `-0.92`, temperature/vegetation scale `0.125` (larger biomes) ([configs.md](configs.md))
- World-data / removability: changes Overworld shape; old chunks stay old
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Lithostitched

- Pinned file / version: `lithostitched-forge-1.20.1-1.4.11.jar` (Modrinth version `srPoHKt8`)
- Download source: https://modrinth.com/mod/lithostitched/version/srPoHKt8
- packwiz `side`: both
- Category: library (worldgen)
- Why chosen: Hard requirement of Tectonic 3.0.17 (`lithostitched` 1.4.11 or above). Missing it is a boot error, not optional.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none
- World-data / removability: library; remove only with Tectonic
- License / attribution: MIT; https://modrinth.com/mod/lithostitched
- Date added: 2026-09-16

### YUNG's Bridges

- Pinned file / version: `YungsBridges-1.20-Forge-4.0.3.jar` (Modrinth version `KgO1gfM2`)
- Download source: https://modrinth.com/mod/yungs-bridges/version/KgO1gfM2
- packwiz `side`: both
- Category: worldgen (features)
- Why chosen: River bridges. Tectonic/Terralith make them rarer; 4.0.3 bakes `rarity_filter` chance `3` in the jar.
- Required dependencies: YUNG's API (present)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — no pack toml for spawn rate on this file
- World-data / removability: generated features stay in chunks
- License / attribution: LGPL-3.0-only; see Modrinth project page
- Date added: 2026-09-16

### YUNG's Better Caves

- Pinned file / version: `YungsBetterCaves-1.20.1-Forge-2.0.7.jar` (Modrinth version `BO1vVvun`)
- Download source: https://modrinth.com/mod/yungs-better-caves/version/BO1vVvun
- packwiz `side`: both
- Category: worldgen (caves)
- Why chosen: Overworld cave carvers only (`#minecraft:is_overworld`). Nether stays Amplified/BetterNether.
- Required dependencies: YUNG's API (present)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — already Overworld-only
- World-data / removability: carved caves stay in chunks
- License / attribution: LGPL-3.0-only; see Modrinth project page
- Date added: 2026-09-16

### YetAnotherConfigLib (YACL)

- Pinned file / version: `yet_another_config_lib_v3-3.6.6+1.20.1-forge.jar` (Modrinth version `sCWgXDYQ`)
- Download source: https://modrinth.com/mod/yacl/version/sCWgXDYQ
- packwiz `side`: both
- Category: library (config GUI)
- Why chosen: Required by Structurify.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while Structurify is installed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Structurify - Structure Control

- Pinned file / version: `structurify-forge-2.0.37+mc1.20.1.jar` (Modrinth version `FMlB4OQ1`)
- Download source: https://modrinth.com/mod/structurify/version/FMlB4OQ1
- packwiz `side`: both
- Category: worldgen (structure spacing)
- Why chosen: Structure Control for ruined portals, villages, strongholds, custom ids.
- Required dependencies: YACL
- Optional dependencies: none
- Recommended companions: Sparse Structures (shipped at spread 1)
- Config changes: `pack/config/structurify.json` — global spacing modifier **off** so it does not stack with Sparse
- World-data / removability: clean to remove; already-generated structures stay
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Sparse Structures

- Pinned file / version: `sparsestructures-forge-1.20.1-3.0.jar` (Modrinth version `oqEnX6AN`)
- Download source: https://modrinth.com/mod/sparsestructures/version/oqEnX6AN
- packwiz `side`: both
- Category: worldgen (structure spacing)
- Why chosen: Unique salts per structure set (`idBasedSalt`). Spread factor is **1** (vanilla density) so locates match placed structures.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: `pack/config/sparsestructures.json5` `spreadFactor` 1 ([configs.md](configs.md))
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Epic Structures: Villages

- Pinned file / version: `epic-structures-villages-2.0.0.jar` (Modrinth version `hCRa4eFr`)
- Download source: https://modrinth.com/mod/epic-structures-villages/version/hCRa4eFr
- packwiz `side`: both
- Category: worldgen (villages)
- Why chosen: Village overhaul from the Epic Structures set.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world.
- World-data / removability: generated structures stay in chunks
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Epic Structures: Dungeons

- Pinned file / version: `epic-structures-dungeons-1.0.jar` (Modrinth version `fMMms6dF`)
- Download source: https://modrinth.com/mod/epic-structures-dungeons/version/fMMms6dF
- packwiz `side`: both
- Category: worldgen (dungeons)
- Why chosen: Dungeon overhaul from the Epic Structures set. Pin the 1.20-native 1.0 jar (`pack_format` 15). 1.1+ (including files tagged 1.20) bake 1.21 `components` NBT into item frames, so 1.20.1 logs “Unable to load item” / hanging entity at invalid position and can hitch the server.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none. Do not bump to 1.2.5 (`tcsK0UPh`) or the later unified jars.
- World-data / removability: generated structures stay in chunks. Chunks already generated with 1.2.5 keep empty frames until those chunks are wiped.
- License / attribution: see Modrinth project page
- Date added: 2026-09-16
- Date updated: 2026-09-16 (1.2.5 → 1.0 1.20-native)

### Epic Structures: Witch Huts

- Pinned file / version: `Epic Witch Huts v1.3.1.jar` (Modrinth version `WAWShTQy`)
- Download source: https://modrinth.com/mod/epic-structures-witch-huts/version/WAWShTQy
- packwiz `side`: both
- Category: worldgen (witch huts)
- Why chosen: Witch hut overhaul from the Epic Structures set.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world.
- World-data / removability: generated structures stay in chunks
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Epic Structures: Jungle Temples

- Pinned file / version: `Epic Jungle Temples v1.0.2.jar` (Modrinth version `aN4PmOt6`)
- Download source: https://modrinth.com/mod/epic-structures-jungle-temples/version/aN4PmOt6
- packwiz `side`: both
- Category: worldgen (jungle temples)
- Why chosen: Jungle temple overhaul from the Epic Structures set.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world.
- World-data / removability: generated structures stay in chunks
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### When Dungeons Arise

- Pinned file / version: `DungeonsArise-1.20.x-2.1.58-release.jar` (Modrinth version `6hQpx5Tc`)
- Download source: https://modrinth.com/mod/when-dungeons-arise/version/6hQpx5Tc
- packwiz `side`: both
- Category: worldgen (dungeons)
- Why chosen: Extra overworld dungeons.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Seven Seas (shipped)
- Config changes: none — defaults. New world.
- World-data / removability: generated structures stay in chunks
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### When Dungeons Arise: Seven Seas

- Pinned file / version: `DungeonsAriseSevenSeas-1.20.x-1.0.2-forge.jar` (Modrinth version `Ak226ElN`)
- Download source: https://modrinth.com/mod/when-dungeons-arise-seven-seas/version/Ak226ElN
- packwiz `side`: both
- Category: worldgen (ocean dungeons)
- Why chosen: Ocean WDA. Pinned the `1.20.x` jar, not the `1.19.2`-named file also tagged 1.20.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults. New world.
- World-data / removability: generated structures stay in chunks
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Create: Sky Village

- Pinned file / version: `create_sky_village-0.0.38 Forge 1.20.1.jar` (Modrinth version `630wzTP1`)
- Download source: https://modrinth.com/mod/create-sky-village/version/630wzTP1
- packwiz `side`: both
- Category: worldgen (Create)
- Why chosen: Create is already in.
- Required dependencies: Create (present)
- Optional dependencies: none
- Recommended companions: none
- Config changes: `pack/config/create_sky_village-common.toml` — spacing 32 / separation 16, height offset 64 ([configs.md](configs.md))
- World-data / removability: generated structures stay in chunks
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Streams Reflowing

- Pinned file / version: `StreamsReflowing-1.20.1-forge-2.13.7.jar` (Modrinth version `OZN2NMml`)
- Download source: https://modrinth.com/mod/streams-reflowing/version/OZN2NMml
- packwiz `side`: both
- Category: worldgen (rivers)
- Why chosen: Real flowing rivers on Tectonic terrain. 2.13.7 is the spawn-chunk stall fix: currents prepare several times faster on multi-core, arrive with the land, and large plates no longer rebuild every stream network on dedicated start. Worlds from 2.12.9+ keep existing streams.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: `pack/config/streamsreflowing-common.toml` — `terrainAccuracyLevel = "LOW"` (author default MEDIUM). Coarser rivers, cheaper plates on Tectonic. New chunks only after restart. Do not add Ksyxis or C2ME.
- World-data / removability: river shape stays in chunks
- License / attribution: see Modrinth project page
- Date added: 2026-09-16
- Date updated: 2026-09-16 (2.13.5 → 2.13.7)

### Countered's Terrain Slabs

- Pinned file / version: `terrain_slabs-forge-4.0.3-beta.jar` (Modrinth version `fhdOSK5I`)
- Download source: https://modrinth.com/mod/countereds-terrain-slabs/version/fhdOSK5I
- packwiz `side`: both
- Category: worldgen (terrain mesh)
- Why chosen: Smooths stair-step terrain. **Beta**. Architectury already in.
- Required dependencies: Architectury API (present)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: visual/collision mesh; removing changes slopes in existing chunks
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Nature's Compass

- Pinned file / version: `NaturesCompass-1.20.1-1.12.0-forge.jar` (Modrinth version `eRSDvCjN`)
- Download source: https://modrinth.com/mod/natures-compass/version/eRSDvCjN
- packwiz `side`: both
- Category: utility (biome locator)
- Why chosen: Find biomes in a stacked TerraBlender + Terralith world.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Explorer's Compass (shipped)
- Config changes: none — defaults
- World-data / removability: items stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Explorer's Compass

- Pinned file / version: `ExplorersCompass-1.20.1-1.4.0-forge.jar` (Modrinth version `7ZdJbCOx`)
- Download source: https://modrinth.com/mod/explorers-compass/version/7ZdJbCOx
- packwiz `side`: both
- Category: utility (structure locator)
- Why chosen: Find structures in a dense structure stack.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Nature's Compass (shipped)
- Config changes: none — defaults
- World-data / removability: items stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Chunky

- Pinned file / version: `Chunky-1.3.146.jar` (Modrinth version `4FTDk9wv`)
- Download source: https://modrinth.com/mod/chunky/version/4FTDk9wv
- packwiz `side`: both
- Category: admin (pregen)
- Why chosen: Pregenerate chunks. Writes the world.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — run a radius on purpose ([configs.md](configs.md))
- World-data / removability: already-written chunks stay; the mod itself is clean to remove
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### Distant Horizons

- Pinned file / version: `DistantHorizons-3.2.0-b-1.20.1-fabric-forge.jar` (Modrinth version `FWGxbEM3`)
- Download source: https://modrinth.com/mod/distanthorizons/version/FWGxbEM3
- packwiz `side`: client
- Category: rendering (LOD)
- Why chosen: Optional far terrain. **Beta.** Dedicated server must not run it.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: Oculus 1.8.0 (already claims DH 2.2+ shader support)
- Config changes: `pack/config/DistantHorizons.toml` — renderer off, distant gen off, floor quality if enabled. Launcher JVM: `pack/user_jvm_args.txt` (`-XX:+UseZGC` on Java 17). Prism sync applies it ([configs.md](configs.md), CONTRIBUTING.md).
- World-data / removability: LOD databases under the instance; clean to remove the mod. Existing LODs stay on disk until deleted.
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Balm

- Pinned file / version: `balm-forge-1.20.1-7.3.43.jar` (Modrinth version `1VlYVa3k`)
- Download source: https://modrinth.com/mod/balm/version/1VlYVa3k
- packwiz `side`: both
- Category: library
- Why chosen: Required by Waystones, Crafting Tweaks, NetherPortalFix, TrashSlot, Default Options.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while those mods are in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Moonlight Lib

- Pinned file / version: `moonlight-1.20-2.16.35-forge.jar` (Modrinth version `W0ZWjZib`)
- Download source: https://modrinth.com/mod/moonlight/version/W0ZWjZib
- packwiz `side`: both
- Category: library
- Why chosen: Required by Supplementaries and MmmMmmMmmMmm.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while those mods are in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Patchouli

- Pinned file / version: `Patchouli-1.20.1-85-FORGE.jar` (Modrinth version `94dtOLgZ`)
- Download source: https://modrinth.com/mod/patchouli/version/94dtOLgZ
- packwiz `side`: both
- Category: library (books)
- Why chosen: Required by Ars Nouveau.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while Ars is in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### GuideME

- Pinned file / version: `guideme-20.1.15.jar` (Modrinth version `i7Tp1AHw`)
- Download source: https://modrinth.com/mod/guideme/version/i7Tp1AHw
- packwiz `side`: both
- Category: library (guides)
- Why chosen: Required by AE2 15.4.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while AE2 is in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Searchables

- Pinned file / version: `Searchables-forge-1.20.1-1.0.3.jar` (Modrinth version `PM9yAW1G`)
- Download source: https://modrinth.com/mod/searchables/version/PM9yAW1G
- packwiz `side`: client
- Category: library
- Why chosen: Required by Controlling.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client library; keep while Controlling is in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Konkrete

- Pinned file / version: `konkrete_forge_1.8.0_MC_1.20-1.20.1.jar` (Modrinth version `skYziQQL`)
- Download source: https://modrinth.com/mod/konkrete/version/skYziQQL
- packwiz `side`: client
- Category: library
- Why chosen: Required by FancyMenu and Drippy.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client library; keep while FancyMenu/Drippy are in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Melody

- Pinned file / version: `melody_forge_1.0.3_MC_1.20.1-1.20.4.jar` (Modrinth version `lJlW5r8R`)
- Download source: https://modrinth.com/mod/melody/version/lJlW5r8R
- packwiz `side`: client
- Category: library
- Why chosen: Required by FancyMenu 3.9.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client library; keep while FancyMenu is in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Ars Nouveau

- Pinned file / version: `ars_nouveau-1.20.1-4.12.7-all.jar` (Modrinth version `Hw2aD01e`)
- Download source: https://modrinth.com/mod/ars-nouveau/version/Hw2aD01e
- packwiz `side`: both
- Category: magic
- Why chosen: Spellcraft. Planned magic line. EMI plugin in-jar.
- Required dependencies: Patchouli, Geckolib (already in)
- Optional dependencies: Curios (already in)
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: blocks, glyphs, and Archwood stay in the save if removed. New chunks for wild Archwood.
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Applied Energistics 2

- Pinned file / version: `appliedenergistics2-forge-15.4.10.jar` (Modrinth version `7KVs6HMQ`)
- Download source: https://modrinth.com/mod/ae2/version/7KVs6HMQ
- packwiz `side`: both
- Category: storage (network)
- Why chosen: Item/fluid network. Native EMI in this file — no JEI, no extra EMI addon.
- Required dependencies: GuideME
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: cables, drives, and meteors stay in the save if removed. New chunks for meteorites.
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### The Twilight Forest

- Pinned file / version: `twilightforest-1.20.1-4.3.2508-universal.jar` (CurseForge file `5468648`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/the-twilight-forest/files/5468648
- packwiz `side`: both
- Category: dimension
- Why chosen: Adventure dimension. Official CurseForge jar, not the Modrinth unofficial port.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: the TF dimension and portal blocks stay if removed. New overworld chunks for portals.
- License / attribution: see CurseForge project page
- Date added: 2026-09-16

### Supplementaries

- Pinned file / version: `supplementaries-1.20-3.1.43-forge.jar` (Modrinth version `S0TIJ1hU`)
- Download source: https://modrinth.com/mod/supplementaries/version/S0TIJ1hU
- packwiz `side`: both
- Category: vanilla-plus
- Why chosen: Extra blocks/items. EMI plugin in-jar.
- Required dependencies: Moonlight Lib
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: blocks and items stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Waystones

- Pinned file / version: `waystones-forge-1.20.1-14.1.21.jar` (Modrinth version `Y0IgdaoP`)
- Download source: https://modrinth.com/mod/waystones/version/Y0IgdaoP
- packwiz `side`: both
- Category: utility (warps)
- Why chosen: Public warps. Homes stay FTB Essentials.
- Required dependencies: Balm
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: waystone blocks stay in the save if removed. New village chunks may place waystones.
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Lootr

- Pinned file / version: `lootr-forge-1.20-0.7.35.94.jar` (Modrinth version `mWTXC1ZX`)
- Download source: https://modrinth.com/mod/lootr/version/mWTXC1ZX
- packwiz `side`: both
- Category: loot
- Why chosen: Per-player dungeon loot. Does not replace Sophisticated Storage.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: converted loot chests stay as Lootr blocks if removed until converted back
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### MmmMmmMmmMmm

- Pinned file / version: `dummmmmmy-1.20-2.0.12-forge.jar` (Modrinth version `c1HMqDvI`)
- Download source: https://modrinth.com/mod/mmmmmmmmmmmm/version/c1HMqDvI
- packwiz `side`: both
- Category: combat (dummy)
- Why chosen: Target dummy for testing damage.
- Required dependencies: Moonlight Lib
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: placed dummies stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Polymorph

- Pinned file / version: `polymorph-forge-0.49.10+1.20.1.jar` (Modrinth version `UZBKtFyR`)
- Download source: https://modrinth.com/mod/polymorph/version/UZBKtFyR
- packwiz `side`: both
- Category: recipes
- Why chosen: Overlapping recipes (Farmer's Delight / Create / AE2 / Ars). Stay on 0.49.10 — 0.49.11 optionally requires JEI 15.57.0.207+, which TMRV's stub reports as 15.20.0.132 and Forge treats as a load failure.
- Required dependencies: none
- Optional dependencies: JEI (not declared on 0.49.10; skipped — EMI + TMRV is the viewer)
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Crafting Tweaks

- Pinned file / version: `craftingtweaks-forge-1.20.1-18.2.9.jar` (Modrinth version `KOqT9kSZ`)
- Download source: https://modrinth.com/mod/crafting-tweaks/version/KOqT9kSZ
- packwiz `side`: both
- Category: utility (crafting UI)
- Why chosen: Rotate/balance/clear crafting grids.
- Required dependencies: Balm
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### NetherPortalFix

- Pinned file / version: `netherportalfix-forge-1.20-13.0.1.jar` (Modrinth version `cWPAnu7u`)
- Download source: https://modrinth.com/mod/netherportalfix/version/cWPAnu7u
- packwiz `side`: both
- Category: utility (portals)
- Why chosen: Return-portal linking. `both` so Prism singleplayer matches the dedicated server (Modrinth marks the file server-only).
- Required dependencies: Balm
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove; vanilla linking returns
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### TrashSlot

- Pinned file / version: `trashslot-forge-1.20.1-15.1.5.jar` (Modrinth version `r0K8IYd7`)
- Download source: https://modrinth.com/mod/trashslot/version/r0K8IYd7
- packwiz `side`: both
- Category: utility (inventory)
- Why chosen: Inventory trash slot. Different from FTB `/trashcan`.
- Required dependencies: Balm
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Controlling

- Pinned file / version: `Controlling-forge-1.20.1-12.0.2.jar` (Modrinth version `LH6Bi6Am`)
- Download source: https://modrinth.com/mod/controlling/version/LH6Bi6Am
- packwiz `side`: client
- Category: utility (controls)
- Why chosen: Searchable keybind screen.
- Required dependencies: Searchables
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Mouse Tweaks

- Pinned file / version: `MouseTweaks-forge-mc1.20.1-2.25.1.jar` (Modrinth version `7JVXOe3K`)
- Download source: https://modrinth.com/mod/mouse-tweaks/version/7JVXOe3K
- packwiz `side`: client
- Category: utility (inventory)
- Why chosen: Drag-to-move stacks in inventories.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Better Advancements

- Pinned file / version: `BetterAdvancements-Forge-1.20.1-0.6.0.73.jar` (Modrinth version `zKOCnRdK`)
- Download source: https://modrinth.com/mod/better-advancements/version/zKOCnRdK
- packwiz `side`: client
- Category: utility (UI)
- Why chosen: Readable advancement tree.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### FancyMenu

- Pinned file / version: `fancymenu_forge_3.9.12_MC_1.20.1.jar` (Modrinth version `ucAaUjAE`)
- Download source: https://modrinth.com/mod/fancymenu/version/ucAaUjAE
- packwiz `side`: client
- Category: menu framework
- Why chosen: Required by Drippy. No custom title art yet.
- Required dependencies: Konkrete, Melody
- Optional dependencies: none
- Recommended companions: Drippy Loading Screen
- Config changes: none — no custom layout until one is chosen
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Drippy Loading Screen

- Pinned file / version: `drippyloadingscreen_forge_3.1.5_MC_1.20.1.jar` (Modrinth version `Nof419YS`)
- Download source: https://modrinth.com/mod/drippy-loading-screen/version/Nof419YS
- packwiz `side`: client
- Category: loading overlay
- Why chosen: Loading screen. Needs FancyMenu.
- Required dependencies: FancyMenu, Konkrete
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client; clean to remove
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Default Options

- Pinned file / version: `defaultoptions-forge-1.20.1-18.0.5.jar` (Modrinth version `AVz3mvZZ`)
- Download source: https://modrinth.com/mod/default-options/version/AVz3mvZZ
- packwiz `side`: client
- Category: utility (pack defaults)
- Why chosen: Unbind FTB Chunks Open Map without shipping a full `options.txt`.
- Required dependencies: Balm
- Optional dependencies: none
- Recommended companions: none
- Config changes: `pack/config/defaultoptions/keybindings.txt` unbinds `key.ftbchunks.map` ([configs.md](configs.md))
- World-data / removability: client; removing it does not restore **M** on instances that already saved the unbound key
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Too Fast

- Pinned file / version: `toofast-1.20-0.4.3.5.jar` (Modrinth version `2pix3xrW`)
- Download source: https://modrinth.com/mod/too-fast/version/2pix3xrW
- packwiz `side`: server
- Category: utility (movement checks)
- Why chosen: Stops dedicated-server “moved too quickly” rubber-banding on Create trains and other fast travel. Noobanidus (same author as Lootr). Modrinth marks it server-only.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: mixin only; clean to remove. Vanilla speed checks return.
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### Amendments

- Pinned file / version: `amendments-1.20-2.2.6.jar` (Modrinth version `nJORWvdh`)
- Download source: https://modrinth.com/mod/amendments/version/nJORWvdh
- packwiz `side`: both
- Category: vanilla-plus
- Why chosen: Supplementaries 3.x moved wall lanterns, skull candles, ceiling pots/banners, and skull piles here. Without it those placed blocks vanish.
- Required dependencies: Moonlight Lib (already in)
- Optional dependencies: none
- Recommended companions: Supplementaries
- Config changes: none — defaults
- World-data / removability: blocks stay in the save if removed
- License / attribution: Supplementaries Team License 1.1; see Modrinth project page
- Date added: 2026-09-16

### SuperMartijn642's Core Lib

- Pinned file / version: `supermartijn642corelib-1.1.24a-forge-mc1.20.1.jar` (Modrinth version `Rty5QRB6`)
- Download source: https://modrinth.com/mod/supermartijn642s-core-lib/version/Rty5QRB6
- packwiz `side`: both
- Category: library
- Why chosen: Required by Trash Cans
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while Trash Cans is in
- License / attribution: All Rights Reserved; see Modrinth project page
- Date added: 2026-09-16

### SuperMartijn642's Config Lib

- Pinned file / version: `supermartijn642configlib-1.1.8-forge-mc1.20.jar` (Modrinth version `ZKor79dR`)
- Download source: https://modrinth.com/mod/supermartijn642s-config-lib/version/ZKor79dR
- packwiz `side`: both
- Category: library
- Why chosen: Required by Trash Cans
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while Trash Cans is in
- License / attribution: All Rights Reserved; see Modrinth project page
- Date added: 2026-09-16

### Trash Cans

- Pinned file / version: `trashcans-1.1.0a-forge-mc1.20.4.jar` (Modrinth version `iiNJsz5q`; file lists 1.20–1.20.4 Forge)
- Download source: https://modrinth.com/mod/trash-cans/version/iiNJsz5q
- packwiz `side`: both
- Category: utility (void)
- Why chosen: Placeable item/fluid/energy voids for Create/AE2 lines. Different from TrashSlot and FTB `/trashcan`.
- Required dependencies: Core Lib, Config Lib
- Optional dependencies: Mekanism (not in)
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: blocks stay in the save if removed
- License / attribution: All Rights Reserved; see Modrinth project page
- Date added: 2026-09-16

### Jupiter

- Pinned file / version: `jupiter-2.3.7-1.20.1-forge.jar` (CurseForge file `7738299`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/jupiter/files/7738299
- packwiz `side`: both
- Category: library
- Why chosen: Required by IceAndFire Community Edition (config GUI)
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — IAF settings live in the Jupiter GUI
- World-data / removability: library; keep while IceAndFire CE is in
- License / attribution: see CurseForge project page
- Date added: 2026-09-16

### Uranus

- Pinned file / version: `uranus-2.2.6-bugfix.2-1.20.1-forge.jar` (CurseForge file `7745532`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/uranus/files/7745532
- packwiz `side`: both
- Category: library
- Why chosen: Required by IceAndFire Community Edition (animation/util; replaces Citadel for CE)
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while IceAndFire CE is in. Citadel stays for Alex's Caves.
- License / attribution: see CurseForge project page
- Date added: 2026-09-16

### IceAndFire Community Edition

- Pinned file / version: `IceAndFireCE-1.2.8-1.20.1-forge.jar` (CurseForge file `8757817`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/iceandfire-ce/files/8757817
- packwiz `side`: both
- Category: content (dragons)
- Why chosen: Maintained fork of Ice and Fire for 1.20.1. Original `2.1.13-beta-5` cannot load beside it.
- Required dependencies: Jupiter, Uranus
- Optional dependencies: EMI, Jade, Farmer's Delight (already in)
- Recommended companions: Ice and Fire Dragons X Better Combat
- Config changes: none — defaults. Tune spawn/structure rates in Jupiter if TPS drops.
- World-data / removability: dragons, structures, and blocks stay in the save. Do not swap to original Ice and Fire on an existing world.
- License / attribution: unofficial fork; see CurseForge project page
- Date added: 2026-09-16

### [TaCZ] Timeless and Classics Zero

- Pinned file / version: `tacz-1.20.1-1.1.8-hotfix.jar` (Modrinth version `yOVIzIJR`)
- Download source: https://modrinth.com/mod/timeless-and-classics-zero/version/yOVIzIJR
- packwiz `side`: both
- Category: content (guns)
- Why chosen: Official TACZ. Default gun pack is in this jar. Planned content.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: extra gun packs below
- Config changes: none — defaults
- World-data / removability: guns/ammo stay in the save if removed
- License / attribution: GPL-3.0; see Modrinth project page
- Date added: 2026-09-16

### [TACZ] LesRaisins Tactical Equipements

- Pinned file / version: `lrtactical-1.20.1-0.4.3.jar` (Modrinth version `eygQmqIl`)
- Download source: https://modrinth.com/mod/lr-tactical/version/eygQmqIl
- packwiz `side`: both
- Category: content (TACZ addon)
- Why chosen: Extra TACZ throwables/melee. Needs TACZ 1.1.8.
- Required dependencies: TACZ
- Optional dependencies: none
- Recommended companions: LesRaisins Append Pack
- Config changes: none — defaults
- World-data / removability: items stay in the save if removed
- License / attribution: GPL-3.0; see Modrinth project page
- Date added: 2026-09-16

### [TACZ] LesRaisins Append Pack

- Pinned file / version: `lradd-1.20.1-0.3.0.jar` (Modrinth version `KbReepVU`)
- Download source: https://modrinth.com/mod/lesraisins-weapon/version/KbReepVU
- packwiz `side`: both
- Category: content (TACZ gun pack)
- Why chosen: Extra LesRaisins guns
- Required dependencies: TACZ
- Optional dependencies: none
- Recommended companions: LesRaisins Tactical
- Config changes: none — defaults
- World-data / removability: guns stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### [TACZ] Gucci & Vuitton Attachments

- Pinned file / version: `guccivuitton-1.20.1-0.2.2.jar` (Modrinth version `NnUWhMdw`)
- Download source: https://modrinth.com/mod/tacz-gucci-vuitton-attachments/version/NnUWhMdw
- packwiz `side`: both
- Category: content (TACZ attachments)
- Why chosen: Extra TACZ attachments listed with community packs
- Required dependencies: TACZ
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: attachments stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### [TACZ Addons] Daffa's Arsenal

- Pinned file / version: `daffas_arsenal-3.7.1.1.jar` (Modrinth version `1Q9ypxVQ`)
- Download source: https://modrinth.com/mod/daffasarsenal/version/1Q9ypxVQ
- packwiz `side`: both
- Category: content (TACZ gun pack)
- Why chosen: Large extra gun pack, still updated
- Required dependencies: TACZ
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: guns stay in the save if removed
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Iceberg

- Pinned file / version: `Iceberg-1.20.1-forge-1.1.25.jar` (Modrinth version `BQ8rJPXV`)
- Download source: https://modrinth.com/mod/iceberg/version/BQ8rJPXV
- packwiz `side`: client
- Category: library
- Why chosen: Required by Legendary Tooltips and Equipment Compare
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client library; keep while those tooltip mods are in
- License / attribution: CC-BY-NC-ND-4.0; see Modrinth project page
- Date added: 2026-09-16

### Prism

- Pinned file / version: `Prism-1.20.1-forge-1.0.5.jar` (Modrinth version `FFyss87M`)
- Download source: https://modrinth.com/mod/prism-lib/version/FFyss87M
- packwiz `side`: client
- Category: library
- Why chosen: Required by Legendary Tooltips. Not Prism Launcher.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client library; keep while Legendary Tooltips is in
- License / attribution: CC-BY-NC-ND-4.0; see Modrinth project page
- Date added: 2026-09-16

### Legendary Tooltips

- Pinned file / version: `LegendaryTooltips-1.20.1-forge-1.4.5.jar` (Modrinth version `JhxD2e6J`)
- Download source: https://modrinth.com/mod/legendary-tooltips/version/JhxD2e6J
- packwiz `side`: client
- Category: utility (UI)
- Why chosen: Rarity frames on item hover
- Required dependencies: Iceberg, Prism
- Optional dependencies: Equipment Compare
- Recommended companions: Equipment Compare
- Config changes: none — defaults. If frames glitch, disable ImmediatelyFast `hud_batching`.
- World-data / removability: client; clean to remove
- License / attribution: CC-BY-NC-ND-4.0; see Modrinth project page
- Date added: 2026-09-16

### Equipment Compare

- Pinned file / version: `EquipmentCompare-1.20.1-forge-1.3.7.jar` (Modrinth version `x1lxEKIp`)
- Download source: https://modrinth.com/mod/equipment-compare/version/x1lxEKIp
- packwiz `side`: client
- Category: utility (UI)
- Why chosen: Shift-compare equipped gear
- Required dependencies: Iceberg
- Optional dependencies: Legendary Tooltips
- Recommended companions: Legendary Tooltips
- Config changes: none — defaults
- World-data / removability: client; clean to remove
- License / attribution: CC-BY-NC-ND-4.0; see Modrinth project page
- Date added: 2026-09-16

### Fzzy Config

- Pinned file / version: `fzzy_config-0.7.7+1.20.1+forge.jar` (Modrinth version `53kg5uoF`)
- Download source: https://modrinth.com/mod/fzzy-config/version/53kg5uoF
- packwiz `side`: both
- Category: library
- Why chosen: Required by Simply Swords 1.70. Not EMI Loot.
- Required dependencies: Kotlin for Forge (already in)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while Simply Swords is in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Simply Tooltips

- Pinned file / version: `SimplyTooltips-forge-0.1.5-1.20.1.jar` (Modrinth version `s87jNabF`)
- Download source: https://modrinth.com/mod/simply-tooltips/version/s87jNabF
- packwiz `side`: client
- Category: library
- Why chosen: Required by Simply Swords 1.70
- Required dependencies: Fzzy Config, Architectury (already in)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: client library; keep while Simply Swords is in
- License / attribution: see Modrinth project page
- Date added: 2026-09-16

### Simply Swords

- Pinned file / version: `simplyswords-forge-neoforge-1.70.2-1.20.1.jar` (Modrinth version `Na6e94J1`)
- Download source: https://modrinth.com/mod/simply-swords/version/Na6e94J1
- packwiz `side`: both
- Category: content (weapons)
- Why chosen: Extra weapon types. This file’s loot inject works with Lootr.
- Required dependencies: Fzzy Config, Simply Tooltips, Architectury (already in)
- Optional dependencies: Better Combat (installed)
- Recommended companions: Simply More
- Config changes: none — defaults
- World-data / removability: weapons stay in the save if removed
- License / attribution: custom; see Modrinth project page
- Date added: 2026-09-16

### Simply More

- Pinned file / version: `simplymore-forge-neoforge-1.1.4+1.20.1.jar` (Modrinth version `u4dfPRHB`)
- Download source: https://modrinth.com/mod/simplymore/version/u4dfPRHB
- packwiz `side`: both
- Category: content (weapons)
- Why chosen: More Simply Swords types. 1.1.4 is the holdover that boots with Simply Swords 1.70.
- Required dependencies: Simply Swords
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: weapons stay in the save if removed
- License / attribution: All Rights Reserved; see Modrinth project page
- Date added: 2026-09-16

### playerAnimator

- Pinned file / version: `player-animation-lib-forge-1.0.2-rc1+1.20.jar` (Modrinth version `xe2EVE6q`)
- Download source: https://modrinth.com/mod/playeranimator/version/xe2EVE6q
- packwiz `side`: both
- Category: library
- Why chosen: Required by Better Combat
- Required dependencies: none
- Optional dependencies: bendy-lib (not added)
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: library; keep while Better Combat is in
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### Better Combat

- Pinned file / version: `bettercombat-forge-1.9.0+1.20.1.jar` (Modrinth version `rnhiaw3t`)
- Download source: https://modrinth.com/mod/better-combat/version/rnhiaw3t
- packwiz `side`: both
- Category: combat
- Why chosen: Melee animations for Simply Swords / IAF / Alex's Caves. Guns stay TACZ.
- Required dependencies: playerAnimator, Cloth Config (already in)
- Optional dependencies: none
- Recommended companions: IAF x Better Combat, Alex's Caves Better Combat
- Config changes: none — defaults
- World-data / removability: mixin/animations; clean to remove
- License / attribution: All Rights Reserved; see Modrinth project page
- Date added: 2026-09-16

### Ice and Fire Dragons X Better Combat

- Pinned file / version: `iceandfirebettercombat.jar` (Modrinth version `d5Vp1w6z`)
- Download source: https://modrinth.com/mod/ice-and-fire-dragons-x-better-combat/version/d5Vp1w6z
- packwiz `side`: both
- Category: combat (compat)
- Why chosen: Maps Ice and Fire weapons onto Better Combat. packwiz `both` so Prism singleplayer gets it (store tag is server-only).
- Required dependencies: Better Combat, IceAndFire CE
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: animation map; clean to remove
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### Alex's Caves Better Combat

- Pinned file / version: `alexscavesbettercombat.jar` (Modrinth version `25y1lqsO`)
- Download source: https://modrinth.com/mod/alexs-caves-better-combat/version/25y1lqsO
- packwiz `side`: both
- Category: combat (compat)
- Why chosen: Maps Alex's Caves weapons onto Better Combat. packwiz `both` so Prism singleplayer gets it.
- Required dependencies: Better Combat, Alex's Caves (already in)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: animation map; clean to remove
- License / attribution: MIT; see Modrinth project page
- Date added: 2026-09-16

### Ars Elemental

- Pinned file / version: `ars_elemental-1.20.1-0.6.8.0.jar` (CurseForge file `8399870`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/ars-elemental/files/8399870
- packwiz `side`: both
- Category: magic (Ars addon)
- Why chosen: Elemental foci, glyphs, and armor for Ars Nouveau 4.12.7. Author ships 1.20.1 on CurseForge only.
- Required dependencies: Ars Nouveau (kept on Modrinth `Hw2aD01e`)
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: blocks, foci, and familiars stay in the save if removed
- License / attribution: see CurseForge project page
- Date added: 2026-09-16

## Credits / Attribution

Credit each author via the project URL above when distributing the pack. Recheck licenses before a public store upload if a project is All Rights Reserved or requires explicit permission.

| Mod | Project |
|---|---|
| Embeddium | https://modrinth.com/mod/embeddium |
| Oculus | https://modrinth.com/mod/oculus |
| FerriteCore | https://modrinth.com/mod/ferrite-core |
| ImmediatelyFast | https://modrinth.com/mod/immediatelyfast |
| ModernFix | https://modrinth.com/mod/modernfix |
| FastWorkbench | https://modrinth.com/mod/fastworkbench |
| Placebo | https://modrinth.com/mod/placebo |
| FastFurnace | https://modrinth.com/mod/fastfurnace |
| BadOptimizations | https://modrinth.com/mod/badoptimizations |
| Embeddium Extra | https://modrinth.com/mod/rubidium-extra |
| Crash Assistant | https://modrinth.com/mod/crash-assistant |
| Radium | https://modrinth.com/mod/radium |
| Let Me Despawn | https://modrinth.com/mod/lmd |
| Almanac | https://modrinth.com/mod/almanac |
| AllTheLeaks | https://www.curseforge.com/minecraft/mc-mods/alltheleaks |
| Entity Culling | https://modrinth.com/mod/entityculling |
| Dynamic FPS | https://modrinth.com/mod/dynamic-fps |
| FastSuite | https://modrinth.com/mod/fastsuite |
| Noisium | https://modrinth.com/mod/noisium |
| Clumps | https://modrinth.com/mod/clumps |
| Smooth Chunk Save | https://www.curseforge.com/minecraft/mc-mods/smooth-chunk-save |
| Cupboard | https://www.curseforge.com/minecraft/mc-mods/cupboard |
| Neruina | https://modrinth.com/mod/neruina |
| Architectury API | https://modrinth.com/mod/architectury-api |
| Kotlin for Forge | https://modrinth.com/mod/kotlin-for-forge |
| FTB Library | https://www.curseforge.com/minecraft/mc-mods/ftb-library-forge |
| FTB Teams | https://www.curseforge.com/minecraft/mc-mods/ftb-teams-forge |
| FTB Chunks | https://www.curseforge.com/minecraft/mc-mods/ftb-chunks-forge |
| FTB Quests | https://www.curseforge.com/minecraft/mc-mods/ftb-quests-forge |
| FTB Ultimine | https://www.curseforge.com/minecraft/mc-mods/ftb-ultimine-forge |
| FTB Essentials | https://www.curseforge.com/minecraft/mc-mods/ftb-essentials |
| FTB XMod Compat | https://www.curseforge.com/minecraft/mc-mods/ftb-xmod-compat |
| FTB Filter System | https://www.curseforge.com/minecraft/mc-mods/ftb-filter-system |
| Jade | https://modrinth.com/mod/jade |
| EMI | https://modrinth.com/mod/emi |
| Too Many Recipe Viewers | https://modrinth.com/mod/tmrv |
| Accelerated Decay | https://www.curseforge.com/minecraft/mc-mods/accelerated-decay |
| Create | https://modrinth.com/mod/create |
| Create Ultimine | https://modrinth.com/mod/create-ultimine |
| Colorwheel | https://modrinth.com/mod/colorwheel |
| Colorwheel Patcher | https://modrinth.com/mod/colorwheel-patcher |
| Xaero's Minimap | https://modrinth.com/mod/xaeros-minimap |
| Xaero's World Map | https://modrinth.com/mod/xaeros-world-map |
| Titanium | https://modrinth.com/mod/titanium |
| Functional Storage | https://modrinth.com/mod/functional-storage |
| Sophisticated Core | https://modrinth.com/mod/sophisticated-core |
| Curios API | https://modrinth.com/mod/curios |
| Sophisticated Storage | https://modrinth.com/mod/sophisticated-storage |
| Sophisticated Backpacks | https://modrinth.com/mod/sophisticated-backpacks |
| Sophisticated Storage Create Integration | https://modrinth.com/mod/sophisticated-storage-create-integration |
| Sophisticated Backpacks Create Integration | https://modrinth.com/mod/sophisticated-backpacks-create-integration |
| Amplified Nether | https://modrinth.com/mod/amplified-nether |
| WunderLib Forge | https://modrinth.com/mod/wunderlib-forge |
| BCLib Forge | https://modrinth.com/mod/bclib-forge |
| BetterNether Forge | https://modrinth.com/mod/betternether-forge |
| YUNG's API | https://modrinth.com/mod/yungs-api |
| YUNG's Better Nether Fortresses | https://modrinth.com/mod/yungs-better-nether-fortresses |
| GeckoLib | https://modrinth.com/mod/geckolib |
| Cloth Config API | https://modrinth.com/mod/cloth-config |
| Infernal Expansion Redux | https://modrinth.com/mod/infernal-expansion-redux |
| Stalwart Dungeons | https://modrinth.com/mod/stalwart-dungeons |
| Bygone Nether | https://modrinth.com/mod/bygone-nether |
| Farmer's Delight | https://modrinth.com/mod/farmers-delight |
| My Nether's Delight | https://modrinth.com/mod/my-nethers-delight |
| Library Ferret | https://modrinth.com/mod/library-ferret |
| Awesome Dungeon | https://modrinth.com/mod/awesome-dungeon |
| Awesome Dungeon Nether | https://modrinth.com/mod/awesome-dungeon-nether |
| Moog's Structure Lib | https://modrinth.com/mod/moogs-structure-lib |
| MMR - Moog's Mineshafts Reimagined | https://modrinth.com/mod/mmr-moogs-mineshafts-reimagined |
| TerraBlender | https://modrinth.com/mod/terrablender |
| Fragmentum | https://modrinth.com/mod/fragmentum |
| Aquamirae | https://modrinth.com/mod/aquamirae |
| Regions Unexplored | https://modrinth.com/mod/regions-unexplored |
| CorgiLib | https://modrinth.com/mod/corgilib |
| Oh The Trees You'll Grow | https://modrinth.com/mod/oh-the-trees-youll-grow |
| Oh The Biomes We've Gone | https://modrinth.com/mod/oh-the-biomes-weve-gone |
| Citadel | https://modrinth.com/mod/citadel |
| Alex's Caves | https://modrinth.com/mod/alexs-caves |
| Terralith | https://modrinth.com/mod/terralith |
| Tectonic | https://modrinth.com/mod/tectonic |
| Lithostitched | https://modrinth.com/mod/lithostitched |
| YUNG's Bridges | https://modrinth.com/mod/yungs-bridges |
| YUNG's Better Caves | https://modrinth.com/mod/yungs-better-caves |
| YetAnotherConfigLib | https://modrinth.com/mod/yacl |
| Structurify | https://modrinth.com/mod/structurify |
| Sparse Structures | https://modrinth.com/mod/sparsestructures |
| Epic Structures: Villages | https://modrinth.com/mod/epic-structures-villages |
| Epic Structures: Dungeons | https://modrinth.com/mod/epic-structures-dungeons |
| Epic Structures: Witch Huts | https://modrinth.com/mod/epic-structures-witch-huts |
| Epic Structures: Jungle Temples | https://modrinth.com/mod/epic-structures-jungle-temples |
| When Dungeons Arise | https://modrinth.com/mod/when-dungeons-arise |
| When Dungeons Arise: Seven Seas | https://modrinth.com/mod/when-dungeons-arise-seven-seas |
| Create: Sky Village | https://modrinth.com/mod/create-sky-village |
| Streams Reflowing | https://modrinth.com/mod/streams-reflowing |
| Countered's Terrain Slabs | https://modrinth.com/mod/countereds-terrain-slabs |
| Nature's Compass | https://modrinth.com/mod/natures-compass |
| Explorer's Compass | https://modrinth.com/mod/explorers-compass |
| Chunky | https://modrinth.com/mod/chunky |
| Distant Horizons | https://modrinth.com/mod/distanthorizons |
| Balm | https://modrinth.com/mod/balm |
| Moonlight Lib | https://modrinth.com/mod/moonlight |
| Patchouli | https://modrinth.com/mod/patchouli |
| GuideME | https://modrinth.com/mod/guideme |
| Searchables | https://modrinth.com/mod/searchables |
| Konkrete | https://modrinth.com/mod/konkrete |
| Melody | https://modrinth.com/mod/melody |
| Ars Nouveau | https://modrinth.com/mod/ars-nouveau |
| Applied Energistics 2 | https://modrinth.com/mod/ae2 |
| The Twilight Forest | https://www.curseforge.com/minecraft/mc-mods/the-twilight-forest |
| Supplementaries | https://modrinth.com/mod/supplementaries |
| Waystones | https://modrinth.com/mod/waystones |
| Lootr | https://modrinth.com/mod/lootr |
| MmmMmmMmmMmm | https://modrinth.com/mod/mmmmmmmmmmmm |
| Polymorph | https://modrinth.com/mod/polymorph |
| Crafting Tweaks | https://modrinth.com/mod/crafting-tweaks |
| NetherPortalFix | https://modrinth.com/mod/netherportalfix |
| TrashSlot | https://modrinth.com/mod/trashslot |
| Controlling | https://modrinth.com/mod/controlling |
| Mouse Tweaks | https://modrinth.com/mod/mouse-tweaks |
| Better Advancements | https://modrinth.com/mod/better-advancements |
| FancyMenu | https://modrinth.com/mod/fancymenu |
| Drippy Loading Screen | https://modrinth.com/mod/drippy-loading-screen |
| Default Options | https://modrinth.com/mod/default-options |
| Too Fast | https://modrinth.com/mod/too-fast |
| Amendments | https://modrinth.com/mod/amendments |
| SuperMartijn642's Core Lib | https://modrinth.com/mod/supermartijn642s-core-lib |
| SuperMartijn642's Config Lib | https://modrinth.com/mod/supermartijn642s-config-lib |
| Trash Cans | https://modrinth.com/mod/trash-cans |
| Jupiter | https://www.curseforge.com/minecraft/mc-mods/jupiter |
| Uranus | https://www.curseforge.com/minecraft/mc-mods/uranus |
| IceAndFire Community Edition | https://www.curseforge.com/minecraft/mc-mods/iceandfire-ce |
| [TaCZ] Timeless and Classics Zero | https://modrinth.com/mod/timeless-and-classics-zero |
| LesRaisins Tactical Equipements | https://modrinth.com/mod/lr-tactical |
| LesRaisins Append Pack | https://modrinth.com/mod/lesraisins-weapon |
| Gucci & Vuitton Attachments | https://modrinth.com/mod/tacz-gucci-vuitton-attachments |
| Daffa's Arsenal | https://modrinth.com/mod/daffasarsenal |
| Iceberg | https://modrinth.com/mod/iceberg |
| Prism | https://modrinth.com/mod/prism-lib |
| Legendary Tooltips | https://modrinth.com/mod/legendary-tooltips |
| Equipment Compare | https://modrinth.com/mod/equipment-compare |
| Fzzy Config | https://modrinth.com/mod/fzzy-config |
| Simply Tooltips | https://modrinth.com/mod/simply-tooltips |
| Simply Swords | https://modrinth.com/mod/simply-swords |
| Simply More | https://modrinth.com/mod/simplymore |
| playerAnimator | https://modrinth.com/mod/playeranimator |
| Better Combat | https://modrinth.com/mod/better-combat |
| Ice and Fire Dragons X Better Combat | https://modrinth.com/mod/ice-and-fire-dragons-x-better-combat |
| Alex's Caves Better Combat | https://modrinth.com/mod/alexs-caves-better-combat |
| Ars Elemental | https://www.curseforge.com/minecraft/mc-mods/ars-elemental |

## Future / Deferred Mods

| Mod | Why not now | What would change that |
|---|---|---|
| Shader packs | Loader (Oculus) is in; packs chosen later | Pick a pack on purpose and ship it |
| ServerCore | Overlaps Radium / Let Me Despawn; activation range is gameplay | Explicit ruleset decision |
| Better Beds Reforged | Tiny FPS; last file 1.0.0 (2023) | Want beds later |
| Iris & Oculus Flywheel Compat | Colorwheel is the Create + Oculus path and is incompatible with this jar | Do not add |
| Connectivity | Packet/timeout fixer; Cupboard already in | Create/AE2/Mekanism/TACZ multiplayer packet issues |
| Particle Core | Fzzy Config is now in for Simply Swords. Can hide gun/spell FX | Only with a whitelist config that does not strip TACZ / Ars particles |
| Create: Nowheel | Create + Entity Culling companion | Contraptions go invisible |
| Fast Item Frames | Needs Forge Config API Port; no Forge 1.20.1 file | Fabric-only FCAP or a native Forge FIF build |
| Expanded Ecosphere | Feature Order Cycle with RU + BWG | Drop RU/BWG first |
| Terratonic | Datapack-only Terralith+Tectonic blend | Stay on the Forge mod jars |
| Lithosphere | Same noise job as Tectonic | Drop Tectonic first |
| Sodium / Enhanced Block Entities | Embeddium + Oculus is the renderer | Do not add |
| Larion / Voxy / Atmospherics / Wet Sand / Luki's Ancient Cities | No usable Forge 1.20.1 file | A real 1.20.1 Forge build |
| C2ME / C2MEF / VMP / Krypton / Indium / More Culling / Debugify (asked slugs) | Fabric or unofficial/overlapping | See [performance.md](performance.md) Fabric video list |
| Storage Drawers | Functional Storage is the drawer line | Do not add both |
| Iron Chests | Sophisticated Storage is the chest-upgrade line | Do not add both |
| Tom’s Simple Storage | Would be a second item network next to AE2 | Do not add unless we drop AE2 |
| Incendium | Incompatible with Amplified Nether | Do not add |
| Infernal Expansion (original) | No 1.20.1 file | Stay on Infernal Expansion Redux |
| Nether’s Delight (`nethers-delight`) | Unmaintained 2023; My Nether’s Delight is the 1.20.1 addon | Do not add both |
| YUNG’s Better Mineshafts | MMR is the mineshaft line | Do not add both |
| Awesome Dungeon End / Ocean | Held this cut (overworld + Nether only) | If dungeon density still feels sparse |
| LambDynamicLights | Infernal Redux optional; Oculus is the light path | Do not add |

## Deferred Ecosystem Upgrades

None. Do not bump Minecraft or Forge to accommodate a single mod without a separate approved change.

## Removed

| Mod | Removed on | Why | Re-add? |
|---|---|---|---|
| EMI QoL Tweaks | 2026-09-13 | CurseForge third-party API download is disabled (`packwiz-installer` cannot fetch file `8713840`). No Modrinth/GitHub file. | Only if the author enables API distribution or posts the same file on Modrinth |
| StructureOverlapless | 2026-09-16 | Skips placement when a section is “occupied,” including by the same structure start. Dedicated logs skipped Sky Villages and WDA bandit towers at the `/locate` coords | Do not re-add unless a relocate-not-skip tool exists |
| Dungeons Arise Sparse Structures compat | 2026-09-16 | Extra thinning on top of Sparse Structures made WDA unfindable | Do not re-add while Sparse spread is 1 |
| Dungeons Arise Seven Seas Sparse Structures compat | 2026-09-16 | Same extra thinning for ocean WDA | Do not re-add while Sparse spread is 1 |


