---
description: "Plan and stage the public communications that bring participants,"
skill_number: "09"
skill_id: community-outreach-plan
name: Community Outreach Plan
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 6-12 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/02-event-charter/event-charter.md
    - artifacts/02-event-charter/scope-boundaries.md
    - artifacts/03-stakeholder-map/stakeholder-map.md
    - artifacts/03-stakeholder-map/partner-register.csv
    - artifacts/05-track-strategy/final-track-strategy.md
    - artifacts/05-track-strategy/track-rationale.md
    - artifacts/06-problem-statement-development/final-problem-statements.md
    - artifacts/06-problem-statement-development/track-context-briefs.md
    - artifacts/08-partnership-and-sponsor-plan/sponsor-tier-structure.md
    - artifacts/08-partnership-and-sponsor-plan/partnership-asks.md
  optional: []
outputs:
  - artifacts/09-community-outreach-plan/outreach-plan.md
  - artifacts/09-community-outreach-plan/audience-segments.md
  - artifacts/09-community-outreach-plan/outreach-calendar.md
  - artifacts/09-community-outreach-plan/outreach-messages/README.md
downstream_skills:
  - 10-participant-experience-plan
  - 11-mentor-volunteer-ops
  - 12-event-operations-plan
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/09-community-outreach-plan/outreach-plan.template.md
  - templates/09-community-outreach-plan/audience-segments.template.md
  - templates/09-community-outreach-plan/outreach-calendar.template.md
  - templates/09-community-outreach-plan/outreach-message.template.md
search_paths:
  - artifacts/09-community-outreach-plan/
  - templates/09-community-outreach-plan/
  - examples/*/09-community-outreach-plan/
  - ../**/outreach/
  - ../**/kickoff-emails/
  - ../**/marketing*
  - docs/comms/
---

# Skill 09 — Community Outreach Plan

## Purpose

Plan and stage the public communications that bring participants,
mentors, and judges to the event. Without this, the charter is
private and the event empty.

Four artifacts:

1. **`outreach-plan.md`** — the overall strategy: who, what, when,
   how, owned by whom.
2. **`audience-segments.md`** — each audience the plan addresses,
   with characteristics and channels.
3. **`outreach-calendar.md`** — week-by-week schedule of outbound
   activity.
4. **`outreach-messages/`** — a folder of message drafts (kickoff
   email per track, social posts, partner emails, press release).

## When to use

- Once tracks, problem statements, and sponsor structure are
  stable enough that the message can be true
- 8-12 weeks before the event for the launch announcement
- Continuously thereafter until the event

## Who should use it

Comms lead + executive lead + each track committee (for
track-specific outreach). The agent can draft messages but a human
must approve every public send.

## Prerequisites

**Required:** all listed above. Skill 09 has the largest required
prerequisite surface in the pre-event arc — outreach cannot be
written until tracks, problem statements, and sponsor identity are
all stable.

## Inputs

- Upstream artifacts
- Audience knowledge: who in the city responds to which channels
- Prior-year outreach (if any) — kickoff emails, social posts,
  press coverage

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `outreach-plan.md` | `needs-review` | yes |
| `audience-segments.md` | `draft` | no |
| `outreach-calendar.md` | `draft` | no |
| `outreach-messages/` (folder) | varies | yes (every send) |

## Search behavior

1. `artifacts/09-community-outreach-plan/*` — existing?
2. `templates/09-community-outreach-plan/*` — load.
3. `examples/*/09-community-outreach-plan/*` — reference.
4. Parent repo:
   - `kickoff-emails/` — prior-event launch emails per track;
     extremely high-value source for tone and structure
   - `outreach/` — pre-event outreach to civic partners and SMEs
   - any marketing or press archive
5. User-supplied content.

## Validation behavior

Run the four artifact blocks. Additional:

- Every audience segment in `audience-segments.md` has at least
  one channel and one message in `outreach-messages/` that targets
  it
- Every track in `track-list.md` has a kickoff message in
  `outreach-messages/`
- Every outbound activity in the calendar has an owner

## Normalization behavior

Prior-year kickoff emails are gold for the
`outreach-messages/` folder. Normalize by track, treating the
prior emails as drafts that need this year's content. Preserve the
prior structure (which has been externally tested) and update
specifics.

Do not normalize sponsor logos or testimonials without explicit
permission from the sponsor.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Define audience segments.** Walk the user through:
   - Civic technologists (developers, designers, PMs)
   - Civic-minded non-technical residents
   - Students (CS, design, public policy, urban planning)
   - City employees
   - Subject-matter mentors
   - Press / media
   - Potential judges
   - Sponsors (current and prospective)
   - Prior participants
3. **For each segment**, capture: size estimate, characteristics,
   what they care about, where they are reachable (channel), the
   message frame that resonates.
4. **Build the calendar.** Week-by-week schedule of:
   - Launch announcement
   - Track-specific kickoff emails
   - Sponsor announcements
   - Registration push waves
   - Mentor / judge recruitment
   - Final reminders
   - Day-of comms
5. **Draft messages.** Use templates for: launch email, track
   kickoff, sponsor recruitment, mentor recruitment, judge
   invitation, registration nudge, day-of welcome.
6. **Cross-check.** Every track has a kickoff message; every
   sponsor tier benefit (logo, mention) appears in at least one
   scheduled message.
7. **Write artifacts.** Each message in `outreach-messages/`
   carries its own frontmatter with `status: draft` and
   `human_review_required: true`.
8. **Report.**

## User interaction rules

- Outreach messages that mention named individuals, sponsors, or
  the city require those parties' approval before send. The
  artifact's status remains `needs-review` until that approval is
  on file.
- Tone discipline: messages should match the event's brand and the
  audience's expectations. The agent should not adopt slang or
  marketing voice unless the comms lead has approved it.
- Channel choice is the user's call. The agent should not insist
  on Twitter/X if the user knows the city responds to LinkedIn or
  email.

## Completion criteria

- [ ] Four artifacts (or message folder) at canonical paths
- [ ] Every audience has a message
- [ ] Every track has a kickoff message
- [ ] Calendar covers from launch to day-of
- [ ] Every message has an owner and an approval status

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Sponsor logo not yet approved | Hold the sponsor-bearing messages at `draft` until approval. Send unsponsored versions if timing requires. |
| Audience segment has no obvious channel | Add as an `open_question` for the comms lead. Some segments may not be reachable cost-effectively; the segment may need to drop. |
| A track's kickoff message can't be drafted because the problem statements are too vague | Loop back to Skill 06. The outreach is downstream of the statements. |
| City sponsor objects to a public claim | Revise; surface the objection to governance if persistent. The City's voice has veto over event-related public statements involving them. |
| Translation needs (language access) emerge | Add as an `open_question` cross-referenced to Skill 10's accessibility plan. |

## Templates used

- `templates/09-community-outreach-plan/outreach-plan.template.md`
- `templates/09-community-outreach-plan/audience-segments.template.md`
- `templates/09-community-outreach-plan/outreach-calendar.template.md`
- `templates/09-community-outreach-plan/outreach-message.template.md`

## Downstream skills

- **10 (Participant Experience)** uses audience segments to design
  the journey.
- **11 (Mentor/Volunteer)** uses mentor and volunteer recruitment
  messages.
- **12 (Event Ops)** uses the calendar to align day-of comms.
- **18 (Retrospective)** uses the calendar to assess channel
  effectiveness.

## Example invocation

> "Plan outreach. Tracks are finalized; sponsors have a tier
> structure. Source material: `2026-annual-hackathon/kickoff-
> emails/` (last year's per-track emails)."

Expected steps:

1. Skill normalizes the seven prior-year kickoff emails into
   `outreach-messages/kickoff-<track>.md`, each as a draft for
   this year.
2. Skill walks audience segments with the user.
3. Skill builds the calendar.
4. Skill drafts the launch announcement.
5. Reports: "09 complete (pending review). 7 track kickoffs
   drafted. 4 segments missing channels — flagged. Launch
   announcement awaits city sponsor approval."

## Changelog

- 1.0.0 (initial) — First version. Per-message frontmatter; explicit
  sponsor-approval gate before send.
