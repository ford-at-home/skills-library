---
description: "Define how the event evaluates and recognizes work: rubric, awards"
skill_number: "14"
skill_id: judging-system
name: Judging System
version: 1.0.0
status: initial
lifecycle_stage: event
estimated_duration: 4-8 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/01-civic-alignment/civic-priority-map.md
    - artifacts/01-civic-alignment/success-definition.md
    - artifacts/02-event-charter/event-charter.md
    - artifacts/02-event-charter/operating-principles.md
    - artifacts/03-stakeholder-map/decision-maker-map.md
    - artifacts/04-governance-model/governance-model.md
    - artifacts/04-governance-model/track-committee-roster.md
    - artifacts/04-governance-model/decision-rights-matrix.md
    - artifacts/05-track-strategy/final-track-strategy.md
    - artifacts/05-track-strategy/track-list.md
    - artifacts/05-track-strategy/track-rationale.md
    - artifacts/06-problem-statement-development/final-problem-statements.md
    - artifacts/06-problem-statement-development/track-context-briefs.md
    - artifacts/07-data-readiness/data-readiness-matrix.md
    - artifacts/08-partnership-and-sponsor-plan/sponsor-tier-structure.md
    - artifacts/08-partnership-and-sponsor-plan/fiscal-sponsor-agreement.md
    - artifacts/10-participant-experience-plan/code-of-conduct.md
    - artifacts/10-participant-experience-plan/participant-journey.md
    - artifacts/11-mentor-volunteer-ops/mentor-roster.csv
    - artifacts/12-event-operations-plan/run-of-show.md
    - artifacts/12-event-operations-plan/comms-tree.md
    - artifacts/13-technology-setup/tech-stack.md
    - artifacts/13-technology-setup/slack-config.yaml
    - artifacts/13-technology-setup/github-org-plan.md
    - artifacts/13-technology-setup/ai-tooling-plan.md
  optional: []
outputs:
  - artifacts/14-judging-system/rubric.md
  - artifacts/14-judging-system/awards.md
  - artifacts/14-judging-system/judge-roster.md
  - artifacts/14-judging-system/judging-runbook.md
  - artifacts/14-judging-system/submission-spec.md
downstream_skills:
  - 15-ai-assisted-evaluation
  - 16-post-event-pipeline
  - 17-open-source-handoff
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/14-judging-system/rubric.template.md
  - templates/14-judging-system/awards.template.md
  - templates/14-judging-system/judge-roster.template.md
  - templates/14-judging-system/judging-runbook.template.md
  - templates/14-judging-system/submission-spec.template.md
search_paths:
  - artifacts/14-judging-system/
  - templates/14-judging-system/
  - examples/*/14-judging-system/
  - ../**/RUBRIC.md
  - ../**/JUDGE_SHEET.md
  - ../**/LIFECYCLE_RUBRIC.md
  - ../**/judging*
  - docs/judging/
---

# Skill 14 — Judging System

## Purpose

Define how the event evaluates and recognizes work: rubric, awards
and weighting, judges, day-of cadence, submission format. Publish
the rubric **at kickoff**, not at demo time — participants build
to what they understand will be evaluated.

Five artifacts:

1. **`rubric.md`** — scoring categories and scale.
2. **`awards.md`** — each award, its weighting profile, its prize.
3. **`judge-roster.md`** — confirmed judges with track expertise
   and attendance.
4. **`judging-runbook.md`** — day-of cadence, scoring tool,
   tiebreak procedure, prize-cash logistics.
5. **`submission-spec.md`** — what participants submit (video,
   links, demo) and how.

## When to use

- 6-8 weeks before the event so the rubric can be announced at
  kickoff
- 2-4 weeks before event for judge confirmations and runbook
- Day-of and immediately post-event: runbook is live

## Who should use it

Judging lead + executive lead + per-track committee leads. Judges
themselves only see the rubric and runbook after they're at
`needs-review`.

## Prerequisites

**Required:** 25 upstream artifacts. The judging system depends
on virtually everything upstream because it operationalizes the
event's values.

## Inputs

- Upstream artifacts
- Prior-year rubric and judge sheet (if any)
- The fiscal sponsor's W-9 / 1099 process for cash prize
  distribution

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `rubric.md` | `needs-review` | yes |
| `awards.md` | `needs-review` | yes |
| `judge-roster.md` | `needs-review` | yes |
| `judging-runbook.md` | `needs-review` | yes |
| `submission-spec.md` | `needs-review` | yes |

## Search behavior

1. `artifacts/14-judging-system/*` — existing?
2. `templates/14-judging-system/*` — load.
3. `examples/*/14-judging-system/*` — reference.
4. Parent repo for `RUBRIC.md`, `JUDGE_SHEET.md`,
   `LIFECYCLE_RUBRIC.md`, prior judging runbooks.
5. User-supplied content.

## Validation behavior

Run the five blocks. Additional:

- Every award in `awards.md` has a weighting profile that
  references the rubric categories.
- Every judge in `judge-roster.md` has track expertise mapped to
  at least one `track-list.md` entry.
- `submission-spec.md` references the Slack workflow (from
  `slack-config.yaml`) used for submissions.
- `judging-runbook.md` includes prize-cash logistics if
  `awards.md` lists cash prizes.

## Normalization behavior

A prior `RUBRIC.md` or `LIFECYCLE_RUBRIC.md` is the single
highest-value input. Normalize structure and category names; the
weights and thresholds need re-confirmation against this year's
charter.

A prior `JUDGE_SHEET.md` informs the runbook's scoring tool
layout; do not copy weights without re-confirmation.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Draft rubric.** With the user:
   - Number and names of scoring categories (3-7 typical)
   - Scoring scale (1-5 typical, with anchor descriptors per
     score)
   - The categories must reflect the operating principles
     (`02/operating-principles.md`).
3. **Draft awards.** For each:
   - Name
   - Criteria (one-paragraph "what this award honors")
   - Weighting profile (per-category multipliers summing to a
     consistent total)
   - Prize value (cash, in-kind, recognition)
   - Number of recipients
4. **Draft judge roster.** For each judge:
   - name, affiliation, track expertise, attendance status,
     CoC acknowledgement status
5. **Draft submission spec.** Cover:
   - Format (2-min video; N links; demo-on-site optional)
   - Submission channel (Slack workflow from
     `slack-config.yaml`)
   - Deadline (referenced to `run-of-show.md`)
   - Files / repo expectations
6. **Draft judging runbook.** Cover:
   - Pre-event: rubric announced at kickoff; judges briefed
   - Submission intake (workflow → triage → assignment to
     judges)
   - Live cadence (X minutes per team; video then Q&A then
     scoring then debate)
   - Scoring tool (paper, sheet, custom; reference
     `tech-stack.md`)
   - Tiebreak procedure
   - Result disclosure procedure
   - Prize-cash flow: W-9 collection on site, 1099 process,
     check distribution
   - Banquet / closing flow (live demos as showcase, family-
     friendly)
7. **Cross-check.** Every award has a weighting profile that adds
   up; every judge can cover at least one track; submission spec
   integrates with the Slack workflow.
8. **Report.**

## User interaction rules

- The rubric is the single most-cited artifact during the event.
  Push for clarity over cleverness. A judge in real time should
  understand each category from the rubric alone.
- Announce the rubric at kickoff. The Richmond year-1 lesson is
  that rubric mid-event is rubric too late. Document the kickoff
  announcement in `outreach-messages/`.
- Prize-cash logistics: do not invent a process. The fiscal
  sponsor's actual W-9 / 1099 workflow is the source. The
  runbook documents that workflow; it does not propose a new one.
- Frame judging publicly as "positive innovation for the city"
  rather than competition for money. The Richmond year-1 frame
  worked well; carry it forward.

## Completion criteria

- [ ] Five artifacts at canonical paths
- [ ] Rubric published in `outreach-messages/` for the kickoff
- [ ] Awards have weighting profiles
- [ ] Judges confirmed with expertise mapped to tracks
- [ ] Submission spec integrates with the Slack workflow
- [ ] Judging runbook covers prize-cash logistics
- [ ] All artifacts `needs-review` with named reviewers

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| Judge cancels late | Backup from `judge-roster.md`; otherwise track may go under-judged. Flag to governance. |
| Rubric category disagreement among committees | Surface to governance (`04/decision-rights-matrix.md`). The decision-rights matrix names the rubric decider. |
| Cash prize total exceeds confirmed sponsorship | Reduce prize amounts or pursue more sponsorship (Skill 08). Do not commit to prizes you cannot pay. |
| W-9 / 1099 logistics unclear | Loop to fiscal sponsor. Cash cannot be distributed without IRS-compliant collection. |
| Submission deadline causes time-zone confusion | Use a single time zone in the deadline; restate in every reminder. |
| Tied scoring | Apply the tiebreak procedure from the runbook (typically: weighted on impact category, or governance decision). Do not invent on the fly. |

## Templates used

- See frontmatter.

## Downstream skills

- **15 (AI Eval)** uses `rubric.md` and `submission-spec.md`
  directly. AI evaluation runs against the same submissions
  judges see, with the IR rubric layered on top.
- **16 (Post-Event Pipeline)** uses `awards.md` and judging
  results for handoff.
- **17 (OSS Handoff)** uses `submission-spec.md` to know what
  participant repos contain.
- **18 (Retrospective)** consumes the entire skill output to
  assess judging quality.

## Example invocation

> "Build the judging system. Three awards: Mayor's Choice,
> Moonshot, Pillar (one per track). Cash prizes total $X. Source:
> `2026-annual-hackathon/RUBRIC.md`."

Expected steps:

1. Skill normalizes `RUBRIC.md` into this year's `rubric.md` at
   `needs-review`.
2. Skill drafts awards.md with weighting profiles.
3. Skill drafts judge-roster.md from `03/partner-register.csv`
   filtered for judges.
4. Skill drafts submission-spec referencing the Slack workflow.
5. Skill drafts judging-runbook with W-9 / 1099 logistics.
6. Reports: "14 complete (pending review). 16 judges confirmed.
   Rubric ready for kickoff announcement. 1 award has weighting
   that doesn't sum — flagged."

## Changelog

- 1.0.0 (initial) — First version. Rubric-at-kickoff requirement;
  prize-cash documented against fiscal sponsor's real workflow.
