import type { EnrichedMod } from "@/lib/types";

type Props = {
  title: string;
  mods: EnrichedMod[];
};

export function ModTable({ title, mods }: Props) {
  return (
    <div className="overflow-hidden rounded-2xl border border-card-border bg-card/80">
      <div className="border-b border-card-border px-4 py-3 text-sm font-medium text-accent">
        {title}
      </div>
      <div className="overflow-x-auto">
        <table className="min-w-full text-left text-sm">
          <thead className="bg-background/40 text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-4 py-2 font-medium">Mod</th>
              <th className="px-4 py-2 font-medium">Side</th>
              <th className="px-4 py-2 font-medium">Tags</th>
              <th className="px-4 py-2 font-medium">What it adds</th>
            </tr>
          </thead>
          <tbody>
            {mods.map((mod) => (
              <tr key={mod.file} className="border-t border-card-border/80 align-top">
                <td className="px-4 py-3">
                  <div className="font-medium text-foreground">{mod.name}</div>
                  <div className="mt-1 font-mono text-[11px] text-muted">{mod.filename}</div>
                </td>
                <td className="px-4 py-3 text-muted">{mod.side}</td>
                <td className="px-4 py-3">
                  <div className="flex flex-wrap gap-1">
                    {mod.manual_tags.map((tag) => (
                      <span
                        key={tag}
                        className="rounded-full bg-chip px-2 py-0.5 text-[11px] text-accent"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>
                </td>
                <td className="px-4 py-3 text-muted">{mod.blurb}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
