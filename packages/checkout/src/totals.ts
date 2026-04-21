import { formatMoney } from "@modular-ecommerce/utils";

export function formatSubtotal(amount: number): string {
  return `Subtotal ${formatMoney(amount)}`;
}

export function formatGrandTotal(amount: number): string {
  return `Total ${formatMoney(amount)}`;
}
