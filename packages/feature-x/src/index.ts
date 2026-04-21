import { formatMoney } from "@modular-ecommerce/utils";

/** System 1: present catalog rows (IDs align with Python `src/` catalog SKUs in demos). */
export function formatProductLabel(name: string, unitPrice: number): string {
  return `${name} — ${formatMoney(unitPrice)}`;
}
