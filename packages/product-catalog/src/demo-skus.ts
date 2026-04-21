/**
 * Demo SKUs kept in sync with the Python catalog in `src/main.py`
 * (Ceramic Mug + Clean Code PDF).
 */
export const DEMO_SKUS = {
  MUG: "SKU-MUG",
  EBOOK: "SKU-EBOOK",
} as const;

export type DemoSku = (typeof DEMO_SKUS)[keyof typeof DEMO_SKUS];

export function catalogPathForSku(sku: string): string {
  return `/catalog/${encodeURIComponent(sku)}`;
}
