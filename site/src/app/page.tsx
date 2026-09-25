import { Suspense } from "react";

import { CatalogBrowser } from "@/components/CatalogBrowser";
import { SiteHeader } from "@/components/SiteHeader";
import { loadBrowserData } from "@/lib/catalog";

export const dynamic = "force-dynamic";

export default async function HomePage() {
  const data = await loadBrowserData();
  const { catalog, commit, source } = data.snapshot;

  return (
    <>
      <SiteHeader
        pack={catalog.pack}
        modCount={data.mods.length}
        commit={commit}
        source={source}
      />
      <Suspense fallback={<div className="p-8 text-muted">Loading catalog…</div>}>
        <CatalogBrowser
          mods={data.mods}
          categories={catalog.categories}
          tagVocabulary={data.tags}
        />
      </Suspense>
    </>
  );
}
