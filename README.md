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
│   ├── feature-x/            # @modular-ecommerce/feature-x — system 1 (catalog-style)
│   └── feature-y/            # @modular-ecommerce/feature-y — system 2 (checkout-style)
└── src/                      # Python CBSE modules (`python -m src.main`)
```

| Package | Role |
|--------|------|
| **utils** | Cross-cutting helpers (`clamp`, `formatMoney`). |
| **ui-components** | Reusable **React** primitives (e.g. `Button`). Hand-authored for zero Tailwind setup; you can add **ShadCN** later with `npx shadcn@latest init` inside this package. |
| **feature-x** | **System 1** — example feature that **depends on `utils`** (catalog row formatting). |
| **feature-y** | **System 2** — example feature that **depends on `utils` + `ui-components`** (quantity clamp + pay button). |

## Prerequisites

- **Node.js** 18+ and **npm** 9+ (workspaces `workspace:*` protocol).
- **Python** 3.10+ for `src/`.

## Setup

From the repository root:

```bash
npm install
```

Optional: create a virtual environment (`python -m venv .venv` then activate). The current `src/` demo uses the **standard library only** (no `pip install` required).

## Build (TypeScript packages)

```bash
npm run build
```

This runs `npm run build --workspaces --if-present`, compiling each package’s `src/` to `packages/<name>/dist/`.

Build a single workspace:

```bash
npm run build -w @modular-ecommerce/utils
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

## Tooling note

The coursework asks for **Yarn / npm / Nx** workspaces — this repo uses **npm workspaces**. **Nx** can be added later for task caching and affected-graph builds without removing the current layout.

## Clean streak / docs

Log each meaningful **git commit hash** in your Progress tab when you change `packages/*` or `src/`.
