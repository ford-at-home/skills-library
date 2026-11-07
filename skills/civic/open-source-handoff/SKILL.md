---
description: "Define how the event's outputs become public, durable artifacts the"
skill_number: "17"
skill_id: open-source-handoff
name: open-source-handoff
display_name: "Open-Source Handoff"
version: 1.0.0
status: initial
lifecycle_stage: post-event
estimated_duration: 2-4 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/03-stakeholder-map/partner-register.csv
    - artifacts/04-governance-model/decision-rights-matrix.md
    - artifacts/10-participant-experience-plan/code-of-conduct.md
    - artifacts/13-technology-setup/tech-stack.md
    - artifacts/13-technology-setup/github-org-plan.md
    - artifacts/14-judging-system/awards.md
    - artifacts/14-judging-system/submission-spec.md
    - artifacts/15-ai-assisted-evaluation/results-package-spec.md
    - artifacts/16-post-event-pipeline/handoff-shortlist.md
    - artifacts/16-post-event-pipeline/city-champion-path.md
  optional: []
outputs:
  - artifacts/17-open-source-handoff/oss-handoff-plan.md
  - artifacts/17-open-source-handoff/license-policy.md
  - artifacts/17-open-source-handoff/public-marketplace-listing.md
  - artifacts/17-open-source-handoff/contributor-guide.md
downstream_skills:
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/17-open-source-handoff/oss-handoff-plan.template.md
  - templates/17-open-source-handoff/license-policy.template.md
  - templates/17-open-source-handoff/public-marketplace-listing.template.md
  - templates/17-open-source-handoff/contributor-guide.template.md
search_paths:
  - artifacts/17-open-source-handoff/
  - templates/17-open-source-handoff/
  - examples/*/17-open-source-handoff/
  - ../**/LICENSE*
  - ../**/CONTRIBUTING*
  - docs/oss/
---

# Skill 17 — Open-Source Handoff

## Purpose

Define how the event's outputs become public, durable artifacts the
city and other regions can build on. Set the licensing default,
publish each idea's listing, and write the contributor guide that
keeps maintenance possible.

Four artifacts (one legal):

1. **`oss-handoff-plan.md`** — what's open-sourced, where, on what
   schedule.
2. **`license-policy.md`** — chosen license, asset exceptions,
   data exceptions. **Legal review required.**
3. **`public-marketplace-listing.md`** — the spec for the
   per-idea public listing (status, demo links, grades,
   evaluations, feedback, next steps).
4. **`contributor-guide.md`** — how outside contributors engage;
   references the code of conduct.

## When to use

- 2-3 weeks after the event so listings can include AI eval
  scorecards
- Before the Day 30 announcement if the listings are part of
  what gets announced

## Who should use it

OSS lead + executive lead + legal counsel for the license policy.
Track committees may review their pillar's listings.

## Prerequisites

**Required:** 10 upstream artifacts. The OSS handoff cannot
proceed without the handoff shortlist (Skill 16) and the AI eval
results package spec (Skill 15).

## Inputs

- Upstream artifacts
- Participant submissions (videos, repos, links)
- Sponsor branding guidance (what acknowledgements are required)

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `oss-handoff-plan.md` | `needs-review` | yes |
| `license-policy.md` | `needs-review` | yes (legal) |
| `public-marketplace-listing.md` | `needs-review` | yes |
| `contributor-guide.md` | `draft` | no |

## Search behavior

1. `artifacts/17-open-source-handoff/*` — existing?
2. `templates/17-open-source-handoff/*` — load.
3. `examples/*/17-open-source-handoff/*` — reference.
4. Parent repo for `LICENSE*`, `CONTRIBUTING*` files.
5. User-supplied content.

## Validation behavior

Run the four blocks. Additional:

- `license-policy.md` cannot reach `approved` without legal
  counsel review.
- Every idea on `16/handoff-shortlist.md` has a corresponding
  listing in the public marketplace (or an explicit private
  exemption with stated reason).
- `contributor-guide.md` references `10/code-of-conduct.md`.

## Normalization behavior

Permissive open-source licenses (MIT, Apache 2.0) and
governance-favored licenses (e.g. GPL family) are well-documented.
Normalize the license text from upstream-of-the-license sources
(Open Source Initiative, SPDX), but the **selection** is a legal
decision.

`CONTRIBUTING.md` standards from the wider open-source community
inform the structure; the body needs local-context adaptation.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Decide license policy** (with legal counsel):
   - Code default (MIT, Apache 2.0, etc.)
   - Asset exceptions (logos, fonts; often non-open licenses)
   - Data exceptions (city data often has its own license;
     reference rather than republish)
   - Participant retention of IP if applicable
3. **Draft oss-handoff-plan.** Cover:
   - Which submissions become public (every shortlisted idea
     unless opted out)
   - Which repos move where (participant repos → event GitHub
     org? remain on participants' personal orgs?)
   - Asset attribution and sponsor acknowledgements
   - Schedule (Day 30? rolling? per-team consent gate?)
4. **Draft public-marketplace-listing spec.** Per-idea listing
   structure:
   - Title, team, pillar/track, problem statement
   - Demo video link
   - Code repo link
   - Live judging score (from `14/rubric.md`)
   - AI eval scorecard + rationale packet (from
     `15/results-package-spec.md`)
   - Civic feedback (from working sessions if applicable)
   - Next steps (championed? working session? archived?)
   - Status (active, archived, championed, blocked)
5. **Draft contributor-guide.** Cover:
   - How to engage with a listed idea (issues, PRs)
   - Code of conduct reference
   - Maintenance expectations (this is post-event volunteer work;
     do not overpromise)
6. **Cross-check.** Listings match shortlist; license policy is
   compatible with sponsor expectations; CoC is referenced.
7. **Report.**

## User interaction rules

- License selection is legal. The agent recommends from common
  options; counsel decides. The agent does not pick.
- Participant consent: do not publish a participant's repo or
  video without consent. Build the consent into Skill 10's
  registration flow (or back-fill via outreach).
- Marketplace listings serve two audiences (City + participants).
  Make the listing legible to both.
- Maintenance expectations are minimal. Do not promise the
  organizers will maintain participant code. The listing exists
  for discovery, not stewardship.

## Completion criteria

- [ ] Four artifacts at canonical paths
- [ ] License decision named with legal owner
- [ ] Every shortlisted idea has a listing
- [ ] Contributor guide references CoC
- [ ] Sponsor acknowledgements documented
- [ ] All `needs-review` artifacts have reviewers named

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Participant withholds consent for public listing | Honor it. Listing is private or omitted; document in shortlist. |
| Sponsor wants exclusive rights to a participant's IP | Refuse per operating principles (open-source default). Surface to governance. |
| Legal counsel unavailable | License-policy stays at `needs-review`. The handoff plan may proceed with provisional license noted. Do not publish without legal sign-off. |
| Participant code contains accidental secrets or PII | Hold the listing; participant must clean the repo first. Provide instructions. |
| City data referenced in repo is restricted | Listing notes the data dependency without including the data. Reference `07/data-blockers-register.md`. |

## Templates used

- See frontmatter.

## Downstream skills

- **18 (Retrospective)** consumes the marketplace listings for
  follow-through assessment.

## Example invocation

> "Plan OSS handoff. License default: MIT. Legal counsel: [name].
> Shortlist is in `16/handoff-shortlist.md`."

Expected steps:

1. Skill drafts license-policy stub citing MIT for code; legal
   reviews.
2. Skill drafts oss-handoff-plan with participant-consent gate.
3. Skill drafts public-marketplace-listing spec.
4. Skill drafts contributor-guide referencing CoC.
5. Reports: "17 complete (pending review and legal). 12 listings
   to publish. 2 require participant consent confirmation. 1
   sponsor exclusivity ask refused — surfaced to governance."

## Changelog

- 1.0.0 (initial) — First version. License is a legal decision;
  participant consent gated; sponsor exclusivity refused as
  default.
