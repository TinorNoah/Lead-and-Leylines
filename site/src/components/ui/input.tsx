import * as React from "react";

import { cn } from "@/lib/utils";

export function Input({ className, type, ...props }: React.ComponentProps<"input">) {
  return (
    <input
      type={type}
      className={cn(
        "flex h-10 w-full rounded border border-card-border bg-[#111a18] px-3 py-2 text-sm text-foreground placeholder:text-card-border-active outline-none transition focus:border-primary focus:shadow-[inset_0_0_6px_rgba(223,177,108,0.15)]",
        className,
      )}
      {...props}
    />
  );
}
