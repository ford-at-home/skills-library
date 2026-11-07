---
skill_number: "15"
skill_id: ai-assisted-evaluation
name: AI-Assisted Evaluation
version: 1.0.0
status: initial
lifecycle_stage: post-event
estimated_duration: 1-3 weeks (compressed; runs after event)
requires_human_review: true
prerequisites:
  required:
    - artifacts/06-problem-statement-development/final-problem-statements.md
    - artifacts/06-problem-statement-development/track-context-briefs.md
    - artifacts/06-problem-statement-development/dataset-inventory.md
    - artifacts/07-data-readiness/data-readiness-matrix.md
    - artifacts/07-data-readiness/data-blockers-register.md
    - artifacts/13-technology-setup/tech-stack.md
    - artifacts/13-technology-setup/ai-tooling-plan.md
    - artifacts/14-judging-system/rubric.md
    - artifacts/14-judging-system/submission-spec.md
  optional: []
outputs:
  - artifacts/15-ai-assisted-evaluation/ai-eval-plan.md
  - artifacts/15-ai-assisted-evaluation/evaluator-personas.md
  - artifacts/15-ai-assisted-evaluation/implementation-reality-rubric.md
  - artifacts/15-ai-assisted-evaluation/eval-runbook.md
  - artifacts/15-ai-assisted-evaluation/results-package-spec.md
downstream_skills:
  - 16-post-event-pipeline
  - 17-open-source-handoff
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/15-ai-assisted-evaluation/ai-eval-plan.template.md
  - templates/15-ai-assisted-evaluation/evaluator-personas.template.md
  - templates/15-ai-assisted-evaluation/implementation-reality-rubric.template.md
  - templates/15-ai-assisted-evaluation/eval-runbook.template.md
  - templates/15-ai-assisted-evaluation/results-package-spec.template.md
search_paths:
  - artifacts/15-ai-assisted-evaluation/
  - templates/15-ai-assisted-evaluation/
  - examples/*/15-ai-assisted-evaluation/
  - ../**/agents/CIVIC_EVAL_PERSONAS*
  - ../**/LIFECYCLE_RUBRIC.md
  - ../**/IMPLEMENTATION_REALITY*
  - ../**/ai_evaluations*
  - ../**/ai_rationale*
  - docs/ai-eval/
---

# Skill 15 — AI-Assisted Evaluation

## Purpose

Run a structured AI evaluation pass over the full submission corpus
(and any post-event idea expansion) using a fixed rubric, named
evaluator personas, and a multi-agent annotation pattern. The
output is a second evaluation layer that complements — does not
replace — live human judging.

The Implementation Reality rubric is the survivability lens: can
this idea actually ship past prototype?

Five artifacts:

1. **`ai-eval-plan.md`** — what AI evaluation adds beyond live
   judging; methodology overview.
2. **`evaluator-personas.md`** — the personas the agents adopt
   (e.g. city CTO, ops director, civic technologist, equity
   advocate, sponsor); each persona has a lens and prompt template.
3. **`implementation-reality-rubric.md`** — survivability dimensions
   (ownership clarity, data readiness, tech stack fit, integration
   surface, maintenance burden) and tier definitions (S/A/B/C/D).
4. **`eval-runbook.md`** — how to actually run the eval pass and
   validate AI output against a held-out human review.
5. **`results-package-spec.md`** — what gets packaged for the City
   and for participants.

## When to use

- Within 1-3 weeks after the event so the day-30 announcement
  has substance
- Can also run pre-event in a planning capacity, scoring blue-sky
  problem statements before participants engage them

## Who should use it

The evaluation lead, with human review by track committees. The
agent does the run; humans validate outputs.

## Prerequisites

**Required:** all 9 upstream listed. The rubric and submission
spec from Skill 14 are non-negotiable inputs — the AI eval scores
the same submissions judges saw, with the IR rubric layered on.

## Inputs

- Upstream artifacts
- Submitted projects (videos, repos, links per `submission-spec.md`)
- Optional: post-event idea expansion (AI-generated ideas to fill
  problem-statement coverage gaps)

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `ai-eval-plan.md` | `needs-review` | yes |
| `evaluator-personas.md` | `needs-review` | yes |
| `implementation-reality-rubric.md` | `needs-review` | yes |
| `eval-runbook.md` | `draft` | no |
| `results-package-spec.md` | `needs-review` | yes |

## Search behavior

1. `artifacts/15-ai-assisted-evaluation/*` — existing?
2. `templates/15-ai-assisted-evaluation/*` — load.
3. `examples/*/15-ai-assisted-evaluation/*` — reference.
4. Parent repo:
   - `agents/CIVIC_EVAL_PERSONAS*` — Richmond's persona definitions
   - `LIFECYCLE_RUBRIC.md` — Richmond's IR rubric
   - `IMPLEMENTATION_REALITY*` — synthesis docs
   - `ai_evaluations.csv` / `ai_rationale*` — prior eval outputs
5. User-supplied content.

## Validation behavior

Run the five blocks. Additional:

- `evaluator-personas.md` must declare each persona's lens and
  what they would flag.
- `implementation-reality-rubric.md` must define how dimension
  scores roll up to a tier (S/A/B/C/D).
- `ai-eval-plan.md` must name the models used, version, and
  data-handling stance (consistent with `13/ai-tooling-plan.md`).
- `eval-runbook.md` must include a human-validation step: a
  held-out sample is reviewed by humans and compared to AI scores.

## Normalization behavior

Richmond's parent-repo artifacts (`CIVIC_EVAL_PERSONAS.md`,
`LIFECYCLE_RUBRIC.md`) are the highest-value source. Normalize
verbatim where the user confirms applicability; otherwise
`needs-review`.

The AI eval pattern documented here follows the MAFA
(Multi-Agent Framework for Annotation) shape: specialized agents
apply structured reasoning, a judge agent reranks or consenses.
The pattern is platform-agnostic; the implementation choice (which
model, which orchestration) is in `ai-tooling-plan.md`.

## Step-by-step procedure

1. **Search and read upstream.**
2. **Draft ai-eval-plan.** Cover:
   - What this layer adds beyond live judging (consistent
     application across the full corpus; survivability lens;
     surfacing of overlooked items)
   - Models used + version
   - Data-handling stance (consistent with `13/ai-tooling-plan.md`)
   - Honest caveats: AI eval is not a substitute for judges; it
     scores along a fixed rubric and cannot replace civic judgment
3. **Draft evaluator personas.** With the user:
   - 5-10 personas typical
   - Each persona: name, role, lens, what they would flag,
     sample prompt scaffold
4. **Draft IR rubric.** Survivability dimensions:
   - Ownership clarity (named department / org that would own it)
   - Data readiness (does required data exist + access path)
   - Tech stack fit (uses tech the City has or can acquire)
   - Integration surface (how many external systems must it touch)
   - Maintenance burden (can a non-engineer keep it running)
   - Each dimension scored 1-5; total rolls up to S (21-25), A
     (16-20), B (11-15), C (6-10), D (1-5)
5. **Draft eval runbook.** Steps:
   - Prepare inputs (submissions, problem statements, rubric)
   - Run persona agents (one pass per persona)
   - Run judge / consensus agent
   - Produce scorecard + rationale packet per idea
   - Human-validation step: held-out sample, cross-check
6. **Draft results-package-spec.** What gets produced and to whom:
   - For the City: shortlist of ideas + IR scores + rationale
   - For participants: per-idea scorecard + rationale packet
   - Public vs. private split (per `17/license-policy.md`)
7. **Cross-check.** Rubric categories from `14/rubric.md` are
   reflected in the AI eval, not replaced by it.
8. **Report.**

## User interaction rules

- AI eval does not produce winners. Winners come from live
  judging. This must be stated in every artifact.
- Persona prompts should be specific enough that two different
  agents would produce similar outputs given the same input.
- Human validation is required. The eval-runbook must include a
  step where humans review a held-out sample and compare. If
  agreement is below threshold (e.g. 80%), the AI eval is
  discarded for that round.
- Disclosure: results published with AI evaluation must say so.
  Do not present AI scores as if they were human judgments.

## Completion criteria

- [ ] Five artifacts at canonical paths
- [ ] AI eval plan names model + version + data policy
- [ ] Personas have lenses and sample prompts
- [ ] IR rubric has dimensions + tier rollup
- [ ] Eval runbook includes human validation step
- [ ] Results-package-spec separates City and participant
      packages
- [ ] All `needs-review` artifacts have reviewers named

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| AI scores disagree wildly across personas | Expected; the consensus agent's job. If disagreement persists after consensus, flag the idea for human review rather than publishing a number. |
| Human validation step shows low agreement with AI | Discard the AI scores for that round. Investigate persona prompts; rerun. |
| Data-handling policy conflicts with submission content (PII in a video) | Refuse to send to AI; flag the submission for manual review only. |
| Model output cannot be reproduced (non-deterministic) | Record temperature, seed if available, exact prompt. Acknowledge non-determinism in `ai-eval-plan.md`. |
| Participant objects to AI evaluation of their submission | Provide opt-out path; document in `submission-spec.md` (Skill 14) and in the public results listing. |

## Templates used

- See frontmatter.

## Downstream skills

- **16 (Post-Event Pipeline)** uses IR scores to build the
  handoff shortlist.
- **17 (OSS Handoff)** uses the results package spec for the
  public marketplace listings.
- **18 (Retrospective)** uses the IR rubric data to assess
  whether scored ideas actually shipped year over year.

## Example invocation

> "Plan AI evaluation. Submissions are in. Rubric is at
> `14/rubric.md`. Use the MAFA-style multi-agent pattern. Models:
> Claude Opus 4.7 primary."

Expected steps:

1. Skill normalizes Richmond persona file into
   `evaluator-personas.md`.
2. Skill normalizes Richmond LIFECYCLE_RUBRIC into
   `implementation-reality-rubric.md`.
3. Skill drafts ai-eval-plan with model + data policy.
4. Skill drafts eval-runbook including human-validation step.
5. Skill drafts results-package-spec separating City and
   participant packages.
6. Reports: "15 complete (pending review). 7 personas defined. IR
   rubric with 5 dimensions and S/A/B/C/D tiers. Eval can run on
   N submissions; expected duration X hours per persona pass."

## Changelog

- 1.0.0 (initial) — First version. MAFA-style multi-agent pattern
  documented; human validation required; AI is complement, not
  replacement, of judging.
