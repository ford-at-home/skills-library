---
description: "Convert each track into named, scoped, data-grounded problem"
skill_number: "06"
skill_id: problem-statement-development
name: Problem Statement Development
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 4-8 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/01-civic-alignment/civic-priority-map.md
    - artifacts/03-stakeholder-map/stakeholder-map.md
    - artifacts/04-governance-model/track-committee-roster.md
    - artifacts/05-track-strategy/final-track-strategy.md
    - artifacts/05-track-strategy/track-list.md
  optional:
    - artifacts/03-stakeholder-map/partner-register.csv
outputs:
  - artifacts/06-problem-statement-development/final-problem-statements.md
  - artifacts/06-problem-statement-development/track-context-briefs.md
  - artifacts/06-problem-statement-development/dataset-inventory.md
  - artifacts/06-problem-statement-development/open-questions-for-city-sponsors.md
downstream_skills:
  - 07-data-readiness
  - 09-community-outreach-plan
  - 10-participant-experience-plan
  - 13-technology-setup
  - 14-judging-system
  - 15-ai-assisted-evaluation
  - 16-post-event-pipeline
templates_used:
  - templates/06-problem-statement-development/problem-statement.template.md
  - templates/06-problem-statement-development/final-problem-statements.template.md
  - templates/06-problem-statement-development/track-context-brief.template.md
  - templates/06-problem-statement-development/track-context-briefs.template.md
  - templates/06-problem-statement-development/dataset-inventory.template.md
  - templates/06-problem-statement-development/open-questions-for-city-sponsors.template.md
search_paths:
  - artifacts/06-problem-statement-development/
  - templates/06-problem-statement-development/
  - examples/*/06-problem-statement-development/
  - ../**/problem-statements/
  - ../**/PILLARS.md
  - ../**/research/
  - ../**/roundtables/
  - ../**/breakouts/
  - docs/problem-statements/
---

# Skill 06 — Problem Statement Development

## Purpose

Convert each track into named, scoped, data-grounded problem
statements that participants can build against. This is the highest
content-density skill in the pre-event arc; it produces the
artifacts every participant team and every judge will read first.

Four artifacts:

1. **`final-problem-statements.md`** — the canonical statements,
   two per track (one practical, one blue-sky), or other count
   justified by track rationale.
2. **`track-context-briefs.md`** — for each track, the civic
   context, prior work, and the people who would use a solution.
3. **`dataset-inventory.md`** — every dataset a statement references,
   with owner, format, access path, and known limitations.
4. **`open-questions-for-city-sponsors.md`** — questions the
   organizers still need answered by city departments before the
   event.

## When to use

- Once tracks are stable (Skill 05 at `needs-review` or higher)
- Once track committees are staffed enough to author content
- 4–8 weeks before the event; statements need time to be reviewed
  by city sponsors and refined

## Who should use it

Per-track committees, coordinated by the executive lead and
city-side liaison. The agent is a scribe and a stress-tester.

## Prerequisites

**Required:**

- `01/civic-priority-map.md` (anchors the "why this matters" of
  each statement)
- `03/stakeholder-map.md` (identifies the users each statement
  serves)
- `04/track-committee-roster.md` (identifies the authors)
- `05/final-track-strategy.md` and `05/track-list.md` (define the
  tracks the statements organize under)

**Optional:**

- `03/partner-register.csv` (provides civic partner contact info
  for context briefs)

If any required input is missing, stop and report.

## Inputs

- Upstream artifacts
- Per-track research: prior art, regional context, conversations
  with city allies, existing datasets
- Existing problem statements from prior events, if any

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `final-problem-statements.md` | `needs-review` | yes |
| `track-context-briefs.md` | `draft` | optional |
| `dataset-inventory.md` | `needs-review` | yes |
| `open-questions-for-city-sponsors.md` | `needs-review` | yes |

## Search behavior

1. `artifacts/06-problem-statement-development/*` — existing?
2. `templates/06-problem-statement-development/*` — load.
3. `examples/*/06-problem-statement-development/*` — reference.
4. Parent repo for:
   - `PILLARS.md` (frequently contains problem statement language)
   - `problem-statements/` directories
   - `research/` directories — likely to contain track-specific
     prior-art research
   - `roundtables/` or `breakouts/` — meeting transcripts where
     statements were drafted
5. User-supplied content.

**Special case for the Richmond parent repo:**
`2026-annual-hackathon/PILLARS.md` contains two problem statements
per pillar in its current form. Offer to normalize into
`final-problem-statements.md`. Mark each statement `needs-review`
because problem statements drift year to year.

`2026-annual-hackathon/research/` contains track-specific
contextual research (e.g.
`cats-institutional-framework-and-design.md`,
`cats-technology-architecture-and-prior-art.md`). Offer to
normalize into `track-context-briefs.md`.

`2026-annual-hackathon/roundtables/` contains breakout transcripts.
Treat as source material, not direct artifact content; reference
in `track-context-briefs.md` as `source_materials`.

## Validation behavior

Run the four artifacts' validation blocks. Additional checks:

- Every problem statement names a **user** (the person whose
  problem this is). "Residents" is too vague; "first-time
  entrepreneurs registering an LLC in Richmond" is acceptable.
- Every statement describes a **problem**, not a solution. Reject
  statements like "Build an app that..." — rewrite as "Residents
  cannot..." or "City staff struggle to..."
- Every statement is anchored to at least one dataset in
  `dataset-inventory.md`. If the dataset does not exist, the
  statement is `blocked` until Skill 07 confirms the data is
  acquirable.
- Every track in `track-list.md` has at least one statement.
- Every statement names a track from `track-list.md`.

## Normalization behavior

Per the guide. Special considerations for problem statements:

- **Verbatim preservation matters.** If a city sponsor or civic
  partner has approved specific language, the normalization must
  preserve that language. Mark as a block quote with the source
  cited.
- **A statement without a named user gets a user added during
  normalization as an `open_question`**, not invented.
- **Blue-sky statements** are intentionally less constrained than
  practical statements. The schema is the same, but blue-sky
  statements may have weaker data anchors. Flag them as
  `blue_sky: true` in the per-statement metadata.

## Step-by-step procedure

1. **Search.** Inventory all candidate sources.
2. **Read upstream.** Confirm tracks are stable.
3. **For each track:**
   a. Convene the committee (or, in agent mode, work with the
      committee lead).
   b. Draft two statements: one **practical** (the city could
      pilot a solution within a year), one **blue-sky** (the
      problem matters but the path forward is open).
   c. For each statement, capture:
      - Title (4-8 words, plain English)
      - User (specific cohort)
      - Problem (current state, not solution)
      - Why it matters (cite `civic-priority-map.md`)
      - What good looks like (success criteria, not specs)
      - Owning track
      - Anchor dataset(s)
      - `blue_sky: true|false`
   d. Draft the track's context brief: civic context, prior work,
      users, partners, key data sources.
   e. Add datasets referenced to `dataset-inventory.md`.
   f. Add any unanswered questions to
      `open-questions-for-city-sponsors.md`, tagged to the city
      office that can answer.
4. **Cross-track review.** Look for statements that duplicate or
   that should be in a different track.
5. **City sponsor pass.** Send `open-questions-for-city-sponsors.md`
   to named city contacts. Their answers feed back into the
   statements before they go to `approved`.
6. **Write all four artifacts.**
7. **Report.**

## User interaction rules

- Push back hard on solution-language. "Build a dashboard" is not
  a problem statement.
- Push back on vague users. "Help residents" is not a user.
- Reject statements without dataset anchors. If the team thinks the
  data exists but doesn't know where, the statement is
  `open_question` material until Skill 07 confirms.
- Blue-sky statements get more latitude on data anchors, but they
  still need a named user.
- Resist the urge to write more than two statements per track.
  Extra statements dilute participant attention.

## Completion criteria

- [ ] Four artifacts at canonical paths
- [ ] Every track has the planned number of statements
- [ ] Every statement names a user and a problem (not a solution)
- [ ] Every statement anchors to at least one dataset
- [ ] Every dataset is in `dataset-inventory.md` with owner and
      access path (even if "unknown — flagged for Skill 07")
- [ ] City-sponsor open questions are drafted and the recipients
      named
- [ ] `final-problem-statements.md` is `needs-review`

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Track committee can't generate two statements | Likely the track is too narrow or the committee is under-staffed. Loop back to Skill 05 (combine tracks?) or Skill 03/04 (more committee members?). |
| A statement has no dataset anchor and the team doesn't know what data exists | Mark statement `blocked` and create a row in `dataset-inventory.md` with `status: unknown`. Skill 07 will resolve. |
| Two tracks produce statements that overlap | Move the duplicate to the better-fitting track. Update `track-rationale.md` to note the move. |
| A city sponsor declines to approve specific language | Negotiate; if no resolution, flag the statement as `needs-review` indefinitely and surface to governance for a decision. Never publish unapproved language. |
| A statement was carried forward from last year without review | Force `needs-review` regardless. Prior-year problems may have been solved, abandoned, or transformed. |
| Solution-language keeps creeping in | Add a note to the skill's run log; coach the committee. Consider a refinement pass with the city-side liaison. |

## Templates used

- `templates/06-problem-statement-development/problem-statement.template.md`
  (per-statement schema; referenced by all four output templates)
- `templates/06-problem-statement-development/final-problem-statements.template.md`
- `templates/06-problem-statement-development/track-context-brief.template.md`
- `templates/06-problem-statement-development/track-context-briefs.template.md`
- `templates/06-problem-statement-development/dataset-inventory.template.md`
- `templates/06-problem-statement-development/open-questions-for-city-sponsors.template.md`

## Downstream skills

- **07 (Data Readiness)** consumes `dataset-inventory.md` and
  `open-questions-for-city-sponsors.md`.
- **09, 10, 13, 14, 15, 16** all reference
  `final-problem-statements.md`.

## Example invocation

> "Develop problem statements. Tracks are in `track-list.md`.
> Source material: `2026-annual-hackathon/PILLARS.md` and the
> `2026-annual-hackathon/research/` directory."

Expected steps:

1. Skill reads `PILLARS.md`, normalizes into
   `final-problem-statements.md` with every statement at
   `needs-review`.
2. Skill reads `research/` files, normalizes into
   `track-context-briefs.md` per track.
3. Skill walks each statement with the user: confirm user, confirm
   problem, confirm dataset, confirm `blue_sky` flag.
4. Skill builds `dataset-inventory.md` from references found.
5. Skill builds `open-questions-for-city-sponsors.md` for any
   unresolved questions.
6. Reports: "06 complete (pending review). 14 statements across 7
   tracks. 3 statements lack dataset anchors — flagged for Skill 07.
   8 city sponsor questions drafted."

## Changelog

- 1.0.0 (initial) — First version. Enforces user/problem/dataset
  schema; allows blue-sky variant with weaker data anchor.
