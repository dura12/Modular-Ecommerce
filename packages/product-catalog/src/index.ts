import { formatMoney } from "@modular-ecommerce/utils";

export { DEMO_SKUS, catalogPathForSku } from "./demo-skus";
export type { DemoSku } from "./demo-skus";

/** Single line for listings, receipts, or admin tables. */
export function formatProductLabel(name: string, unitPrice: number): string {
  return `${name} — ${formatMoney(unitPrice)}`;
}

/** Short cart-style line using SKU + computed line total. */
export function formatLineSummary(sku: string, quantity: number, lineTotal: number): string {
  return `${sku} ×${quantity} → ${formatMoney(lineTotal)}`;
}
