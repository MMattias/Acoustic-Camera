# Acoustic Camera

Locate sound sources by combining a **MiniDSP UMA-16** (16-mic USB array) with a camera,
then overlay a heatmap showing *where* sound is coming from. Live and offline modes.

> 🧭 **How we build this:** verification-first. We prove the DSP against *synthetic ground
> truth* (a signal from a known direction must be recovered correctly) before trusting any
> real-world result. See [`CLAUDE.md`](./CLAUDE.md) for the full working method.

## Status

Phase 0 — **foundations** (project skeleton, tooling, CI). No acoustic code yet.
Roadmap in [`CLAUDE.md`](./CLAUDE.md).

## Requirements

- [uv](https://docs.astral.sh/uv/) (manages Python 3.12 and dependencies)
- Hardware (for later phases): MiniDSP UMA-16, a camera

## Getting started

```powershell
# Install the environment (creates .venv from the locked versions)
uv sync

# Run the checks
uv run ruff format .      # format
uv run ruff check .       # lint
uv run mypy               # type-check
uv run pytest             # tests

# Run the (placeholder) app
uv run acoustic-camera
```

## Project layout

| Path | What it is |
|------|------------|
| `src/acoustic_camera/` | The application code |
| `tests/` | Tests (ground-truth DSP tests live here from Phase 1) |
| `pyproject.toml` | Project metadata, dependencies, and tool config |
| `CLAUDE.md` / `AGENTS.md` | Working method + guardrails for AI agents and humans |
| `.github/workflows/ci.yml` | Runs all checks automatically on every push/PR |
