# Lead and Leylines — mod manifest

Synced with `pack/mods/*.pw.toml` on 2026-09-13. Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml). Decision logs: [performance.md](performance.md), [utility.md](utility.md). Config notes: [configs.md](configs.md).

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
- Config changes: none — defaults
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
- Optional dependencies: Cloth Config (in-game screen only; not shipped)
- Recommended companions: none
- Config changes: none — defaults without Cloth Config
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

- Pinned file / version: `architectury-9.2.14-forge.jar` (CurseForge file `5137938`)
- Download source: https://www.curseforge.com/minecraft/mc-mods/architectury-api/files/5137938
- packwiz `side`: both
- Category: library
- Why chosen: Required by the FTB suite and EMI.
- Required dependencies: none
- Optional dependencies: none
- Recommended companions: none
- Config changes: none — defaults
- World-data / removability: do not remove while FTB mods or EMI are installed
- License / attribution: see CurseForge project page
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
- Config changes: none — defaults
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
- Why chosen: EMI list/UI helper. Incompatible with JEI.
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
| Architectury API | https://www.curseforge.com/minecraft/mc-mods/architectury-api |
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

## Future / Deferred Mods

| Mod | Why not now | What would change that |
|---|---|---|
| Shader packs | Loader (Oculus) is in; packs chosen later | Pick a pack on purpose and ship it |
| ServerCore | Overlaps Radium / Let Me Despawn; activation range is gameplay | Explicit ruleset decision |
| Better Beds Reforged | Tiny FPS; last file 1.0.0 (2023) | Want beds later |
| Iris & Oculus Flywheel Compat | Colorwheel is the Create + Oculus path and is incompatible with this jar | Do not add |
| Connectivity | Packet/timeout fixer; Cupboard already in | Create/AE2/Mekanism/TACZ multiplayer packet issues |
| Particle Core | Needs Fzzy Config; Kotlin is now in. Can hide gun/spell FX | Only with a whitelist config |
| Create: Nowheel | Create + Entity Culling companion | Contraptions go invisible |
| Chunky | Pregen/admin, writes world | the panel pregen decision |
| C2ME / C2MEF / VMP / Krypton / Indium / More Culling / Debugify (asked slugs) | Fabric or unofficial/overlapping | See [performance.md](performance.md) Fabric video list |

## Deferred Ecosystem Upgrades

None. Do not bump Minecraft or Forge to accommodate a single mod without a separate approved change.

## Removed

| Mod | Removed on | Why | Re-add? |
|---|---|---|---|
| EMI QoL Tweaks | 2026-09-13 | CurseForge third-party API download is disabled (`packwiz-installer` cannot fetch file `8713840`). No Modrinth/GitHub file. | Only if the author enables API distribution or posts the same file on Modrinth |


