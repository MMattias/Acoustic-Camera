# AGENTS.md

This file is for Codex and other AI coding agents.

**The source of truth is [`CLAUDE.md`](./CLAUDE.md) in this same folder — read it first.**
Everything there applies to you too.

Quick reference (full details in `CLAUDE.md`):

- **Verification-first:** prove DSP against synthetic ground truth before trusting real data.
- **Stack:** uv-managed Python 3.12. Checks: `uv run ruff check .`, `uv run mypy`, `uv run pytest`.
- **Guardrails:** don't `git commit`/`push` unless asked; keep this repo out of OneDrive.

If you change shared guidance, update `CLAUDE.md` (the source of truth) so Claude and Codex
stay in sync — do not let the two drift apart.
