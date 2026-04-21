import { Button } from "@modular-ecommerce/ui-components";
import { clamp } from "@modular-ecommerce/utils";

export { formatGrandTotal, formatSubtotal } from "./totals";

/** Clamp requested quantity to [1, max] for cart / checkout inputs. */
export function boundedQuantity(requested: number, max: number): number {
  return clamp(requested, 1, Math.max(1, max));
}

export function PayButton(props: { label: string; onClick?: () => void }) {
  return <Button onClick={props.onClick}>{props.label}</Button>;
}
