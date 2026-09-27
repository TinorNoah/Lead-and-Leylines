import { unstable_cache } from "next/cache";

import { enrichMod, getModMetadataMap } from "./metadata";
import { getCatalogSnapshot } from "./source";
import type { CatalogSnapshot, EnrichedMod } from "./types";

export type BrowserData = {
  snapshot: CatalogSnapshot;
  mods: EnrichedMod[];
  tags: Record<string, string>;
};

export const CATALOG_CACHE_TAG = "catalog";

async function loadCatalogSnapshotCached(): Promise<CatalogSnapshot> {
  return getCatalogSnapshot();
}

/** Catalog JSON only — never bake CurseForge icons into this (build has no API key /data). */
const getCachedCatalogSnapshot = unstable_cache(
  loadCatalogSnapshotCached,
  ["catalog-snapshot"],
  { revalidate: 600, tags: [CATALOG_CACHE_TAG] },
);

export async function loadBrowserData(options?: {
  force?: boolean;
  sha?: string;
}): Promise<BrowserData> {
  const snapshot = options?.force || options?.sha
    ? await getCatalogSnapshot(options)
    : await getCachedCatalogSnapshot();
  // Meta comes from /data/meta-cache.json at runtime (volume), not from Next ISR.
  const metaMap = await getModMetadataMap(snapshot.catalog.mods);
  const mods = snapshot.catalog.mods.map((mod) => enrichMod(mod, metaMap));
  return {
    snapshot,
    mods,
    tags: snapshot.catalog.tags,
  };
}

/** Page + /api/mods entry: cached catalog, live meta enrichment. */
export async function loadCachedBrowserData(): Promise<BrowserData> {
  return loadBrowserData();
}
