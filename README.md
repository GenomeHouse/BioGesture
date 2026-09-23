# BioGesture

BioGesture is a research-oriented workspace for controlling sequence analysis
tools with hand gestures. The repository is organized as a small monorepo:

- `apps/web` contains the Next.js user interface.
- `apps/api` contains the FastAPI service.
- `packages/vision` contains hand and gesture recognition primitives.
- `packages/bioinformatics` contains sequence analysis primitives.
- `packages/intent` translates recognized gestures into commands.
- `packages/shared` contains shared constants, enums, errors, and utilities.
- `ml` and `research` contain model training and reproducible experiments.

## Development

The initial scaffold is deliberately dependency-light. Python libraries use
`pyproject.toml`, while the web application has its own `package.json` under
`apps/web`.

```bash
python -m pytest
python -m uvicorn apps.api.app.main:app --reload
cd apps/web && npm install && npm run dev
```

The API exposes `GET /health` and `GET /docs`. The web application provides a
small dashboard shell that can be expanded as the gesture and sequence
contracts become concrete.