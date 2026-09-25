import { monogram, sideLabel } from "@/lib/format";
import type { EnrichedMod } from "@/lib/types";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";

type Props = {
  mod: EnrichedMod;
  selected?: boolean;
  onOpen: (mod: EnrichedMod) => void;
};

export function ModCard({ mod, selected, onOpen }: Props) {
  return (
    <button
      type="button"
      onClick={() => onOpen(mod)}
      className={cn(
        "flex h-full w-full flex-col gap-3 rounded border border-card-border bg-card p-4 text-left transition hover:border-card-border-active hover:bg-card-elevated",
        selected &&
          "border-primary/60 bg-gradient-to-r from-[rgba(223,177,108,0.08)] to-transparent shadow-[var(--ley-glow)]",
      )}
    >
      <div className="flex items-start gap-3">
        {mod.iconUrl ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src={mod.iconUrl}
            alt=""
            className="h-11 w-11 rounded border border-card-border object-cover"
          />
        ) : (
          <div className="flex h-11 w-11 items-center justify-center rounded border border-card-border bg-accent-soft font-display text-sm font-semibold text-primary">
            {monogram(mod.name)}
          </div>
        )}
        <div className="min-w-0 flex-1">
          <h3 className="truncate font-display text-base font-semibold text-primary-bright">
            {mod.name}
          </h3>
          <div className="mt-1.5 flex flex-wrap gap-1.5">
            <Badge variant={mod.side === "both" ? "moss" : "muted"}>{sideLabel(mod.side)}</Badge>
            <Badge variant="outline">{mod.category_title}</Badge>
          </div>
        </div>
      </div>
      <p className="line-clamp-2 text-sm text-muted">{mod.blurb || mod.summary || "—"}</p>
      <div className="mt-auto flex flex-wrap gap-1.5">
        {mod.manual_tags.slice(0, 3).map((tag) => (
          <span key={tag} className="font-mono text-[11px] text-secondary">
            #{tag}
          </span>
        ))}
      </div>
    </button>
  );
}
