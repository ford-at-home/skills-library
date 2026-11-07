---
description: "Decide the track structure: how many tracks, what each is called,"
skill_number: "05"
skill_id: track-strategy
name: Track Strategy
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 2-4 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/01-civic-alignment/civic-priority-map.md
    - artifacts/02-event-charter/scope-boundaries.md
    - artifacts/03-stakeholder-map/stakeholder-map.md
    - artifacts/04-governance-model/governance-model.md
  optional:
    - artifacts/04-governance-model/track-committee-roster.md
outputs:
  - artifacts/05-track-strategy/final-track-strategy.md
  - artifacts/05-track-strategy/track-list.md
  - artifacts/05-track-strategy/track-rationale.md
downstream_skills:
  - 06-problem-statement-development
  - 07-data-readiness
  - 08-partnership-and-sponsor-plan
  - 09-community-outreach-plan
  - 11-mentor-volunteer-ops
  - 13-technology-setup
  - 14-judging-system
  - 16-post-event-pipeline
templates_used:
  - templates/05-track-strategy/final-track-strategy.template.md
  - templates/05-track-strategy/track-list.template.md
  - templates/05-track-strategy/track-rationale.template.md
search_paths:
  - artifacts/05-track-strategy/
  - templates/05-track-strategy/
  - examples/*/05-track-strategy/
  - ../**/PILLARS.md
  - ../**/tracks*.md
  - ../**/pillars*.md
  - docs/tracks/
---

# Skill 05 — Track Strategy

## Purpose

Decide the track structure: how many tracks, what each is called,
which civic priorities each maps to, which committee owns each.
Produce the artifacts every subsequent skill keys off of.

Three artifacts:

1. **`final-track-strategy.md`** — the strategy narrative: why this
   structure, why this count, what was considered and rejected.
2. **`track-list.md`** — the operational list every downstream
   skill reads. One section per track.
3. **`track-rationale.md`** — alternatives considered, decisions
   made, reasons. Becomes part of the retrospective input.

## When to use

- Once governance and stakeholder maps are stable enough to know
  who can staff a committee
- Once the civic priority map identifies which priorities are in
  scope
- Before any track-keyed skill (06, 07, etc.) runs

## Who should use it

Executive lead + governance body. The track decision is one of the
year's load-bearing calls.

## Prerequisites

**Required:**

- `01/civic-priority-map.md`
- `02/scope-boundaries.md`
- `03/stakeholder-map.md`
- `04/governance-model.md`

**Optional but strongly recommended:**

- `04/track-committee-roster.md` — if available, it constrains how
  many tracks are staffable

## Inputs

- Upstream artifacts
- The user's intuition about a workable track count for the event's
  scale
- Optional: prior-year track list

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `final-track-strategy.md` | `needs-review` | yes |
| `track-list.md` | `needs-review` | yes |
| `track-rationale.md` | `draft` | no |

## Search behavior

1. `artifacts/05-track-strategy/*` — existing?
2. `templates/05-track-strategy/*` — load.
3. `examples/*/05-track-strategy/*` — reference.
4. Parent repo for `PILLARS.md`, `tracks*.md`, `pillars*.md`.
5. User-supplied content.

**Special case for the Richmond parent repo:**
`2026-annual-hackathon/PILLARS.md` is a fully filled-in Richmond
track list. If found, offer to **normalize** it into
`track-list.md` for the user. Normalization here means: copy the
structure, mark every track as `needs-review`, and flag the
priorities for re-confirmation with the current civic priority map.

## Validation behavior

Run the three artifacts' validation blocks. Additional checks:

- Every track in `track-list.md` maps to at least one priority in
  `civic-priority-map.md`
- Every track has a committee in `04/track-committee-roster.md` —
  if the committee roster is missing, flag a forward dependency
- The track count is justified in `final-track-strategy.md` (no
  silent "7 because that's what Richmond did")

## Normalization behavior

If a prior `PILLARS.md` exists, normalize into `track-list.md`. The
prior pillar set is treated as a **proposal**, not a default.
Every row is `needs-review`, and the rationale document records
"carried over from year N; re-confirm each track against year N+1
civic priority map."

## Step-by-step procedure

1. **Search and read upstream.**
2. **Pull priorities in scope.** From `civic-priority-map.md`, list
   the priorities that the charter said the event would work on.
3. **Decide track count.** With the user:
   - How many committees can we actually staff? (from
     `04/track-committee-roster.md` or the user's read of
     `03/partner-register.csv`)
   - How many problem statements can we realistically develop?
     (rough rule: 2 per track)
   - How many tracks can a participant choose from without paralysis?
     (typical range: 5-8)
4. **Map priorities to tracks.** A track may correspond 1:1 with a
   priority, or merge two related priorities, or split a broad
   priority into two tracks. Justify each decision in the rationale.
5. **Name each track.** Names should be plain-English and
   resident-facing. Avoid government jargon.
6. **Write `track-list.md`.** One section per track. Per track:
   name, one-sentence description, priority(ies) it maps to,
   committee.
7. **Write `final-track-strategy.md`.** Strategy narrative — why
   this count, why these tracks, what the participant experience
   looks like across tracks.
8. **Write `track-rationale.md`.** Alternatives considered, rejects
   with reasons. Reference operating principles (`02/operating-
   principles.md`) when relevant.
9. **Report.**

## User interaction rules

- The track count is a real constraint. Push back if the user
  proposes a count that exceeds the available committee capacity —
  Richmond's year-1 lesson is that under-staffed tracks become
  participant-experience disasters.
- Track names: plain English. Reject jargon. "Maternal Health Data
  Coordination" beats "MCH Data Ops".
- Resist "we'll figure out the committee later." A track without a
  committee in year N is a track that drifts.

## Completion criteria

- [ ] Three artifacts at canonical paths
- [ ] Every track maps to a priority
- [ ] Every track has (or has a placeholder for) a committee
- [ ] Track count is justified
- [ ] All artifacts have reviewers named

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| User wants more tracks than staffable | Reduce count or recruit more committee members (loop back to Skill 03). Do not proceed with under-staffed tracks. |
| A priority cannot find a track home | Either drop the priority from scope (update `civic-priority-map.md` and `scope-boundaries.md`) or split an existing track. |
| Two tracks overlap heavily | Merge them. Record the merge in `track-rationale.md` for the retrospective. |
| Track name draws complaints from a stakeholder | Negotiate; record the negotiation in `track-rationale.md`. Names matter publicly. |
| User wants to carry forward last year's tracks unchanged | Allow but flag for re-confirmation against current civic-priority-map.md. Do not auto-`approved`. |

## Templates used

- `templates/05-track-strategy/final-track-strategy.template.md`
- `templates/05-track-strategy/track-list.template.md`
- `templates/05-track-strategy/track-rationale.template.md`

## Downstream skills

Skill 05's outputs gate roughly 8 downstream skills. `track-list.md`
in particular is the most-cited artifact in the plugin.

## Example invocation

> "Decide tracks. We have the Richmond Mayor's Action Plan with 7
> pillars; we have committee leads for 7 tracks; we want to keep
> the 7-pillar structure from year 1."

Expected steps:

1. Skill normalizes `2026-annual-hackathon/PILLARS.md` into
   `track-list.md` with every row at `needs-review`.
2. Skill writes `final-track-strategy.md` capturing the
   "7-tracks-because-7-pillars" rationale.
3. Skill writes `track-rationale.md` listing the alternatives
   considered (5 tracks, 9 tracks, 7 with different cuts) and why
   the 7-pillar mapping was kept.
4. Reports: "05 complete. Next: 06 (Problem Statement Development).
   The track committee roster has 1 unfilled city-ally seat
   (Inclusive Communities) — that's a blocker for 06."

## Changelog

- 1.0.0 (initial) — First version. Treats prior-year track lists as
  proposals, not defaults. Enforces track count against committee
  capacity.
