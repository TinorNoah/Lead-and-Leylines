---
name: modpack-audit
description: Read-only audit of this modpack against a reference modpack GitHub repo, comparing optimization, stability, config, load-time, or maintenance setup one phase at a time. Use only when the user names a reference repo and a phase number (for example "compare against ATM-10, phase 1"). Not for installing mods, updating the pack, or general code review.
---

# Modpack audit

Compare this pack against a reference modpack, one phase at a time, and write findings to a report. Never change the pack during an audit.

## Inputs

Ask for these before doing anything if they are not already given in the request:

- `REFERENCE_REPO` — GitHub URL of the reference modpack.
- `PHASE_TO_RUN` — a single number from 1 to 5 (see Phases).

`MY_PACK` is the current working directory (this repo).

If either input is missing, ask and wait. Do not guess a reference repo or run more than one phase.

## Ground rules

1. **READ-ONLY.** Never modify, delete, or overwrite anything in this pack during an audit. The only file the audit may create is its report under `docs/`. Changes happen only after the user approves specific items, and then as a separate task.
2. **Clone the reference outside the pack.** Use `git clone --depth 1 <REFERENCE_REPO> ../_reference_pack` so nothing lands inside `pack/`. If the clone fails, or the reference repo has no mod list and no configs, tell the user instead of working around it.
3. **Detect pack details yourself, for both packs.** Minecraft version, loader and loader version, mod count, client/server/both split, and launcher format (CurseForge manifest, `.mrpack`, instance folder, packwiz). This pack's source of truth is `pack/pack.toml` (`version`, `[versions]`) plus `pack/mods/*.pw.toml`. Report what was found and what could not be determined.
4. **Check version and loader compatibility before recommending anything.** State explicitly which findings transfer from the reference pack and which do not, and why.
5. **Cite exact paths for every finding.** File paths plus line number or TOML/JSON key where possible. If there is no evidence for something, write `not found`. Never guess.
6. **Label every statement** `VERIFIED` (seen in files), `INFERRED` (reasoning given), or `UNKNOWN`.
7. **Never invent** mod names, config keys, JVM flags, or settings. Before recommending one, confirm the mod is in this pack (or exists for this MC version and loader, if it is a candidate to add) and that the key actually exists in this pack's config files.
8. **Never recommend copying reference configs wholesale.** Judge each item against this pack's size, purpose, and mod list. This pack is not the reference pack.
9. **Prefer evidence from the two repos.** If external documentation is needed, name the source.

## Phases

Run **only** the requested phase, then stop.

| # | Area |
|---|-----|
| 1 | Performance and optimization: optimization mods, their configs, JVM/launch args, render/entity/chunk/memory tuning |
| 2 | Mod conflicts and bug fixes: KubeJS/CraftTweaker scripts, mixin or config overrides, fix/patch mods, removed or replaced mods, known-issue workarounds |
| 3 | Config management: `defaultconfigs`, server vs. client configs, config sync, datapacks and resource packs |
| 4 | Startup, load time, and memory: launch scripts, caching, loading behavior |
| 5 | Maintenance and quality: versioning, changelogs, testing, update workflow |

If a phase is too large to finish reliably, split it: do the first part properly and list the remainder as follow-ups in the report.

## Procedure for the chosen phase

1. Inventory this pack for the phase's area. Cite paths.
2. Inventory the reference pack for the same area. Cite paths inside `../_reference_pack`.
3. Compare in a table: `Area | Reference does | My pack does | Gap or difference | Evidence (paths) | Confidence`.
4. For each gap: what to change, why it helps, risk (`low`/`med`/`high`), and how to test it (before/after launch, log line, or profiler check).
5. List what this pack does well or differently on purpose, so it is not changed needlessly.
6. Rank recommendations by impact versus risk.

## Output

- Write the full report to `docs/audit_<reference-name>_phase<N>.md` (create `docs/` if needed). `<reference-name>` is the reference repo's directory name, lowercased and hyphenated (for example `atm-10`).
- In chat: top 5 findings, anything uncertain, anything that could not be verified.
- End the report with `Remaining phases / follow-up tasks` and `Questions for me`.

## Stop condition

Apply no changes. After the report, stop and wait for the user to choose what to implement.

For this pack, implement any approved item through the `minecraft-modding` and `add-mod` skills, and verify with `local-smoke-test` — not inside an audit.