# Audit: Lead and Leylines vs ATM-10 — Phase 5 (maintenance and quality)

- **Reference:** `AllTheMods/ATM-10`, shallow clone at `../_reference_pack`
- **This pack:** `Lead and Leylines` 0.1.24, `pack/pack.toml`
- **Scope:** versioning, changelogs, testing, update workflow
- **Read-only.** This report is the only file created.

## 0. Evidence limits

Same as phases 1–4: ATM-10's CurseForge builds, server, and launcher profile are outside the repo. Maintenance findings are about what is *in git* on each side.

## 1. Maintenance surface

| | This pack | ATM-10 |
|---|---|---|
| Pack version | 0.1.24 in `pack/pack.toml`, tag `v0.1.24` | 8.2 in `config/bcc-common.toml` |
| Versioning scheme | SemVer, `vX.Y.Z` tags, documented tag rules in `CHANGELOG.md` header | `major.minor` per release (8.2), no scheme doc in repo |
| Changelog | One `CHANGELOG.md`, 26 version sections, Keep-a-Changelog, player-facing prose | `CHANGELOG.md` (54 headers, **53 empty**) + 57 per-version files with full mod-bump lists |
| Release tooling | `scripts/release.py` (tag + GitHub Release + Pelican + Prism), `draft_changelog.py`, `publish_stores.py`, `docs/RELEASING.md` policy | none in repo |
| Update checking | `scripts/check_outdated.py` (report-only, temp-copy diff) | none in repo |
| Pre-commit | `scripts/pre_commit_check.py` (blocks jars, warns on missing changelog/catalog) + opt-in `.githooks/pre-commit` | none in repo |
| CI | `installed-catalog.yml` (`--check`), `publish-stores.yml` | none (issue templates only) |
| Test harnesses | `smoke_test.py`, `save_bench.py`, `audit_overrides.py` | none |
| Mod docs | `docs/installed/` (catalog + 30 categories, generated + `--check`) | `MOD_ISSUES.md` (per-mod issue links) |

## 2. Comparison table

| Area | ATM-10 does | My pack does | Gap or difference | Evidence | Confidence |
|---|---|---|---|---|---|
| Changelog content | 57 per-version files, each a full mod-bump list (`Ad Astra (1.16.19) -> (1.16.26)`, thousands of bullets in 8.1-8.2) grouped under Mods/Recipes/Tags/Registries/Loot Table | One file, player-facing prose per version, machine-readable `## [X.Y.Z]` headers consumed by `release.py` as the GitHub Release body | **Different audiences, both valid.** Theirs answers "what changed exactly" for a team; mine answers "what will I notice" for players. Their main CHANGELOG is 53-empty, so the index file is decorative | `_reference_pack/changelogs/CHANGELOG-ATM10-8.1-8.2.md` (3308 bullets) vs `CHANGELOG.md` + `scripts/release.py` | VERIFIED |
| Mod-bump traceability | Every version lists every mod change with versions | `CHANGELOG.md` rarely names mod versions; `pack/mods/*.pw.toml` + git history carry the pins | **Real gap, low cost to close.** When a player reports "broke in 0.1.23", there is no version-to-version mod diff in prose — only git | `CHANGELOG.md` vs `changelogs/CHANGELOG-ATM10-*.md` | VERIFIED |
| Release process | Not in repo (CurseForge UI + panel, presumably) | `scripts/release.py`: tag → GitHub Release → Pelican pull → Prism sync, with `--channel`, `--skip-server`, `--skip-prism` flags, all from one command | **Advantage.** Reproducible, reviewable, documented in `docs/RELEASING.md` | `scripts/release.py`; `docs/RELEASING.md` | VERIFIED |
| Update workflow | Not in repo | `check_outdated.py` diffs `packwiz update --all` in a temp copy without touching `pack/`; `draft_changelog.py` drafts bullets from `.pw.toml` diffs for rewriting into player prose | Advantage; both are report-only by design | Both scripts' docstrings | VERIFIED |
| Pre-commit safety | none | Blocks staged jars; warns when `.pw.toml` is staged without changelog/catalog updates | Advantage; the jar block is the load-bearing one for a packwiz pack | `scripts/pre_commit_check.py`; `.githooks/pre-commit` | VERIFIED |
| Catalog as docs | none (`MOD_ISSUES.md` links each mod to its issue tracker) | Generated `docs/installed/` (590 mods, 30 categories) with `--check` in CI and as a `release.py` preflight | **Different jobs.** Theirs routes bug reports; mine browses the pack. Neither replaces the other | `docs/installed/` vs `_reference_pack/MOD_ISSUES.md` | VERIFIED |
| Issue routing | `MOD_ISSUES.md`: every mod → issue page | none | **Genuine gap.** A player hitting a mod bug here has no recorded place to file it | `_reference_pack/MOD_ISSUES.md` | VERIFIED |
| Secrets handling | n/a | Tokens in gitignored `.env`, never in git; documented in `server/README.md` and `docs/RELEASING.md` | Good practice, verified by absence (no tokens in repo) | `.env.example`; `git log -p` shows no token commits (not exhaustively audited) | VERIFIED (practice) |

## 3. Recommendations

Ranked by impact ÷ risk. **Nothing applied.**

### R1 — Add per-version mod-bump lists without changing the changelog's voice (impact: med, risk: low)

The player prose stays. What is missing is the mechanical record: which mods moved between versions. `draft_changelog.py` already produces exactly that from `.pw.toml` diffs, but its output is a starting point that gets rewritten away.

Cheapest version: keep a `docs/changelogs/` per-version file (or an appendix section) with the raw mod-bump list per release, generated by `draft_changelog.py` at release time and committed unedited. Player prose in `CHANGELOG.md` stays the front door; the bump list is the fire escape for "broke in 0.1.23" reports. No new tooling — the generator exists.

Do **not** copy their 57-file split or their emoji headers. One file per version, plain names, is enough.

### R2 — Add a per-mod issue-routing doc (impact: low, risk: low)

`MOD_ISSUES.md` is the one ATM-10 maintenance artifact with no equivalent here, and it is genuinely useful: when a player hits a mod bug, "file it upstream at this link" beats "ask in Discord". This pack has 590 mods; the list can be generated from `pack/mods/*.pw.toml` project IDs (CurseForge) the same way `installed_catalog.py` generates the catalog.

Generate, do not hand-write. If generation is too much work, skip it — a stale hand-written list is worse than none.

### R3 — Keep the single changelog (no action)

Their 53-empty main CHANGELOG with content in 57 side files is strictly worse as an index than one file with 26 real sections. Do not imitate the shape; R1 adds the missing content without the split.

## 4. What this pack does better — do not "fix" these

- **Reproducible releases.** One command, flags for every skip, policy in `docs/RELEASING.md`. Their process is not in git at all.
- **Report-only update tooling.** `check_outdated.py` and `draft_changelog.py` both refuse to write, by design. Safe to run, impossible to fat-finger.
- **Pre-commit jar block.** The single most valuable hook in a packwiz pack, and it is a hard block rather than a warning.
- **Catalog with CI enforcement.** `--check` runs in CI and as a release preflight; drift is caught, not discovered.
- **Player-facing changelog discipline.** Every entry is written for the person installing the update, and the `publish-release` skill promotes `[Unreleased]` rather than rewriting history.

## 5. Could not be verified

- How ATM-10 actually releases (CurseForge UI flow, panel steps) — not in the repo.
- Whether their per-version files are generated or hand-written — the uniformity suggests generation, but no generator is in git.
- Whether anyone reads the 3308-bullet files — no analytics in a repo, obviously.

## Audit close-out

All five phases are now reported:

| Phase | Report | Status |
|---|---|---|
| 1 Performance/optimization | `docs/audit_atm-10_phase1.md` | Implemented (R1–R6), merged in #59 |
| 2 Conflicts/bug fixes | `docs/audit_atm-10_phase2.md` | Follow-ups implemented, merged in #60 |
| 3 Config management | `docs/audit_atm-10_phase3.md` | Corrected (206 files, 21 non-default); R1/R2 open |
| 4 Startup/load/memory | `docs/audit_atm-10_phase4.md` | Reported; R1/R2 are one-line docs changes |
| 5 Maintenance/quality | this file | Reported below |

Open items live in one place: `docs/TODO.md`.

## Questions for me

1. R1 (per-version mod-bump lists): want them? It is a small addition to the release flow — commit `draft_changelog.py` output unedited per version.
2. R2 (issue routing): generate from project IDs, or skip? Hand-writing 590 links is not on the table.
3. Anything else before this audit is closed, or is `docs/TODO.md` + these two questions the complete handoff?
