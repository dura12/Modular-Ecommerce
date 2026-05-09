import { formatMoney } from "@modular-ecommerce/utils";

import { formatGrandTotal, formatNegativeMoney, formatSubtotal } from "./totals";

export type CheckoutLine = { label: string; amount: number };

export type CheckoutSummaryProps = {
  lines: CheckoutLine[];
  headline?: string;
  /** Optional cart-level discount in the same units as line amounts. */
  discount?: number;
};

/** Receipt-style panel for storefront apps (pure presentation; totals match line sum). */
export function CheckoutSummary(props: CheckoutSummaryProps) {
  const sum = props.lines.reduce((acc, line) => acc + line.amount, 0);
  const discount = Math.max(0, props.discount ?? 0);
  const total = Math.max(0, sum - discount);

  return (
    <section
      style={{
        border: "1px solid #ddd",
        borderRadius: 8,
        padding: 16,
        maxWidth: 380,
        fontFamily: "system-ui, sans-serif",
      }}
    >
      <h3 style={{ marginTop: 0 }}>{props.headline ?? "Order summary"}</h3>
      <ul style={{ listStyle: "none", padding: 0, margin: "8px 0 12px" }}>
        {props.lines.map((line, idx) => (
          <li
            key={idx}
            style={{
              display: "flex",
              justifyContent: "space-between",
              gap: 12,
              marginBottom: 6,
            }}
          >
            <span>{line.label}</span>
            <span>{formatMoney(line.amount)}</span>
          </li>
        ))}
      </ul>
      {discount > 0 ? (
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            gap: 12,
            marginBottom: 8,
            color: "#2e7d32",
          }}
        >
          <span>Discount</span>
          <span>{formatNegativeMoney(discount)}</span>
        </div>
      ) : null}
      <hr style={{ border: 0, borderTop: "1px solid #eee" }} />
      <p style={{ margin: "10px 0 4px", fontWeight: 600 }}>{formatSubtotal(sum)}</p>
      <p style={{ margin: "4px 0 0", fontWeight: 700 }}>{formatGrandTotal(total)}</p>
    </section>
  );
}
