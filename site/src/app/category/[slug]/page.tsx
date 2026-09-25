import Link from "next/link";
import { notFound } from "next/navigation";

import { ModTable } from "@/components/ModTable";
import { SiteHeader } from "@/components/SiteHeader";
import { loadBrowserData } from "@/lib/catalog";

export const dynamic = "force-dynamic";

type Props = {
  params: Promise<{ slug: string }>;
};

export default async function CategoryPage({ params }: Props) {
  const { slug } = await params;
  const data = await loadBrowserData();
  const category = data.snapshot.catalog.categories.find((item) => item.slug === slug);
  if (!category) {
    notFound();
  }

  const mods = data.mods.filter((mod) => mod.category === slug);
  const groups = category.groups.map((group) => ({
    name: group.name,
    mods: mods.filter((mod) => mod.group === group.name),
  }));

  return (
    <>
      <SiteHeader
        pack={data.snapshot.catalog.pack}
        modCount={data.mods.length}
        commit={data.snapshot.commit}
        source={data.snapshot.source}
      />
      <main className="mx-auto w-full max-w-7xl space-y-6 px-4 py-8">
        <div className="space-y-2">
          <Link href="/" className="text-sm text-accent hover:underline">
            ← All mods
          </Link>
          <h2 className="text-3xl font-semibold">{category.title}</h2>
          <p className="max-w-3xl text-muted">{category.intro}</p>
        </div>
        {groups.map((group) =>
          group.mods.length > 0 ? (
            <ModTable key={group.name} title={group.name} mods={group.mods} />
          ) : null,
        )}
      </main>
    </>
  );
}
