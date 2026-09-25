export type PackInfo = {
  name: string;
  version: string;
  minecraft: string;
  loader: string;
  loader_version: string;
};

export type CatalogMod = {
  file: string;
  name: string;
  filename: string;
  side: string;
  folder: string;
  kind: string;
  source: string;
  project_id: string | number | null;
  blurb: string;
  tags: string[];
  manual_tags: string[];
  category: string;
  category_title: string;
  group: string;
};

export type CatalogGroup = {
  name: string;
  mods: Array<{
    file: string;
    blurb: string;
    tags: string[];
    name: string;
    filename: string;
    side: string;
    source: string;
    project_id: string | number | null;
    kind: string;
  }>;
};

export type CatalogCategory = {
  slug: string;
  title: string;
  intro: string;
  groups: CatalogGroup[];
};

export type CatalogPayload = {
  pack: PackInfo;
  tags: Record<string, string>;
  categories: CatalogCategory[];
  mods: CatalogMod[];
  mod_count: number;
};

export type CommitInfo = {
  sha: string;
  message: string;
  date: string;
  url: string;
};

export type ReleaseInfo = {
  tag: string;
  version: string;
  name: string;
  url: string;
};

export type ModMetadata = {
  iconUrl: string | null;
  summary: string | null;
  url: string | null;
};

export type EnrichedMod = CatalogMod & {
  iconUrl: string | null;
  summary: string | null;
  storeUrl: string | null;
};

export type CatalogSnapshot = {
  catalog: CatalogPayload;
  commit: CommitInfo | null;
  source: "github" | "data" | "seed";
  fetchedAt: string;
};
