import { Suspense } from "react";
import { connection } from "next/server";

import { CatalogBrowser } from "@/components/CatalogBrowser";
import { LeylineParticles } from "@/components/LeylineParticles";
import { SiteHeader } from "@/components/SiteHeader";
import { loadCachedBrowserData } from "@/lib/catalog";
import { fetchReleaseChannels } from "@/lib/release";

/** Runtime ISR window; connection() prevents baking empty icons at docker build. */
export const revalidate = 600;

export default async function HomePage() {
  await connection();
  const data = await loadCachedBrowserData();
  const { catalog, source } = data.snapshot;
  const { official, prerelease } = await fetchReleaseChannels(catalog.pack.version);

  return (
    <>
      <LeylineParticles />
      <div className="relative z-10">
        <SiteHeader
          pack={catalog.pack}
          modCount={data.mods.length}
          official={official}
          prerelease={prerelease}
          source={source}
        />
        <Suspense fallback={<div className="p-8 text-muted">Loading catalog…</div>}>
          <CatalogBrowser
            mods={data.mods}
            categories={catalog.categories}
            tagVocabulary={data.tags}
          />
        </Suspense>
      </div>
    </>
  );
}
