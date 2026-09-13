# Performance mods — considered, chosen, dropped

Research snapshot: 2026-09-13. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml) (at snapshot: Minecraft 1.20.1, Forge 47.4.23). Re-check store pages before install; do not add a file that does not list that pair.

**Status:** first cut **installed** (2026-09-13), including **shaders as a pack feature** (Oculus `1.8.0` + Embeddium `0.3.31`). Second client cut: Entity Culling `1.10.5` + Dynamic FPS `3.11.4`. Smoothness cut: FastSuite, Noisium, Clumps, Smooth Chunk Save + Cupboard, Neruina. Dynamic lights stay out. Flywheel compat stays out until Create. packwiz `side` is set as in the tables.

## Side (packwiz)

| `side` | Meaning |
|---|---|
| `client` | Prism / player instance only. Dedicated server must not require it. |
| `server` | Dedicated server (and not needed on a pure client). Rare for this list. |
| `both` | Must run in singleplayer’s integrated server **and** on the dedicated server. Use this for every “server optimizer” we actually ship, or singleplayer will not get the benefit. |

Nothing in the chosen set is dedicated-server-only. Let Me Despawn, Radium, FastWorkbench, and similar are documented as server-logic mods on Modrinth, but this pack uses **`both`** so Prism and the dedicated server stay in sync.

## Decision rules

1. Compatibility first. Mixin overlap or two mods solving the same subsystem → keep one.
2. Prefer the maintained Forge 1.20.1 project, not an abandoned fork with a familiar name.
3. Do not add a compat mod until the content mod it compatibilizes exists (Create → Flywheel compat).
4. Do not add a second leaf-culler, second dynamic-lights mod, or a second Lithium port.
5. Gameplay-changing “optimizers” (mob freeze range, redstone rewrite) are hold/skip unless explicitly wanted.

---

## Chosen (recommended first cut)

Install these together. They occupy different layers (renderer, RAM, HUD GL, recipes, ticking, leak fixes, crash UI).

| Mod | Project | `side` | Why add |
|---|---|---|---|
| Embeddium | [modrinth.com/mod/embeddium](https://modrinth.com/mod/embeddium) | client | Forge Sodium. Rubidium is abandoned; this is the renderer the rest of the client stack expects. Latest 1.20.1 file seen: `0.3.31+mc1.20.1`. |
| FerriteCore | [modrinth.com/mod/ferrite-core](https://modrinth.com/mod/ferrite-core) | both | Blockstate/model memory. No real alternative. Harmless on dedicated server. |
| ImmediatelyFast | [modrinth.com/mod/immediatelyfast](https://modrinth.com/mod/immediatelyfast) | client | Batches immediate-mode / HUD rendering. Different layer from Embeddium. **Pinned** `1.5.5+1.20.4` (version id `rvsLEEZU`); that file lists 1.20.1. Do not let packwiz pick the older `1.2.7` default. |
| ModernFix | [modrinth.com/mod/modernfix](https://modrinth.com/mod/modernfix) | both | Launch time, memory, vanilla bugfixes. Author intends it next to other perf mods. Leave mixin defaults alone. |
| FastWorkbench | [modrinth.com/mod/fastworkbench](https://modrinth.com/mod/fastworkbench) | both | Crafting-table recipe scan. **Must** match on client and server or recipes desync. |
| FastFurnace | [modrinth.com/mod/fastfurnace](https://modrinth.com/mod/fastfurnace) | both | Furnace tick shortcut. Same author and same both-sides rule as FastWorkbench. |
| BadOptimizations | [modrinth.com/mod/badoptimizations](https://modrinth.com/mod/badoptimizations) | client | CPU work that is not chunk meshing (toasts, sky, etc.). Complements Embeddium. |
| Embeddium Extra | [modrinth.com/mod/rubidium-extra](https://modrinth.com/mod/rubidium-extra) (listed as Embeddium/Rubidium Extra) | client | Sodium Extra port: fog, particles, animation, leaf *settings*. One extras mod only. |
| Oculus | [modrinth.com/mod/oculus](https://modrinth.com/mod/oculus) | client | Iris for Forge. Shaders are a pack feature. Pair with Embeddium `0.3.31` + Oculus `1.8.0` (latest 1.20.1 files at research). No separate dynamic-lights mod. |
| Crash Assistant | [modrinth.com/mod/crash-assistant](https://modrinth.com/mod/crash-assistant) | client | Crash GUI and log analysis. Better default than Not Enough Crashes. Does not raise FPS. |
| Radium | [modrinth.com/mod/radium](https://modrinth.com/mod/radium) (Reforged-Hub Lithium port) | both | Lithium for Forge: AI, block updates, ticking. Chosen instead of Canary and instead of CurseForge “Radium Reforged” as a second jar. |
| Let Me Despawn | [modrinth.com/mod/lmd](https://modrinth.com/mod/lmd) | both | Despawn for mobs that picked up gear and would otherwise live forever. Real server stutter fix. |
| AllTheLeaks | [curseforge.com/.../alltheleaks](https://www.curseforge.com/minecraft/mc-mods/alltheleaks) (CurseForge only) | both | Leak patches for vanilla and popular mods. Cheap insurance before the pack grows. |
| Placebo | FastWorkbench dependency | both | Library. Pulled in by packwiz. |
| Almanac | Let Me Despawn dependency | both | Library. Pulled in by packwiz. Set `both` so singleplayer gets it. |
| Entity Culling | [modrinth.com/mod/entityculling](https://modrinth.com/mod/entityculling) | client | Async line-of-sight hide for entities/block entities. Official Forge `1.10.5` (version `MloBcsQQ`). Different layer from Embeddium Extra. Cloth Config not required. |
| Dynamic FPS | [modrinth.com/mod/dynamic-fps](https://modrinth.com/mod/dynamic-fps) | client | Lowers CPU when the window is unfocused. Official Forge `3.11.4` (version `EjdIWWqG`). Not in-game FPS. Cloth Config optional and not shipped. |
| FastSuite | [modrinth.com/mod/fastsuite](https://modrinth.com/mod/fastsuite) | both | Recipe index for all JSON recipes. Same author as FastWorkbench / Apotheosis. Placebo already in. Does not replace FastWorkbench/FastFurnace. Helps magic/tech/utility recipes as the pack grows. |
| Noisium | [modrinth.com/mod/noisium](https://modrinth.com/mod/noisium) | both | Faster vanilla-parity worldgen. Official Forge `2.3.0+mc1.20-1.20.1`. `both` so Prism singleplayer gets it. For planned biome mods. |
| Clumps | [modrinth.com/mod/clumps](https://modrinth.com/mod/clumps) | both | Merges XP orbs. For Mob Grinding Utils and other farm XP spam. |
| Smooth Chunk Save | [curseforge.com/.../smooth-chunk-save](https://www.curseforge.com/minecraft/mc-mods/smooth-chunk-save) | both | Spreads autosave disk writes. Forge `4.1` file id `6296598`. |
| Cupboard | Smooth Chunk Save dependency | both | someaddon library. Forge `4.1` file id `8746423`. Reuse later if Connectivity is added. |
| Neruina | [modrinth.com/mod/neruina](https://modrinth.com/mod/neruina) | both | Isolates ticking entity/block crashes so a bad farm or magic tick does not brick the world. |

---

## Fabric video list (2026-09-13)

Checked against Minecraft 1.20.1 Forge in `pack/pack.toml`. The linked projects are a **Fabric** performance set. Do not install those slugs as-is.

| Asked as | Forge 1.20.1 file? | Outcome |
|---|---|---|
| Sodium | No (Fabric / NeoForge only) | **Already covered:** Embeddium |
| Sodium Extra | No | **Already covered:** Embeddium Extra (`rubidium-extra`) |
| Indium | No (Fabric/Quilt). Sodium FRAPI shim | **Dropped.** Embeddium ships integrated Fabric Rendering API support. Installing Indium on Forge would crash. |
| ImmediatelyFast | Yes (`1.5.5+1.20.4`, version `rvsLEEZU`) | **Already installed** (same pin) |
| Entity Culling | Yes (`1.10.5`, version `MloBcsQQ`, 2026-06-20) | **Chosen**, client. Official Forge. Different layer from Embeddium Extra (async LOS vs leaf/fog settings). License allows CurseForge/Modrinth packs; do not rehost the jar. Cloth Config not required. |
| More Culling | No on the official project (Fabric/NeoForge/Quilt) | **Dropped** the asked slug. Unofficial CurseForge [More Culling Reforged](https://www.curseforge.com/minecraft/mc-mods/more-culling-reforged) exists; leaf culling overlaps Embeddium Extra; needs Cloth Config. Do not add a second leaf culler. |
| Lithium | No | **Already covered:** Radium (Reforged-Hub) |
| C2ME (`c2me-fabric`) | No (Fabric). NeoForge is a different project | **Dropped** the asked slug. Unofficial [C2MEF](https://modrinth.com/mod/c2mef) is an alpha mixin port. Worldgen hitch is covered by **Noisium**. |
| Chunky | Yes (`1.3.146`, version `4FTDk9wv`, 2024-05-06) | **Held.** Official Forge. Pregen/admin tool, not FPS. Writes world data. Revisit when we want the panel pregen. |
| FerriteCore | Yes | **Already installed** |
| ModernFix | Yes | **Already installed** |
| Krypton | No (Fabric). 1.20.1 file is `0.2.3` (2023) | **Dropped** the asked slug. [Pluto](https://modrinth.com/mod/pluto) (unofficial Krypton fork) has **no 1.20.1**. [Krypton Reforged](https://www.curseforge.com/minecraft/mc-mods/krypton-reforged) is unofficial. [Connectivity](https://www.curseforge.com/minecraft/mc-mods/connectivity) is a timeout/packet-size fixer (needs Cupboard), not a Netty rewrite — hold until real MP connection issues. |
| VeryManyPlayers (`vmp-fabric`) | No. [vmp-forge](https://modrinth.com/mod/vmp-forge) last 1.20.1 file 2023-07; README still says early development | **Dropped.** High-playercount mixin pack; stale Forge port; overlaps the kind of work Radium already does. |
| Debugify | No Forge on 1.20.1 (Fabric/Quilt `1.20.1+2.0`, 2023-07) | **Dropped.** ModernFix already ships vanilla bugfixes. Unofficial CurseForge Debugify Reforge is a tiny port — skip. |
| Dynamic FPS | Yes (`3.11.4`, version `EjdIWWqG`, 2026-01-29) | **Chosen**, client. Official Forge, MIT. Lowers CPU when unfocused. Cloth Config is **optional** and not shipped. No world data. |

Do not add Sinytra Connector just to run the Fabric jars.

---

## Held (not chosen yet)

| Mod | Project | `side` | Why wait |
|---|---|---|---|
| ServerCore | [modrinth.com/mod/servercore](https://modrinth.com/mod/servercore) | both | Overlaps Radium / Let Me Despawn. Activation range and mobcaps **change gameplay** (distant mobs freeze). Not a silent optimizer. |
| Better Beds Reforged | [modrinth.com/mod/better-beds-reforged](https://modrinth.com/mod/better-beds-reforged) | client | Correct Forge port (upstream Better Beds has no Forge 1.20.1). Tiny FPS. Last file is 1.0.0 (2023). Optional later. |
| Iris & Oculus Flywheel Compat | [modrinth.com/mod/iris-flw-compat](https://modrinth.com/mod/iris-flw-compat) | client | Only useful with Create’s Flywheel + Oculus. No Create in the pack yet. |
| Chunky | [modrinth.com/plugin/chunky](https://modrinth.com/plugin/chunky) | both | Official Forge pregen. Admin tool; writes chunks. Wait for a the panel pregen decision. |
| Connectivity | [curseforge.com/.../connectivity](https://www.curseforge.com/minecraft/mc-mods/connectivity) | both | Packet/timeout fixer. Cupboard is already in. Add with Create / AE2 / Mekanism / TACZ multiplayer, not as FPS. |
| Particle Core | [modrinth.com/mod/particle-core](https://modrinth.com/mod/particle-core) | client | Particle cull/cap. Needs Kotlin for Forge + Fzzy Config. Could hide TACZ / Superb Warfare / Ars Nouveau VFX. Only with a config that does not strip gun/spell particles. |
| Create: Nowheel | [modrinth.com/mod/create-nowheel](https://modrinth.com/mod/create-nowheel) | client | Create + Entity Culling companion. Shader path wants Colorwheel, which is a different stack than Oculus + iris-flw-compat. Research at Create install; do not stack blindly. |

---

## Dropped

| Asked as | What we found | `side` if it had shipped | Why drop |
|---|---|---|---|
| Rubidium (not asked, but the trap) | Abandoned Embeddium predecessor | client | Same renderer as Embeddium. Never add. |
| Better Beds (Motschen) | [modrinth.com/mod/better-beds](https://modrinth.com/mod/better-beds) is Fabric/NeoForge only on 1.20.1 | client | **No Forge 1.20.1 file.** Use Better Beds Reforged if we ever want beds, do not install this slug. |
| Sodium/Embeddium Dynamic Lights, RyoamicLights, Extra lights | Three products, one job | client | **Dropped:** shaders (Oculus) are a pack feature. Extra DL mods flicker or fight shader lighting. Do not add a second DL mod later either. |
| CullLessLeaves Reforged (Unofficial) | [modrinth.com/mod/cull-less-leaves-reforged](https://modrinth.com/mod/cull-less-leaves-reforged) | client | Last 1.20.1 file 2023. Same job as Embeddium Extra leaf settings. Looks wrong with Oculus shaders. |
| Alternate Current | [modrinth.com/mod/alternate-current](https://modrinth.com/mod/alternate-current) | both | Rewrites redstone dust. Radium/Lithium already touches that subsystem. Mixin overlap; pick Radium (broader). |
| Canary | [modrinth.com/mod/canary](https://modrinth.com/mod/canary) | both | Second Lithium port. Older 1.20.1 build than Radium; reports of disabled Lithium opts and Apotheosis issues. |
| Radium Reforged **as a second jar** | CurseForge [radium-reforged](https://www.curseforge.com/minecraft/mc-mods/radium-reforged) (Asek3) vs Modrinth Radium (Reforged-Hub) | both | One Lithium port only. Chosen project is Modrinth **Radium**. Do not install both listings. |
| Iris & Oculus Flywheel Compat (now) | iris-flw-compat | client | Dead weight without Create. |
| ServerCore (as a silent add) | servercore | both | See Held. Dropped from the first cut because it is a ruleset, not a free FPS win. |
| Not Enough Crashes | (alternative to Crash Assistant) | client | Worse crash-on-crash reputation. Crash Assistant is the replacement. |
| Optimized Block Entities (OBE) | [modrinth.com/mod/obe](https://modrinth.com/mod/obe) | client | Author notes 1.20.1 Forge **crashes with Embeddium** unless extra Fabric-API-shaped deps. We ship Embeddium. |
| Ksyxis | [modrinth.com/mod/ksyxis](https://modrinth.com/mod/ksyxis) | both | Speeds load by skipping spawn chunks. Breaks chunkloaders / Create / AE2 / Mekanism-style always-on machines. |
| Does It Tick / Immersive Optimization / APTweaks Spawn | various | both | Freeze or skip distant entity ticks. Same class of problem as ServerCore vs Create farms, Mekanism, AE2, Apotheosis spawners. |
| Starlight (Forge unofficial) | CurseForge starlight-forge | both | Lighting engine rewrite. Unofficial on Forge; fights Embeddium/Oculus/Create lighting. Official Starlight is Fabric. |
| MemoryLeakFix | [modrinth.com/mod/memoryleakfix](https://modrinth.com/mod/memoryleakfix) | both | AllTheLeaks is the 1.20.1 replacement. Do not stack. |
| Saturn / Graphene / Tritium / Palladium | all-in-one opt packs | — | Overlap FerriteCore, ModernFix, Radium. Prefer one job per mod. |
| Fast Noise (`zfastnoise`) | [modrinth.com/mod/zfastnoise](https://modrinth.com/mod/zfastnoise) | both | Worldgen mixin. Incompat tagged vs other noise/xray/Moonrise projects. Prefer official Noisium if we want worldgen CPU. |

---

## Planned content (do not sabotage)

Target content named 2026-09-13: TACZ, Superb Warfare, Apotheosis, Create, AE2, Ars Nouveau, Modern Industrialization, Building Gadgets, Mining Gadgets, Mekanism, Mob Grinding Utils, plus later biome / magic / tech / utility mods.

Rules for extra opt mods:

1. **No distant-tick freezers** (ServerCore, Does It Tick, Immersive Optimization, APTweaks Spawn). Create contraptions, AE2 grids, Mekanism machines, and Apotheosis spawners must keep ticking.
2. **No second Lithium / redstone rewrite** (Canary, Alternate Current). Radium stays. Create uses redstone; Apotheosis historically fought Canary.
3. **No spawn-chunk strippers** (Ksyxis). Tech mods need loaded machines.
4. **Shaders + Create** need [Iris & Oculus Flywheel Compat](https://modrinth.com/mod/iris-flw-compat) **when Create is added**, not before. Pair with the then-current Oculus/Embeddium files. Do not add Colorwheel/Nowheel in the same cut without a dedicated check.
5. **Entity Culling** is already in. When Create lands, watch for invisible contraption entities; Nowheel claims to fix one Entity Culling + simulated-contraption case.
6. **Particle caps** (Particle Core, Embeddium Extra particle settings) must not eat TACZ / Superb Warfare tracers or Ars Nouveau spell FX.
7. **ImmediatelyFast `hud_batching`** may need off later if gadget/JEI/Apotheosis tooltips glitch.
8. TACZ and Superb Warfare are **two gun systems**. That is a content overlap for later, not an optimizer problem.

Safe opt that **helps** that list: FastSuite (Apotheosis/AE2/MI/magic recipes), Clumps (Mob Grinding Utils XP), Noisium (biome worldgen hitch), Smooth Chunk Save (autosave with bigger worlds), AllTheLeaks (already in), Neruina (bad tick isolation), Connectivity later (large mod packets), Flywheel compat later (Create + Oculus).

---

## Incompatibility matrix (this set)

Do not combine:

| Pair | Result |
|---|---|
| Embeddium + Rubidium | Duplicate renderer |
| Radium + Canary | Duplicate Lithium |
| Radium + Alternate Current | Duplicate redstone implementation |
| Two dynamic-light mods | Flicker / crash |
| CullLessLeaves + Embeddium Extra leaf culling | Duplicate leaf pass |
| Oculus + dynamic lights | Shader lighting vs extra DL |
| Oculus + CullLessLeaves | Holey trees under shaders |
| Flywheel compat without Create | No effect |
| Embeddium + Oculus with unmatched versions | Common 1.20.1 crash source. Pair store files; do not mix random builds. |
| Embeddium Extra leaf culling + More Culling (or CullLessLeaves) | Duplicate leaf pass |
| Official Fabric slugs (Sodium, Lithium, C2ME, Krypton, VMP, Indium, Debugify 1.20.1) on this Forge pack | Wrong loader; crash or no file |
| Unofficial C2MEF / VMP-Forge / Pluto-on-1.20.1 | Stale or alpha mixin ports; not a substitute for the Fabric originals |

Soft (later content, not this cut): ImmediatelyFast `hud_batching` vs fancy tooltip/HUD mods; ServerCore activation range vs spawner/AI mods.

---

## Configs worth documenting (only these)

Do **not** hand-tune Embeddium, FerriteCore, FastWorkbench, FastFurnace, BadOptimizations, Crash Assistant, AllTheLeaks, Entity Culling, or Dynamic FPS unless a log names them.

When the chosen mods are installed, ship notes (and config overrides only if defaults are wrong). Details: [configs.md](configs.md).

| Mod | Why a pack note |
|---|---|
| Let Me Despawn | Gameplay: which equipped mobs may despawn. Document equipment / whitelist so named or raid mobs are not surprising. |
| Embeddium Extra | If any other leaf or dynamic-light mod is added later, turn those Extra toggles off. |
| ImmediatelyFast | If a later HUD/tooltip mod glitches, disable `hud_batching`. Otherwise leave default. |
| Oculus | Version pair with Embeddium is the real “config”. No default shader pack until one is chosen on purpose. |
| ServerCore (if held → chosen) | Activation range and mobcaps must be written down; they change what players see in the distance. |
| ModernFix | Defaults are the feature. Do not edit mixin flags unless a crash log points at one. |

---

## Original ask → outcome

| Original name | Outcome |
|---|---|
| Embeddium | Chosen, client |
| FerriteCore | Chosen, both |
| ImmediatelyFast | Chosen, client |
| ModernFix | Chosen, both |
| FastWorkbench | Chosen, both |
| Oculus | **Chosen**, client — shaders are a pack feature |
| Fast Furnace | Chosen, both |
| Alternate Current | Dropped (Radium covers redstone; mixin clash) |
| Better Beds (Client Only) | Held as Better Beds **Reforged**; upstream Forge file missing |
| AllTheLeaks | Chosen, both (CurseForge) |
| Sodium/Embeddium Dynamic Lights | **Dropped** — Oculus is in |
| BadOptimizations | Chosen, client |
| Let Me Despawn | Chosen, both |
| Sodium/Embeddium Extras | Chosen as Embeddium Extra, client |
| Crash Assistant | Chosen, client |
| Radium Reforged | Chosen as Modrinth **Radium**, both; not Canary; not two Radium jars |
| Iris & Oculus Flywheel Compat | Held until Create |
| CullLessLeaves Reforged (Unofficial) | Dropped |
| ServerCore | Held / not in first cut |

---

## Locked: shaders

Shaders are a pack feature. Oculus is the Forge shader loader. Dynamic lights mods stay out. Flywheel shader compat is still held until Create.
