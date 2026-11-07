---
description: "For every dataset the problem statements reference, answer four"
skill_number: "07"
skill_id: data-readiness
name: Data Readiness
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 3-6 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/04-governance-model/track-committee-roster.md
    - artifacts/05-track-strategy/track-list.md
    - artifacts/06-problem-statement-development/final-problem-statements.md
    - artifacts/06-problem-statement-development/dataset-inventory.md
  optional:
    - artifacts/06-problem-statement-development/open-questions-for-city-sponsors.md
outputs:
  - artifacts/07-data-readiness/data-readiness-matrix.md
  - artifacts/07-data-readiness/data-access-plan.md
  - artifacts/07-data-readiness/data-blockers-register.md
downstream_skills:
  - 13-technology-setup
  - 14-judging-system
  - 15-ai-assisted-evaluation
  - 16-post-event-pipeline
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/07-data-readiness/data-readiness-matrix.template.md
  - templates/07-data-readiness/data-access-plan.template.md
  - templates/07-data-readiness/data-blockers-register.template.md
search_paths:
  - artifacts/07-data-readiness/
  - templates/07-data-readiness/
  - examples/*/07-data-readiness/
  - ../**/data/
  - ../**/datasets*.md
  - ../**/RICHMOND_TECH_STACK*.md
  - docs/data/
---

# Skill 07 — Data Readiness

## Purpose

For every dataset the problem statements reference, answer four
questions before participants arrive on day 1:

1. Does the dataset exist?
2. Can a participant team actually access it?
3. Is the format usable without a city employee in the room?
4. If any answer is "no," is there a workaround?

Three artifacts:

1. **`data-readiness-matrix.md`** — a row per dataset; columns for
   exists, accessible, usable, refresh cadence, blockers.
2. **`data-access-plan.md`** — for each accessible dataset, the
   access path (API, public portal, file share, FOIA, partner relay)
   and the time-to-access estimate.
3. **`data-blockers-register.md`** — every "no" in the matrix, with
   a proposed workaround, an owner, and a status.

This skill is the firewall between "we have a problem statement" and
"a team can actually build against it."

## When to use

- Immediately after Skill 06 finalizes statements and the dataset
  inventory
- Whenever a new dataset is added to a problem statement
- Periodically (every 2 weeks) until the event, because access often
  takes longer than expected

## Who should use it

The data lead + city-side liaison + the track committee with the
relevant city ally. Many access decisions require a department
sign-off this skill cannot grant on its own.

## Prerequisites

**Required:**

- `04/track-committee-roster.md` — to know who to ask
- `05/track-list.md` — to scope datasets per track
- `06/final-problem-statements.md` — to know which statements
  each dataset serves
- `06/dataset-inventory.md` — the input list

If `dataset-inventory.md` is at `not-started`, Skill 07 has nothing
to evaluate. Stop and return to Skill 06.

## Inputs

- Upstream artifacts
- Any tech-stack reference from the parent repo (e.g. Richmond's
  `RICHMOND_TECH_STACK_2026.md` lists known data systems and their
  access status)
- City department responses to
  `open-questions-for-city-sponsors.md` if available

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `data-readiness-matrix.md` | `needs-review` | yes |
| `data-access-plan.md` | `needs-review` | yes |
| `data-blockers-register.md` | `needs-review` | yes |

## Search behavior

1. `artifacts/07-data-readiness/*` — existing?
2. `templates/07-data-readiness/*` — load.
3. `examples/*/07-data-readiness/*` — reference.
4. Parent repo:
   - `RICHMOND_TECH_STACK*.md` or equivalent municipal tech-stack
     doc — extremely high-value
   - `data/` directories
   - any prior FOIA responses or data-sharing agreements
5. User-supplied content.

## Validation behavior

Run the three blocks from `validation/checks.md`.

Additional cross-artifact checks:

- Every dataset in `06/dataset-inventory.md` has a row in
  `data-readiness-matrix.md`. Missing rows are a failure.
- Every "no" cell in the matrix has a corresponding entry in
  `data-blockers-register.md`. Orphan "no" cells are a failure.
- Every dataset marked "accessible" in the matrix has an entry in
  `data-access-plan.md` with a time-to-access estimate.

## Normalization behavior

Per the guide. A prior-event tech-stack document is often the single
highest-value input here. Normalize verbatim where the user confirms
the access landscape has not changed; mark `needs-review`
otherwise.

City open-data portal exports and FOIA responses can be referenced
directly in `data-access-plan.md`; the artifact does not need to
ingest the data, just its location and access path.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Walk every dataset.** For each row in
   `dataset-inventory.md`:
   a. Does it exist? (yes / no / unknown — flag unknowns)
   b. Is it accessible? (public API / public portal / restricted /
      FOIA-only / not accessible)
   c. Format usable? (CSV/JSON/SQL good; PDFs and legacy systems
      flagged)
   d. Refresh cadence acceptable for the event window?
   e. Known blockers (vendor lock-in, no API, PII issues, contract
      lapses)
3. **For each accessible dataset**, draft an access plan:
   - URL or endpoint
   - Credentials / API key process
   - Time-to-access estimate (today / days / weeks / FOIA-clock)
   - Person providing access
4. **For each "no" cell**, draft a blocker entry:
   - Description
   - Affected datasets and statements
   - Proposed workaround (synthetic data? scoped subset? alternate
     dataset? drop the statement?)
   - Owner
   - Status (open / in-progress / resolved / accepted-as-blocker)
5. **Loop with the city-side liaison.** Some blockers can only
   resolve via city action. Surface those to governance for a
   decision.
6. **Cross-check.** Every blocker that affects a statement should
   appear in that statement's `open_questions` for traceability.
7. **Write artifacts** at `needs-review`.
8. **Report.** Include a count of unresolved blockers and which
   statements are at risk.

## User interaction rules

- "Unknown" is a valid answer. Push for resolution, but do not
  invent "yes" or "no."
- Time-to-access estimates must come from a city contact or a
  documented portal SLA. Do not guess.
- Workarounds that involve synthetic / mock data are flagged
  prominently — the Richmond year-1 lesson is that participants
  who build against synthetic data produce demos the City cannot
  pilot. Surface this risk explicitly in the blocker entry.
- If a blocker affects a statement and cannot resolve in time,
  the **statement** (Skill 06) needs revision, not just the data
  plan. Surface this to the track committee.

## Completion criteria

- [ ] Three artifacts at canonical paths
- [ ] Every dataset has a row in the matrix
- [ ] Every "no" cell has a blocker entry
- [ ] Every accessible dataset has an access plan entry
- [ ] Every blocker has an owner and a status
- [ ] Unresolved blockers are summarized in the skill's report

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| A dataset is locked behind a vendor system with no API (e.g. Richmond's AvePoint, B2GNow, EnerGov) | Record as blocker; propose workaround (synthetic with prominent disclaimer, alternate dataset, scope reduction); escalate to city sponsor. Do not pretend the data is accessible. |
| FOIA timelines exceed the event window | Mark blocker `accepted-as-blocker`. The team must either drop the statement or accept the limitation. |
| A city contact confirms a dataset exists but cannot share it | Negotiate; if no path, the dataset is `restricted` and the access plan documents the alternative. |
| Synthetic data is the only path | Allow but mark the statement at risk in `data-blockers-register.md` and flag for Skill 16's post-event review. |
| The team finds a new dataset mid-process | Add to `06/dataset-inventory.md` first, then return to Skill 07. The matrix is the consumer of the inventory, not the source. |

## Templates used

- `templates/07-data-readiness/data-readiness-matrix.template.md`
- `templates/07-data-readiness/data-access-plan.template.md`
- `templates/07-data-readiness/data-blockers-register.template.md`

## Downstream skills

- **13 (Technology Setup)** uses the access plan to decide how
  data will be exposed to participants.
- **14 (Judging)** uses the blocker register to score "feasibility"
  honestly.
- **15 (AI Eval)** uses the blocker register to score
  "Implementation Reality" honestly — projects relying on
  inaccessible data get scored down.
- **16, 18** consume the blocker register for follow-through.

## Example invocation

> "Check data readiness. Datasets are in `06/dataset-inventory.md`.
> Tech-stack reference is at
> `2026-annual-hackathon/ideas/RICHMOND_TECH_STACK_2026.md`."

Expected steps:

1. Skill reads the tech-stack reference; many access answers come
   straight from it.
2. Skill walks every dataset, fills the matrix.
3. Skill emits 5-15 blocker entries (typical for a first run).
4. Skill writes artifacts at `needs-review`.
5. Reports: "07 complete. 23 datasets. 5 fully accessible, 11
   restricted with paths, 7 blocked. 4 statements at risk."

## Changelog

- 1.0.0 (initial) — First version. Surfaces synthetic-data risk
  explicitly; enforces orphan-"no" check.
