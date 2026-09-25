"use client";

import { useEffect, useRef } from "react";

type Particle = {
  x: number;
  y: number;
  vx: number;
  vy: number;
  r: number;
  alpha: number;
  color: string;
};

const COLORS = ["#dfb16c", "#e9c381", "#84d8a7", "#489b6f"];

function createParticle(width: number, height: number): Particle {
  return {
    x: Math.random() * width,
    y: Math.random() * height,
    vx: (Math.random() - 0.5) * 0.18,
    vy: -0.05 - Math.random() * 0.2,
    r: 0.6 + Math.random() * 1.8,
    alpha: 0.12 + Math.random() * 0.28,
    color: COLORS[Math.floor(Math.random() * COLORS.length)]!,
  };
}

export function LeylineParticles() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let frame = 0;
    let particles: Particle[] = [];
    let running = true;
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const width = window.innerWidth;
      const height = window.innerHeight;
      canvas!.width = Math.floor(width * dpr);
      canvas!.height = Math.floor(height * dpr);
      canvas!.style.width = `${width}px`;
      canvas!.style.height = `${height}px`;
      ctx!.setTransform(dpr, 0, 0, dpr, 0, 0);
      const count = reducedMotion ? 18 : Math.min(70, Math.floor((width * height) / 28000));
      particles = Array.from({ length: count }, () => createParticle(width, height));
    }

    function tick() {
      if (!running || !ctx || !canvas) return;
      const width = window.innerWidth;
      const height = window.innerHeight;
      ctx.clearRect(0, 0, width, height);

      for (const particle of particles) {
        if (!reducedMotion) {
          particle.x += particle.vx;
          particle.y += particle.vy;
          if (particle.y < -8) {
            particle.y = height + 8;
            particle.x = Math.random() * width;
          }
          if (particle.x < -8) particle.x = width + 8;
          if (particle.x > width + 8) particle.x = -8;
        }

        ctx.beginPath();
        ctx.fillStyle = particle.color;
        ctx.globalAlpha = particle.alpha;
        ctx.arc(particle.x, particle.y, particle.r, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.globalAlpha = 1;

      if (!reducedMotion) {
        // Soft leyline threads between nearby particles
        for (let i = 0; i < particles.length; i += 1) {
          const a = particles[i]!;
          for (let j = i + 1; j < particles.length; j += 1) {
            const b = particles[j]!;
            const dx = a.x - b.x;
            const dy = a.y - b.y;
            const dist = Math.hypot(dx, dy);
            if (dist > 110) continue;
            ctx.beginPath();
            ctx.strokeStyle = a.color;
            ctx.globalAlpha = (1 - dist / 110) * 0.08;
            ctx.lineWidth = 0.7;
            ctx.moveTo(a.x, a.y);
            ctx.lineTo(b.x, b.y);
            ctx.stroke();
          }
        }
        ctx.globalAlpha = 1;
        frame = window.requestAnimationFrame(tick);
      }
    }

    resize();
    tick();
    window.addEventListener("resize", resize);

    return () => {
      running = false;
      window.cancelAnimationFrame(frame);
      window.removeEventListener("resize", resize);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      aria-hidden
      className="pointer-events-none fixed inset-0 z-0"
    />
  );
}
