# Lead and Leylines — installed-mod browser

Browse, search, and filter every mod currently in the pack. The site reads one pre-built file, [`docs/installed/catalog.json`](../docs/installed/catalog.json), from GitHub. It does not download the repo tarball or parse packwiz TOML at runtime.

## Local development

```bash
cd site
cp .env.example .env
# Optional: point at local seed while iterating
# SEED_CATALOG_PATH=./seed/catalog.json
# DATA_DIR=./.data
mkdir -p seed .data
cp ../docs/installed/catalog.json seed/catalog.json
bun install
bun run dev
```

Open [http://localhost:3000](http://localhost:3000).

```bash
bun run test      # chunking + webhook HMAC unit tests
bun run build
```

Uses **Bun** for install/build/test. UI follows the Stitch **Leyline Cartographer** theme (Playfair / Plus Jakarta / JetBrains Mono; amber + moss on forest ink).

## Docker (local)

Build context is the **repo root** so the image can bake in `docs/installed/catalog.json`.

```bash
# from repo root
docker build -f site/Dockerfile -t ll-mod-browser .
docker run --rm -p 3000:3000 -v ll-mod-data:/data --env-file site/.env ll-mod-browser

# or
cd site && docker compose up --build
```

The root [`.dockerignore`](../.dockerignore) is an allowlist: only `site/` and `docs/installed/catalog.json` enter the build context.

## Dokploy

Use a **Dockerfile** application pointed at this repo (branch `main`).

1. **Create Application** → source = this GitHub repo, branch `main`.
2. **Build**
   - Build type: **Dockerfile**
   - Build context / context path: `.` (repository root — required so the image can bake `docs/installed/catalog.json`)
   - Dockerfile path: `site/Dockerfile`
3. **Network**
   - Publish port **3000** (container) → your domain or Dokploy port mapping.
4. **Volume**
   - Mount a persistent volume at `/data` (last-good catalog + CurseForge/Modrinth metadata cache).
5. **Environment** (copy from [`site/.env.example`](.env.example)):

   | Variable | Required | Example / notes |
   |---|---|---|
   | `GITHUB_REPO` | yes | `TinorNoah/Lead-and-Leylines` |
   | `GITHUB_BRANCH` | yes | `main` |
   | `REVALIDATE_SECRET` | yes | Long random string; same value as the GitHub webhook secret |
   | `CACHE_TTL_SECONDS` | no | `600` (poll interval) |
   | `DATA_DIR` | no | `/data` |
   | `SEED_CATALOG_PATH` | no | `/app/seed/catalog.json` (baked in image) |
   | `CURSEFORGE_API_KEY` | no | Icons/summaries; without it, monograms + CF links still work |
   | `GITHUB_TOKEN` | no | Raises GitHub API rate limits for the commit poll |

6. **Deploy**. Open `https://<your-host>/api/health` — expect `"ok": true` and `"mod_count": 451` (or current count). Then open `/`.

### Optional GitHub webhook (near-instant updates)

1. GitHub repo → Settings → Webhooks → Add webhook.
2. Payload URL: `https://<your-host>/api/revalidate`
3. Content type: `application/json`
4. Secret: same as `REVALIDATE_SECRET`
5. Events: **Just the push event**
6. Active → Add webhook. GitHub’s ping should return 200.

Without the webhook, the site still refreshes on its poll interval when `main` moves.

### After deploy

- Mod list changes: merge catalog updates to `main` (no site rebuild needed).
- Site code / Dockerfile changes: redeploy the Dokploy application.

## How updates work

1. Hand-edit [`docs/installed/catalog.toml`](../docs/installed/catalog.toml) when adding/removing mods (packwiz does not update it). Policy: [`docs/installed/MAINTENANCE.md`](../docs/installed/MAINTENANCE.md).
2. Run `python3 scripts/installed_catalog.py` to regenerate markdown + `catalog.json`.
3. Merge to `main`.
4. The site polls the latest commit (default every 10 minutes) or refreshes immediately via the webhook.
5. Last-good data is kept on `/data`. A baked seed covers cold starts with no network.

## API

| Route | Purpose |
|---|---|
| `GET /api/mods` | Full catalog JSON with tags and store metadata |
| `GET /api/health` | Liveness / readiness |
| `POST /api/revalidate` | GitHub push webhook |
