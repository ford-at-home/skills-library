---
description: "Convert the event's outputs (submissions + AI evaluation + judging"
skill_number: "16"
skill_id: post-event-pipeline
name: post-event-pipeline
display_name: "Post-Event Pipeline"
version: 1.0.0
status: initial
lifecycle_stage: post-event
estimated_duration: 4-8 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/01-civic-alignment/civic-priority-map.md
    - artifacts/01-civic-alignment/city-sponsor-brief.md
    - artifacts/02-event-charter/scope-boundaries.md
    - artifacts/03-stakeholder-map/stakeholder-map.md
    - artifacts/03-stakeholder-map/partner-register.csv
    - artifacts/03-stakeholder-map/decision-maker-map.md
    - artifacts/04-governance-model/governance-model.md
    - artifacts/04-governance-model/track-committee-roster.md
    - artifacts/04-governance-model/decision-rights-matrix.md
    - artifacts/05-track-strategy/final-track-strategy.md
    - artifacts/05-track-strategy/track-list.md
    - artifacts/06-problem-statement-development/final-problem-statements.md
    - artifacts/06-problem-statement-development/open-questions-for-city-sponsors.md
    - artifacts/07-data-readiness/data-readiness-matrix.md
    - artifacts/07-data-readiness/data-access-plan.md
    - artifacts/07-data-readiness/data-blockers-register.md
    - artifacts/08-partnership-and-sponsor-plan/sponsor-pipeline.csv
    - artifacts/14-judging-system/rubric.md
    - artifacts/14-judging-system/awards.md
    - artifacts/15-ai-assisted-evaluation/ai-eval-plan.md
    - artifacts/15-ai-assisted-evaluation/evaluator-personas.md
    - artifacts/15-ai-assisted-evaluation/implementation-reality-rubric.md
    - artifacts/15-ai-assisted-evaluation/eval-runbook.md
    - artifacts/15-ai-assisted-evaluation/results-package-spec.md
  optional: []
outputs:
  - artifacts/16-post-event-pipeline/day-30-plan.md
  - artifacts/16-post-event-pipeline/city-champion-path.md
  - artifacts/16-post-event-pipeline/civic-working-session-plan.md
  - artifacts/16-post-event-pipeline/handoff-shortlist.md
downstream_skills:
  - 17-open-source-handoff
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/16-post-event-pipeline/day-30-plan.template.md
  - templates/16-post-event-pipeline/city-champion-path.template.md
  - templates/16-post-event-pipeline/civic-working-session-plan.template.md
  - templates/16-post-event-pipeline/handoff-shortlist.template.md
search_paths:
  - artifacts/16-post-event-pipeline/
  - templates/16-post-event-pipeline/
  - examples/*/16-post-event-pipeline/
  - ../**/POST_HACKATHON*
  - ../**/post-event*
  - ../**/day-30*
  - docs/post-event/
---

# Skill 16 — Post-Event Pipeline

## Purpose

Convert the event's outputs (submissions + AI evaluation + judging
results) into a structured handoff the City can actually act on,
and a parallel path that keeps non-championed ideas in the civic
conversation without the City carrying every one of them.

Four artifacts:

1. **`day-30-plan.md`** — the Day 30 announcement: what it
   contains, when it goes out, who it goes to.
2. **`city-champion-path.md`** — how the City reviews and claims
   ideas it can lead. Reframes ownership: the City is given
   strategic leadership; ideas are not "given away."
3. **`civic-working-session-plan.md`** — the parallel track for
   ideas the City doesn't champion: 15-minute walkthroughs,
   dialogue with civic experts (not City staff in the room),
   facilitated introductions.
4. **`handoff-shortlist.md`** — the curated list of ideas being
   handed off, with status, owner, and pillar context.

## When to use

- Begin drafting at week 1 post-event so Day 30 is hit
- Refresh at month 3 and month 6 to track follow-through

## Who should use it

Executive lead + city-side liaison + governance body. The agent
drafts; humans negotiate with City Hall.

## Prerequisites

**Required:** 24 upstream artifacts. Post-event pipeline depends
on civic alignment, governance, judging results, and AI eval
results.

## Inputs

- Upstream artifacts
- Event submissions
- Live judging results
- AI eval scorecards from Skill 15
- City Hall innovation-intake calendar (when does the budget
  cycle hit? when does the product-innovation review meet?)

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `day-30-plan.md` | `needs-review` | yes |
| `city-champion-path.md` | `needs-review` | yes |
| `civic-working-session-plan.md` | `needs-review` | yes |
| `handoff-shortlist.md` | `needs-review` | yes |

## Search behavior

1. `artifacts/16-post-event-pipeline/*` — existing?
2. `templates/16-post-event-pipeline/*` — load.
3. `examples/*/16-post-event-pipeline/*` — reference.
4. Parent repo for `POST_HACKATHON*`, `post-event*`, `day-30*`.
5. User-supplied content (City Hall intake calendar, etc.).

## Validation behavior

Run the four blocks. Additional:

- `handoff-shortlist.md` may not contain ideas whose data
  blockers are `accepted-as-blocker` unless explicitly noted.
- Every idea on the shortlist references its submission and at
  least one of its scorecards.
- `city-champion-path.md` cannot promise the City a commitment;
  it documents the path the City may opt into.
- `civic-working-session-plan.md` must state explicitly that the
  City is not in the working-session room.

## Normalization behavior

A prior `POST_HACKATHON_CONTACTS` document is useful for the
working-session invite list. Normalize names into the relevant
artifact's `participants` section.

A Day 30 announcement from a prior event can serve as a structure
reference. Do not copy content; the announcement is event-specific.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Confirm the day-30 target.** Calendar a date 30 days
   post-event. Align with any City Hall meeting (budget cycle,
   product-innovation review) that the announcement should hit.
3. **Build handoff-shortlist.** Apply selection criteria:
   - Strong IR tier (S or A typical)
   - Civic alignment to a current priority
   - Either championed by judges or surfaced by AI eval as
     overlooked
   - Data path realistic (per `07/data-readiness-matrix.md`)
   - For each shortlisted idea: title, team, problem statement,
     IR tier, status, owner
4. **Draft day-30 announcement plan.** The plan covers:
   - What the announcement contains (overview of event,
     shortlist, paths)
   - Recipients (City stakeholders named in
     `03/decision-maker-map.md`, partners, participants, press)
   - The verbatim announcement may live in an
     `outreach-messages/` file referenced from this plan
5. **Draft city-champion-path.** Reframe ownership:
   - The City is given strategic leadership for any initiative it
     chooses; ideas are open-source by default
   - If another regional group runs with an idea independently,
     everyone wins
   - "Considered and not chosen: assigning each idea a single
     owner up front" — document the rationale
   - The City's product-innovation intake (if it exists) is the
     mechanism; this skill documents it, does not invent it
6. **Draft civic-working-session-plan.** Cover:
   - Format: 15-minute walkthroughs of each non-championed idea
   - Dialogue with civic experts who would use the solution
   - Facilitated introductions, partnership-building
   - Three goals: collaboration, invite the absent, build on
     momentum
   - "Considered and not chosen: including the City in the
     working sessions" — surface conflict-of-interest reasoning
7. **Cross-check.** Shortlist size matches what the City and
   civic groups can actually engage. Working-session capacity
   matches non-championed count.
8. **Report.**

## User interaction rules

- The "ownership" framing is delicate. Do not say "give this
  idea to the City." Say "the City may take strategic leadership
  on this initiative if it chooses." The difference matters.
- Verbatim Day 30 announcement may be preserved as the org has
  drafted it; the plan around it is what this skill produces.
- The civic working sessions explicitly exclude the City from
  the room. Surface this as a design choice with a stated reason
  (free-of-conflict dialogue, candor about implementation
  realities). Do not let scope creep blur the line.
- "Champion" status is opt-in, by the City, on the City's
  timeline. The skill does not assign champions.

## Completion criteria

- [ ] Four artifacts at canonical paths
- [ ] Day 30 date set with rationale (e.g. aligned to budget
      cycle)
- [ ] Handoff shortlist has 5-15 items typical
- [ ] City champion path documents the City's actual intake
      mechanism
- [ ] Civic working session plan excludes the City explicitly
- [ ] All artifacts `needs-review` with reviewers named

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Shortlist is empty (no idea cleared IR threshold) | Lower threshold or hand off the highest-scoring tier-B with explicit caveat. The event still produced civic value; the shortlist is one measure, not the only one. |
| City declines to engage with the day-30 announcement | Continue with civic working sessions; document the decline in the lessons log (Skill 18). |
| Working-session capacity exceeds available facilitator bandwidth | Reduce scope or stagger over weeks. Do not run sessions you can't facilitate well. |
| A team objects to their idea being on the shortlist (e.g. wants to commercialize independently) | Remove from shortlist; respect the team's preference. Add to civic working sessions only if the team consents. |
| City champion path conflicts with sponsor expectations of exclusivity | Surface to governance. The open-source default is non-negotiable per the operating principles; sponsorship does not buy exclusivity. |

## Templates used

- See frontmatter.

## Downstream skills

- **17 (OSS Handoff)** consumes `handoff-shortlist.md` and
  `city-champion-path.md` to scope the public marketplace
  listings.
- **18 (Retrospective)** consumes the entire skill output for
  follow-through assessment.

## Example invocation

> "Build the post-event pipeline. Day 30 target: April 28. City
> Hall innovation meeting is May 5; align if possible."

Expected steps:

1. Skill confirms upstream, reads AI eval scorecards.
2. Skill builds handoff-shortlist from IR-tier and judging cross-
   reference.
3. Skill drafts day-30 plan with recipient list from
   `03/decision-maker-map.md`.
4. Skill drafts city-champion-path with intake mechanism.
5. Skill drafts civic-working-session plan with no-City rule.
6. Reports: "16 complete (pending review). Day 30: 2026-04-28
   (aligned with City innovation meeting 2026-05-05). Shortlist:
   12 ideas. Working sessions: 26 ideas, ~7 facilitator-hours."

## Changelog

- 1.0.0 (initial) — First version. Ownership reframed (City is
  given strategic leadership, not given an idea); working
  sessions explicitly exclude the City.
