---
description: "Resolve everything upstream into the operational artifacts the"
skill_number: "12"
skill_id: event-operations-plan
name: Event Operations Plan
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 6-10 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/02-event-charter/event-charter.md
    - artifacts/02-event-charter/operating-principles.md
    - artifacts/08-partnership-and-sponsor-plan/sponsor-tier-structure.md
    - artifacts/08-partnership-and-sponsor-plan/sponsor-pipeline.csv
    - artifacts/08-partnership-and-sponsor-plan/partnership-asks.md
    - artifacts/08-partnership-and-sponsor-plan/fiscal-sponsor-agreement.md
    - artifacts/09-community-outreach-plan/outreach-plan.md
    - artifacts/09-community-outreach-plan/outreach-calendar.md
    - artifacts/10-participant-experience-plan/participant-journey.md
    - artifacts/10-participant-experience-plan/registration-flow.md
    - artifacts/10-participant-experience-plan/code-of-conduct.md
    - artifacts/10-participant-experience-plan/accessibility-plan.md
    - artifacts/11-mentor-volunteer-ops/mentor-roster.csv
    - artifacts/11-mentor-volunteer-ops/volunteer-roster.csv
    - artifacts/11-mentor-volunteer-ops/shift-schedule.md
  optional: []
outputs:
  - artifacts/12-event-operations-plan/run-of-show.md
  - artifacts/12-event-operations-plan/venue-plan.md
  - artifacts/12-event-operations-plan/safety-plan.md
  - artifacts/12-event-operations-plan/comms-tree.md
  - artifacts/12-event-operations-plan/incident-response.md
downstream_skills:
  - 13-technology-setup
  - 14-judging-system
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/12-event-operations-plan/run-of-show.template.md
  - templates/12-event-operations-plan/venue-plan.template.md
  - templates/12-event-operations-plan/safety-plan.template.md
  - templates/12-event-operations-plan/comms-tree.template.md
  - templates/12-event-operations-plan/incident-response.template.md
search_paths:
  - artifacts/12-event-operations-plan/
  - templates/12-event-operations-plan/
  - examples/*/12-event-operations-plan/
  - ../**/run-of-show*
  - ../**/venue*
  - ../**/safety*
  - docs/operations/
---

# Skill 12 — Event Operations Plan

## Purpose

Resolve everything upstream into the operational artifacts the
event runs on. Run-of-show, venue plan, safety plan, comms tree,
incident response.

This skill has the largest required-prerequisite surface in the
plugin (15 inputs). That is by design: event ops cannot fudge any
of them.

Five artifacts:

1. **`run-of-show.md`** — minute-by-minute agenda for all three
   days plus setup and teardown.
2. **`venue-plan.md`** — room assignments, capacities, AV,
   connectivity.
3. **`safety-plan.md`** — emergency contacts, evacuation, medical
   incidents. **Legal review required.**
4. **`comms-tree.md`** — escalation hierarchy during the event.
5. **`incident-response.md`** — incident categories, reporter /
   responder / decider for each. **Legal review required.**

## When to use

- 4-6 weeks before the event, once all upstream is at `draft` or
  higher
- Final pass 1 week before the event with the venue walkthrough
- Day-of has a live update permitted (frozen state captured in
  pre-event `approved` version + a `delta-log.md` for day-of
  changes)

## Who should use it

Operations lead + executive lead + venue contact + safety contact
+ comms lead. Legal counsel for safety and incident response.

## Prerequisites

**Required:** all 15 upstream artifacts listed above. This is the
convergence skill; if any are missing, stop.

Practically: this skill will block more often than any other skill
in the plugin. That is correct behavior.

## Inputs

- Upstream artifacts (15 of them)
- Venue contract / floor plan
- Any local code or insurance requirements for the venue
- Prior-event run-of-show, if available

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `run-of-show.md` | `needs-review` | yes |
| `venue-plan.md` | `needs-review` | yes |
| `safety-plan.md` | `needs-review` | yes (legal) |
| `comms-tree.md` | `draft` | no |
| `incident-response.md` | `needs-review` | yes (legal) |

## Search behavior

1. `artifacts/12-event-operations-plan/*` — existing?
2. `templates/12-event-operations-plan/*` — load.
3. `examples/*/12-event-operations-plan/*` — reference.
4. Parent repo for `run-of-show*`, `venue*`, `safety*`.
5. User-supplied content (venue contract, floor plan).

## Validation behavior

Run all five blocks. Additional:

- Every minute in `run-of-show.md` has an owner.
- Every room in `venue-plan.md` lists capacity and AV.
- `safety-plan.md` and `incident-response.md` cannot reach
  `approved` without legal counsel review.
- `comms-tree.md` has after-hours contacts.

## Normalization behavior

Prior run-of-show: high-value source. Normalize the structure and
adjust times. Do not carry over assumptions about staffing or
venue without re-confirming.

Safety and incident-response: do not normalize from another
event's artifact without legal review. The legal landscape may
differ.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Draft run-of-show.** Walk all three days plus setup and
   teardown:
   - Friday: setup → registration → kickoff → team formation →
     track breakouts → start of hacking
   - Saturday: open hacking with mentor windows, meals,
     check-ins, evening
   - Sunday: morning prep → demos → judging deliberation →
     awards → closing → teardown
3. **Map run-of-show to shift schedule.** Every block in the
   run-of-show should reference at least one shift owner.
4. **Draft venue plan.** Room by room:
   - capacity
   - AV (mics, projectors, screens, recording)
   - power and connectivity
   - signage
   - accessibility per `10/accessibility-plan.md`
5. **Draft safety plan** with legal:
   - Emergency contacts (911 plus local)
   - Evacuation routes
   - Medical incident procedure (first aid kits, AED locations,
     trained personnel)
   - Severe weather procedure
6. **Draft comms tree.** During-event escalation:
   - Floor volunteer → role lead → operations lead → executive
     lead
   - Off-hours: named contacts with phone numbers
7. **Draft incident response** with legal:
   - Incident categories (safety, conduct, technical, IP, press)
   - For each: reporter (who can report), responder (who acts),
     decider (who decides outcome)
   - Reference `10/code-of-conduct.md` for CoC incidents
8. **Cross-check.** Run-of-show times align with venue
   availability; shift schedule covers all open hours; comms
   tree resolves through to the executive lead.
9. **Report.**

## User interaction rules

- The run-of-show is not approximate. Every block has a time and
  an owner.
- The safety plan and incident response require legal review.
  The skill writes the structure; counsel writes the binding
  language.
- Comms tree must extend to after-hours. A 3 AM medical issue
  during Saturday's overnight hacking has to reach a real human
  fast.
- If the venue contact has constraints (no overnight access,
  specific AV requirements), those are part of the venue plan —
  do not assume.

## Completion criteria

- [ ] Five artifacts at canonical paths
- [ ] Run-of-show covers every minute from setup through teardown
- [ ] Every run-of-show block has an owner
- [ ] Venue plan covers every room with capacity and AV
- [ ] Safety plan has legal owner named
- [ ] Comms tree extends to after-hours
- [ ] Incident response has reporter/responder/decider for every
      category

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Venue contract not yet signed | Cannot reach `approved`. `venue-plan.md` stays `draft` until contract executes. Run-of-show may be drafted with provisional venue, with venue dependencies flagged. |
| Legal counsel unavailable | Safety and incident-response artifacts stay `needs-review`. The event organizer accepts personal risk by running without legal sign-off; document explicitly. |
| Shift schedule has gaps | Loop to Skill 11. Run-of-show cannot finalize over gaps. |
| Run-of-show overruns realistic times | Compress agenda. Skill 02 (charter) may need to update scope. |
| Sponsor commitment changes affecting venue / food / AV | Loop to Skill 08. Update partnership-asks. Run-of-show updates accordingly. |
| Day-of change needed | Add to a `delta-log.md` inside this artifact directory; do not rewrite the frozen `approved` artifact mid-event. |

## Templates used

- `templates/12-event-operations-plan/run-of-show.template.md`
- `templates/12-event-operations-plan/venue-plan.template.md`
- `templates/12-event-operations-plan/safety-plan.template.md`
- `templates/12-event-operations-plan/comms-tree.template.md`
- `templates/12-event-operations-plan/incident-response.template.md`

## Downstream skills

- **13 (Tech Setup)** consumes run-of-show, venue plan, comms tree.
- **14 (Judging)** consumes run-of-show (specifically the
  judging / demo / awards blocks).
- **18 (Retrospective)** consumes the run-of-show to compare
  planned vs. actual.

## Example invocation

> "Build the event ops plan. Venue is VCU Snead Hall, contract
> signed, legal counsel is [name]."

Expected steps:

1. Skill confirms 15 upstream artifacts present.
2. Skill drafts run-of-show by reading the journey, shift
   schedule, and outreach calendar.
3. Skill drafts venue plan from the floor plan.
4. Skill drafts safety / incident stubs for legal review.
5. Skill writes comms tree.
6. Reports: "12 complete (pending review and legal). Run-of-show
   has 1 unowned 30-min block (Saturday dinner) — flagged."

## Changelog

- 1.0.0 (initial) — First version. Largest prerequisite surface
  in the plugin by design. Legal-sign-off gate on safety and
  incident-response.
