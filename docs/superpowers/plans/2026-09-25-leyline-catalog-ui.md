# Leyline Catalog UI Implementation Plan

> **For agentic workers:** Execute task-by-task. Steps use checkbox syntax.

**Goal:** Redesign the installed-mods site to match Stitch Leyline Cartographer, migrate to Bun, keep catalog APIs intact.

**Architecture:** Next.js App Router client browse shell over existing server catalog enrichment. Design tokens + emblem drive look; Radix-based primitives for sheet/drawer/command; Fuse filters unchanged in spirit.

**Tech Stack:** Next 16, React 19, Tailwind 4, Bun, Fuse.js, Radix UI (Dialog/Sheet via custom), cmdk, lucide-react, class-variance-authority, clsx, tailwind-merge

## Global Constraints

- Player-first; no accounts; no Field Terminal fake nav
- Live pack data from catalog.json only
- Docker: Bun build, standalone Next, port 3000, `/data` volume
- Do not commit secrets; do not break `/api/health` contract

---

### Task 1: Bun migration

**Files:**
- Modify: `site/package.json`
- Create: `site/bun.lock` (via `bun install`)
- Delete: `site/package-lock.json`
- Modify: `site/Dockerfile`
- Modify: `site/README.md` (Bun commands)

- [ ] Replace scripts to use `bun`; add UI deps
- [ ] `cd site && bun install`
- [ ] Dockerfile: `oven/bun` multi-stage; `bun install --frozen-lockfile`; `bun run build`; runner can use `oven/bun` or node for standalone — prefer bun runtime `bun server.js` if standalone works, else node alpine with copied standalone
- [ ] Verify: `bun run build` succeeds

### Task 2: Design tokens + emblem + fonts

**Files:**
- Modify: `site/src/app/globals.css`, `site/src/app/layout.tsx`
- Create: `site/public/emblem.svg` (from Stitch)
- Modify: `site/src/lib/utils.ts` (cn helper)

- [ ] Port Stitch CSS variables
- [ ] Load Playfair Display, Plus Jakarta Sans, JetBrains Mono via next/font/google
- [ ] Copy emblem SVG to public

### Task 3: UI primitives

**Files:**
- Create: `site/src/components/ui/{button,badge,input,sheet,scroll-area,toggle-group,separator,tooltip}.tsx`
- Create: `site/src/components/ui/command.tsx` (cmdk)

- [ ] Install `@radix-ui/react-dialog`, `@radix-ui/react-toggle-group`, `@radix-ui/react-scroll-area`, `@radix-ui/react-separator`, `@radix-ui/react-tooltip`, `cmdk`, `lucide-react`, `class-variance-authority`, `clsx`, `tailwind-merge`
- [ ] Style primitives with Leyline tokens (amber primary, moss secondary, stone surfaces)

### Task 4: Browse shell rebuild

**Files:**
- Rewrite: `site/src/components/SiteHeader.tsx`, `CatalogBrowser.tsx`, `ModCard.tsx`, `ModTable.tsx`, `TagChip.tsx`
- Create: `site/src/components/ModDetailDrawer.tsx`, `FilterSidebar.tsx`, `MobileFilterSheet.tsx`, `ViewToolbar.tsx`, `ModList.tsx`
- Modify: `site/src/app/page.tsx` as needed

- [ ] Header with emblem + Playfair brand + pack meta + sync chip
- [ ] Sticky search with ⌘K
- [ ] Filters: categories+counts, side, searchable tags
- [ ] Cards / List / Grouped
- [ ] Detail drawer `?mod=`
- [ ] Mobile filter sheet

### Task 5: Verify

- [ ] `bun run build` + `bun run test`
- [ ] Local `bun run start` smoke `/api/health` and UI
- [ ] Update `site/README.md` for Bun + redesign notes

---

## Self-review

- Spec coverage: Bun, tokens, IA, out-of-scope carve, deploy constraints → tasks 1–5
- No Field Terminal chrome in tasks
- APIs unchanged
