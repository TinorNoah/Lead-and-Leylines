import { monogram, sideLabel } from "@/lib/format";
import type { EnrichedMod } from "@/lib/types";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";

type Props = {
  mods: EnrichedMod[];
  selectedFile?: string;
  onOpen: (mod: EnrichedMod) => void;
};

export function ModList({ mods, selectedFile, onOpen }: Props) {
  return (
    <div className="overflow-hidden rounded border border-card-border bg-card">
      <div className="overflow-x-auto">
        <table className="min-w-full text-left text-sm">
          <thead className="border-b border-card-border bg-[#141d1b] font-mono text-[11px] uppercase tracking-wider text-muted">
            <tr>
              <th className="px-4 py-3 font-medium">Mod</th>
              <th className="px-4 py-3 font-medium">Category</th>
              <th className="px-4 py-3 font-medium">Side</th>
              <th className="px-4 py-3 font-medium">Summary</th>
              <th className="px-4 py-3 font-medium">Tags</th>
            </tr>
          </thead>
          <tbody>
            {mods.map((mod) => (
              <tr
                key={mod.file}
                className={cn(
                  "cursor-pointer border-t border-card-border/70 align-top transition hover:bg-card-elevated",
                  selectedFile === mod.file && "bg-accent-soft",
                )}
                onClick={() => onOpen(mod)}
              >
                <td className="px-4 py-3">
                  <div className="flex items-center gap-2">
                    {mod.iconUrl ? (
                      // eslint-disable-next-line @next/next/no-img-element
                      <img src={mod.iconUrl} alt="" className="h-8 w-8 rounded border border-card-border object-cover" />
                    ) : (
                      <div className="flex h-8 w-8 items-center justify-center rounded border border-card-border bg-chip text-[10px] font-semibold text-primary">
                        {monogram(mod.name)}
                      </div>
                    )}
                    <div className="min-w-0">
                      <div className="truncate font-medium text-foreground">{mod.name}</div>
                    </div>
                  </div>
                </td>
                <td className="px-4 py-3 text-muted">{mod.category_title}</td>
                <td className="px-4 py-3">
                  <Badge variant={mod.side === "both" ? "moss" : "muted"}>{sideLabel(mod.side)}</Badge>
                </td>
                <td className="max-w-xs px-4 py-3 text-muted">
                  <span className="line-clamp-2">{mod.blurb || mod.summary || "—"}</span>
                </td>
                <td className="px-4 py-3">
                  <div className="flex flex-wrap gap-1">
                    {mod.manual_tags.slice(0, 4).map((tag) => (
                      <span key={tag} className="font-mono text-[11px] text-secondary">
                        #{tag}
                      </span>
                    ))}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
