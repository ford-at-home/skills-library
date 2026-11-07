---
skill_number: "18"
skill_id: retrospective-and-next-year-plan
name: Retrospective and Next-Year Plan
version: 1.0.0
status: initial
lifecycle_stage: post-event
estimated_duration: 4-8 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/01-civic-alignment/success-definition.md
    - artifacts/02-event-charter/operating-principles.md
    - artifacts/05-track-strategy/track-rationale.md
    - artifacts/07-data-readiness/data-blockers-register.md
    - artifacts/08-partnership-and-sponsor-plan/sponsor-pipeline.csv
    - artifacts/09-community-outreach-plan/outreach-plan.md
    - artifacts/09-community-outreach-plan/outreach-calendar.md
    - artifacts/12-event-operations-plan/run-of-show.md
    - artifacts/12-event-operations-plan/venue-plan.md
    - artifacts/14-judging-system/rubric.md
    - artifacts/14-judging-system/awards.md
    - artifacts/14-judging-system/judge-roster.md
    - artifacts/14-judging-system/judging-runbook.md
    - artifacts/15-ai-assisted-evaluation/implementation-reality-rubric.md
    - artifacts/16-post-event-pipeline/day-30-plan.md
    - artifacts/16-post-event-pipeline/city-champion-path.md
    - artifacts/16-post-event-pipeline/civic-working-session-plan.md
    - artifacts/17-open-source-handoff/oss-handoff-plan.md
    - artifacts/17-open-source-handoff/license-policy.md
    - artifacts/17-open-source-handoff/public-marketplace-listing.md
  optional: []
outputs:
  - artifacts/18-retrospective-and-next-year-plan/retrospective-report.md
  - artifacts/18-retrospective-and-next-year-plan/lessons-log.md
  - artifacts/18-retrospective-and-next-year-plan/next-year-charter-deltas.md
  - artifacts/18-retrospective-and-next-year-plan/decision-records/README.md
downstream_skills:
  - "next year's 01-civic-alignment"
  - "next year's 02-event-charter"
templates_used:
  - templates/18-retrospective-and-next-year-plan/retrospective-report.template.md
  - templates/18-retrospective-and-next-year-plan/lessons-log.template.md
  - templates/18-retrospective-and-next-year-plan/next-year-charter-deltas.template.md
  - templates/18-retrospective-and-next-year-plan/decision-record.template.md
search_paths:
  - artifacts/18-retrospective-and-next-year-plan/
  - templates/18-retrospective-and-next-year-plan/
  - examples/*/18-retrospective-and-next-year-plan/
  - ../**/retrospective*
  - ../**/lessons*
  - ../**/postmortem*
  - docs/retro/
---

# Skill 18 — Retrospective and Next-Year Plan

## Purpose

Close the loop. Compare what actually happened to what was
planned, capture the lessons, and feed them into next year's
planning. The skill also captures **decision records** for
load-bearing decisions so the team's institutional knowledge
survives turnover.

Four artifacts (one of which is a folder):

1. **`retrospective-report.md`** — actual vs. planned across the
   success definition; what worked, what didn't, what to change.
2. **`lessons-log.md`** — categorized lessons with observation,
   recommendation, and owner.
3. **`next-year-charter-deltas.md`** — proposed changes for year
   N+1's charter (Skill 02).
4. **`decision-records/`** — one ADR per load-bearing decision
   (with context, decision, consequences). Optional but strongly
   encouraged.

## When to use

- 3-6 weeks after the event (long enough for Day 30 outcomes
  to be visible, short enough for memory to be fresh)
- Continued additions as 90-day and 6-month outcomes resolve

## Who should use it

The full organizing team. The agent structures inputs and drafts
sections; the team contributes lessons.

## Prerequisites

**Required:** 20 upstream artifacts. The retrospective compares
the full planning corpus to actual outcomes.

## Inputs

- All upstream plugin artifacts
- Event metrics (attendance, submission count, judge feedback,
  participant survey)
- Day-30 outcomes (City response, working session participation,
  championed ideas)
- 90-day and 6-month outcomes as they become known

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `retrospective-report.md` | `needs-review` | yes |
| `lessons-log.md` | `draft` | no |
| `next-year-charter-deltas.md` | `needs-review` | yes |
| `decision-records/` (folder) | `draft` | no |

## Search behavior

1. `artifacts/18-retrospective-and-next-year-plan/*` — existing?
2. `templates/18-retrospective-and-next-year-plan/*` — load.
3. `examples/*/18-retrospective-and-next-year-plan/*` — reference.
4. Parent repo for `retrospective*`, `lessons*`, `postmortem*`,
   participant survey results.
5. User-supplied content.

## Validation behavior

Run the four blocks. Additional:

- `retrospective-report.md` must compare actual against every
  goal in `01/success-definition.md`.
- Every lesson in `lessons-log.md` has an owner.
- Every charter delta proposal in `next-year-charter-deltas.md`
  references at least one lesson supporting it.
- Each decision record uses ADR format (context, decision,
  consequences).

## Normalization behavior

Participant surveys are particularly high-value source material.
Normalize summary statistics into the report; keep raw response
data referenced as `source_materials`, not inlined (privacy).

A prior year's retrospective is useful as a structure reference
but the content is event-specific.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Compare planned to actual.** For each goal in
   `01/success-definition.md`, capture what actually happened
   and the gap.
3. **Walk the team through what worked / didn't work / what to
   change.** Three columns; each entry has a one-line summary,
   the affected skill(s), and a proposed direction.
4. **Categorize lessons.** Buckets:
   - Civic alignment and governance
   - Tracks and problem statements
   - Data readiness
   - Sponsorship and partnerships
   - Outreach and registration
   - Participant experience
   - Mentor / volunteer ops
   - Event ops
   - Technology
   - Judging
   - AI evaluation
   - Post-event pipeline
   - Open-source handoff
5. **Build lessons-log.** One row per lesson:
   - category, observation, recommendation, owner, status
6. **Draft next-year-charter-deltas.** Specific changes to
   propose for Skill 02 (Event Charter) of year N+1.
7. **Capture load-bearing decisions as ADRs.** A load-bearing
   decision is one that:
   - Was non-obvious
   - Had significant consequences
   - Would benefit from being remembered by year N+2's team
   Examples (Richmond year-1): pricing structure, fiscal sponsor
   choice, track count, blue-sky problem statement format,
   AI-eval inclusion, no-City rule for working sessions.
8. **Write artifacts.**
9. **Report.**

## User interaction rules

- The retrospective is honest, not performative. The skill should
  surface uncomfortable lessons (e.g. "we promised X mentors and
  delivered Y") rather than soften them.
- Lessons without owners atrophy. Every lesson gets a named
  owner — typically the role lead for the affected area (per
  `04/governance-model.md`'s role catalog).
- ADRs are written for the next team, not the current one.
  Context should be enough for someone with no event history to
  understand why a decision was made.
- The "what to change" column proposes; it does not decide. Next
  year's Skill 02 is where charter changes actually land.

## Completion criteria

- [ ] Four artifacts at canonical paths
- [ ] Retrospective compares to every success goal
- [ ] Every lesson has an owner
- [ ] Charter deltas reference supporting lessons
- [ ] At least 3 ADRs for load-bearing decisions
- [ ] `needs-review` artifacts have reviewers named

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Goals had no measurement plan | Document the gap and propose a measurement plan in `next-year-charter-deltas.md`. The lesson is "define success measurably" — Skill 01's job for year N+1. |
| Participant survey response rate low | Document the limitation. Don't extrapolate; report what was learned and the methodology. |
| Day-30 outcomes not yet visible | Run an interim retrospective; revisit at 90 days. |
| Team disagrees on a lesson | Capture both perspectives explicitly. Disagreement is signal, not noise. |
| A load-bearing decision was made informally and no one remembers the reasoning | Document the reasoning best you can; mark the ADR `status: reconstructed`. Lesson: capture decisions in real time, not at retrospective. |

## Templates used

- See frontmatter.

## Downstream skills

- **Next year's 01 (Civic Alignment)** uses
  `retrospective-report.md` and `lessons-log.md` as
  `source_materials`. Year N+1 starts fresh; year N is reference.
- **Next year's 02 (Event Charter)** consumes
  `next-year-charter-deltas.md`.
- **Future years** can read the `decision-records/` folder to
  understand load-bearing prior decisions.

## Example invocation

> "Run the retrospective. Event is 4 weeks past. Day 30
> announcement went out 1 week ago; 3 ideas championed. Survey
> response rate: 62%."

Expected steps:

1. Skill reads all 20 upstream artifacts.
2. Skill drafts retrospective comparing actual to
   `01/success-definition.md`.
3. Skill walks team through what worked / what didn't / what to
   change (categorized).
4. Skill builds lessons-log with owners.
5. Skill drafts charter deltas for next year.
6. Skill captures 5 ADRs for load-bearing decisions (fiscal
   sponsor, paywall, AI eval, no-City working sessions, license
   default).
7. Reports: "18 complete (pending review). 31 lessons logged. 8
   charter deltas proposed. 5 ADRs captured."

## Changelog

- 1.0.0 (initial) — First version. ADR capture optional but
  encouraged; honesty over performativity; lessons require
  owners.
