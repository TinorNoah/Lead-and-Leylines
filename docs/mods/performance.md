# Performance mods — considered, chosen, dropped

Research snapshot: 2026-09-13. Target is whatever Minecraft + Forge are in [`pack/pack.toml`](../../pack/pack.toml) (at snapshot: Minecraft 1.20.1, Forge 47.4.23). Re-check store pages before install; do not add a file that does not list that pair.

**Status:** first cut **installed** (2026-09-13), including **shaders as a pack feature** (Oculus `1.8.0` + Embeddium `0.3.31`). Dynamic lights stay out. Flywheel compat stays out until Create. packwiz `side` is set as in the tables.

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

---

## Held (not chosen yet)

| Mod | Project | `side` | Why wait |
|---|---|---|---|
| ServerCore | [modrinth.com/mod/servercore](https://modrinth.com/mod/servercore) | both | Overlaps Radium / Let Me Despawn. Activation range and mobcaps **change gameplay** (distant mobs freeze). Not a silent optimizer. |
| Better Beds Reforged | [modrinth.com/mod/better-beds-reforged](https://modrinth.com/mod/better-beds-reforged) | client | Correct Forge port (upstream Better Beds has no Forge 1.20.1). Tiny FPS. Last file is 1.0.0 (2023). Optional later. |
| Iris & Oculus Flywheel Compat | [modrinth.com/mod/iris-flw-compat](https://modrinth.com/mod/iris-flw-compat) | client | Only useful with Create’s Flywheel + Oculus. No Create in the pack yet. |
| Entity Culling | [modrinth.com/mod/entityculling](https://modrinth.com/mod/entityculling) | client | Not on the original ask. Stronger FPS than CullLessLeaves. Consider later. |
| Noisium | [modrinth.com/mod/noisium](https://modrinth.com/mod/noisium) | both | Not on the original ask. Worldgen CPU. Consider when exploration/worldgen mods land. |

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

Soft (later content, not this cut): ImmediatelyFast `hud_batching` vs fancy tooltip/HUD mods; ServerCore activation range vs spawner/AI mods.

---

## Configs worth documenting (only these)

Do **not** hand-tune Embeddium, FerriteCore, FastWorkbench, FastFurnace, BadOptimizations, Crash Assistant, or AllTheLeaks unless a log names them.

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
