---
name: stitch-screen
description: Turn a Stitch screen into a working, browser-verified site surface. Use when a screen is generated or edited in Stitch, when a new mod-browser surface is needed (card/list view, filter, drawer, empty state), or when an existing surface must be checked against the running site. Not for pack, mod, or release work.
---

# Stitch a screen

Design in Stitch, implement against the site theme, verify in a real browser. One screen per pass.

Theme tokens, primitive list, and brand rules: [site/design/README.md](../../../site/design/README.md).

## Steps

1. **Generate in Stitch.** One screen per call via the `stitch` MCP, named after the surface (`cards-view`, `list-view`, `detail-drawer`, `mobile-filters`) — never a generation id. Broad "design the whole app" prompts come back vague; narrow to one surface and say which breakpoint it targets.
2. **Save the reference.** Export the screen to `site/design/stitch/<name>.png`. That file is the diff target in step 6, so overwrite it deliberately rather than accumulating `-v2` copies.
3. **Implement against the theme, not the mock.** Recreate the layout; do not paste Stitch's HTML or CSS. Use the Tailwind `@theme` tokens (`bg-card`, `text-primary-bright`, `border-card-border`, `accent-soft`, `moss-soft`, `ley-glow`, `font-display`, `font-mono`) and reuse `site/src/components/ui/`. Add a primitive only when none fits. Icons are `lucide-react`.
4. **Run the site.** `cd site && bun run dev`, then http://localhost:3000. Bun only — never npm. Seed first if `seed/catalog.json` is missing (see `site/README.md`).
5. **Verify in Playwright.** Via the `playwright` MCP against the running dev server. Check both 390x844 and 1440x900 — a Stitch screen is usually one of them only. Screenshot each.
6. **Diff against the reference.** Compare the Playwright screenshot to `site/design/stitch/<name>.png`. Fix real divergence (spacing, hierarchy, colour, missing states), not Stitch's incidental artifacts. Console errors fail this step.
7. **Gate.** `cd site && bun run lint && bun run test`. Then `update-changelog` if the change is player-visible.

## Side

Stitch is a starting point, not the spec — the theme wins wherever they disagree. A screen that reads as a SaaS dashboard is wrong even if the mock says otherwise; this is a player-first mod browser, not an admin console. Background particles must respect `prefers-reduced-motion`. Never invent mod data to fill a layout; empty and loading states come from the real catalog fetch.
