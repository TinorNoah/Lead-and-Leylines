import { Suspense } from "react";

import { CatalogBrowser } from "@/components/CatalogBrowser";
import { LeylineParticles } from "@/components/LeylineParticles";
import { SiteHeader } from "@/components/SiteHeader";
import { loadBrowserData } from "@/lib/catalog";
import { fetchLatestRelease } from "@/lib/release";

export const dynamic = "force-dynamic";

export default async function HomePage() {
  const data = await loadBrowserData();
  const { catalog, source } = data.snapshot;
  const release = await fetchLatestRelease(catalog.pack.version);

  return (
    <>
      <LeylineParticles />
      <div className="relative z-10">
        <SiteHeader
          pack={catalog.pack}
          modCount={data.mods.length}
          release={release}
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
