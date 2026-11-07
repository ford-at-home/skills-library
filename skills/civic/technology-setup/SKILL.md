---
description: "Decide and document every tool the event runs on: communications,"
skill_number: "13"
skill_id: technology-setup
name: Technology Setup
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 4-8 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/02-event-charter/scope-boundaries.md
    - artifacts/05-track-strategy/track-list.md
    - artifacts/06-problem-statement-development/final-problem-statements.md
    - artifacts/06-problem-statement-development/track-context-briefs.md
    - artifacts/06-problem-statement-development/dataset-inventory.md
    - artifacts/07-data-readiness/data-readiness-matrix.md
    - artifacts/07-data-readiness/data-access-plan.md
    - artifacts/10-participant-experience-plan/registration-flow.md
    - artifacts/10-participant-experience-plan/participant-journey.md
    - artifacts/11-mentor-volunteer-ops/mentor-onboarding.md
    - artifacts/12-event-operations-plan/run-of-show.md
    - artifacts/12-event-operations-plan/venue-plan.md
    - artifacts/12-event-operations-plan/comms-tree.md
  optional: []
outputs:
  - artifacts/13-technology-setup/tech-stack.md
  - artifacts/13-technology-setup/slack-config.yaml
  - artifacts/13-technology-setup/github-org-plan.md
  - artifacts/13-technology-setup/ai-tooling-plan.md
  - artifacts/13-technology-setup/tech-runbook.md
downstream_skills:
  - 14-judging-system
  - 15-ai-assisted-evaluation
  - 17-open-source-handoff
templates_used:
  - templates/13-technology-setup/tech-stack.template.md
  - templates/13-technology-setup/slack-config.template.yaml
  - templates/13-technology-setup/github-org-plan.template.md
  - templates/13-technology-setup/ai-tooling-plan.template.md
  - templates/13-technology-setup/tech-runbook.template.md
search_paths:
  - artifacts/13-technology-setup/
  - templates/13-technology-setup/
  - examples/*/13-technology-setup/
  - ../**/infra/
  - ../**/hackathon-slack/
  - ../**/slack-config*
  - ../**/AGENTS.md
  - ../**/.cursor/skills/
  - docs/tech/
---

# Skill 13 — Technology Setup

## Purpose

Decide and document every tool the event runs on: communications,
code hosting, AI assistance, registration plumbing. Justify each
choice and name a fallback.

Five artifacts:

1. **`tech-stack.md`** — one row per tool: purpose, cost,
   complexity, why chosen, alternatives evaluated.
2. **`slack-config.yaml`** — Slack workspace configuration with
   channels, workflows, role-based onboarding.
3. **`github-org-plan.md`** — GitHub organization, repo structure,
   permissions model.
4. **`ai-tooling-plan.md`** — AI tools, budget, data-handling
   policy.
5. **`tech-runbook.md`** — setup steps, on-call rotation, known
   issues.

## When to use

- After Skill 12 (event ops needs are stable enough to set tech
  against)
- 4-6 weeks before the event for non-trivial provisioning (Slack
  Business plan trial, GitHub org, AI tool budgets)
- Day-of tech support is owned by this runbook

## Who should use it

Tech lead + operations lead. The agent can draft configs but a
human runs the provisioning.

## Prerequisites

**Required:** all 13 upstream listed. Tech serves the event;
nothing here is invented absent event need.

## Inputs

- Upstream artifacts
- Existing tooling subscriptions the organizing team brings
- Sponsor-provided tooling credits (cloud, AI, dev tools)
- Prior-event tech runbooks if available

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `tech-stack.md` | `needs-review` | yes |
| `slack-config.yaml` | `needs-review` | yes |
| `github-org-plan.md` | `needs-review` | yes |
| `ai-tooling-plan.md` | `needs-review` | yes |
| `tech-runbook.md` | `draft` | no |

## Search behavior

1. `artifacts/13-technology-setup/*` — existing?
2. `templates/13-technology-setup/*` — load.
3. `examples/*/13-technology-setup/*` — reference.
4. Parent repo:
   - `infra/` directories — extremely high-value; often contains
     provisioning code
   - `infra/hackathon-slack/` style (Richmond pattern) — Slack
     provisioning from a YAML file
   - `AGENTS.md`, `.cursor/skills/` — AI-tooling enablement
     artifacts the parent repo may already carry
5. User-supplied content.

## Validation behavior

Run the five blocks. Additional:

- Every tool in `tech-stack.md` has a stated cost and a stated
  alternative.
- `slack-config.yaml` has the `_meta:` frontmatter block.
- `ai-tooling-plan.md` states a budget cap and a data-handling
  policy. No AI tool may be used without both.
- `tech-runbook.md` references the comms tree for on-call
  escalation.

## Normalization behavior

A prior `infra/hackathon-slack/config/hackathon.yaml` (Richmond
pattern) is the highest-value input. Normalize into this year's
`slack-config.yaml`, updating channels, workflows, and role
groups. Preserve the workflow definitions (mentor-help, team
intake, submission intake, post-join routing).

`AGENTS.md` and `.cursor/skills/` files from a prior repo can be
referenced (not duplicated) from `ai-tooling-plan.md` as
recommended patterns to carry forward.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Build tech-stack table.** For each need (central comms, code
   hosting, AI assist, registration, video, swag fulfillment, AV,
   payment processing, etc.), capture:
   - Need
   - Chosen tool
   - Cost (monthly / event-period)
   - Complexity (low/medium/high)
   - Why chosen
   - Alternatives evaluated and why rejected
3. **Slack config.** Set up workspace structure:
   - Public channels (announcements, help, social)
   - Per-track channels (one per `track-list.md` entry)
   - Per-role private channels (judges, mentors, organizers,
     sponsors)
   - Workflows: team intake, mentor help, final submission,
     post-join routing
4. **GitHub org plan.** Decide:
   - Org name
   - Repo structure (one per team? one per track?)
   - Permissions (who can create repos? merge? push to main?)
   - Template repo for participant teams
5. **AI tooling plan.** Decide:
   - Primary AI tool (e.g. Cursor, Claude Code, ChatGPT)
   - Fallback (e.g. Featherless AI for credit-funded inference)
   - Budget cap
   - Data-handling policy (what participants can / cannot send
     to AI tools; PII, sensitive city data)
   - Optional: `AGENTS.md` and `.cursor/skills/` patterns to
     carry into participant repos
6. **Tech runbook.** Setup steps per tool, on-call rotation
   referenced to the comms tree, known issues.
7. **Cross-check.** Slack channel set matches track-list; GitHub
   repo template matches the submission spec (will be finalized
   in Skill 14); AI tooling budget within event budget.
8. **Report.**

## User interaction rules

- "Why chosen" must be a real reason, not "we already had it."
  If "we already had it" is the real reason, say so explicitly.
- Cost includes setup + monthly. A free tool that takes 20 hours
  to provision is not free.
- AI tooling: data-handling policy is non-negotiable. The
  Richmond year-1 stance is that participants are free to use
  AI, but sensitive city data does not leave city systems. State
  this plainly.
- Slack Business plan: if the trial unlocks API access and
  workflows, document the trial start/end so the team knows when
  to renew or downgrade.

## Completion criteria

- [ ] Five artifacts at canonical paths
- [ ] Every tool has cost, complexity, alternatives
- [ ] Slack config covers tracks and roles
- [ ] GitHub plan covers participant team repos
- [ ] AI tooling has budget cap and data policy
- [ ] Runbook references on-call escalation

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Slack Business trial expires during event | Document in runbook; plan migration or paid extension. |
| AI tool data-handling policy conflicts with sponsor expectations | Surface to governance. Sponsor expectations do not override participant data protection. |
| GitHub org cannot be created in time | Use a personal org with named admin; document in `tech-runbook.md`. |
| Sponsor-provided cloud credits restrict tool choice | Document in `tech-stack.md` as constraint; choose accordingly. |
| Registration platform (Eventbrite, etc.) integrates poorly with Slack | Document the manual reconciliation procedure; reference Skill 10's registration-flow.md. |

## Templates used

- See frontmatter.

## Downstream skills

- **14 (Judging)** uses Slack and GitHub for submission flow.
- **15 (AI Eval)** uses the AI tooling plan.
- **17 (OSS Handoff)** uses the GitHub plan.

## Example invocation

> "Set up tech. Slack Business trial starting [date]. GitHub org
> name is [name]. AI primary: Cursor; fallback: Featherless AI."

Expected steps:

1. Skill normalizes `infra/hackathon-slack/config/hackathon.yaml`
   from the parent repo into this year's `slack-config.yaml`.
2. Skill drafts tech-stack with alternatives evaluated.
3. Skill drafts AI tooling plan with budget and data policy.
4. Skill drafts GitHub org plan.
5. Reports: "13 complete (pending review). Slack trial expires
   <date>. AI budget cap: $X. 1 sponsor credit constraint
   documented."

## Changelog

- 1.0.0 (initial) — First version. Enforces "why chosen" and
  "alternatives evaluated"; AI data policy non-negotiable.
