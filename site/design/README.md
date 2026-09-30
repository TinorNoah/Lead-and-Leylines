# Site design references

Stitch mocks and the conventions for turning them into site code.

`stitch-screen` is the skill that drives the loop (generate → reference → implement → verify → gate). This file is the reference it links to: what the theme actually is, which primitives exist, and the brand rules that decide disputes.

## Files

| File | Surface |
|---|---|
| `cards-view.png` | Mod grid, desktop |
| `list-view.png` | Dense table, desktop |
| `detail-drawer.png` | Radix sheet, desktop |
| `mobile-filters.png` | Vaul drawer, mobile |
| `emblem.svg` / `emblem.png` | Pack emblem (favicon) |

Screenshots are the diff target during verification, not a spec. Overwrite a file when a screen is redesigned rather than adding `-v2` copies.

## Loop

1. Generate one screen in Stitch (narrow prompt, name it after the surface).
2. Export to `stitch/<name>.png`.
3. Implement in `site/src/components/` against the theme below.
4. `cd site && bun run dev`.
5. Screenshot at 390x844 and 1440x900 with the `playwright` MCP.
6. Diff against the reference, iterate.
7. `bun run lint && bun run test`.

## Theme — Leyline Cartographer

Amber and moss on forest ink. Defined in `src/app/globals.css` as CSS variables re-exported through Tailwind v4 `@theme inline`, so reference them as Tailwind utilities, never as raw hex.

| Role | Token | Value |
|---|---|---|
| Page | `bg-background` | `#0c1513` |
| Surface | `bg-card`, `bg-card-elevated` | `#18211f`, `#1c2b28` |
| Border | `border-card-border`, `border-card-border-active` | `#2c403c`, `#3a544f` |
| Amber | `text-primary`, `text-primary-bright` | `#dfb16c`, `#fdcc85` |
| Moss | `text-secondary`, `text-secondary-dim` | `#84d8a7`, `#489b6f` |
| Text | `text-foreground`, `text-muted`, `text-muted-foreground` | `#dbe5e1`, `#9aa8a2`, `#d2c4b4` |
| Fills | `bg-accent-soft`, `bg-moss-soft`, `bg-chip` | amber 12%, moss 16%, `#162220` |
| Alert | `text-danger` | `#d04f4f` |
| Glow | `shadow-[var(--ley-glow)]` | amber 22% bloom |

Type: `font-display` (Playfair Display, headings), `font-sans` (Plus Jakarta Sans, body), `font-mono` (JetBrains Mono, tags and metadata).

A Stitch screen will carry its own hex values and CSS variables. Translate them — a near-match on the wrong token drifts from the palette the moment anything else on the page changes. If a mock asks for a colour that has no token, that is usually a sign the mock is wrong, not that a token is missing.

## Primitives

`src/components/ui/` — `Button`, `Badge` (variants: `default`, `moss`, `muted`, `outline`), `Input`, `ScrollArea`, `Sheet` (Radix Dialog), `ToggleGroup`. Compose with `cn` from `@/lib/utils`.

Reuse these before adding anything. Mobile filters use the Vaul `Drawer`; the desktop detail panel uses `ui/sheet`. A new dependency needs a reason — library swaps are fine when they match the theme, not just to satisfy a mock.

## Brand

Player-first browse: search, filters, full category/tag nav, card/list views, detail drawer, no accounts. Earthy and atmospheric, easy to scan. It is a mod browser, not a SaaS dashboard — if a generated screen looks like an admin console, it is wrong.

Data comes from `docs/installed/catalog.json` fetched at runtime. Do not invent mods to fill a layout; empty and loading states are part of the design.

Background particles are fine only when they respect `prefers-reduced-motion`.
