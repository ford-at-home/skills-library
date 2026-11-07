---
name: pillar-pipeline
description: "A two-pipeline system that (A) evaluates hackathon submissions against the actual problem they were supposed to solve, and (B) independently discovers the highest-leverage opportunities from the problem statements themselves. Submissions are judged by the problem frame — not the other way around."
---

# Pillar Pipeline — Staged Recovery and Rebuild for Hackathon Submissions

**Purpose:** A two-pipeline system that (A) evaluates hackathon submissions against the actual problem they were supposed to solve, and (B) independently discovers the highest-leverage opportunities from the problem statements themselves. Submissions are judged by the problem frame — not the other way around.

**Design principle:** Start with problem statements, not demos. Build the evaluation frame first, then hold submissions against it. This flips from "how do we rescue these demos?" to "which demos are worth rescuing at all?"

---

## Phase 0 — Source-of-Truth Lock

Before anything else, establish the authority hierarchy. All downstream judgments derive from these sources, in this order:

1. `problem_statements/` or equivalent (breakout materials, MAP document)
2. Breakout transcript summaries
3. `INDEX.md`
4. `submissions/*`
5. `data/*`
6. `CONTACTS.md`
7. `skills/INNOVATION_LIFECYCLE/SKILL.md`
8. Other skills and templates

### Hard Fail Rules

These are non-negotiable. Any submission that triggers one gets flagged immediately:

| Flag | Condition |
|------|-----------|
| `FAIL_MISALIGNED` | Submission solves something different from the stated problem |
| `FAIL_DEMO_DATA` | Depends on fake, mock, synthetic, or hand-entered data without a real acquisition path |
| `FAIL_UNVALIDATED` | Skips external validation with a real SME where data access or operational cadence matters |
| `FAIL_NO_PRIOR_ART_SCAN` | No evidence team researched what already exists |
| `FAIL_NO_SME_PATH` | No identified path to the human who can confirm feasibility |
| `FAIL_NO_REAL_IMPLEMENTATION_PATH` | No believable route from current state to pilot |

A submission with a fail flag is not dead — it's classified. The flag tells you what must be fixed first.

---

## Pipeline A — Submission Review (Phases 1–10)

### Phase 1 — Inventory and Normalize

**Goal:** Create a structured manifest of everything in the repo.

For each project in `ideas/`, extract:
- Project name
- Team name if present
- Linked pillar, linked problem statement, and source type (from `README.md` when present, else `INDEX.md` / other artifacts)
- Summary from `INDEX.md` or `README.md`
- Repo path
- Demo asset: `demo.mp4` when present (often linked from `README.md`)
- Datasets referenced
- Claimed users
- Claimed outcomes
- Obvious gaps (missing video, wrong format, dead links)

**Output:**
- `artifacts/submission_manifest.json`
- `artifacts/submission_manifest.md`

**Also read:**
- Each pillar's research corpus lives in its own GitHub repo. For example: `https://github.com/hack4rva/pillar-thriving-built-environment/blob/main/research/INDEX.md`
- Each demo transcript is co-located with the idea: `ideas/{pillar}/{project}/IDEA.md`

---

### Phase 2 — Problem-Fit Reconstruction

For each submission, reconstruct what the problem actually requires by reading the source-of-truth materials (not the demo).

**Steps:**
1. Read the exact problem statement from MAP / breakout materials
2. Read the breakout transcript summary
3. Derive: target user, core JTBD, operational environment, constraints, success conditions, known stakeholders, explicit non-goals

**Output per project:** `ideas/<pillar>/<project_slug>/01_problem_fit.md`

**Template:**

```md
# Problem Fit Review

## Submission
- Name:
- Path:
- Pillar:
- Problem statement:

## Source of Truth Summary
- Primary user:
- Core problem:
- Context:
- Constraints:
- Desired outcomes:
- Non-goals:

## Alignment Assessment
- What the team appears to have built:
- What the problem actually requires:
- Alignment score (1-5):
- Misalignments:
- Missing assumptions:
- Verdict: [ALIGNED | PARTIAL | MISALIGNED | FAIL_MISALIGNED]
```

---

### Phase 3 — Innovation Lifecycle Gap Analysis

Use `skills/INNOVATION_LIFECYCLE/SKILL.md` as the canonical lifecycle. Force every project through each stage.

**The 10 stages:**

1. Problem understanding
2. Stakeholder understanding
3. Questions and unknowns
4. Evidence gathering
5. Prior art scan
6. Data reality check
7. Concept refinement
8. Feasibility and implementation path
9. Validation plan
10. Pilot readiness

For each submission, assess:
- Which stages were completed?
- Which were skipped?
- Which were faked?
- Which require human follow-up?

**Scoring per stage:** `COMPLETE` | `PARTIAL` | `MISSING` | `INVALIDATED`

**Output per project:** `ideas/<pillar>/<project_slug>/02_lifecycle_gap_analysis.md`

---

### Phase 4 — Question Generation

For each problem statement, generate three classes of questions:

**A. Clarification questions**
- What does the city/nonprofit actually mean here?
- What constraint mattered most in the breakout?
- What would count as success in 90 days?

**B. Data questions**
- What system holds the real data?
- Who owns it? How often is it updated?
- API, export, manual report, or vendor system?
- Access process? Privacy/compliance constraints?
- Known data quality issues?

**C. Operational questions**
- Who would use this in practice?
- How does work happen today?
- What breaks if this tool is wrong?
- What is the approval path for adoption?

**Output:** `research/questions/<problem_slug>.md`

---

### Phase 5 — Split Questions by Answer Path

Every question gets routed to one of three destinations:

| Route | Use for |
|-------|---------|
| `web` | Public material, prior art, case studies, academic lit, municipal docs, vendor docs, open data, procurement records, regional pilots |
| `sme` | Non-public workflows, real data access, update cadence, internal approval paths, operational nuance, policy/legal constraints, "how does Richmond actually do this today?" |
| `local_data` | When the answer may already exist in `/data` |

**Output:** `research/question_router.json`

**Schema per question:**

```json
{
  "question": "",
  "problem_slug": "",
  "route": "web|sme|local_data",
  "reason": "",
  "owner": "",
  "status": "pending|answered|blocked"
}
```

---

### Phase 6 — SME Outreach Generation

From `CONTACTS.md`, match `sme`-routed questions to people:
- Nonprofit SMEs for lived experience and program delivery
- City staff for systems, process, data, and feasibility
- Optional regional operators for prior implementation lessons

**Invoke:** `skills/research-grounded-outreach/SKILL.md` (leads with confirmed findings, asks only genuinely unanswered questions)

**Output structure:**
```
outreach/
├── city/
├── nonprofit/
├── followups/
└── CONTACT_LOG.md
```

Also maintain `outreach/CONTACT_LOG.md`:

```md
| Contact | Org | Questions | Email File | Sent | Response |
|---------|-----|-----------|------------|------|----------|
```

---

### Phase 7 — Parallel-Style Deep Research Jobs

Create research jobs only for `web`-routed questions from Phase 5.

Each research job includes:
- Problem statement excerpt
- Breakout summary excerpt
- Exact question
- Why it matters
- Desired output format
- Richmond/regional relevance requirement
- Prior art requirement
- Implementation reality requirement

**Master research prompt:**

```md
You are conducting implementation-oriented civic innovation research.

Use the following as the sole framing source of truth:
1. The original problem statement
2. The breakout transcript summary

Your job is not to brainstorm freely. Your job is to reduce uncertainty.

Research question: [INSERT]

Context:
- Pillar:
- Problem statement:
- Breakout summary:
- Current submission concept:
- Known constraints:
- No demo data allowed
- Any viable solution must identify real data sources, ownership, cadence, and access path
- Regional and municipal prior art is especially important

Research requirements:
1. Identify existing products, pilots, or public-sector efforts addressing this problem
2. Prioritize Richmond, Virginia, Mid-Atlantic, and comparable U.S. cities
3. Identify real datasets or systems that could support the workflow
4. Note whether data appears public, restricted, internal, vendor-held, or unclear
5. Identify key operational constraints, procurement barriers, privacy concerns, and adoption blockers
6. Distinguish clearly between what is proven, plausible, and unknown
7. Flag anything that would require SME confirmation

Return in this format:
## Answer Summary
## Prior Art and Comparable Projects
## Data Sources
## Operational Constraints
## Richmond/Regional Relevance
## What Remains Unknown
## Specific Follow-up Questions for SMEs
## Citations
```

**Fire with:** `parallel-cli research run "<prompt>" --no-wait -o research/findings/<problem_slug>/<question_slug>`

**Output:**
```
research/
├── jobs/<problem_slug>/<question_slug>.md      (prompts)
├── findings/<problem_slug>/<question_slug>.md   (results)
└── question_router.json                         (master index)
```

---

### Phase 8 — Local Data Audit

For anything in `/data`, produce:
- Filename
- Apparent schema
- Owner if inferable
- Freshness
- Likely use case
- Limits
- Whether it is sufficient for real deployment

**Critical rule:** If data in `/data` does not establish real system access and real refresh cadence, it does not satisfy the "no demo data" rule.

**Output:**
- `data_audit/<file>.md` per file
- `data_audit/summary.md`

---

### Phase 9 — Submission Review Rubric

Score each submission 1-5 on 10 dimensions unless a fail flag applies:

| Dimension | Question |
|-----------|----------|
| Problem fidelity | Does it solve the actual stated problem? |
| User realism | Does it reflect a real user, real workflow, real constraints? |
| Evidence base | Grounded in research, stakeholder input, or comparable prior art? |
| Data realism | Identifies real data sources, ownership, access path, and cadence? |
| Operational feasibility | Could a city department or nonprofit plausibly pilot this? |
| Implementation clarity | Is there a believable path from current state to pilot? |
| Novelty with prior art awareness | Meaningfully differentiated from what already exists? |
| Risk awareness | Acknowledges privacy, legal, policy, procurement, staffing, trust risks? |
| Validation readiness | Are the next validation steps obvious and grounded? |
| Overall civic usefulness | Would this materially improve the condition described? |

**Output per project:** `ideas/<pillar>/<project_slug>/03_rubric.md`

**Template:**

```md
# Submission Review Rubric

## Scores
| Dimension | Score | Notes |
|---|---:|---|
| Problem fidelity |  |  |
| User realism |  |  |
| Evidence base |  |  |
| Data realism |  |  |
| Operational feasibility |  |  |
| Implementation clarity |  |  |
| Novelty with prior art awareness |  |  |
| Risk awareness |  |  |
| Validation readiness |  |  |
| Overall civic usefulness |  |  |

## Fail Flags
- [FAIL_MISALIGNED | FAIL_DEMO_DATA | FAIL_UNVALIDATED | FAIL_NO_PRIOR_ART_SCAN | FAIL_NO_SME_PATH | FAIL_NO_REAL_IMPLEMENTATION_PATH | NONE]

## Summary
- Strongest part:
- Weakest part:
- What was fundamentally missed:
- What must be fixed first:
```

---

### Phase 10 — Ralph Loop Quality Pass

Two-pass adversarial review. Invoke `skills/ralph-loop/SKILL.md`.

**Pass 1 — Completeness check:**
- Did the review actually use the source-of-truth artifacts?
- Were all 10 lifecycle stages evaluated?
- Was every major unknown routed?
- Were fail flags applied consistently?

**Pass 2 — Backward correction:**
- What did we falsely assume?
- Where did we let the demo bias the review?
- What evidence is still missing?
- What must be reworked upstream?

**Output per project:** `ideas/<pillar>/<project_slug>/04_ralph_loop.md`

**Template:**

```md
# Ralph Loop Review

## Pass 1: Completeness
- Missing sections:
- Unsupported claims:
- Questions not routed:
- Sources ignored:

## Pass 2: Backward Correction
- Fundamental miss:
- Invalid assumptions:
- Demo-data violations:
- Missing stakeholder validation:
- Required rework:

## Final Status
[READY_FOR_REWORK | BLOCKED_ON_SME | BLOCKED_ON_DATA_ACCESS | FAIL]
```

### Decision Gate

After Phase 10, classify each project:

| Classification | Meaning |
|---------------|---------|
| **Adopt** | Already strong — refine only |
| **Repair** | Promising but skipped core lifecycle steps |
| **Reframe** | Interesting build, wrong problem |
| **Archive** | Demo-only, no real path |
| **Spin out** | Valuable question, not yet a product |

Without this gate, the pipeline produces a museum of markdown files. The gate forces a decision.

---

## Pipeline B — Opportunity Discovery (runs separately)

This pipeline runs independently from submission review because some teams built shiny side quests instead of the highest-leverage opportunities. Start from the problem statement, not from what was built.

### Step A — Create 3 JTBD per Problem Statement

For each problem statement, generate 3 jobs to be done:
- One functional
- One emotional / trust-based
- One systems / coordination-oriented

**Template:**

```md
# Jobs To Be Done

## Problem Statement
[exact text]

## JTBD 1: Functional
When [situation], I want to [motivation], so I can [outcome].

## JTBD 2: Emotional / trust
When [situation], I want to [motivation], so I can [outcome].

## JTBD 3: Systems / coordination
When [situation], I want to [motivation], so I can [outcome].
```

**Output:** `opportunity_analysis/<problem_slug>/01_jtbd.md`

### Step B — Pain Point Research from JTBD

For each JTBD, run deep research:
- Where does this job currently break down?
- What frictions do residents, staff, nonprofits, or businesses face?
- What workarounds exist?
- Where are delays, opacity, mistrust, duplication, or access failures?

**Research prompt:**

```md
Research the pain points associated with this job to be done in a civic or public-service context.

Job to be done: [INSERT]

Requirements:
1. Identify concrete failure points in the current journey
2. Prioritize municipal, nonprofit, education, mobility, housing, or public-service contexts
3. Include resident pain, staff pain, and institutional pain
4. Look for evidence from Richmond first, then Virginia, then comparable U.S. cities
5. Identify where trust, transparency, data access, and coordination break down
6. Distinguish observed pain points from inferred ones
7. Highlight any pain point that appears repeatedly across sources

Return:
## Pain Points
## Who Experiences Them
## Existing Workarounds
## Evidence
## Unknowns
## Implications for Solution Design
```

**Output:** `opportunity_analysis/<problem_slug>/02_pain_points.md`

### Step C — Prior Art First, Always

Before ideating, force a prior art scan.

**Research prompt:**

```md
Research prior art relevant to this civic problem.

Problem statement: [INSERT]
Jobs to be done: [INSERT JTBDs]
Pain points: [INSERT SUMMARY]

Requirements:
1. Identify existing products, nonprofits, municipal programs, pilots, academic projects, and regional initiatives
2. Prioritize Richmond, Virginia, DC, North Carolina, Maryland, and comparable midsize cities
3. Note whether each effort is active, sunset, pilot-only, or unclear
4. For each, explain what it solved, what it missed, and why adoption may have stalled
5. Identify whether the problem is already 80-99% solved somewhere
6. If so, shift from "invent" to "adapt, integrate, or improve"

Return:
## Prior Art Inventory
## Regional Comparables
## Likely Reasons This Hasn't Fully Worked Yet
## Reusable Patterns
## Gaps Still Open
```

**Output:** `opportunity_analysis/<problem_slug>/03_prior_art.md`

### Step D — Generate 10 Solution Ideas

Only after JTBD + pain points + prior art.

Each idea must include:
- Target user
- Pain point addressed
- Prior art it builds on
- What is actually new
- Real data dependency
- Implementation path
- Why it may have failed before
- What Richmond-specific condition makes it more viable now

**Template per idea:**

```md
## Idea N: [Name]
- **User:** [specific person, not abstract persona]
- **JTBD addressed:** [which job]
- **Pain point addressed:** [which pain]
- **Prior art it builds on:** [what exists]
- **What is new here:** [genuine differentiation]
- **Required real data:** [specific sources]
- **Required SME partners:** [who]
- **Pilot path:** [first 90 days]
- **Key risks:** [what could kill it]
- **Why this might work now:** [Richmond-specific conditions]
```

**Output:** `opportunity_analysis/<problem_slug>/04_solution_ideas.md`

---

## Master Orchestrator Prompt

Include this in any agent dispatch to set the operating context:

```md
You are an implementation-focused civic innovation reviewer operating on a repository of hackathon submissions.

Your job is to review, repair, and extend project ideas by forcing them through a complete innovation lifecycle.

# Non-negotiable rules

1. The sole source of truth is:
   - problem statements
   - breakout transcript summaries
   Work backward from those at all times.
   If a submission does not solve the problem as actually stated, it fails.

2. No demo data.
   Any solution that depends on fake, mock, manually-entered, synthetic, or non-operational data is invalid until a real data source, access path, and update cadence are established with a human SME.

3. Use the core skills: INNOVATION_LIFECYCLE.md, jtbd-research, prior-art-regional-research, research-grounded-outreach, ralph-loop.

4. CONTACTS.md identifies people who may answer questions that cannot be resolved from web research or local files.

5. Every substantive claim must be tied to one of: problem statement, breakout transcript summary, local data file, web research finding, or SME outreach target. Do not make unsupported assumptions. When uncertain, write: [Unverified], [Requires SME confirmation], [Data access path unknown], [Operational cadence unknown].

6. At the end of each project review, assign one status:
   PASS | READY_FOR_REWORK | BLOCKED_ON_SME | BLOCKED_ON_DATA_ACCESS | FAIL

7. At the end of the full review, assign one classification:
   Adopt | Repair | Reframe | Archive | Spin out into research
```

---

## Execution Order

The structural inversion matters. Do not start with submissions.

```
1. Lock source of truth                    (Phase 0)
2. Read problem statements + breakouts     (Phase 0)
3. Create JTBD + pain points + prior art   (Pipeline B: Steps A-C)
4. Inventory submissions                   (Phase 1)
5. Problem-fit reconstruction              (Phase 2)
6. Lifecycle gap analysis                  (Phase 3)
7. Question generation                     (Phase 4)
8. Question routing                        (Phase 5)
9. SME outreach generation                 (Phase 6)
10. Deep research jobs                     (Phase 7)
11. Local data audit                       (Phase 8)
12. Rubric scoring                         (Phase 9)
13. Ralph loop                             (Phase 10)
14. Decision gate                          (Phase 10 output)
15. Generate opportunity ideas             (Pipeline B: Step D)
```

Steps 3 and 4-14 can overlap — Pipeline B starts first and informs Pipeline A, but they produce independent outputs.

---

## Output Summary

```
artifacts/
├── submission_manifest.json
└── submission_manifest.md

ideas/<pillar>/<project_slug>/
├── IDEA.md                          (base — every idea dir)
├── README.md                        (base — pillar, problem statement, source type, team, links to `_shared-*` research)
├── RESEARCH_RESULT.md               (base when present)
├── INNOVATION_ANALYSIS.md           (base when present)
├── demo.mp4                         (optional)
├── …                                (optional: shared-research mirrors, lifecycle notes, etc.)
├── 01_problem_fit.md                (pipeline output)
├── 02_lifecycle_gap_analysis.md
├── 03_rubric.md
└── 04_ralph_loop.md

research/
├── questions/<problem_slug>.md
├── question_router.json
├── jobs/<problem_slug>/<question_slug>.md
└── findings/<problem_slug>/<question_slug>.md

outreach/
├── city/
├── nonprofit/
├── followups/
└── CONTACT_LOG.md

data_audit/
├── <file>.md
└── summary.md

opportunity_analysis/<problem_slug>/
├── 01_jtbd.md
├── 02_pain_points.md
├── 03_prior_art.md
└── 04_solution_ideas.md
```

---

## Prerequisites

- `PARALLEL_API_KEY` available in environment (source from parent workspace `.env` if needed)
- Pillar research corpus in each pillar's GitHub repo — e.g. `https://github.com/hack4rva/pillar-{slug}/blob/main/research/INDEX.md`
- Demo narrative in `ideas/{pillar}/{project}/IDEA.md`; demo video typically `demo.mp4` (see `README.md` for links)
- `CONTACTS.md` with SME entries
- Problem statements from MAP / breakout materials

## Load the API Key

```bash
# Source from environment or parent workspace .env
export PARALLEL_API_KEY=<key>
```

---

## Pillar Slug Map

| Pillar | Slug | Research Corpus |
|--------|------|-----------------|
| A Thriving City Hall | `thriving-city-hall` | [pillar-thriving-city-hall](https://github.com/hack4rva/pillar-thriving-city-hall) |
| Thriving Neighborhoods | `thriving-neighborhoods` | [pillar-thriving-neighborhoods](https://github.com/hack4rva/pillar-thriving-neighborhoods) |
| Thriving Families | `thriving-families` | [pillar-thriving-families](https://github.com/hack4rva/pillar-thriving-families) |
| A Thriving Economy | `thriving-economy` | [pillar-thriving-economy](https://github.com/hack4rva/pillar-thriving-economy) |
| Thriving and Inclusive Communities | `thriving-inclusive-communities` | [pillar-thriving-inclusive-communities](https://github.com/hack4rva/pillar-thriving-inclusive-communities) |
| A Thriving and Sustainable Built Environment | `thriving-built-environment` | [pillar-thriving-built-environment](https://github.com/hack4rva/pillar-thriving-built-environment) |
| A City That Tells Its Stories | `city-storytelling` | [pillar-city-storytelling](https://github.com/hack4rva/pillar-city-storytelling) |

## Pipeline C — Post-Lifecycle Extensions

After Pipelines A and B are complete, two additional layers sharpen the output.

### Step E — Blue Ocean ERRC Ideation

Apply `pillar-repos/*/skills/blue_ocean_reframing/SKILL.md` to JTBD + pain points from Pipeline B.

- Generate 1-2 non-duplicative ideas per pillar using Eliminate/Reduce/Raise/Create reframing
- Score with the same desirability rubric used for NEW_IDEAS

**Output per pillar:**
- `ideas/<pillar>/NEW_IDEAS_BLUESKY.md`
- `ideas/<pillar>/NEW_IDEAS_BLUESKY_RUBRIC_GRADES.md`

### Step F — Implementation Reality Scoring

Apply `ideas/IMPLEMENTATION_REALITY_RUBRIC.md` against `ideas/RICHMOND_TECH_STACK_2026.md` to score ALL ideas (demos + NEW_IDEAS + BLUESKY) on 5 survivability dimensions.

**Output:**
- `ideas/<pillar>/IMPLEMENTATION_REALITY_REVIEW.md` (per pillar)
- `ideas/IMPLEMENTATION_REALITY_SYNTHESIS.md` (cross-pillar rankings, infrastructure bundles, structural walls)

---

## Completion Checklist

- [ ] Source-of-truth lock established
- [ ] Problem statements and breakout summaries read
- [ ] Pipeline B JTBD + pain points + prior art complete
- [ ] Submission manifest created
- [ ] Per-project problem fit assessed
- [ ] All lifecycle stages evaluated with COMPLETE/PARTIAL/MISSING/INVALIDATED
- [ ] All questions generated and routed (web/sme/local_data)
- [ ] SME outreach emails drafted, CONTACT_LOG updated
- [ ] Deep research jobs fired, polled, results saved
- [ ] Local data audit complete
- [ ] Rubric scored, fail flags applied
- [ ] Ralph loop 2-pass review complete
- [ ] Decision gate classification assigned per project
- [ ] Opportunity ideas generated from Pipeline B
- [ ] Blue Ocean ERRC ideas generated and scored (Pipeline C, Step E)
- [ ] Implementation Reality scores applied to all ideas (Pipeline C, Step F)
- [ ] Cross-pillar synthesis produced
