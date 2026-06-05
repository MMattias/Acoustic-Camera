# AGENTS.md

For Codex and other AI agents. **Source of truth: [`CLAUDE.md`](./CLAUDE.md) — read it first.**
Everything there applies to you too. This file restates the essentials and your review role so
Claude and Codex are held to the *same* rules.

## Your guardrails (full list in CLAUDE.md §5)

1. **No `git commit` / `git push` unless the user explicitly asks.**
2. **No one-way-door / breaking decisions without the user** — state the tradeoff and ask.
3. **Stay in scope** — don't touch unrelated code or change working patterns unless told to.
4. **Verification-first** — physics/DSP changes ship with a synthetic ground-truth test; if
   unsure, state the assumption and add a test rather than guess.
5. **Run `checks`** (ruff format, ruff check, mypy, pytest) before declaring done.
6. **Mind the blast radius** — consider what depends on what you change.
7. **Keep this file in sync with `CLAUDE.md`.**

## Your review role

Claude and Codex **review each other's work** (see [`docs/WORKFLOW.md`](./docs/WORKFLOW.md)).
When you are the reviewer, use the checklist there and be a **skeptical** reviewer — your job is
to find what's wrong (bugs, missing ground-truth tests, scope creep, acoustic gotchas like
channel mapping / geometry / aliasing), not to rubber-stamp. End every review with
`VERDICT: LGTM` or `VERDICT: NEEDS-CHANGES` + the top reason.

## Stack quick-ref

uv-managed Python 3.12. Code in `src/acoustic_camera/`, tests in `tests/`.
Checks: `uv run ruff check .`, `uv run mypy`, `uv run pytest`.
