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

- [ ] **Override revalidation boot tests** — `scripts/audit_overrides.py --inventory --items` reports **0** re-enable candidates, so the rest needs boots batched per namespace. Plan and batches: `docs/mods/load-fixes-inventory.md` ("TODO — deferred, not started").
- [ ] **JEI Stuff's server-side join sync** — still unmeasured. Client cost is 4.5s of an 11.9min index, so it is not the client stall.
- [ ] **`smoke_test.py` join measurement** — the harness never logs a player in, so it cannot measure join sync at all.
- [ ] **`dynamic_resources` boot-time proof** — proven safe and active through a full F3+T reload, speedup unproven (306s vs 315s is noise, no baseline with it off).
- [ ] **Inventory Essentials re-decision** — rationale went stale when IPN was removed; it declares no IPN dependency, so it stands alone but needs a real justification or removal.

## Upstream (waiting on others)

- [ ] **Tonywww2/JEI-Optimize#12** — re-test if JET ships a 19.57-complete ABI build.
