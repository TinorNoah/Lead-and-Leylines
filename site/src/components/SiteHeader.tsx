import Image from "next/image";
import { Tag } from "lucide-react";

import type { PackInfo, ReleaseInfo } from "@/lib/types";
import { Badge } from "@/components/ui/badge";

type Props = {
  pack: PackInfo;
  modCount: number;
  release: ReleaseInfo | null;
  source: string;
};

export function SiteHeader({ pack, modCount, release, source }: Props) {
  return (
    <header className="relative z-10 border-b border-card-border/80 bg-background/80 backdrop-blur">
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
          {release ? (
            <a
              href={release.url}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 rounded border border-card-border bg-card px-3 py-1.5 font-mono text-xs text-primary hover:border-primary/50 hover:shadow-[var(--ley-glow)]"
            >
              <Tag className="h-3.5 w-3.5 shrink-0" />
              <span>v{release.version}</span>
              <span className="text-muted">·</span>
              <span className="max-w-[14rem] truncate text-muted-foreground hover:text-primary">
                Latest release
              </span>
            </a>
          ) : (
            <Badge variant="muted">Release unavailable</Badge>
          )}
        </div>
      </div>
    </header>
  );
}
