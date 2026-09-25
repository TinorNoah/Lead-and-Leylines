# Lead and Leylines Catalog UI Redesign

**Date:** 2026-09-25  
**Status:** Approved (build)  
**Stitch project:** `589439745876233446` (Leyline Cartographer)

## Goals

Player-first browse of ~450 installed mods with an adventure/leyline brand. Maintainer detail (filename, source) lives in a detail drawer only. No accounts.

## Approach

Polish the existing Next.js App Router site in place. Switch tooling to Bun. Restyle and rebuild browse UX from Stitch mocks; keep catalog sync APIs (`/api/health`, `/api/mods`, `/api/revalidate`) and GitHub SHA-pinned loader unchanged.

## Visual system (from Stitch)

- **Name:** Leyline Cartographer
- **Fonts:** Playfair Display (display), Plus Jakarta Sans (UI), JetBrains Mono (meta)
- **Colors:** forest ink `#0c1513`, amber primary `#dfb16c` / `#fdcc85`, moss secondary `#84d8a7` / `#489b6f`, warm stone surfaces
- **Emblem:** geometric compass/diamond SVG from Stitch screen `c9201eaecad3482a9281890abae0e4e7`
- **Reference screens:** cards, list, detail drawer, mobile filter sheet under `site/design/stitch/`

## Information architecture

- Single Installed Mods surface (home)
- Sticky search (`⌘/Ctrl+K`)
- Desktop: category rail + side filter + searchable tags
- Mobile: filter bottom sheet
- Views: Cards | List | Grouped (default Cards)
- Detail drawer via `?mod=<file>`; shareable URLs for filters

## Out of scope (Stitch chrome not built)

Field Terminal extra nav, RAM/heap gauges, export/lock, multi-select checkboxes, user profile, Discover/Engine tabs, fake pack versions, dependency graph, favorites.

## Stack

- Next.js 16, React 19, Tailwind 4
- Bun for install/build/test and Docker image
- Fuse.js search (existing)
- UI primitives: Radix/shadcn-style or equivalent (Sheet, Dialog/Command, ToggleGroup, ScrollArea) — swap allowed if a library fits Stitch better
- Lucide (or similar) icons sparingly

## Deploy constraints

- Repo-root Docker context; `site/Dockerfile`; port 3000; volume `/data`
- Env vars unchanged (`GITHUB_REPO`, `REVALIDATE_SECRET`, etc.)
