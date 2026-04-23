# Modular E-Commerce (monorepo)

This repository is a **monorepo**: **npm workspaces** for TypeScript libraries and a **Python** package at the repo root for the CBSE component-based e-commerce core (catalog, cart, payment stubs, order stubs).

## Directory layout

```text
.
├── package.json              # Root workspace + scripts
├── tsconfig.base.json        # Shared TypeScript defaults
├── packages/
│   ├── utils/                # @modular-ecommerce/utils — shared helpers
│   ├── ui-components/        # @modular-ecommerce/ui-components — reusable React UI
│   ├── product-catalog/      # @modular-ecommerce/product-catalog — catalog labels & demo SKUs
│   └── checkout/             # @modular-ecommerce/checkout — totals, quantity rules, pay UI
└── src/                      # Python CBSE modules (`python -m src.main`)
```

| Package | Role |
|--------|------|
| **utils** | Cross-cutting helpers (`clamp`, `formatMoney`). |
| **ui-components** | Reusable **React** primitives (e.g. `Button`). Hand-authored for zero Tailwind setup; you can add **ShadCN** later with `npx shadcn@latest init` inside this package. |
| **product-catalog** | **Catalog domain (TS)** — `formatProductLabel`, `formatLineSummary`, `DEMO_SKUS` aligned with the Python demo in `src/main.py`; **depends on `utils`**. |
| **checkout** | **Checkout domain (TS)** — `formatSubtotal` / `formatGrandTotal`, `boundedQuantity`, `PayButton`; **depends on `utils` + `ui-components`**. |

## Prerequisites

- **Node.js** 18+ and **npm** 6+ (internal packages use `file:../…` links so older npm works; upgrade to npm 7+ if you prefer `workspace:*`).
- **Python** 3.10+ for `src/`.

## Setup

From the repository root:

```bash
npm install
```

That creates or updates `package-lock.json` (not always committed on every machine; commit it when installs succeed for reproducible builds).

Optional: create a virtual environment (`python -m venv .venv` then activate). The current `src/` demo uses the **standard library only** (no `pip install` required).

## Build (TypeScript packages)

```bash
npm run build
```

This runs `npm run build --workspaces --if-present`, compiling each package’s `src/` to `packages/<name>/dist/`.

Build a single workspace:

```bash
npm run build -w @modular-ecommerce/product-catalog
```

## Run (Python demo)

```bash
npm run python:demo
```

Or directly:

```bash
python -m src.main
```

Run from the **repo root** so imports like `src.components...` resolve.

The Python demo also exercises **`IPaymentGateway`** with **`StripePaymentAdapter`** and **`PayPalPaymentAdapter`** (fake `stripe_api` / `paypal_api` modules).

## Tooling note

The coursework asks for **Yarn / npm / Nx** workspaces — this repo uses **npm workspaces**. **Nx** can be added later for task caching and affected-graph builds without removing the current layout.

## Clean streak / docs

Log each meaningful **git commit hash** in your Progress tab when you change `packages/*` or `src/`.
