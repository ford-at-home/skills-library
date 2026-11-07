---
description: "Recruit, onboard, and schedule the two cohorts that make an event"
skill_number: "11"
skill_id: mentor-volunteer-ops
name: Mentor and Volunteer Ops
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 4-8 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/03-stakeholder-map/partner-register.csv
    - artifacts/05-track-strategy/track-list.md
    - artifacts/09-community-outreach-plan/audience-segments.md
    - artifacts/10-participant-experience-plan/participant-journey.md
    - artifacts/10-participant-experience-plan/registration-flow.md
    - artifacts/10-participant-experience-plan/code-of-conduct.md
    - artifacts/10-participant-experience-plan/accessibility-plan.md
  optional: []
outputs:
  - artifacts/11-mentor-volunteer-ops/mentor-roster.csv
  - artifacts/11-mentor-volunteer-ops/mentor-roster.csv.meta.yaml
  - artifacts/11-mentor-volunteer-ops/volunteer-roster.csv
  - artifacts/11-mentor-volunteer-ops/volunteer-roster.csv.meta.yaml
  - artifacts/11-mentor-volunteer-ops/mentor-onboarding.md
  - artifacts/11-mentor-volunteer-ops/volunteer-runbook.md
  - artifacts/11-mentor-volunteer-ops/shift-schedule.md
downstream_skills:
  - 12-event-operations-plan
  - 13-technology-setup
  - 14-judging-system
templates_used:
  - templates/11-mentor-volunteer-ops/mentor-roster.template.csv
  - templates/11-mentor-volunteer-ops/mentor-roster.meta.template.yaml
  - templates/11-mentor-volunteer-ops/volunteer-roster.template.csv
  - templates/11-mentor-volunteer-ops/volunteer-roster.meta.template.yaml
  - templates/11-mentor-volunteer-ops/mentor-onboarding.template.md
  - templates/11-mentor-volunteer-ops/volunteer-runbook.template.md
  - templates/11-mentor-volunteer-ops/shift-schedule.template.md
search_paths:
  - artifacts/11-mentor-volunteer-ops/
  - templates/11-mentor-volunteer-ops/
  - examples/*/11-mentor-volunteer-ops/
  - ../**/mentors*
  - ../**/volunteers*
  - docs/mentors/
  - docs/volunteers/
---

# Skill 11 — Mentor and Volunteer Ops

## Purpose

Recruit, onboard, and schedule the two cohorts that make an event
function: subject-matter mentors (who help teams) and operations
volunteers (who help the event).

Five artifacts:

1. **`mentor-roster.csv`** — confirmed mentors with expertise,
   track preferences, shift availability.
2. **`volunteer-roster.csv`** — confirmed volunteers with roles
   and shifts.
3. **`mentor-onboarding.md`** — what mentors need to know before
   day 1.
4. **`volunteer-runbook.md`** — per-role task and escalation
   guide.
5. **`shift-schedule.md`** — the master schedule that resolves
   both rosters into time blocks.

## When to use

- Once the participant journey (Skill 10) is stable
- 4-6 weeks before the event for mentor recruitment
- 2-4 weeks before the event for volunteer scheduling

## Who should use it

Mentor lead + volunteer coordinator + operations lead. The agent
drafts onboarding and runbook content; humans recruit.

## Prerequisites

**Required:** all listed above. Notably, the code of conduct must
be at `needs-review` (or higher) because every mentor and volunteer
agrees to it during onboarding.

## Inputs

- Upstream artifacts
- The partnership-asks list (mentors often come from sponsor
  companies as in-kind contribution)
- Prior-event mentor and volunteer rosters

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `mentor-roster.csv` | `needs-review` | yes |
| `volunteer-roster.csv` | `needs-review` | yes |
| `mentor-onboarding.md` | `draft` | no |
| `volunteer-runbook.md` | `draft` | no |
| `shift-schedule.md` | `draft` | no |

## Search behavior

1. `artifacts/11-mentor-volunteer-ops/*` — existing?
2. `templates/11-mentor-volunteer-ops/*` — load.
3. `examples/*/11-mentor-volunteer-ops/*` — reference.
4. Parent repo for mentor / volunteer rosters from prior events.
5. `03/partner-register.csv` filtered to people with mentor-able
   expertise.

## Validation behavior

Run the five blocks. Additional:

- Every confirmed mentor must be in `03/partner-register.csv`.
- Every shift in `shift-schedule.md` must have a named owner from
  one of the rosters.
- Every mentor's track preference must be a track in
  `05/track-list.md`.
- `mentor-onboarding.md` and `volunteer-runbook.md` must
  reference `10/code-of-conduct.md`.

## Normalization behavior

Prior-year rosters are useful contact starts; every name needs
re-confirmation. Status starts at `stale` until the mentor /
volunteer confirms.

For mentors sourced from sponsor companies, the sponsor's HR /
ops lead confirms participation; one company may provide multiple
mentors via a single point of contact.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Build mentor roster.** For each mentor:
   - name, organization, expertise, track preference, shift
     availability, contact, status
3. **Build volunteer roster.** For each volunteer:
   - name, role (greeter, runner, AV, photo, judging support,
     etc.), shift, contact, status
4. **Draft mentor onboarding.** Cover:
   - What mentoring is and is not (advice, not building)
   - Code of conduct (reference, don't duplicate)
   - How mentors get matched to teams (via Slack, walk-up,
     scheduled hour blocks)
   - Sign-out / shift handoff
5. **Draft volunteer runbook.** One section per volunteer role.
   For each: tasks, escalation, handoff procedure.
6. **Build shift schedule.** Resolve both rosters into time
   blocks across the three days. Identify gaps and named backups.
7. **Cross-check.** Every track has at least one mentor
   available during peak hacking hours. Every critical role has
   a primary and a backup.
8. **Report.**

## User interaction rules

- Mentor expertise must be specific. "Software" is too vague;
  "Python data engineering for civic open data" is useful.
- Shift availability comes from the person, not the coordinator's
  guess. Confirm directly.
- Volunteers covering critical roles (medical-incident lead,
  reporting channel for CoC issues) must be named individually
  and trained. Do not put generic volunteers on those roles.

## Completion criteria

- [ ] Five artifacts at canonical paths (or 7 incl. sidecars)
- [ ] Each roster has confirmed entries (not just prospects)
- [ ] Onboarding and runbook reference the CoC
- [ ] Shift schedule has no unfilled critical slots
- [ ] Every shift has a backup or an accepted-risk note

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Not enough confirmed mentors | Surface to Skill 08 (sponsor partnership asks) and Skill 09 (outreach) to request more. Track committees may also recruit directly. |
| A track has no mentor coverage | The track is at risk. Either find a mentor or warn participants of the gap in advance. |
| Volunteer role is unfilled close to event | Either drop the role (and update the journey) or pull from a friends-and-family list. Do not run the event with critical roles uncovered. |
| Mentor expertise is generic ("software") | Push back; ask the mentor to specify a subdomain. If unwilling, mark generic and use as float capacity rather than track-anchored. |
| Sponsor pulls a mentor commitment late | Loop to Skill 08 for replacement. The mentor's slot is vacant until refilled. |

## Templates used

- See frontmatter `templates_used` list.

## Downstream skills

- **12 (Event Ops)** integrates the shift schedule into the
  run-of-show.
- **13 (Tech Setup)** uses the mentor roster to populate
  mentor-help Slack channels.
- **14 (Judging)** uses the mentor list to recruit judges from
  domain experts.

## Example invocation

> "Build mentor and volunteer ops. Last year's rosters are at
> [path]. Sponsors providing mentors: [list]."

Expected steps:

1. Skill normalizes prior rosters at `stale`; user confirms each.
2. Skill builds shift schedule from the rosters and the run-of-
   show draft.
3. Skill flags 2 unfilled critical volunteer roles.
4. Skill writes artifacts.
5. Reports: "11 complete (pending confirmations). 18 mentors
   confirmed (target 25). 2 critical volunteer slots open."

## Changelog

- 1.0.0 (initial) — First version. Critical-slot identification;
  no-generic-experts rule.
