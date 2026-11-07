---
name: innovation-lifecycle
description: "The canonical lifecycle that every hackathon submission must be forced through. Each stage is scored as `COMPLETE`, `PARTIAL`, `MISSING`, or `INVALIDATED`. No stage can be skipped — skipping is the thing hackathons are best at, and this skill exists to catch it."
---

# Innovation Lifecycle — 10-Stage Completeness Audit

**Purpose:** The canonical lifecycle that every hackathon submission must be forced through. Each stage is scored as `COMPLETE`, `PARTIAL`, `MISSING`, or `INVALIDATED`. No stage can be skipped — skipping is the thing hackathons are best at, and this skill exists to catch it.

**Part of:** Phase 3 of `skills/pillar-pipeline/SKILL.md` (Pipeline A — Submission Review)

---

## Absolute Constraint

The **problem statement is the source of truth at all times.** If the demo does not solve the problem as stated, it is incomplete regardless of how well-built it is. Work backwards from the problem statement — never forward from what was built.

## Hard Rule: No Demo Data

Any solution that depends on synthetic, mock, placeholder, or invented data is incomplete. Real data sources must be named, their access method documented, and — where access requires a human relationship — an SME outreach email must be drafted. If real data cannot be identified, the project is blocked and must say so explicitly.

---

## The 10 Stages

### Stage 1 — Problem Understanding

**Question:** Does the team understand the actual problem as stated?

**Evidence required:**
- Problem statement quoted verbatim (not paraphrased)
- Primary user identified with specificity (not "residents" — "a Richmond resident leaving incarceration who needs housing within 72 hours")
- Pain articulated from the user's perspective
- Desired outcome stated in measurable terms
- Success conditions at 90 days and 2 years

**Scoring:**
- `COMPLETE` — all elements present and grounded in source of truth
- `PARTIAL` — problem restated but user or outcome is vague
- `MISSING` — team appears to have worked from their own interpretation
- `INVALIDATED` — team solved a different problem (triggers `FAIL_MISALIGNED`)

---

### Stage 2 — Stakeholder Understanding

**Question:** Does the team know who else cares, who blocks, and who enables?

**Evidence required:**
- Primary user (from Stage 1)
- Secondary users (staff, case managers, nonprofit workers who interact with the system)
- Institutional stakeholders (department heads, budget holders, IT gatekeepers)
- Community stakeholders (advocacy groups, trusted intermediaries)
- Opponents or skeptics (unions, vendors with incumbency, privacy advocates)

**Scoring:**
- `COMPLETE` — named stakeholders with roles and relationships
- `PARTIAL` — primary user clear, institutional context missing
- `MISSING` — no evidence of stakeholder mapping
- `INVALIDATED` — stakeholder map contradicts source of truth (e.g., built for a user the problem statement doesn't describe)

---

### Stage 3 — Questions and Unknowns

**Question:** Did the team identify what they don't know before building?

**Evidence required:**
- At least 10 open questions across: data, user, integration, equity, prior art
- Questions are specific enough to have factual answers
- Questions acknowledge constraints the team cannot resolve alone

**Scoring:**
- `COMPLETE` — structured question list covering all categories
- `PARTIAL` — some questions, but missing categories (equity almost always missing)
- `MISSING` — team built without articulating unknowns
- `INVALIDATED` — questions are rhetorical or self-answering

---

### Stage 4 — Evidence Gathering

**Question:** Did the team gather real evidence before or during the build?

**Evidence required:**
- Research findings cited (web, corpus, interviews, observations)
- Data inspected (real datasets opened and examined)
- User input (even informal conversations count if documented)
- Comparable systems reviewed

**Scoring:**
- `COMPLETE` — multiple evidence types, cited with sources
- `PARTIAL` — some research, but gaps in data or user evidence
- `MISSING` — no evidence gathering documented; built from assumptions
- `INVALIDATED` — evidence cited but fabricated or misattributed

---

### Stage 5 — Prior Art Scan

**Question:** Did the team look at what already exists before building?

**Evidence required:**
- Named comparable products, pilots, or programs (minimum 3)
- Regional comparables (Richmond, Virginia, Mid-Atlantic, comparable US cities)
- For each: what it solved, what it missed, why adoption stalled
- Assessment of whether the problem is already 80-99% solved somewhere

**Scoring:**
- `COMPLETE` — thorough scan with regional and national examples, failure analysis
- `PARTIAL` — aware of some prior art, but no failure analysis or regional context
- `MISSING` — no prior art referenced; team assumed they were first (triggers `FAIL_NO_PRIOR_ART_SCAN`)
- `INVALIDATED` — prior art cited but wrong (confused product, wrong city, sunset tool presented as active)

---

### Stage 6 — Data Reality Check

**Question:** Does the solution identify real data sources with real access paths?

**Evidence required:**
- Named datasets with specific identifiers (API endpoints, portal URLs, dataset IDs)
- Data owner identified (department, agency, vendor)
- Access method documented (public API, FOIA, partnership, vendor contract)
- Update cadence known (real-time, daily, monthly, annual, unknown)
- Data quality issues acknowledged

**Scoring:**
- `COMPLETE` — all data claims verified with source, owner, access, cadence
- `PARTIAL` — some real data, some assumptions about access
- `MISSING` — demo uses synthetic/mock data with no real source identified (triggers `FAIL_DEMO_DATA`)
- `INVALIDATED` — claims real data but it's actually demo data, or claims public access to restricted data

---

### Stage 7 — Concept Refinement

**Question:** Did the concept evolve based on evidence, or was it locked in from day one?

**Evidence required:**
- Design decisions traced to evidence (research finding → design choice)
- Trade-offs acknowledged (what was considered and rejected, with reasons)
- Scope narrowed to something buildable in the available time
- User value proposition articulated in one sentence

**Scoring:**
- `COMPLETE` — clear evidence of refinement based on findings
- `PARTIAL` — some iteration, but core concept unchanged despite contradicting evidence
- `MISSING` — concept appears to have been decided before any research
- `INVALIDATED` — refinement went in wrong direction (made concept less aligned with problem)

---

### Stage 8 — Feasibility and Implementation Path

**Question:** Could a city department or nonprofit plausibly adopt or pilot this?

**Evidence required:**
- Technical architecture matches institutional capacity (no Kubernetes for a 3-person department)
- Procurement path identified (open source, existing vendor, new RFP)
- Staffing implications acknowledged (who maintains this after the hackathon?)
- Integration with existing systems addressed (not "replaces everything")
- Timeline to pilot: 90-day roadmap with concrete steps

**Scoring:**
- `COMPLETE` — believable implementation path with institutional awareness
- `PARTIAL` — technically feasible but ignores procurement, staffing, or integration
- `MISSING` — no implementation path beyond "deploy to production"
- `INVALIDATED` — implementation path requires conditions that don't exist (e.g., "city adopts our custom database")

---

### Stage 9 — Validation Plan

**Question:** Are the next validation steps obvious and grounded?

**Evidence required:**
- Named SME contacts for validation (from `CONTACTS.md` or identified through research)
- Specific questions for each SME
- Data access requests identified (what needs to be requested, from whom)
- User testing plan (who tests, where, what feedback is collected)
- Risk register (what could kill the project, and what triggers the kill)

**Scoring:**
- `COMPLETE` — validation plan with named contacts, specific asks, and timeline
- `PARTIAL` — knows what needs validation but no plan to execute
- `MISSING` — no validation plan; team assumes correctness (triggers `FAIL_UNVALIDATED` if data access or operational cadence matters)
- `INVALIDATED` — validation plan targets wrong stakeholders or asks wrong questions

---

### Stage 10 — Pilot Readiness

**Question:** If someone said "go" tomorrow, could this actually launch?

**Evidence required:**
- Working prototype (not slides)
- Real data connected (not mock)
- User tested (at least informally)
- Institutional sponsor identified or at least targeted
- First 30-day plan documented
- Known blockers documented with owners

**Scoring:**
- `COMPLETE` — ready for a supervised pilot with identified partners
- `PARTIAL` — prototype works but needs 1-3 specific things to be pilot-ready
- `MISSING` — demo only; significant work needed before any real deployment
- `INVALIDATED` — prototype creates false impression of readiness (e.g., works on demo data but breaks on real data)

---

## Post-Lifecycle Extensions

After the 10-stage lifecycle is complete for all demos in a pillar, two additional layers can be applied:

**Stage 11 — Blue Ocean ERRC Ideation** (via `pillar-repos/*/skills/blue_ocean_reframing/SKILL.md`)
- Input: `jtbd_analysis.md` + `pain_points.md` from `_shared-*` dirs (or the per-idea dir when no shared version exists — e.g. `thriving-built-environment` has only per-idea copies)
- Output: `ideas/<pillar>/NEW_IDEAS_BLUESKY.md` + `ideas/<pillar>/NEW_IDEAS_BLUESKY_RUBRIC_GRADES.md`
- Generates 1-2 additional ideas per pillar using Eliminate/Reduce/Raise/Create reframing

**Stage 12 — Implementation Reality Scoring** (via `ideas/IMPLEMENTATION_REALITY_RUBRIC.md`)
- Input: All ideas (demos + NEW_IDEAS + BLUESKY) + `ideas/RICHMOND_TECH_STACK_2026.md`
- Output: `ideas/<pillar>/IMPLEMENTATION_REALITY_REVIEW.md` per pillar + `ideas/IMPLEMENTATION_REALITY_SYNTHESIS.md` cross-pillar
- Scores every idea on 5 survivability dimensions: Ownership Clarity, Data Readiness, Tech Stack Fit, Integration Surface, Maintenance Burden

---

## Output

`ideas/<pillar>/<project_slug>/lifecycle_gap_analysis.md`

**Template:**

```md
# Innovation Lifecycle Gap Analysis — [Project Name]

**Pillar:** [pillar]
**Problem Statement:** [verbatim]
**Review Date:** [date]

## Stage Assessment

| # | Stage | Status | Evidence | Notes |
|---|-------|--------|----------|-------|
| 1 | Problem understanding | | | |
| 2 | Stakeholder understanding | | | |
| 3 | Questions and unknowns | | | |
| 4 | Evidence gathering | | | |
| 5 | Prior art scan | | | |
| 6 | Data reality check | | | |
| 7 | Concept refinement | | | |
| 8 | Feasibility and implementation path | | | |
| 9 | Validation plan | | | |
| 10 | Pilot readiness | | | |

## Summary
- Stages completed: X/10
- Stages skipped: [list]
- Stages faked: [list]
- Stages requiring human follow-up: [list]

## Fail Flags Triggered
- [list or NONE]

## What Was Fundamentally Missed
[1-3 sentences]

## What Must Be Fixed First
[ordered list]
```

---

## Notes

- Do not give credit for intent. A stage is `COMPLETE` only when the output exists and contains the required evidence.
- `INVALIDATED` is worse than `MISSING`. Missing means the team didn't do it. Invalidated means they did it wrong and the result is actively misleading.
- Most hackathon projects will score `MISSING` on stages 3, 5, 6, 9, and 10. This is expected and the whole reason this skill exists.
