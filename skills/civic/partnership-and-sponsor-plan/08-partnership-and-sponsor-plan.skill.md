---
skill_number: "08"
skill_id: partnership-and-sponsor-plan
name: Partnership and Sponsor Plan
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 8-16 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/01-civic-alignment/city-sponsor-brief.md
    - artifacts/02-event-charter/event-charter.md
    - artifacts/02-event-charter/scope-boundaries.md
    - artifacts/03-stakeholder-map/partner-register.csv
    - artifacts/03-stakeholder-map/decision-maker-map.md
    - artifacts/04-governance-model/decision-rights-matrix.md
    - artifacts/05-track-strategy/final-track-strategy.md
  optional:
    - artifacts/05-track-strategy/track-list.md
outputs:
  - artifacts/08-partnership-and-sponsor-plan/sponsor-tier-structure.md
  - artifacts/08-partnership-and-sponsor-plan/sponsor-pipeline.csv
  - artifacts/08-partnership-and-sponsor-plan/sponsor-pipeline.csv.meta.yaml
  - artifacts/08-partnership-and-sponsor-plan/partnership-asks.md
  - artifacts/08-partnership-and-sponsor-plan/fiscal-sponsor-agreement.md
downstream_skills:
  - 09-community-outreach-plan
  - 12-event-operations-plan
  - 14-judging-system
  - 16-post-event-pipeline
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/08-partnership-and-sponsor-plan/sponsor-tier-structure.template.md
  - templates/08-partnership-and-sponsor-plan/sponsor-pipeline.template.csv
  - templates/08-partnership-and-sponsor-plan/sponsor-pipeline.meta.template.yaml
  - templates/08-partnership-and-sponsor-plan/partnership-asks.template.md
  - templates/08-partnership-and-sponsor-plan/fiscal-sponsor-agreement.template.md
search_paths:
  - artifacts/08-partnership-and-sponsor-plan/
  - templates/08-partnership-and-sponsor-plan/
  - examples/*/08-partnership-and-sponsor-plan/
  - ../**/sponsors*
  - ../**/fiscal*
  - ../**/budget*
  - docs/sponsors/
---

# Skill 08 — Partnership and Sponsor Plan

## Purpose

Define how the event raises money, in-kind contributions, and
partnerships, and document the legal vehicle (fiscal sponsor) that
makes any of it possible.

Four artifacts (one of which is legal):

1. **`sponsor-tier-structure.md`** — tiers, costs, benefits,
   capacity per tier.
2. **`sponsor-pipeline.csv`** — operational pipeline of prospects:
   contact, tier sought, status, next step, owner.
3. **`partnership-asks.md`** — in-kind asks (venue, food, AV,
   mentors, prizes) with status.
4. **`fiscal-sponsor-agreement.md`** — the named fiscal sponsor and
   the signed agreement reference. **Legal review required.**

This skill is where civic alignment becomes financial reality.

## When to use

- After the charter is `needs-review` so sponsors know what they
  are funding
- 12+ weeks before the event for the headline sponsor ask
- 6-8 weeks before the event for in-kind partnership confirmations
- Whenever a sponsor is added or status changes

## Who should use it

Partnership / business-development lead + executive lead + fiscal
sponsor representative. Legal counsel for the fiscal sponsor
agreement.

## Prerequisites

**Required:** all listed above. In particular,
`decision-rights-matrix.md` is required because it names the
decider for sponsor commitments — this skill does not unilaterally
accept sponsorships.

## Inputs

- Upstream artifacts
- Last year's sponsor list (if any)
- The fiscal sponsor candidate (often an existing nonprofit;
  Richmond used 1717 Collective)

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `sponsor-tier-structure.md` | `needs-review` | yes |
| `sponsor-pipeline.csv` | `needs-review` | yes |
| `partnership-asks.md` | `needs-review` | yes |
| `fiscal-sponsor-agreement.md` | `needs-review` | yes (legal) |

## Search behavior

1. `artifacts/08-partnership-and-sponsor-plan/*` — existing?
2. `templates/08-partnership-and-sponsor-plan/*` — load.
3. `examples/*/08-partnership-and-sponsor-plan/*` — reference.
4. Parent repo for sponsor lists, fiscal agreements, budget docs,
   prior-year financial records.
5. User-supplied content.

## Validation behavior

Run the four blocks from `validation/checks.md`. Additional:

- Every confirmed sponsor in the CSV must be in
  `03/partner-register.csv` (cross-artifact consistency).
- The fiscal sponsor named in `fiscal-sponsor-agreement.md` must
  appear in `03/partner-register.csv` and in the sponsor pipeline.
- `fiscal-sponsor-agreement.md` cannot reach `approved` without
  `approved_by` naming legal counsel.

## Normalization behavior

Prior-year sponsor lists are useful contact starts but not
confirmed commitments. Normalize names and contacts into the
pipeline at `status: stale` until the user re-confirms each.

Prior fiscal sponsor agreements: do not normalize the agreement
text. Reference the prior agreement as `source_materials` and have
legal counsel draft fresh language.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Draft tier structure.** With the user, define:
   - Number of tiers (typical: 3-5)
   - Per-tier price
   - Per-tier benefits (logo placement, mention frequency, judge
     seat, mentor seat, demo-table presence, naming rights for an
     award, etc.)
   - Per-tier capacity (how many sponsors at this tier)
3. **Build pipeline.** For every named prospect (from prior years,
   from `03/partner-register.csv`, from user knowledge):
   - Name, contact, tier sought, status, next step, owner, last
     contact date, notes
   - Statuses: `prospect`, `contacted`, `in-talks`, `verbal`,
     `confirmed`, `declined`, `stale`
4. **Build partnership asks.** Separate from cash sponsorship:
   - Venue (donation? discount?)
   - Food (sponsored meals?)
   - AV / IT support
   - Mentors (from companies; sometimes paid time, sometimes
     volunteer)
   - Prizes (cash, gift cards, services)
   - Each ask gets a status and an owner.
5. **Fiscal sponsor.** With legal counsel:
   - Name the fiscal sponsor (existing nonprofit, often)
   - Reference the signed agreement (path or URL)
   - State the fiscal sponsor's percentage / fee structure
   - State the agreement's term
   - This artifact is `needs-review` until legal signs off.
6. **Cross-check.** Total committed funds + asks ≥ event budget?
   If not, flag as a blocker for Skill 12.
7. **Write artifacts.**
8. **Report.**

## User interaction rules

- The status field is load-bearing. `verbal` is not `confirmed`;
  `confirmed` requires a signed agreement or written commitment.
  Do not let optimism creep into status.
- The fiscal sponsor agreement is the most consequential legal
  document in the planning process. Do not draft language; refer
  to the agreement that legal counsel produces.
- Prize money: if the event awards cash, the fiscal sponsor's W-9
  / 1099 process applies. Document this in
  `partnership-asks.md` and flag for Skill 14 (judging
  runbook needs the W-9 distribution flow).
- Sponsor logo placement: every logo commitment implies a
  brand-asset request. Document the brand-asset request as an
  open question for the comms lead.

## Completion criteria

- [ ] Four artifacts at canonical paths
- [ ] Tier structure published with capacities
- [ ] Pipeline has every named prospect with owner and next step
- [ ] Partnership asks list is exhaustive (venue, food, AV,
      mentors, prizes at minimum)
- [ ] Fiscal sponsor named and agreement referenced
- [ ] Sum of confirmed commitments meets minimum budget threshold
      (or the gap is flagged)

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| No fiscal sponsor identified | Stop. Cash sponsorship cannot flow without a vehicle. Loop back to Skill 03 to identify a candidate. |
| Confirmed sponsorship total below budget threshold | Either reduce scope (Skill 02 scope-boundaries.md) or extend the recruiting window. Do not begin event commitments against unfunded budget lines. |
| A prospective sponsor wants conditions the operating principles forbid | Surface to governance (`04/decision-rights-matrix.md`). The decider per the matrix accepts or declines. |
| Prior year's fiscal sponsor cannot continue | Loop to legal counsel; potentially loop back to Skill 03 to identify an alternative. |
| Prize-cash logistics (W-9, 1099) not yet figured out | Document as an open question for Skill 14 (judging runbook). The judging runbook owns the on-site flow. |
| A sponsor wants to influence track / problem statements | Refuse per Tenet 1 (governance owns priorities, not sponsors). Surface to governance. |

## Templates used

- `templates/08-partnership-and-sponsor-plan/sponsor-tier-structure.template.md`
- `templates/08-partnership-and-sponsor-plan/sponsor-pipeline.template.csv`
- `templates/08-partnership-and-sponsor-plan/sponsor-pipeline.meta.template.yaml`
- `templates/08-partnership-and-sponsor-plan/partnership-asks.template.md`
- `templates/08-partnership-and-sponsor-plan/fiscal-sponsor-agreement.template.md`

## Downstream skills

- **09 (Outreach)** needs sponsor logos and tier names to publish
  externally.
- **12 (Event Ops)** needs budget to plan venue, food, AV.
- **14 (Judging)** needs prize-cash logistics for the awards
  runbook.
- **16, 18** consume the pipeline for retrospective.

## Example invocation

> "Build the sponsor plan. Fiscal sponsor is [name]. We need
> roughly $X to run the event."

Expected steps:

1. Skill reads upstream, confirms scope and budget envelope.
2. Skill drafts tier structure with the user.
3. Skill normalizes prior contacts into the pipeline at `stale`.
4. Skill walks partnership asks domain by domain.
5. Skill writes fiscal sponsor stub for legal review.
6. Reports: "08 complete (pending review and legal). Pipeline: 24
   prospects. Confirmed: 3. Budget gap: $Y. 5 in-kind asks
   pending."

## Changelog

- 1.0.0 (initial) — First version. Enforces commitment-status
  discipline; refuses to let `verbal` masquerade as `confirmed`.
