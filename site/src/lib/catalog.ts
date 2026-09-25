import { enrichMod, getModMetadataMap } from "./metadata";
import { getCatalogSnapshot } from "./source";
import type { CatalogSnapshot, EnrichedMod } from "./types";

export type BrowserData = {
  snapshot: CatalogSnapshot;
  mods: EnrichedMod[];
  tags: Record<string, string>;
};

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
