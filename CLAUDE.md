# CLAUDE.md — Acoustic Camera

Guidance for AI agents (Claude Code, Codex) **and** humans working in this repo.
This file is the single source of truth. (Codex reads `AGENTS.md`, which points here.)

## What we're building

An **acoustic camera**: a MiniDSP **UMA-16** (16-mic USB array) combined with a camera.
We "beamform" the 16 audio channels to estimate *where* sound is coming from, then overlay
a heatmap on the camera image. Goal: both a live mode and an offline-analysis mode.

## The golden rule: verification-first

A previous attempt "ran but produced **wrong results**" — the code worked, but the
physics/DSP was off (the heatmap pointed at the wrong place). That class of bug is
invisible to normal running and to "vibe coding." Therefore:

- Before trusting any real-world output, **prove the math against synthetic ground truth**:
  generate a signal from a *known* direction/location and assert the algorithm recovers it
  within tolerance.
- **Tests are the spec.** Every DSP / beamforming feature ships with a ground-truth test that
  has a clear pass/fail. This is also what makes unattended/agentic runs safe.
- Watch the classic acoustic-camera bugs: channel→mic-position mapping, array-geometry units,
  speed of sound, near- vs far-field steering, spatial aliasing (UMA-16 ~42 mm spacing →
  aliasing above ~4 kHz), per-mic gain calibration, sample alignment.

## Tech stack

- **Python 3.12**, managed by **uv** (not bare pip/poetry).
- **ruff** (lint + format), **pytest** (tests), **mypy --strict** (types).
- Source layout: code in `src/acoustic_camera/`, tests in `tests/`.

## Commands (run from the repo root)

| Task | Command |
|------|---------|
| Sync/refresh environment | `uv sync` |
| Run the app / a script | `uv run acoustic-camera` |
| Format code | `uv run ruff format .` |
| Lint (add `--fix` to auto-fix) | `uv run ruff check .` |
| Type-check | `uv run mypy` |
| Tests | `uv run pytest` |

**Before any PR/commit, all four must pass:** `ruff format`, `ruff check`, `mypy`, `pytest`.

## Conventions

- Everything is type-annotated (mypy strict passes). Public functions get docstrings.
- Keep modules small and single-purpose. Prefer **pure functions** for DSP — they're trivial
  to ground-truth test.
- Use NumPy for numerics; **document array shapes** in docstrings, e.g. `(n_mics, n_samples)`.
- No magic numbers for physics — name constants (speed of sound, mic spacing) and keep them
  in config, not scattered in code.
- New code mirrors the patterns of existing code; the agentic workflow depends on consistency.

## Workflow / guardrails

- **Do NOT `git commit` or `git push` unless explicitly asked.**
- This repo must live **outside OneDrive** (sync locks `.venv`). Path: `C:\Users\matti\dev\Acoustic-Camera`.
- Primary shell: **PowerShell**. `uv` is at `C:\Users\matti\.local\bin`.
- When unsure about a physics/DSP decision, **state the assumption and add a ground-truth test**
  rather than guessing.

## Roadmap

- **Phase 0 — Foundations** (in progress): skeleton, tooling, CI, this harness doc.
- **Phase 1** — synthetic ground-truth harness + first beamformer (delay-and-sum).
- **Phase 2** — real UMA-16 audio input + channel/geometry verification.
- **Phase 3** — live heatmap + camera overlay.
- **Phase 4** — autonomous/agentic workflow (git worktrees, skills, overnight loop).
