import type { ButtonHTMLAttributes } from "react";

export type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement>;

/** Primary action button (hand-authored; swap for ShadCN Button when you add Tailwind). */
export function Button({ children, style, ...rest }: ButtonProps) {
  return (
    <button
      type="button"
      style={{
        padding: "0.5rem 0.75rem",
        borderRadius: 8,
        border: "1px solid #ccc",
        background: "#111",
        color: "#fff",
        cursor: "pointer",
        ...style,
      }}
      {...rest}
    >
      {children}
    </button>
  );
}
