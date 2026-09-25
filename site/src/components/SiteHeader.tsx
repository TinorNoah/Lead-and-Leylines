import type { CommitInfo, PackInfo } from "@/lib/types";

type Props = {
  pack: PackInfo;
  modCount: number;
  commit: CommitInfo | null;
  source: string;
};

export function SiteHeader({ pack, modCount, commit, source }: Props) {
  return (
    <header className="border-b border-card-border/80 bg-background/70 backdrop-blur">
      <div className="mx-auto flex w-full max-w-7xl flex-col gap-3 px-4 py-6 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <div className="text-xs uppercase tracking-[0.35em] text-accent">Lead and Leylines</div>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-foreground">
            Installed mods
          </h1>
          <p className="mt-2 max-w-2xl text-sm text-muted">
            {pack.name} {pack.version} · Minecraft {pack.minecraft} · {pack.loader}{" "}
            {pack.loader_version} · {modCount} entries
          </p>
        </div>
        <div className="rounded-2xl border border-card-border bg-card/70 px-4 py-3 text-sm text-muted">
          <div>
            Source: <span className="text-foreground">{source}</span>
          </div>
          {commit ? (
            <a href={commit.url} target="_blank" rel="noreferrer" className="mt-1 block text-accent">
              {commit.sha.slice(0, 7)} · {commit.message}
            </a>
          ) : (
            <div className="mt-1">Waiting for GitHub sync</div>
          )}
        </div>
      </div>
    </header>
  );
}
