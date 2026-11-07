---
name: ralph-loop
description: "A two-pass quality gate that catches the optimism bias inherent in first-pass reviews. Pass 1 checks completeness against source-of-truth artifacts. Pass 2 looks backward and asks 'what did we falsely assume?'"
---

# Ralph Loop — Two-Pass Adversarial Review

**Purpose:** A two-pass quality gate that catches the optimism bias inherent in first-pass reviews. Pass 1 checks completeness against source-of-truth artifacts. Pass 2 looks backward and asks "what did we falsely assume?"

**Part of:** Phase 10 of `skills/pillar-pipeline/SKILL.md` — runs at the end of each project's review.

---

## When To Use

- After completing Phases 1-9 of Pipeline A for a project
- As the closing gate before assigning a decision classification
- When a review feels suspiciously complete — that's usually when it isn't

## Inputs

- `ideas/<pillar>/<project_slug>/01_problem_fit.md`
- `ideas/<pillar>/<project_slug>/02_lifecycle_gap_analysis.md`
- `ideas/<pillar>/<project_slug>/03_rubric.md`
- `research/question_router.json` — to verify all questions were routed
- `research/findings/` — to verify research was actually used
- Source-of-truth artifacts (problem statements, breakout summaries)

## Output

- `ideas/<pillar>/<project_slug>/04_ralph_loop.md`

---

## Pass 1 — Completeness Check

Ask each question. If the answer is "no," document exactly what's missing.

1. **Source fidelity:** Did the review actually use the source-of-truth artifacts (problem statement, breakout summary)? Or did it drift into evaluating the demo on its own terms?

2. **Lifecycle coverage:** Were all 10 lifecycle stages evaluated in `02_lifecycle_gap_analysis.md`? Were any stages marked `COMPLETE` without sufficient evidence?

3. **Question routing:** Was every major unknown from Phase 4 routed in `question_router.json`? Are there questions that were generated but never assigned a destination?

4. **Fail flag consistency:** Were fail flags applied where warranted? Is there a demo-data dependency that wasn't flagged? A misalignment that was overlooked because the demo was impressive?

5. **Research integration:** Did the rubric scores in `03_rubric.md` actually reflect the research findings? Or were scores assigned based on demo quality independent of the evidence?

6. **Outreach coverage:** Is there at least one SME outreach draft for every `[Still Unknown]` or `[Requires SME confirmation]` item?

---

## Pass 2 — Backward-Looking Correction

This pass assumes the first review was optimistic and asks what it got wrong.

1. **Fundamental miss:** What is the single most important thing the review got wrong or failed to catch? Not a minor gap — the thing that would make a senior reviewer say "you missed the point."

2. **Invalid assumptions:** What did the review assume that has no evidence? List every assumption and tag each:
   - `[Supported]` — evidence exists in research or source materials
   - `[Unsupported]` — no evidence, but plausible
   - `[Contradicted]` — evidence actually argues against this

3. **Demo-data violations:** Re-examine every data claim in the submission. Is any data source actually synthetic, manually entered, or accessed via a one-time export rather than a sustainable integration? If yes, flag it even if the first review didn't.

4. **Missing stakeholder validation:** Is there any claim about how a city department, nonprofit, or community group would use this tool that has not been validated with someone from that group? If yes, flag it.

5. **Required rework:** Based on Pass 2 findings, what specific upstream artifacts need to be corrected? Name the file and the section.

---

## Output Template

```md
# Ralph Loop Review — [Project Name]

**Pillar:** [pillar]
**Review Date:** [date]

## Pass 1: Completeness

### Source Fidelity
- Problem statement used: [yes/no]
- Breakout summary used: [yes/no]
- Drift detected: [description or none]

### Lifecycle Coverage
- All 10 stages evaluated: [yes/no]
- Stages with insufficient evidence for COMPLETE rating: [list]

### Question Routing
- Total questions generated: [N]
- Questions routed: [N]
- Unrouted questions: [list]

### Fail Flag Consistency
- Flags applied: [list]
- Flags that should have been applied: [list]
- Flags incorrectly applied: [list]

### Research Integration
- Rubric scores supported by research: [yes/partially/no]
- Scores that appear detached from evidence: [list dimensions]

### Outreach Coverage
- [Still Unknown] items with outreach: [N/M]
- Items without outreach path: [list]

---

## Pass 2: Backward Correction

### Fundamental Miss
[1-3 sentences — the thing that matters most]

### Invalid Assumptions
| Assumption | Status | Evidence |
|------------|--------|----------|
| | [Supported/Unsupported/Contradicted] | |

### Demo-Data Violations
| Data Claim | Reality | Flag |
|-----------|---------|------|
| | | |

### Missing Stakeholder Validation
| Claim | Who Should Validate | Status |
|-------|-------------------|--------|
| | | |

### Required Rework
| File | Section | Issue | Action |
|------|---------|-------|--------|
| | | | |

---

## Final Status
[READY_FOR_REWORK | BLOCKED_ON_SME | BLOCKED_ON_DATA_ACCESS | FAIL]

## Decision Gate Classification
[Adopt | Repair | Reframe | Archive | Spin out into research]

## Rationale
[2-3 sentences justifying the classification]
```

---

## Stopping Conditions

- If Pass 1 finds no gaps and Pass 2 finds no invalid assumptions → `READY_FOR_REWORK` (because nothing is ever truly complete at this stage — the classification "Adopt" still requires external validation)
- If Pass 2 finds contradicted assumptions → rework upstream artifacts before classifying
- If both passes find the review was honest and thorough → assign the decision gate classification with confidence

## Notes

- Do not soften findings. The point of Pass 2 is to be adversarial — it exists because first-pass reviews are biased toward the demo they just spent time analyzing.
- The fundamental miss (Pass 2, #1) is the most important output. If you can only write one sentence, write that one.
- `Spin out into research` is not a failure. Some demos surface valuable questions that need 6 months of investigation before they become products. That's a legitimate outcome.
