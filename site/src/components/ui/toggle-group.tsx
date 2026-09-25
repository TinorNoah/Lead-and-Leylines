"use client";

import * as React from "react";
import * as ToggleGroupPrimitive from "@radix-ui/react-toggle-group";

import { cn } from "@/lib/utils";

export const ToggleGroup = ToggleGroupPrimitive.Root;

export function ToggleGroupItem({
  className,
  ...props
}: React.ComponentProps<typeof ToggleGroupPrimitive.Item>) {
  return (
    <ToggleGroupPrimitive.Item
      className={cn(
        "inline-flex flex-1 items-center justify-center rounded px-3 py-1.5 text-xs font-semibold text-muted transition hover:text-foreground data-[state=on]:bg-primary data-[state=on]:text-primary-foreground",
        className,
      )}
      {...props}
    />
  );
}
