function readEnv(name: string, fallback = ""): string {
  return (process.env[name] ?? fallback).trim();
}

export function siteConfig() {
  const ttl = Number(readEnv("CACHE_TTL_SECONDS", "600"));
  return {
    githubRepo: readEnv("GITHUB_REPO", "TinorNoah/Lead-and-Leylines"),
    githubBranch: readEnv("GITHUB_BRANCH", "main"),
    githubToken: readEnv("GITHUB_TOKEN"),
    curseforgeApiKey: readEnv("CURSEFORGE_API_KEY"),
    revalidateSecret: readEnv("REVALIDATE_SECRET"),
    cacheTtlSeconds: Number.isFinite(ttl) && ttl > 0 ? ttl : 600,
    dataDir: readEnv("DATA_DIR", "/data"),
    seedPath: readEnv("SEED_CATALOG_PATH", "/app/seed/catalog.json"),
  };
}
