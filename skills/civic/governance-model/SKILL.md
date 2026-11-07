---
description: "Define how the event is governed: the organizing body's structure,"
skill_number: "04"
skill_id: governance-model
name: Governance Model
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 1-3 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/02-event-charter/event-charter.md
    - artifacts/02-event-charter/operating-principles.md
    - artifacts/03-stakeholder-map/stakeholder-map.md
    - artifacts/03-stakeholder-map/partner-register.csv
  optional:
    - artifacts/03-stakeholder-map/decision-maker-map.md
outputs:
  - artifacts/04-governance-model/governance-model.md
  - artifacts/04-governance-model/track-committee-roster.md
  - artifacts/04-governance-model/decision-rights-matrix.md
downstream_skills:
  - 05-track-strategy
  - 06-problem-statement-development
  - 07-data-readiness
  - 14-judging-system
  - 16-post-event-pipeline
  - 17-open-source-handoff
templates_used:
  - templates/04-governance-model/governance-model.template.md
  - templates/04-governance-model/track-committee-roster.template.md
  - templates/04-governance-model/decision-rights-matrix.template.md
search_paths:
  - artifacts/04-governance-model/
  - templates/04-governance-model/
  - examples/*/04-governance-model/
  - ../**/governance*.md
  - ../**/committee*.md
  - ../**/3C*.md
  - docs/governance/
---

# Skill 04 — Governance Model

## Purpose

Define how the event is governed: the organizing body's structure,
per-track committees, and the decision-rights matrix that says who
decides what.

Civic hackathons fail when no one knows who can sign off on a
sponsor deal, who picks the judging rubric, or who can speak for the
event publicly. This skill is the antidote.

Three artifacts:

1. **`governance-model.md`** — the organizing body's structure,
   meeting cadence, and decision-making process.
2. **`track-committee-roster.md`** — for each track, the committee
   that owns it (typically: a civic partner, a city ally, and an
   organizing-team lead — the "3C" pattern in the Richmond example).
3. **`decision-rights-matrix.md`** — for each decision domain,
   exactly one decider, plus recommenders and informed parties.

## When to use

- Immediately after Skill 03
- When a decision-rights conflict appears (two people claim
  authority over the same domain)
- When a new track is added or removed
- When the organizing team changes composition mid-cycle

## Who should use it

The executive lead and the city-side liaison. This is the most
politically delicate skill in the pre-event arc; the agent's role is
to record clearly, not to mediate.

## Prerequisites

**Required:**

- `02/event-charter.md`, `02/operating-principles.md`
- `03/stakeholder-map.md`, `03/partner-register.csv`

If `decision-maker-map.md` from Skill 03 already exists at `draft` or
higher, **read it first** — it is the rough version of this skill's
`decision-rights-matrix.md`, and the goal is to elevate it to a
formal artifact.

## Inputs

- Upstream artifacts
- The user's knowledge of the organizing body's structure
- Any prior governance documents (bylaws, committee charters)

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `governance-model.md` | `needs-review` | yes |
| `track-committee-roster.md` | `needs-review` | yes |
| `decision-rights-matrix.md` | `needs-review` | yes |

## Search behavior

1. `artifacts/04-governance-model/*` — existing?
2. `templates/04-governance-model/*` — load.
3. `examples/*/04-governance-model/*` — reference.
4. Parent repo for `governance*.md`, `committee*.md`, `3C*.md`,
   bylaws, prior charters.
5. User-supplied content.

## Validation behavior

Run the three artifacts' validation blocks. Additional checks:

- Every track that exists (per `03/partner-register.csv`'s
  `pillar_or_track` column, if present) has a committee in
  `track-committee-roster.md`. If tracks are not yet finalized
  (Skill 05), allow `track-committee-roster.md` to list "expected
  tracks" with a forward reference to Skill 05.
- The decision-rights matrix has **exactly one** decider per
  domain. Multiple deciders is a validation failure.
- Every named person in the governance model and committee roster
  is in `partner-register.csv`.

## Normalization behavior

If the user has a prior governance doc, normalize per the guide.
Watch for: bylaws written for a different event scale, committee
structures inherited from a prior org that don't match current
team composition, decision-rights language borrowed from corporate
templates that doesn't translate to volunteer-led work.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Draft the governance model.** Capture:
   - The organizing body's name (or "ad hoc")
   - Reporting structure (who reports to whom, if applicable)
   - Meeting cadence (weekly steering, monthly all-hands, etc.)
   - Decision-making process (consensus, majority, executive lead's
     call, sponsor sign-off)
3. **Draft the track-committee roster.** For each expected track,
   list:
   - Track name
   - Committee lead (organizing-team member)
   - Civic partner(s) (from `partner-register.csv`)
   - City ally (from `partner-register.csv`)
   - Optional: capacity partner / sponsor
   - Meeting cadence for the committee
4. **Draft the decision-rights matrix.** Domains to cover at
   minimum:
   - Civic alignment (decider typically: city-side liaison)
   - Event scope and dates (decider: executive lead)
   - Sponsor commitments (decider: partnership lead or exec)
   - Track selection (decider: governance body collectively)
   - Problem statement approval (decider: track committee)
   - Judging rubric (decider: governance body or judging lead)
   - Judge selection (decider: judging lead)
   - Award decisions (decider: judges, by process defined in
     judging runbook)
   - Public communications (decider: comms lead or exec)
   - Legal sign-off (decider: legal counsel; no other defaults)
   - Technology choices (decider: tech lead)
   - Code-of-conduct enforcement (decider: defined in CoC artifact)
5. **Cross-check.** No domain has two deciders. Every decider is in
   `partner-register.csv`. Every track is covered.
6. **Write artifacts** at `needs-review`.
7. **Report.**

## User interaction rules

- The single-decider rule is non-negotiable. If the team insists on
  shared authority for a domain, ask them to name the tiebreaker.
  The tiebreaker is the decider.
- If the user is uncomfortable naming a decider for a politically
  charged domain (e.g. award decisions), do not paper over it.
  Surface the discomfort and ask the team to resolve.
- The governance model can describe consensus or majority-rule
  processes, but for the decision-rights matrix, the buck has to
  stop somewhere.

## Completion criteria

- [ ] Three artifacts at canonical paths
- [ ] Every track has a committee with at least one civic partner,
      one city ally, and one organizing-team lead (the 3C pattern,
      or equivalent)
- [ ] Every decision domain has exactly one decider
- [ ] Every named person is in `partner-register.csv`
- [ ] All three artifacts at `needs-review` with reviewer named

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Track committee can't find a city ally | Loop back to Skill 03 to identify a city contact. Skill 04 cannot proceed for that track until an ally is named. |
| Two people claim the same decision domain | Stop. Surface to the governance body. The matrix cannot be `needs-review` with the conflict unresolved. |
| Capacity / sponsor role for a committee is unfilled | Allow as optional. Note in `open_questions` for Skill 08 to track. (Richmond's year-1 experience: the "Capacity" seat was often unfilled and that was acceptable; the C of city + civic is the load-bearing pair.) |
| Decision-making process is "exec decides everything" | Acceptable for small events but flag the risk to the user — this concentrates burnout. |
| User cannot name a legal sign-off decider | Status: `blocked`. Legal review cannot be self-assigned. The team must find counsel or formally accept the risk. |

## Templates used

- `templates/04-governance-model/governance-model.template.md`
- `templates/04-governance-model/track-committee-roster.template.md`
- `templates/04-governance-model/decision-rights-matrix.template.md`

## Downstream skills

- **05 (Track Strategy)** uses `track-committee-roster.md` to
  confirm the proposed tracks are actually staffable.
- **06 (Problem Statements)** uses the committee roster as the
  authors of statements.
- **07, 14, 16, 17** use `decision-rights-matrix.md` to know who to
  ask when their own artifacts need sign-off.

## Example invocation

> "Define the governance model. We're using the 3C pattern (city,
> civic, capacity) per the Richmond example. The committee roster
> is provisional until Skill 05 finalizes tracks."

Expected steps:

1. Skill reads upstream, confirms charter and stakeholder map.
2. Skill drafts governance model based on the team's structure.
3. Skill drafts a provisional committee roster keyed to the
   expected (not yet final) track list.
4. Skill walks the decision-rights matrix domain by domain.
5. Skill writes artifacts at `needs-review`.

## Changelog

- 1.0.0 (initial) — First version. Enforces single-decider per
  domain; allows optional capacity seats per Richmond year-1
  experience.
