---
description: Skeptically review the current diff against the project checklist (dual-agent workflow)
---

You are the **reviewer** in our dual-agent workflow (see `docs/WORKFLOW.md`). Another agent (or
the user) implemented a change. Review it — do **not** modify code, do **not** commit.

Steps:

1. Run `git diff` and `git status` to see the uncommitted change. If nothing is uncommitted,
   review the latest commit instead with `git show`.
2. Read `CLAUDE.md` (golden rule + guardrails §4–5) and the reviewer checklist in
   `docs/WORKFLOW.md`.
3. Evaluate the change against that checklist. Be **skeptical** — actively hunt for:
   - logic / edge-case / units bugs,
   - a *missing or weak* synthetic ground-truth test (does it really assert the right answer?),
   - scope creep (unrelated changes),
   - acoustic gotchas: channel→mic mapping, geometry units, speed of sound, near/far-field,
     spatial aliasing, gain calibration, sample alignment.

Output exactly:

- **Issues** — each tagged `blocker` / `major` / `minor`, with a concrete suggested fix.
- **Questions** — anything you need the author to clarify.
- A final line: `VERDICT: LGTM` or `VERDICT: NEEDS-CHANGES` + the single most important reason.

$ARGUMENTS
