---
description: "Design what a participant actually goes through: register, arrive,"
skill_number: "10"
skill_id: participant-experience-plan
name: Participant Experience Plan
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 4-8 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/02-event-charter/event-charter.md
    - artifacts/02-event-charter/operating-principles.md
    - artifacts/02-event-charter/scope-boundaries.md
    - artifacts/06-problem-statement-development/final-problem-statements.md
    - artifacts/06-problem-statement-development/track-context-briefs.md
    - artifacts/09-community-outreach-plan/audience-segments.md
  optional: []
outputs:
  - artifacts/10-participant-experience-plan/participant-journey.md
  - artifacts/10-participant-experience-plan/registration-flow.md
  - artifacts/10-participant-experience-plan/code-of-conduct.md
  - artifacts/10-participant-experience-plan/accessibility-plan.md
downstream_skills:
  - 11-mentor-volunteer-ops
  - 12-event-operations-plan
  - 13-technology-setup
  - 14-judging-system
  - 17-open-source-handoff
templates_used:
  - templates/10-participant-experience-plan/participant-journey.template.md
  - templates/10-participant-experience-plan/registration-flow.template.md
  - templates/10-participant-experience-plan/code-of-conduct.template.md
  - templates/10-participant-experience-plan/accessibility-plan.template.md
search_paths:
  - artifacts/10-participant-experience-plan/
  - templates/10-participant-experience-plan/
  - examples/*/10-participant-experience-plan/
  - ../**/code-of-conduct*
  - ../**/COC*
  - ../**/registration*
  - ../**/accessibility*
  - docs/participant/
---

# Skill 10 — Participant Experience Plan

## Purpose

Design what a participant actually goes through: register, arrive,
form a team, pick a track, hack, demo, leave. Plus the legal and
accessibility surface that protects the people doing it.

Four artifacts:

1. **`participant-journey.md`** — the end-to-end experience from
   discovery through post-event.
2. **`registration-flow.md`** — the mechanics: team-lead vs.
   individual, pricing, no-show mitigation, accommodations.
3. **`code-of-conduct.md`** — prohibited conduct, reporting,
   enforcement. **Legal review required.**
4. **`accessibility-plan.md`** — physical, dietary, language, and
   sensory access.

## When to use

- After Skill 06 (statements stable enough that the journey can
  reference them) and Skill 09 (audience segments defined)
- 6-10 weeks before the event for the participant-facing surface
  (registration, code of conduct)

## Who should use it

Operations lead + executive lead + a participant-experience
advocate (often a prior participant). Legal counsel for the code
of conduct.

## Prerequisites

**Required:** all listed above. The participant journey cannot be
designed without knowing what the event is for (charter), what
they will work on (problem statements), and who they are (audience
segments).

## Inputs

- Upstream artifacts
- Prior code of conduct (any reputable event's CoC is a starting
  point; Berlin Code of Conduct, Contributor Covenant, etc.)
- Prior registration data if available
- Accessibility input from local disability advocates if accessible

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `participant-journey.md` | `draft` | optional |
| `registration-flow.md` | `needs-review` | yes |
| `code-of-conduct.md` | `needs-review` | yes (legal) |
| `accessibility-plan.md` | `needs-review` | yes |

## Search behavior

1. `artifacts/10-participant-experience-plan/*` — existing?
2. `templates/10-participant-experience-plan/*` — load.
3. `examples/*/10-participant-experience-plan/*` — reference.
4. Parent repo for `code-of-conduct*`, `COC*`,
   `registration*`, `accessibility*`.
5. Reputable external code-of-conduct templates (Contributor
   Covenant, Berlin CoC) — note as source, do not copy verbatim
   into the artifact without confirming applicability.
6. User-supplied content.

## Validation behavior

Run the four blocks. Additional:

- `code-of-conduct.md` cannot reach `approved` without
  `approved_by` naming legal counsel
- `registration-flow.md` must state the refund policy
- `accessibility-plan.md` must name an accessibility contact

## Normalization behavior

External CoC templates (Contributor Covenant) are widely used and
legally vetted, but require local-context adaptation (named
enforcement parties, reporting channels). Normalize the structure;
the body needs review.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Draft the participant journey.** A timeline:
   - Discovery (Skill 09 channels)
   - Registration
   - Pre-event comms (Slack invite, kickoff materials)
   - Arrival (Friday)
   - Team formation
   - Track / problem statement selection
   - Hacking (Saturday)
   - Demo prep (late Saturday / Sunday morning)
   - Demo and judging (Sunday)
   - Closing event
   - Post-event follow-up
3. **For each step**, note: what the participant does, what the
   organizers do, what friction exists, what the mitigation is.
4. **Draft the registration flow.** Include:
   - Individual vs. team-lead registration
   - Pricing structure (or free, with rationale)
   - No-show mitigation (paywall? deposit? confirmation?)
   - Refund policy
   - Accessibility accommodations request
   - Slack invite trigger
   - Code-of-conduct acknowledgement
5. **Draft the code of conduct.** Working with legal counsel:
   - Prohibited conduct (harassment, discrimination, etc.)
   - Reporting channel (named individual or email)
   - Enforcement process (warning, removal, ban)
   - Conflict-of-interest disclosures
6. **Draft the accessibility plan.** Address:
   - Physical (mobility, sensory)
   - Dietary
   - Language (if relevant to local population)
   - Quiet space
   - Childcare or family considerations
   - Named accessibility contact
7. **Write artifacts.**
8. **Report.**

## User interaction rules

- The CoC is not boilerplate. Do not paste an external template
  without naming local enforcement parties.
- Refund policy: explicit. "No refunds" is a valid policy; "we'll
  figure it out" is not.
- Paywall rationale: if pricing is intended for no-show mitigation
  rather than revenue, say so plainly in `registration-flow.md`.
  The Richmond year-1 lesson is that paywall is a calibration tool
  for capacity estimation; reasonable to use, important to be
  honest about.
- Accessibility: budget reality is acceptable to acknowledge, but
  the plan should name what is and is not provided. "Best effort"
  is not enough.

## Completion criteria

- [ ] Four artifacts at canonical paths
- [ ] Journey maps every step from discovery to post-event
- [ ] Registration flow states pricing and refund policy
- [ ] CoC has reporter, responder, and enforcement chain
- [ ] CoC has legal review owner named
- [ ] Accessibility plan names a contact

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| No legal counsel available for CoC | Stop. CoC stays at `draft`. Recruiting counsel is a Skill 04 / Skill 03 task. Do not publish a CoC without legal sign-off. |
| Refund policy not yet decided | Allow `draft` but force a target date for resolution. |
| Accessibility ask exceeds budget | Document explicitly what is and is not provided. Honesty beats overpromise. |
| Team-lead vs. individual registration introduces deduplication problems | Document the reconciliation process (e.g. Slack channel) in `registration-flow.md`. Surface to Skill 13 (tech setup). |
| Paywall introduces equity concern | Acknowledge in `accessibility-plan.md`; provide scholarship or fee-waiver path; document in registration flow. |

## Templates used

- `templates/10-participant-experience-plan/participant-journey.template.md`
- `templates/10-participant-experience-plan/registration-flow.template.md`
- `templates/10-participant-experience-plan/code-of-conduct.template.md`
- `templates/10-participant-experience-plan/accessibility-plan.template.md`

## Downstream skills

- **11 (Mentor/Volunteer)** uses CoC and accessibility plan.
- **12 (Event Ops)** uses the journey to design the run-of-show.
- **13 (Tech Setup)** uses the registration flow.
- **14 (Judging)** uses the journey to plan the demo / judging
  block.
- **17 (OSS Handoff)** uses the CoC for the contributor guide.

## Example invocation

> "Plan participant experience. The event is 3 days, in-person,
> with a paywall for no-show mitigation. Legal counsel is [name]."

Expected steps:

1. Skill reads upstream.
2. Skill drafts the journey with the user.
3. Skill drafts registration flow including paywall rationale.
4. Skill drafts CoC stub for legal review.
5. Skill drafts accessibility plan with named contact.
6. Reports: "10 complete (pending review and legal). 1 known
   accessibility gap (language access) — flagged."

## Changelog

- 1.0.0 (initial) — First version. Legal-sign-off gate on CoC;
  paywall framed as no-show mitigation tool per Richmond year-1
  experience.
