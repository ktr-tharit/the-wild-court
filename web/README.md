# The Wild Court — Web

Playable frontend for the Taiga vertical slice. It runs the canonical question
bundle, adaptive Judgment scoring, realm reveal and six complete animal results.

## Development

Requires Node.js `>=22.13.0` and `pnpm`.

```bash
pnpm install
pnpm run dev
```

Open `http://localhost:3000`.

## Verification

```bash
pnpm test
```

The test command builds the production bundle, verifies the rendered product
shell and runs deterministic scoring journeys for all six Taiga animals.

`app/game-data.generated.json` is produced from the canonical files in the root
`data/` directory by `scripts/export_web_bundle.py`. It remains committed so a
fresh checkout can build without a separate generation step.
