# Lead and Leylines — mod manifest

Synced with `pack/mods/*.pw.toml` on 2026-09-13. Minecraft, loader, and pack version: see [`pack/pack.toml`](../../pack/pack.toml). Decision log for this cut: [performance.md](performance.md). Config notes: [configs.md](configs.md).

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

## Future / Deferred Mods

| Mod | Why not now | What would change that |
|---|---|---|
| Shader packs | Loader (Oculus) is in; packs chosen later | Pick a pack on purpose and ship it |
| ServerCore | Overlaps Radium / Let Me Despawn; activation range is gameplay | Explicit ruleset decision |
| Better Beds Reforged | Tiny FPS; last file 1.0.0 (2023) | Want beds later |
| Iris & Oculus Flywheel Compat | Needs Create’s Flywheel | When Create is in (required with Oculus) |
| Connectivity | Packet/timeout fixer; Cupboard already in | Create/AE2/Mekanism/TACZ multiplayer packet issues |
| Particle Core | Needs Kotlin + Fzzy; can hide gun/spell FX | Only with a whitelist config |
| Create: Nowheel | Create + Entity Culling; shader path ≠ Oculus compat | Research at Create install |
| Chunky | Pregen/admin, writes world | the panel pregen decision |
| C2ME / C2MEF / VMP / Krypton / Indium / More Culling / Debugify (asked slugs) | Fabric or unofficial/overlapping | See [performance.md](performance.md) Fabric video list |

## Deferred Ecosystem Upgrades

None. Do not bump Minecraft or Forge to accommodate a single mod without a separate approved change.

## Removed

None yet.
