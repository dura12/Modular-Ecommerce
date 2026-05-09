import { formatMoney } from "@modular-ecommerce/utils";

export function formatSubtotal(amount: number): string {
  return `Subtotal ${formatMoney(amount)}`;
}

export function formatGrandTotal(amount: number): string {
  return `Total ${formatMoney(amount)}`;
}

/** Display amount as a negative currency (for a discount row). */
export function formatNegativeMoney(amount: number): string {
  if (amount <= 0) {
    return formatMoney(0);
  }
  return `-${formatMoney(amount)}`;
}
