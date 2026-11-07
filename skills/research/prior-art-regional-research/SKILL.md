---
name: prior-art-regional-research
description: "Research what has already been built — regionally and nationally — before generating solution ideas. Ensures ideas are grounded in what is known to work, what has been tried and failed, and what Richmond could adopt or adapt rather than rebuild from scratch."
---

# prior-art-regional-research

**Purpose:** Research what has already been built — regionally and nationally — before generating solution ideas. Ensures ideas are grounded in what is known to work, what has been tried and failed, and what Richmond could adopt or adapt rather than rebuild from scratch.

**Part of:** Phase 2 (Step 4) of `skills/pillar-pipeline/SKILL.md`
**Note:** Check the pillar research corpus FIRST — each pillar's research is in its own GitHub repo. For example: `https://github.com/hack4rva/pillar-thriving-built-environment/tree/main/research/`. Each pillar has 50+ existing research reports. Synthesize the existing corpus before firing new Parallel AI queries. The `jtbd-research` skill (Phase 3) handles deeper research on specific open questions.
**API Key:** Source from environment or parent workspace `.env`.

## When To Use
- Before generating solution ideas for any problem statement (always before step 10 of INNOVATION_LIFECYCLE)
- When evaluating whether a hackathon demo is original or replicating existing work
- When identifying civic technology vendors, open-source tools, or peer city implementations
- When asking "why hasn't this been done in Richmond?" — the answer requires knowing what exists

## Critical Rule
Run this skill BEFORE ideation. Ideas generated without prior art knowledge are likely to duplicate failed attempts, reinvent solved problems, or miss a 99%-implemented solution that needs only an adoption decision.

## Inputs
- Problem statement (verbatim)
- Pillar name
- Optional: list of comparable cities (Richmond is a mid-sized Southern city; good comparables are Baltimore, Pittsburgh, Louisville, Norfolk, Raleigh, Durham, Chattanooga, New Orleans)

## Outputs
- Shared problem-statement-level research: `ideas/[pillar]/_shared-[problem]/prior_art_research.md`
- Idea-specific research: `ideas/[pillar]/[idea-slug]/prior_art_research.md`

---

## Process

### Step 1 — Frame three research queries
For any problem statement, generate exactly three Parallel AI deep research queries:

**Query 1 — Regional implementations:**
> "What civic technology projects, tools, or platforms have been implemented in US mid-sized cities to solve [problem statement paraphrase]? Focus on Richmond VA, Baltimore, Pittsburgh, Louisville, Norfolk, Raleigh, Durham, Chattanooga, and New Orleans. Include open-source tools, vendor solutions, city-built platforms, and failed attempts. Note which are live vs. sunset."

**Query 2 — Real data sources:**
> "What public data sources exist in Richmond Virginia relevant to [problem statement]? Include Richmond Open Data Portal (data.richmondgov.com), Richmond GeoHub (ags.richmond.gov), Legistar API, VDOT open data, Virginia state data portals, and relevant federal datasets (HUD, Census, FHWA). For each: name the dataset, its update cadence, and its API or download access method."

**Query 3 — Known failure modes and equity dimensions:**
> "What are the documented failure modes, adoption barriers, and equity gaps for civic technology solutions addressing [problem statement]? Include research on digital divide, language access, trust barriers, and which user groups tend to be excluded from these tools."

### Step 2 — Run with Parallel AI
Invoke the `parallel-deep-research` skill for each query. Use processor `pro-fast` for default depth.
Save results to `prior_art_research.md`.

### Step 3 — Synthesize findings
After all three results are returned, write a synthesis section answering:
1. What already exists that Richmond could adopt or adapt? (List 3–5 specific tools or implementations)
2. What has been tried and failed — and why?
3. What data sources are confirmed real and accessible?
4. What user groups are systematically excluded by existing approaches?
5. What is the biggest gap in the prior art that represents a genuine opportunity?

### Step 4 — Output structure

```markdown
# Prior Art Research — [Problem Statement]

**Pillar:** [pillar]
**Date:** [date]
**Processor:** [Parallel AI processor used]

---

## Query 1: Regional Implementations
[Parallel AI output]

## Query 2: Real Data Sources
[Parallel AI output]

## Query 3: Failure Modes and Equity Gaps
[Parallel AI output]

---

## Synthesis

### What Richmond Could Adopt or Adapt
1. [Tool/implementation name] — [city] — [link if available] — [why it's relevant]
2. ...

### What Has Failed and Why
- [Example + reason]

### Confirmed Real Data Sources
| Dataset | Owner | Access | Cadence |
|---------|-------|--------|---------|
| | | | |

### User Groups Systematically Excluded
- [Group] — [reason] — [implication for design]

### Biggest Gap / Genuine Opportunity
[1–2 sentences]
```

---

## Notes
- If Parallel AI is unavailable, use the `parallel-web-search` skill as a fallback for each query separately.
- Always check the pillar's research index before running new research — each pillar repo (e.g. `https://github.com/hack4rva/pillar-{slug}/blob/main/research/INDEX.md`) may already have extensive coverage.
- The synthesis section is the most important output. Raw Parallel AI results are evidence; the synthesis is the insight.
