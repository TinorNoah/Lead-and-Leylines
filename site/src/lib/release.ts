import { siteConfig } from "./env";
import type { ReleaseInfo } from "./types";

const FETCH_TIMEOUT_MS = 8_000;

function authHeaders(): HeadersInit {
  const { githubToken } = siteConfig();
  const headers: Record<string, string> = {
    Accept: "application/vnd.github+json",
    "User-Agent": "lead-and-leylines-mod-browser",
  };
  if (githubToken) {
    headers.Authorization = `Bearer ${githubToken}`;
  }
  return headers;
}

function versionFromTag(tag: string): string {
  return tag.replace(/^v/i, "");
}

export function releaseFromPackVersion(version: string): ReleaseInfo {
  const { githubRepo } = siteConfig();
  const tag = `v${version}`;
  return {
    tag,
    version,
    name: `Lead and Leylines ${version}`,
    url: `https://github.com/${githubRepo}/releases/tag/${tag}`,
  };
}

export async function fetchLatestRelease(
  fallbackVersion?: string,
): Promise<ReleaseInfo | null> {
  const { githubRepo } = siteConfig();
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
  try {
    const response = await fetch(
      `https://api.github.com/repos/${githubRepo}/releases/latest`,
      {
        headers: authHeaders(),
        signal: controller.signal,
        cache: "no-store",
      },
    );
    if (!response.ok) {
      console.warn("github latest release", response.status);
      return fallbackVersion ? releaseFromPackVersion(fallbackVersion) : null;
    }
    const body = (await response.json()) as {
      tag_name?: string;
      name?: string;
      html_url?: string;
    };
    const tag = body.tag_name?.trim();
    if (!tag || !body.html_url) {
      return fallbackVersion ? releaseFromPackVersion(fallbackVersion) : null;
    }
    return {
      tag,
      version: versionFromTag(tag),
      name: body.name?.trim() || `Lead and Leylines ${versionFromTag(tag)}`,
      url: body.html_url,
    };
  } catch (error) {
    console.warn("github latest release failed", error);
    return fallbackVersion ? releaseFromPackVersion(fallbackVersion) : null;
  } finally {
    clearTimeout(timer);
  }
}
