import type { EnrichedMod } from "@/lib/types";
import { ModCard } from "@/components/ModCard";

type Props = {
  title: string;
  intro?: string;
  mods: EnrichedMod[];
  selectedFile?: string;
  onOpen: (mod: EnrichedMod) => void;
};

export function ModTable({ title, intro, mods, selectedFile, onOpen }: Props) {
  return (
    <section className="space-y-3">
      <div>
        <h2 className="font-display text-xl font-semibold text-primary">{title}</h2>
        {intro ? <p className="mt-1 text-sm text-muted">{intro}</p> : null}
      </div>
      <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
        {mods.map((mod) => (
          <ModCard
            key={mod.file}
            mod={mod}
            selected={selectedFile === mod.file}
            onOpen={onOpen}
          />
        ))}
      </div>
    </section>
  );
}
