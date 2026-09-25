import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const badgeVariants = cva(
  "inline-flex items-center rounded px-2 py-0.5 font-mono text-[11px] tracking-wide",
  {
    variants: {
      variant: {
        default: "border border-card-border bg-chip text-primary",
        moss: "border border-secondary-dim/50 bg-moss-soft text-secondary",
        muted: "border border-card-border bg-chip text-muted",
        outline: "border border-card-border text-muted-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  },
);

export type BadgeProps = React.ComponentProps<"span"> & VariantProps<typeof badgeVariants>;

export function Badge({ className, variant, ...props }: BadgeProps) {
  return <span className={cn(badgeVariants({ variant }), className)} {...props} />;
}
