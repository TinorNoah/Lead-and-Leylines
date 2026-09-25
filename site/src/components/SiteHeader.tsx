import Image from "next/image";

import type { CommitInfo, PackInfo } from "@/lib/types";
import { Badge } from "@/components/ui/badge";

type Props = {
  pack: PackInfo;
  modCount: number;
  commit: CommitInfo | null;
  source: string;
};

export function SiteHeader({ pack, modCount, commit, source }: Props) {
  return (
    <header className="border-b border-card-border/80 bg-background/80 backdrop-blur">
      <div className="mx-auto flex w-full max-w-[1560px] flex-col gap-4 px-4 py-5 sm:flex-row sm:items-center sm:justify-between sm:px-6 lg:px-8">
        <div className="flex items-start gap-3 sm:items-center">
          <Image
            src="/emblem.svg"
            alt=""
            width={48}
            height={48}
            className="mt-0.5 shrink-0"
            priority
          />
          <div>
            <div className="font-display text-2xl font-bold tracking-tight text-primary sm:text-3xl">
              Lead &amp; Leylines
            </div>
            <div className="mt-0.5 text-sm text-muted">Installed mods</div>
            <p className="mt-2 font-mono text-xs text-muted-foreground">
              {pack.name} {pack.version} · Minecraft {pack.minecraft} · {pack.loader}{" "}
              {pack.loader_version} · {modCount} mods
            </p>
          </div>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          <Badge variant="moss">{source}</Badge>
          {commit ? (
            <a
              href={commit.url}
              target="_blank"
              rel="noreferrer"
              className="rounded border border-card-border bg-card px-3 py-1.5 font-mono text-xs text-primary hover:border-card-border-active"
            >
              {commit.sha.slice(0, 7)} · {commit.message.slice(0, 48)}
              {commit.message.length > 48 ? "…" : ""}
            </a>
          ) : (
            <Badge variant="muted">Waiting for GitHub sync</Badge>
          )}
        </div>
      </div>
      <div className="ley-rule w-full" />
    </header>
  );
}
