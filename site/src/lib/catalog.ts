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

export async function loadBrowserData(options?: {
  force?: boolean;
  sha?: string;
}): Promise<BrowserData> {
  const snapshot = await getCatalogSnapshot(options);
  const metaMap = await getModMetadataMap(snapshot.catalog.mods);
  const mods = snapshot.catalog.mods.map((mod) => enrichMod(mod, metaMap));
  return {
    snapshot,
    mods,
    tags: snapshot.catalog.tags,
  };
}

/** Cached for page + /api/mods; webhook calls revalidateTag(CATALOG_CACHE_TAG). */
export const loadCachedBrowserData = unstable_cache(
  async () => loadBrowserData(),
  ["browser-data"],
  { revalidate: 600, tags: [CATALOG_CACHE_TAG] },
);
