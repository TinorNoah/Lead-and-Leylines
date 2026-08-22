# Task 6 Report: Root docs

## Status

Completed on branch `phase-1-dev-workflow`.

## Changes

- Replaced the untracked continual-learning `AGENTS.md` with the brief's complete conventions followed by the retargeted learned sections.
- Added `CLAUDE.md` as the exact one-line `@AGENTS.md` pointer.
- Added `README.md` with the project summary and links to contributor and agent documentation.
- Added `CONTRIBUTING.md` with packwiz installation, mod addition, Prism testing, release, secrets, and Pelican guidance.
- Opened the packwiz installer bootstrap releases page before writing. It identifies `v0.0.3` as latest, but the contribution step intentionally retains the brief's version-independent wording and links to the latest-release listing rather than hardcoding a tag.

## Verification

- Version-literal guard across all four docs: passed; no matches for `1\.20|47\.4`.
- `AGENTS.md` line-count guard: passed (`55` nonblank lines reported by PowerShell, below `200`).
- Exact `CLAUDE.md` content and single trailing newline check: passed.
- IDE lint diagnostics for all four files: no errors.
- Final verification command exited `0` with `DOC_CHECKS=PASS`.

## Commit

- `575174c docs: add packwiz workflow conventions and contributor loop`
- Git identity was missing, so the commit used command-scoped identity:
  - `TinorNoah`
  - `TinorNoah@users.noreply.github.com`
- No push was performed.

## Concerns

- Existing untracked `.cursor/` and `docs/` directories remain untouched.
- This report and other `.superpowers/` content were not committed.

## Task 6 fix: bootstrap jar asset URL

### Status

Completed on branch `phase-1-dev-workflow`.

### Finding addressed

`CONTRIBUTING.md` linked only to the releases listing. Updated the Prism test step to use the exact latest release asset URL for `packwiz-installer-bootstrap.jar`.

### URL used

- Latest release tag: `v0.0.3` (confirmed via GitHub API / releases page)
- Asset URL: https://github.com/packwiz/packwiz-installer-bootstrap/releases/download/v0.0.3/packwiz-installer-bootstrap.jar

### Covering check output

```
PS> Select-String -Path CONTRIBUTING.md -Pattern "packwiz-installer-bootstrap"

CONTRIBUTING.md:22:2. Download `packwiz-installer-bootstrap.jar` from
https://github.com/packwiz/packwiz-installer-bootstrap/releases/download/v0.0.3/packwiz-installer-bootstrap.jar into
the instance `.minecraft` folder (same folder as `options.txt`).
CONTRIBUTING.md:26:   `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar http://localhost:8080/pack.toml`

PS> Select-String -Path AGENTS.md,CLAUDE.md,CONTRIBUTING.md,README.md -Pattern "1\.20|47\.4"

(no matches)
```

### Commit

- `fix(docs): use exact packwiz-installer-bootstrap jar URL` (HEAD on `phase-1-dev-workflow`)
- Git identity: `TinorNoah` / `TinorNoah@users.noreply.github.com`
- No push performed.
