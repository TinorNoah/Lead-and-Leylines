#!/usr/bin/env bash
# Dedicated NeoForge start. Java 21 ZGC from pack/user_jvm_args.txt.
# Do not add -XX:+ZGenerational.
set -euo pipefail
cd "$(dirname "$0")"

# Panel SERVER_MEMORY is the container limit. Xmx must leave room for ZGC,
# metaspace, and native buffers or Linux OOM-kills the process (exit 137).
memory="${SERVER_MEMORY:-8192}"
if (( memory > 2048 )); then
  heap=$((memory - 1536))
else
  heap=$((memory * 3 / 4))
fi
jvm_args="user_jvm_args.txt"
unix_args="unix_args.txt"

if [[ ! -f "$jvm_args" ]]; then
  echo "missing $jvm_args (overlay copies pack/user_jvm_args.txt)" >&2
  exit 1
fi

if [[ ! -f "$unix_args" ]]; then
  shopt -s nullglob
  matches=(libraries/net/neoforged/neoforge/*/unix_args.txt)
  shopt -u nullglob
  if [[ ${#matches[@]} -eq 0 ]]; then
    echo "missing unix_args.txt; NeoForge is not installed yet" >&2
    exit 1
  fi
  unix_args="${matches[0]}"
fi

echo "heap ${heap}M (container ${memory}M, ZGC headroom reserved)"
exec java -Xms128M -Xmx"${heap}M" @"$jvm_args" @"$unix_args" nogui
