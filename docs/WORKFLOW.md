# Dual-agent workflow — how Claude & Codex build and check each other

The concrete procedure for the terminal "cockpit" (Claude in one pane, Codex in another). It
encodes Camille/Verso's practice: **one agent implements, the other reviews, before anything is
committed.** There's no automation yet — *you* (Mattias) shuttle context between the panes by
copy-paste. (Automation — skills, scheduled jobs, the "Ralph loop" — arrives in Phase 4.)

## The loop

1. **Scope.** Describe the task to *both* agents. Ask each for a short plan. Reconcile any
   disagreement until they broadly agree. For risky/complex work, have one agent review the
   other's *plan* before any code is written.
2. **Implement.** Pick one agent (the *implementer*). It must:
   - stay in scope (guardrail #3),
   - add/keep a **synthetic ground-truth test** for any DSP/physics (golden rule),
   - run `checks` and make them pass,
   - end with a short summary of what changed + any assumptions made.
3. **Cross-review.** Give the *other* agent the change and the review prompt below. It does **not**
   edit code — it only reports.
4. **Triage & fix.** Bring the review back to the implementer:
   *"Triage these comments — fix what's valid, push back on what's not, and explain."*
   Repeat steps 3–4 until both agents agree.
5. **Decision gate.** If a tradeoff is a one-way door or breaks something that works, **stop and
   ask Mattias** (guardrail #2).
6. **Commit / PR.** Only when both agents agree, `checks` pass, **and** the user has said to
   commit (guardrail #1).

## The review prompt (paste into the reviewing agent)

> You are the **reviewer** in our dual-agent workflow (see `docs/WORKFLOW.md`). Another agent
> implemented a change; review the **current uncommitted diff** (`git diff`; if nothing is
> uncommitted, review the latest commit with `git show`). Read `CLAUDE.md` (golden rule +
> guardrails) and the checklist below. Be **skeptical** — hunt for bugs, missing ground-truth
> tests, scope creep, and acoustic gotchas. Do **not** modify code or commit.
> Output: **Issues** (each tagged blocker / major / minor, with a concrete fix), **Questions**,
> and a final line `VERDICT: LGTM` or `VERDICT: NEEDS-CHANGES` + the top reason.

(Claude users: the `/cross-review` command runs exactly this.)

## Reviewer checklist

- **Correctness** — Does it do what was asked? Any logic / edge-case / units bug?
- **Verification-first** — Is there a synthetic ground-truth test that truly *asserts the right
  answer* (not just "runs without error")?
- **Acoustic gotchas** — channel→mic mapping, geometry units, speed of sound, near/far-field,
  spatial aliasing, gain calibration, sample alignment.
- **Scope** — Only the relevant code touched? Any unrelated changes to revert?
- **Conventions** — Types (mypy strict), docstrings, named constants, documented array shapes?
- **Blast radius** — What else depends on this? Anything downstream affected?
- **Tests / CI** — Do `checks` pass? Are new behaviours covered?

## Why this exists

The previous attempt "ran but gave wrong results." A single agent (or a human vibe-coding) can't
reliably catch that — but a *skeptical second reader* plus a *ground-truth test* can. This loop
is the cheap insurance that keeps the heatmap pointing at the right place.
