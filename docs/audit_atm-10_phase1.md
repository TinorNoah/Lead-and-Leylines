# Audit: Lead and Leylines vs ATM-10 — Phase 1 (performance and optimization)

- **Reference:** `AllTheMods/ATM-10`, shallow clone at `../_reference_pack`
- **This pack:** `Lead and Leylines` 0.1.24, `pack/pack.toml`
- **Scope:** optimization mods, their configs, JVM/launch args, render/entity/chunk/memory tuning
- **Read-only.** Nothing in this pack was modified by this audit. This report is the only file created.

## 0. Evidence limits — read this first

**The ATM-10 repo contains no mod list.** VERIFIED: the clone root has no `manifest.json`, no `.mrpack`, no `minecraftinstance.json`, no `mods/` directory, and no packwiz TOML. Its tree is `config/` (123 entries), `kubejs/`, `datapacks/`, `defaultconfigs/`, `changelogs/`, `README.md`, `CHANGELOG.md`, `MOD_ISSUES.md`. ATM-10's mod manifest lives on CurseForge (project 925200, confirmed by `_reference_pack/config/bcc-common.toml:4` `modpackProjectID = 925200`) and was not fetched for this phase.

Consequences:

- Every "ATM-10 ships mod X" statement below is inferred from a **committed config file named after X**, or is marked `not found`. A mod with no config in ATM-10 is indistinguishable from a mod it does not ship.
- Mod-count and side-split comparison between the two packs is **UNKNOWN**. This pack's own counts are VERIFIED below.
- ATM-10's **JVM/launch args are not in the repo at all**. VERIFIED: `grep -rI` for `Xmx`, `UseG1GC`, `UseZGC`, `MaxMetaspace`, `user_jvm` across the whole clone returns nothing. Those live in the CurseForge launcher profile or the server panel, not git. **No JVM comparison is possible from evidence.**

Compatibility: both packs are **Minecraft 1.21.1**. This pack pins `neoforge = "21.1.252"` (`pack/pack.toml` `[versions]`); ATM-10's loader version is `not found` in the repo, though `README.md` states "1.21.1" and its configs are NeoForge-format (`.toml` common files, `defaultconfigs/`). Findings about loader-level behavior transfer with high confidence. Findings about specific mod versions do **not** transfer.

## 1. Pack details

| Property | This pack | ATM-10 | Confidence |
|---|---|---|---|
| Minecraft | 1.21.1 | 1.21.1 | VERIFIED both |
| Loader | NeoForge 21.1.252 | NeoForge (version not in repo) | VERIFIED / UNKNOWN |
| Pack version | 0.1.24 (`pack/pack.toml`) | 8.2 (`config/bcc-common.toml:5`) | VERIFIED both |
| Launcher format | packwiz (`packwiz:1.1.0`) | CurseForge instance | VERIFIED both |
| Mod count | 571 (`ls pack/mods/*.pw.toml \| wc -l`) | not found | VERIFIED / UNKNOWN |
| Side split | 477 `both`, 94 `client`, 0 `server` | not found | VERIFIED / UNKNOWN |
| Committed config entries | 12 (`ls pack/config \| wc -l`) | 123 | VERIFIED both |

**VERIFIED**, from `grep -h '^side' pack/mods/*.pw.toml | sort | uniq -c`: 477 `both` (+1 duplicate line with different trailing whitespace), 74 `client`, 20 `client` (second whitespace variant). Normalized: ~478 `both`, ~94 `client`, **zero `server`-only mods**.

Note the 477 `both` count is the intended design per `docs/mods/performance.md:13`: "Use this for every 'server optimizer' we actually ship, or singleplayer will not get the benefit." That is correct and better than ATM-10's observable practice.

## 2. Comparison table

| Area | ATM-10 does | My pack does | Gap or difference | Evidence | Confidence |
|---|---|---|---|---|---|
| Optimizer mod set | Large, overlapping; commits configs only for 3 perf mods | 25 perf-named mods, no config for any of them | My pack installs optimizers and never tunes one | `_reference_pack/config/{modernfix-mixins.properties,spark/config.json,alltheleaks.json}` vs `ls pack/config` (no perf config) | VERIFIED |
| ModernFix tuning | `mixin.perf.dynamic_resources=true` + `stability_level=BETA` | not shipped | ATM-10 opts into 2 non-default ModernFix features; my pack takes all defaults | `_reference_pack/config/modernfix-mixins.properties:171,172` | VERIFIED |
| Spark | Ships a config (`backgroundProfiler: false`) | **Not a pack mod.** Injected only by the local smoke harness | Deliberate and documented | `_reference_pack/config/spark/config.json`; `scripts/smoke_test.py:729` comment "not a pack mod" | VERIFIED |
| AllTheLeaks | Ships `config/alltheleaks.json` (7 keys) | Mod installed, no config | Mod defaults only | `_reference_pack/config/alltheleaks.json` | VERIFIED |
| FerriteCore | not found in config | Mod installed, no config | n/a | — | UNKNOWN for ATM-10 |
| Sodium / Iris tuning | `config/iris.properties` committed; no Sodium config | Both installed, **no config for either** | My pack ships no Iris/Sodium config at all | `_reference_pack/config/iris.properties`; `pack/config` listing | VERIFIED |
| Memory-warning guidance | Ships `config/memorysettings.json` with recommended-RAM tiers (16 GB sys → 8 GB, 32/48/64 GB → 12 GB), min client 6000 MB, tolerance 200% | **No equivalent.** `README.md` tells players Java 21 + `-XX:+UseZGC` but never a RAM figure | Players get no allocation guidance for a 571-mod pack whose own server runs 8 GiB | `_reference_pack/config/memorysettings.json`; `README.md:18,28,32` | VERIFIED |
| Early window (FMLEarlyWindow) | `config/fml.toml` committed: 854×480, `maxThreads = -1`, `disableOptimizedDFU = true`, `versionCheck = false` | **No `fml.toml` at all** | NeoForge defaults apply; early window is a cold-start win | `_reference_pack/config/fml.toml:1-25`; `pack/config/fml.toml` absent | VERIFIED |
| Mekanism Covers perf | `config/mekanismcovers.json` → `disableAdvancedCoverRendering: true` | Covers not installed | Not applicable | `_reference_pack/config/mekanismcovers.json`; no covers mod in `pack/mods` | VERIFIED |
| JVM flags | not in repo | ZGC + 5× login/read timeout, mirrored into Prism `instance.cfg` and `server/run.sh` with explicit ZGC headroom math | My pack has a *policy* where ATM-10 has nothing in git | `pack/user_jvm_args.txt`; `server/run.sh:10-14`; `scripts/update_prism.py` | VERIFIED (mine) / UNKNOWN (ATM-10) |
| Regression harness | None in repo (no smoke script, no committed metrics) | `scripts/smoke_test.py` boots a real server, runs `/tick query` + `/neoforge generate`, records MSPT/CPS/RSS to `docs/smoke-runs/`, diffs against the previous run | **Large advantage to my pack.** Not a gap | `scripts/smoke_test.py`; `docs/smoke-runs/2026-10-02T120934Z.md` | VERIFIED |
| Mods banned by load-bearing policy | not determinable | Noisium, Carbon Config, Chunk Pregenerator, Tectonic, Coverage-style optimizer stacking | Cannot compare | `docs/mods/performance.md:92-96`; `AGENTS.md` | VERIFIED (mine) |
| `stability_level=BETA` risk appetite | Accepted, evidently without incident | No BETA mixin features | Copying ATM-10's ModernFix override inherits that risk | `_reference_pack/config/modernfix-mixins.properties:172` | VERIFIED |

## 3. Recommendations

Ranked by impact ÷ risk. All are opt-in proposals; nothing was applied.

### R1 — Ship a player-facing RAM recommendation (impact: high, risk: low)

ATM-10 commits `config/memorysettings.json` with tiered recommended values. This pack has **no RAM guidance anywhere** for players, yet its own dedicated server runs `-Xmx6.5G` by default (`server/run.sh:10`, `DEFAULT_MEMORY_MB = 8192` at `scripts/smoke_test.py:44`) and it uses ZGC, which needs native headroom on top of `-Xmx`. A player who copies the server figure into a 4 GB client allocation will OOM on a 571-mod pack.

What: add a short RAM/JVM block to `README.md` (and consider whether the pack should ship a memory-warning mod — that is a mod decision requiring the `minecraft-modding` flow, not an audit action). Start from measured data, not a guess: the last smoke run reports RSS post-gen 4115.6 MiB on an 8 GiB server (`docs/smoke-runs/2026-10-02T120934Z.md`).

How to test: boot Prism with the documented figure, play 20 min in a loaded chunk, confirm no GC thrash in F3.

### R2 — Commit a `modernfix-mixins.properties` override (impact: med, risk: med)

ATM-10 sets exactly two non-defaults: `mixin.perf.dynamic_resources=true` and `stability_level=BETA` (`_reference_pack/config/modernfix-mixins.properties:171-172`). Every other one of ModernFix's ~90 mixins is at default in both packs.

`dynamic_resources` moves resource (model/texture) loading off the critical path. That is directly relevant to a pack with ~20 required resource packs (`pack/config/global_packs.toml [resourcepacks].required`, which lists 14 zips plus the Armageddon folder) and hundreds of missing-asset warnings per reload (`docs/mods/configs.md:42`). Risk: it is non-default, and this pack's documented failure class is client resource reload aborting and taking AAA Particles down with it (`docs/mods/configs.md:18`). So: **do not adopt `stability_level=BETA`**, which widens the blast radius of any unknown mixin interaction; test `dynamic_resources` alone.

How to test: `python scripts/smoke_test.py` for the server side, then a Prism client boot comparing `latest.log` reload time and asset-warning count with the file present vs absent. Note the smoke test **cannot verify this** — it never loads client mods (`AGENTS.md`).

### R3 — Ship an `fml.toml` (impact: med, risk: low)

ATM-10 commits `config/fml.toml` with 854×480 early window, `earlyWindowFBScale = 1`, `maxThreads = -1`, `disableOptimizedDFU = true`, `versionCheck = false`. My pack ships none, so NeoForge writes defaults at first boot. The early-window keys are pure cold-start: they give a smaller framebuffer to load and present while the mod list initializes.

This pack's boot is **85.4s** (`docs/smoke-runs/2026-10-02T120934Z.md`), so the black-screen window a player stares at is long, and cold start is also when Java heap pressure peaks. `versionCheck = false` is a UX call, not perf — decide separately.

How to test: time `packwiz serve` + Prism launch to main menu with and without the file.

### R4 — Audit the async-save / async-load overlap cluster (impact: med, risk: med)

VERIFIED overlapping optimizers in `pack/mods`, all `both`: `fast-async-world-save-forge-fabric.pw.toml`, `smooth-chunk-save.pw.toml`, `c2me.pw.toml`, `chunk-sending-forge-fabric.pw.toml`, `ksyxis.pw.toml`, `im-fast.pw.toml`, `too-fast.pw.toml`, `observable.pw.toml`, `invasive-optimizations.pw.toml`, `leaky.pw.toml`, `fix-gpu-memory-leak.pw.toml`, `memorymod.pw.toml`. Plus `modernfix`, `alltheleaks`, `ferritecore`.

`docs/mods/performance.md:69` states plainly: "No pack config overlays yet; defaults only." Six mods touching async save/send and not one config file is the concrete gap here. The pack's own policy (`AGENTS.md`) says do not stack overlapping optimizers, and `docs/mods/performance.md:64` already flags FastBoot as "First to remove if launch breaks next to ModernFix / quick pack."

Note this is a **tuning** recommendation, not a removal recommendation. Removing mods is a separate, riskier decision and out of audit scope.

How to test: enable one config at a time, `python scripts/smoke_test.py` between each, keep the run that improves P99 without raising "Can't keep up" count.

### R5 — Commit an AllTheLeaks config (impact: low, risk: low)

ATM-10 ships `config/alltheleaks.json` with 7 keys, including `skipTickingUnloadedFluxNetworks: true`. That key matters more to this pack than to ATM-10 in one specific way: the pack's own load-fixes inventory exists because soft-dep loot tables and unregistered-item recipes are a recurring, documented failure class here (`docs/mods/load-fixes-inventory.md`, `pack/global_packs/required_data/lead-leylines-orphan-loot/`). Low expected gain, near-zero risk.

### R6 — Iris config (impact: low, risk: low)

ATM-10 commits `config/iris.properties`. My pack ships Iris 1.8.14-beta.1 with no config, so every player gets whatever Iris writes on first boot, unreviewed and unversioned. Committing a minimal file with `enableShaders=true` and an explicit `shaderPack=` documents intent and makes shader state reproducible. Do **not** copy ATM-10's `maxShadowRenderDistance=32` — this pack pairs Iris with Colorwheel (`docs/mods/performance.md:84`), which has its own irisflw constraints.

## 4. What this pack does better — do not "fix" these

- **Optimizer `side` discipline.** Zero `server`-only mods; ~478 `both`. Singleplayer matches the dedicated server by construction. ATM-10's split is not in the repo and could not be checked.
- **A real perf regression harness.** `scripts/smoke_test.py` boots the actual server, benches with `/tick query` and `/neoforge generate`, and appends a diffed report under `docs/smoke-runs/`. ATM-10 has nothing comparable in git. This is why R2/R3/R4 are testable here and would be guesswork in ATM-10.
- **Evidence-based rejects.** `docs/mods/performance.md:94-96` records FastNoise at 7.62 vs 7.73 CPS and ScalableLux at 4.89 CPS with named log artifacts, and rejects both. That discipline is better than ATM-10's.
- **ZGC + explicit headroom math.** `server/run.sh:10-14` subtracts 1536 MB from the container limit for ZGC and native buffers to avoid OOM-kill exit 137, and documents why. Most packs hand-wave this.
- **Unresolved-path honesty.** `docs/mods/manifest.md`, `load-fixes-inventory.md`, `known-client-asset-issues.md` are ledgers with per-mod counts and restore steps.

## 5. Could not be verified

- ATM-10's mod list, mod count, side split, and loader version — no manifest in the repo.
- ATM-10's JVM/launch args — absent from the repo entirely.
- Whether ATM-10 ships FerriteCore, C2ME, Smooth Chunk Save, FastSuite/FastWorkbench/FastFurnace, or Sodium. No config files for any of them; presence is `not found`, which is **not** evidence of absence.
- Whether ATM-10's `stability_level=BETA` has caused them a problem. No issue tracker in the clone.

## Applied

R2, R3, R4, and R5 were implemented on a feature branch after this audit. Committed configs under `pack/config/`: `modernfix-mixins.properties`, `fml.toml`, `alltheleaks.json`, `c2me.toml`, `chunksending.json`, `smoothchunk.json`, `ferritecore-mixin.toml`.

Two corrections to the audit above, both found by booting a real server and reading the generated defaults rather than trusting the reference:

- **R3's cold-start claim was wrong.** ATM-10's `fml.toml` early-window, `maxThreads`, and `disableOptimizedDFU` values are *already* the NeoForge 21.1.252 defaults. The generated file here is byte-identical to ATM-10's except `versionCheck`. There was no early-window win to be had; the file is now committed as future-proofing only.
- **ATM-10's `alltheleaks.json` is not transferable.** Its keys (`entitySectionCME`, `scoreboardDebug`) do not exist in the pinned AllTheLeaks 1.1.13, and ours has keys it lacks. The committed file was built from this pack's own generated key set and every key was verified present in `ATLProperties.class`.

Measured result: **no server-side effect, as expected.** Four runs (`docs/smoke-runs/2026-10-05T005028Z.md`, `-011753Z`, `-012002Z`, `-012208Z`) span ~15.9-21.2 CPS and ~68-95s boot regardless of whether the configs were present. A deliberate control run with the configs *removed* scored 21.195 CPS / 67.7s boot, i.e. better than the run with them — so the first run's apparent gain (post-gen P99 455ms -> 7.4ms) was run-to-run variance, not a fix. The 95.3s outlier was a cold-cache first boot.

Still unverified: `mixin.perf.dynamic_resources=true` is client-side (13 of its mixins are in ModernFix's `client` list) and the dedicated-server harness never loads client mods. A Prism client boot is required.

## Remaining phases / follow-up tasks

- Phase 2 (conflicts and bug fixes) would be the higher-value next pass for this pack: the `lead-leylines-orphan-loot` and `lead-leylines-load-fixes` ledgers show recurring soft-dep and unregistered-item breakage, and ATM-10's `kubejs/` recipe-compat tree is the obvious comparison surface.
- Phase 3 (config management): my pack has 12 committed config entries against 123, and no `defaultconfigs/` directory at all. That is the same finding as R4 seen from a different angle, but with the server/client split as the subject.
- Phase 4 (startup and memory): 85.4s boot and ZGC headroom deserve their own pass.
- Phase 5 (maintenance): ATM-10 has `CHANGELOG.md` + 59 per-version `changelogs/` files. This pack has one `CHANGELOG.md` and no per-version split.
- R1–R6 require the `minecraft-modding` and `add-mod` skills for any jar change, and `local-smoke-test` to verify. None may be applied inside an audit.
- `../_reference_pack` can be deleted; it is outside the pack and outside git.

## Questions for me

1. R3: do you want `versionCheck = false`? It is a UX call (no "new NeoForge available" prompt), not performance, and I would keep it out of a perf-driven change unless you want it.
2. R1: do you want RAM guidance in `README.md` only, or a shipped memory-warning mod? The latter is a mod decision needing the research-and-approval flow.
3. R4: is the goal to keep all these mods and tune them, or is a reduction pass on the async-save cluster acceptable? The answer changes R4 from a config task into a removal task.
4. Should the audit stop here, or should I run phase 2?
