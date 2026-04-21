import { Button } from "@modular-ecommerce/ui-components";
import { clamp } from "@modular-ecommerce/utils";

/** System 2: bounded quantity + pay affordance for checkout demos. */
export function boundedQuantity(requested: number, max: number): number {
  return clamp(requested, 1, Math.max(1, max));
}

export function PayButton(props: { label: string; onClick?: () => void }) {
  return <Button onClick={props.onClick}>{props.label}</Button>;
}
