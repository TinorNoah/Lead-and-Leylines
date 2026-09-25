import { monogram, sideLabel } from "@/lib/format";
import type { EnrichedMod } from "@/lib/types";

type Props = {
  mod: EnrichedMod;
};

export function ModCard({ mod }: Props) {
  return (
    <article className="flex h-full flex-col gap-3 rounded-2xl border border-card-border bg-card/90 p-4 shadow-[0_0_0_1px_rgba(110,231,197,0.03)]">
      <div className="flex items-start gap-3">
        {mod.iconUrl ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src={mod.iconUrl}
            alt=""
            className="h-12 w-12 rounded-xl border border-card-border object-cover"
          />
        ) : (
          <div className="flex h-12 w-12 items-center justify-center rounded-xl border border-card-border bg-accent-soft text-sm font-semibold text-accent">
            {monogram(mod.name)}
          </div>
        )}
        <div className="min-w-0 flex-1">
          <h3 className="truncate text-sm font-semibold text-foreground">{mod.name}</h3>
          <div className="mt-1 flex flex-wrap gap-1.5 text-[11px] text-muted">
            <span className="rounded-full bg-chip px-2 py-0.5">{sideLabel(mod.side)}</span>
            <span className="rounded-full bg-chip px-2 py-0.5">{mod.category_title}</span>
            <span className="rounded-full bg-chip px-2 py-0.5">{mod.source}</span>
          </div>
        </div>
      </div>
      <p className="line-clamp-3 text-sm text-muted">{mod.blurb}</p>
      <div className="mt-auto flex flex-wrap gap-1.5">
        {mod.manual_tags.slice(0, 6).map((tag) => (
          <span
            key={tag}
            className="rounded-full border border-card-border px-2 py-0.5 text-[11px] text-accent"
          >
            {tag}
          </span>
        ))}
      </div>
      <div className="flex items-center justify-between gap-2 text-xs text-muted">
        <code className="truncate rounded bg-background/60 px-1.5 py-0.5">{mod.filename}</code>
        {mod.storeUrl && (
          <a
            href={mod.storeUrl}
            target="_blank"
            rel="noreferrer"
            className="shrink-0 text-accent hover:underline"
          >
            Store
          </a>
        )}
      </div>
    </article>
  );
}
