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
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

```bash
npm test          # chunking + webhook HMAC unit tests
npm run build
```

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

1. Create an **Application**.
2. Build type: **Dockerfile**.
3. Build context: `.` (repository root).
4. Dockerfile path: `site/Dockerfile`.
5. Port: `3000`.
6. Mount a volume at `/data`.
7. Set env vars from [`.env.example`](.env.example). At minimum:
   - `GITHUB_REPO=TinorNoah/Lead-and-Leylines`
   - `GITHUB_BRANCH=main`
   - `REVALIDATE_SECRET=<long random string>`
   - Optional `CURSEFORGE_API_KEY` for icons
   - Optional `GITHUB_TOKEN` for higher API limits
8. Deploy.

### Optional GitHub webhook

After deploy, add a repository webhook:

- Payload URL: `https://<your-host>/api/revalidate`
- Content type: `application/json`
- Secret: the same value as `REVALIDATE_SECRET`
- Events: **Just the push event**

The route verifies `X-Hub-Signature-256` over the raw body, accepts only pushes to `GITHUB_BRANCH`, and refreshes `catalog.json` pinned to the push `after` SHA.

## How updates work

1. Edit [`docs/installed/catalog.toml`](../docs/installed/catalog.toml) when adding/removing mods.
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
