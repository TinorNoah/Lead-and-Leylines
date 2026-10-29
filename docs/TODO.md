# To do

The single list of open work. Details live in the linked docs — this file is the index, not a duplicate.

## Needs your input (blocking)

- [ ] **Balance-tuning values + placement** — 7 mods from the phase 3 follow-up (Oritech energy ~2–4×, MI FE:EU 10→16, RS energy 1000→50000, Create Enchantment Industry 30→50/60→100, Apotheosis `miners_fervor` 5→1, Just Dire Things time-wand 100→750 RF, Curios offset skipped). Oritech and MI interact through FE, so decide those two together. Placement is part of the same decision: server-balance items belong in `defaultconfigs/`, which does not exist yet.
- [ ] **R2: want server-operator policy in the pack at all?** (Ultimine permissions, spawn rules, machine tick speeds.) If no, document *why* there is no `defaultconfigs/` so the absence reads as a decision. Overlaps the placement question above — answer once.
- [ ] **R1: permission for a scratch packwiz test** — does `side` work on non-mod index entries? Decides whether the 5 client-only configs in the server zip get a manifest fix or a `pack_artifacts.py` filter.

## Audits remaining

- [ ] **Phase 4** (startup, load time, memory)
- [ ] **Phase 5** (maintenance)

## Parked (deferred, not blocking any release)

- [ ] **Verify the 2026-10-25 mod wave in game** — Animal Pens accepting entities it should not (Ice and Fire dragons, bosses) and Tool Belt's belt bar beside Curios both need a real client session; a dedicated boot cannot show either. Also confirm the starting-kit iron backpack arrives on a fresh join.
- [ ] **Verify the 2026-10-25 tech wave in game** — the second wave of that day needs a client session for things a boot cannot show: Superb Warfare's gun and vehicle keys against TaCZ and Vic's Point Blank (three firearm systems now share the keyboard), SKY ACES' aircraft controls, whether Grim Storage's network and Smartstock's terminals read AE2/Refined Storage inventories correctly, and whether the Grim trio plus Voltex/Singulo/HBM overlap enough in recipes to confuse players. Balance between those tech trees is unmeasured.
- [ ] **One-off client startup crash, 2026-10-25 06:32** — `Failed to wait for future Common setup` from `ExceptionInInitializerError: ClosedWatchServiceException` at `fzzy_config ThreadingUtils.register`, triggered by `simplyswords config.LootConfig.<clinit>`. Fzzy Config 0.7.7 is the newest 1.21.1 build, so there is no update path; the immediate relaunch booted clean. If it recurs, it is a race between Fzzy's shared config watcher being closed and a late config class-init, and needs an upstream report rather than a pack change.
- [ ] **Epitaphs graves in existing worlds** — the Epitaphs→Graveless swap (2026-10-25) orphans Epitaphs grave blocks. Any grave still holding items in the test world is item loss; clear or empty them before updating that world, or accept it.
- [ ] **Override revalidation boot tests** — `scripts/audit_overrides.py --inventory --items` reports **0** re-enable candidates, so the rest needs boots batched per namespace. Plan and batches: `docs/mods/load-fixes-inventory.md` ("TODO — deferred, not started").
- [ ] **TaCZ Tactical Breaching 1.0.7 startup crash** — kept in the pack by choice, but `ClientWeaponHeatHandler.tick` reads `BallisticBlockConfig.ENABLE_WEAPON_HEAT` during the loading-overlay tick, before the config spec is loaded, and throws `Cannot get config value before config is loaded`. Seen on 2026-09-28, 2026-10-05, 2026-10-25 and 2026-10-30 with a healthy JEI, so it is its own race and not the JEI break above; a relaunch usually boots. 1.0.7 is the newest file on CurseForge and Modrinth and its Superb Warfare support is disabled against the pack's SBW 0.8.9.2. Candidate fix: a guard mixin in `leylines_patches` that no-ops the tick until `BallisticBlockConfig.SPEC.isLoaded()`. Re-check for a 1.0.8 before writing it.
- [ ] **JEI Stuff's server-side join sync** — still unmeasured. Client cost is 4.5s of an 11.9min index, so it is not the client stall.
- [ ] **`smoke_test.py` join measurement** — harness added (`scripts/join-test/`, Mineflayer bot; see `local-smoke-test` skill), but the 2026-10-10 spike proved vanilla-protocol bots are rejected at NeoForge negotiation (`vanilla.client.not_supported`), so no login timing. Remaining paths: HeadlessMc real client (Linux+Xvfb, not set up) or fake-player mods (skip login sync itself).
- [ ] **`dynamic_resources` boot-time proof** — proven safe and active through a full F3+T reload, speedup unproven (306s vs 315s is noise, no baseline with it off).
- [ ] **Inventory Essentials re-decision** — rationale went stale when IPN was removed; it declares no IPN dependency, so it stands alone but needs a real justification or removal.

## Upstream (waiting on others)

- [ ] **Tonywww2/JEI-Optimize#12** — re-test if JET ships a 19.57-complete ABI build.
