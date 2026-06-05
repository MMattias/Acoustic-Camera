# CLAUDE.md — Acoustic Camera

Single source of truth for **how we work** in this repo — for AI agents (Claude Code, Codex)
**and** humans. Codex reads `AGENTS.md`, which points here. If you change a shared rule, change
it **here** so the two never drift apart.

## 1. What we're building

An **acoustic camera**: a MiniDSP **UMA-16** (16-mic USB array) + a camera. We "beamform" the
16 audio channels to estimate *where* sound is coming from, then overlay a heatmap on the camera
image. Goal: a live mode and an offline-analysis mode.

## 2. Context & history (why this repo is the way it is)

- A **previous attempt** (kept only as reference, not in this repo) was substantial —
  DAS/MVDR/CLEAN-SC beamformers, Acoular validation, recording, tests — but it **"ran and
  produced wrong results"**: the code worked, yet the *physics/DSP was wrong* (the heatmap
  pointed at the wrong place). **Lesson:** correctness must be *provable*, because that bug class
  is invisible both to running the app and to "vibe coding."
- **This repo is a deliberate fresh start.** Phase 0 (done): uv + ruff + mypy(strict) + pytest +
  GitHub Actions CI; moved out of OneDrive (sync was locking the venv); a terminal-first
  "cockpit" (PowerShell 7, Windows Terminal, `claude` + `codex` CLIs side by side).
- **Owner:** Mattias — has coded before but is *not* a full-time software engineer. Explain
  non-obvious steps in plain language (especially terminal commands).

## 3. Working philosophy (adopted from Camille / Verso)

- **Foundations compound.** Agents build on what's already here: clear patterns compound in the
  right direction, sloppy ones compound the wrong way. Be rigorous about foundations.
- **Invest in the harness, not just the code.** Rules, tests, CI, and these docs are what let
  agents work safely and semi-autonomously.
- **Tests are the spec.** Clear pass/fail is what makes review — and unattended runs — trustworthy.
- **The truth is in the files, not the chat.** Persist decisions and state to files (specs,
  tracking docs, tests), never only in the conversation/context window.
- **Provider-agnostic & interchangeable.** Claude and Codex are swappable; *neither owns the
  codebase*. They **review each other** (see §6).
- **Principles > tools.** Don't chase shiny tools; invest in the workflow.

## 4. Golden rule: verification-first

Before trusting any real-world output, **prove the math against synthetic ground truth**:
generate a signal from a *known* direction/location and assert the algorithm recovers it within
tolerance. Every DSP / beamforming feature ships with such a test.

Classic acoustic-camera bugs to actively guard against: channel→mic-position mapping,
array-geometry units, speed of sound, near- vs far-field steering, spatial aliasing
(UMA-16 ~42 mm spacing → aliasing above ~4 kHz), per-mic gain calibration, sample alignment.

## 5. Hard guardrails — both agents MUST follow

1. **No `git commit` / `git push` unless the user explicitly asks.**
2. **No one-way-door / breaking decisions without the user** (deleting data, changing public
   APIs or working architecture, schema/format changes). State the tradeoff and ask first.
3. **Stay in scope.** Touch only code relevant to the task. Do not refactor unrelated code or
   change patterns/architecture that already work, unless explicitly told to.
4. **Verification-first.** Any signal-processing/physics change comes with a ground-truth test.
   If unsure about a physics decision, **state the assumption and add a test** — never guess.
5. **Run all checks before declaring "done" or proposing a PR**: `ruff format`, `ruff check`,
   `mypy`, `pytest` must pass. (The `checks` alias runs all four.)
6. **Mind the blast radius.** Before changing something, consider what else depends on it.
7. **Keep `CLAUDE.md` and `AGENTS.md` in sync.** Shared rules change here first.
8. **Repo stays outside OneDrive.** Path: `C:\Users\matti\dev\Acoustic-Camera`.

## 6. How Claude and Codex check each other

We run a **two-agent loop**: one implements, the other reviews — *before* anything is committed.
Full procedure + copy-paste prompts: [`docs/WORKFLOW.md`](docs/WORKFLOW.md). In short:

1. **Scope** the task with both agents until they agree on a plan.
2. **Implement** in one agent; it self-reviews and runs `checks`.
3. **Cross-review:** the *other* agent reviews the diff against the checklist in `docs/WORKFLOW.md`.
4. **Triage & fix** the review comments; repeat 3–4 until both agree.
5. **Decision gate:** one-way-door/breaking tradeoff → stop and ask the user (guardrail #2).
6. **Commit/PR** only when both agree, `checks` pass, *and* the user says so (guardrail #1).

Claude convenience: the `/cross-review` command runs step 3. Codex uses the same prompt from
`docs/WORKFLOW.md`.

## 7. Tech stack & commands

Python 3.12 via **uv**; **ruff** (lint+format), **mypy --strict**, **pytest**.
Code in `src/acoustic_camera/`, tests in `tests/`.

| Task | Command | Alias |
|------|---------|-------|
| Sync environment | `uv sync` | |
| Format / lint / types / tests | run individually, or all at once | `checks` |
| Run the app | `uv run acoustic-camera` | `d` |
| Git status / log | `git status -s` / `git log` | `gss` / `gl` |
| Open 3-pane cockpit | `wt …` | `cockpit` |

## 8. Conventions

- Fully type-annotated (mypy strict passes). Public functions get docstrings.
- Prefer **pure functions** for DSP (trivial to ground-truth test). Document NumPy array shapes,
  e.g. `(n_mics, n_samples)`.
- No magic numbers for physics — name constants and keep them in config.
- New code mirrors the patterns of existing code (consistency keeps the agents on-rails).

## 9. Roadmap

- **Phase 0 — Foundations:** ✅ done.
- **Phase 1** — synthetic ground-truth harness + first beamformer (delay-and-sum).
- **Phase 2** — real UMA-16 audio input + channel/geometry verification.
- **Phase 3** — live heatmap + camera overlay.
- **Phase 4** — autonomous workflow (git worktrees, skills, the "Ralph loop").
