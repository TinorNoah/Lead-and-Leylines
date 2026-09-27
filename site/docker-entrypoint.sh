#!/bin/sh
set -e
# Swarm volume /data often arrives as root/ubuntu-owned; the app runs as uid 1001.
if [ -d /data ]; then
  chown -R nextjs:nodejs /data 2>/dev/null || true
fi
exec runuser -u nextjs -- "$@"
