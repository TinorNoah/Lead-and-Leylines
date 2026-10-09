# Audit: Lead and Leylines vs ATM-10 — Phase 4 (startup, load time, memory)

- **Reference:** `AllTheMods/ATM-10`, shallow clone at `../_reference_pack`
- **This pack:** `Lead and Leylines` 0.1.24, `pack/pack.toml`
- **Scope:** launch scripts, caching, loading behavior
- **Read-only.** This report is the only file created.

## 0. Evidence limits

Same as phases 1–3: ATM-10 has no mod manifest, no server build, no launch scripts, no CI workflows, and no JVM args in git. Their launcher profile, server panel, and CurseForge build are all outside the repo. So "ATM-10 does X" below means "X has a committed config", and launch/memory findings are one-sided by construction.

Both packs are Minecraft 1.21.1, so loader mechanisms transfer. Numbers do not — every figure below is this pack's own measurement.

## 1. Launch and memory surface

| | This pack | ATM-10 |
|---|---|---|
| Server start script | `server/run.sh` — Java 21, ZGC, `-Xms128M`, `-Xmx` computed as container minus 1.5 GB headroom | not in repo |
| JVM flags | `pack/user_jvm_args.txt` (`-XX:+UseZGC`, 5× login/read timeout), mirrored into Prism `instance.cfg` by `scripts/update_prism.py` | not in repo |
| Prism sync | `scripts/update_prism.py` (serve + installer bootstrap, JVM args, icon) | not in repo |
| CI | `installed-catalog.yml` (catalog `--check`); release/publish workflows | none (issue templates only) |
| Player memory guidance | `README.md` "Memory": 8 GB floor, 12 GB shaders; server figure measured, client labelled estimate | `config/memorysettings.json` tiers (16 GB sys → 8 GB, 32/48/64 GB → 12 GB); README silent |
| Early window | `pack/config/fml.toml` pins NeoForge defaults (verified byte-identical to ATM-10's except `versionCheck`) | `config/fml.toml` committed |
| Loading-screen UX | Crash Assistant installed (`crash-assistant.pw.toml`, client); no menu mod | FancyMenu + PackMenu (13 non-default keys) + Crash Assistant theme committed |

## 2. Measured loading behavior (this pack only — ATM-10 has none)

| Metric | Value | Source |
|---|---|---|
| Client boot to menu | 306.2 s / 314.9 s (two samples) | ModernFix "Game took" line in `latest.log` |
| JEI indexing after menu | **11.43 min**, of which **166.1 s freezes the render thread** | JET `pluginTiming`, clean boot |
| Server boot | 67–129 s band, machine-load dependent | `docs/smoke-runs/` |
| Chunkgen (CPS) | 13.5–21.2 band, same caveat | `docs/smoke-runs/` |
| Server RSS after worldgen | peaks ~7.4 GB in an 8 GB container | `docs/smoke-runs/` |
| `dynamic_resources` active | 20.55 s model posting at boot, 3.76 min on F3+T reload, zero mixin failures | client `latest.log` |
| F3+T reload | 6.8 min, completed, no abort | client `latest.log` |

ATM-10's repo contains **zero** measured numbers. The `memorysettings.json` tiers are the closest thing to memory policy, and they are static thresholds, not measurements.

## 3. Comparison table

| Area | ATM-10 does | My pack does | Gap or difference | Evidence | Confidence |
|---|---|---|---|---|---|
| Launch reproducibility | Nothing in git; launch lives in CurseForge profile + panel | `server/run.sh` + `user_jvm_args.txt` + `update_prism.py`, all committed | **Advantage.** A fresh machine reproduces this pack's launch exactly; theirs cannot be reconstructed from the repo | `server/run.sh:10-14`; `scripts/update_prism.py` | VERIFIED |
| GC policy | not in repo | ZGC everywhere, `-XX:+ZGenerational` explicitly refused, 1.5 GB headroom math to avoid OOM-kill exit 137 | Policy with a documented reason; no comparison possible | `pack/user_jvm_args.txt`; `server/run.sh` | VERIFIED (mine) / UNKNOWN (theirs) |
| Regression harness | none | `scripts/smoke_test.py`: boot, `/neoforge generate` (radius 8), `/tick query`, RSS, diffed report under `docs/smoke-runs/`; `--skip-bench`, `--profile` Spark injection | **Large advantage.** Every phase-1–3 measurement came from this | `scripts/smoke_test.py --help`; `docs/smoke-runs/` | VERIFIED |
| Save-path bench | none | `scripts/save_bench.py`: shared-world flush/shutdown timing per config | Advantage; settled the Smooth Chunk Save removal | `scripts/save_bench.py` | VERIFIED |
| Override audit | none | `scripts/audit_overrides.py --inventory --items` | Advantage; 0 re-enable candidates, honest buckets | `scripts/audit_overrides.py` | VERIFIED |
| Datapack wiring cost | `[datapacks].required` includes `"resourcepacks/"` — Global Packs re-resolves the whole client pack folder on every data sync | **Removed.** That entry did nothing except the re-resolve (`CHANGELOG.md`, Unreleased) | **Advantage, already landed.** Their file still carries it | `_reference_pack/config/global_data_and_resourcepacks.toml` vs `pack/config/global_packs.toml` | VERIFIED |
| Client pack cache | not found | ResourcePackCached keeps server packs across rejoins (client) | Can't compare; mechanism worth having | `pack/mods/resourcepackcached.pw.toml` | VERIFIED (mine) |
| Zip-parse cache | not found | quick-pack (both) for faster datapack/resourcepack parse | Can't compare | `pack/mods/quick-pack.pw.toml` | VERIFIED (mine) |
| Memory tiers for players | `memorysettings.json` with system-RAM tiers | README prose (8/12 GB) + ZGC headroom warning | Different shape, same job. Theirs is machine-readable by a launcher; mine is human-readable with a measured server figure | Both files | VERIFIED |
| Crash UX | Crash Assistant theme + modlist committed | Crash Assistant installed, no committed theme | Minor; theirs is prettier on crash day | `_reference_pack/config/crash_assistant/` | VERIFIED |
| Menu/loading UX | PackMenu + FancyMenu committed | none | Their main-menu experience is curated; mine is stock. Cosmetic, not performance | `_reference_pack/config/packmenu.cfg` (13 real changes) | VERIFIED |
| Local disk cost of caching | n/a | `.cache` 899 MB, `dist/` 41 GB (kept smoke worlds, zips, resolved mods) | **Self-inflicted.** Nothing reclaims this; worth a periodic clean | `du -sh .cache dist` | VERIFIED |

## 4. Recommendations

Ranked by impact ÷ risk. **Nothing applied.**

### R1 — Reclaim local disk with a documented clean step (impact: low, risk: low)

41 GB in `dist/` and ~900 MB in `.cache` accumulate silently. `dist/_save-bench` (2.1 GB) was already deleted by hand once. Nothing in the repo tells the next person what is safe to delete.

Cheapest fix: a short "disk hygiene" note in `CONTRIBUTING.md` naming what each directory is and what regenerates it (`dist/` artifacts rebuild from `pack/`; `.cache/mod-files` re-downloads; `dist/_smoke-test` rebuilds on next run). No code, no behavior change.

### R2 — Record why there is no menu/loading-screen mod (impact: low, risk: low)

ATM-10 ships PackMenu + FancyMenu; this pack ships neither. That is presumably deliberate (loading-screen mods touch the same early path as ModernFix/FastBoot), but it is unrecorded, so the next person compares screenshots and files a "missing" issue.

One line in `docs/mods/configs.md` or the audit: loading-screen mods stay out while ModernFix + quick-pack + FastBoot own early load. If the reason is different, write the real one.

### R3 — Do **not** chase their memory tiers (no action)

`memorysettings.json` tiers describe ATM-10's pack, not this one, and its numbers were never copied for R1 for exactly that reason. The README prose plus the measured 7.4 GB server figure is the better artifact. No change.

### R4 — Do **not** re-add `resourcepacks/` to datapack loading (no action)

ATM-10 still carries the entry this pack deliberately removed. Their file re-resolves the client pack folder on every sync. Already settled here; recorded so nobody "aligns" with them.

## 5. What this pack does better — do not "fix" these

- **Reproducible launch.** Every flag, every script, every headroom calculation is in git. ATM-10's launch is unreconstructable from its repo.
- **Three measurement harnesses** (`smoke_test.py`, `save_bench.py`, `audit_overrides.py`), each filling a gap the others cannot see. ATM-10 has none.
- **Measured memory policy.** 7.4 GB RSS peak → 8 GB floor is a number with a source. Their tiers have no cited measurement.
- **The `resourcepacks/` datapack removal.** Already landed; theirs still pays the re-resolve cost.
- **Honest variance reporting.** Boot/CPS bands are published with the machine-load caveat rather than as single best-case figures.

## 6. Could not be verified

- Everything about ATM-10's actual launch, GC, boot time, memory use, and join behavior — none of it is in the repo.
- Whether quick-pack / ResourcePackCached equivalents exist in ATM-10 — no config files for either, which is not evidence of absence.
- Whether their `memorysettings.json` tiers were ever validated against real usage.

## Remaining phases / follow-up tasks

- **Phase 5 (maintenance)** is all that remains: their `CHANGELOG.md` + 59 per-version `changelogs/` files vs one `CHANGELOG.md` here, plus versioning, testing, and update workflow.
- R1 is docs-only. R2 is one line of documentation.
- Open items unchanged: `docs/TODO.md` is the single list.

## Questions for me

1. R1/R2 are both one-line docs changes — want them applied, or batched with whatever comes next?
2. Phase 5 next to close out the audit, or pause here? Phases 1–4 have all produced reports; only maintenance remains.
