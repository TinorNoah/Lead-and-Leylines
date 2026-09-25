import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  poweredByHeader: false,
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "media.forgecdn.net" },
      { protocol: "https", hostname: "cdn.modrinth.com" },
    ],
  },
};

export default nextConfig;
