---
name: cross-report-synthesis
description: "Synthesize findings from multiple research reports into a coherent answer while preserving source traceability and acknowledging uncertainty."
---

> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# cross_report_synthesis

Purpose: Synthesize findings from multiple research reports into a coherent answer while preserving source traceability and acknowledging uncertainty.

## When To Use
- A user asks a question that spans multiple reports or sections
- A team needs a summary of findings across a problem domain
- An agent needs to answer: "What does the research say about X across all relevant reports?"
- A user asks for a synthesis of risks, opportunities, or data sources
- A team is deciding between Transportation Project Visibility and Fleet Operations Visibility and needs a cross-report comparison

## Inputs
- User question or synthesis goal
- List of relevant report files (from `research_corpus_navigation` skill)
- Access to the source `.md` files

## Outputs
- Synthesized answer with per-claim source citations
- Tensions or contradictions noted explicitly
- Confidence level per claim (confirmed, likely, uncertain)
- List of reports read vs. reports not read
- Identified gaps where synthesis is incomplete

## Process

### Step 1 — Load Navigation Context

Before synthesizing, confirm you have run `research_corpus_navigation` or equivalent to identify which files are relevant. Do not synthesize from random file selections.

### Step 2 — Read Source Files Fully

For each file in the reading list:
1. Read the full `.md` file (not just summaries or frontmatter)
2. Note specific claims, data points, named entities, and source citations
3. Note the confidence level of each claim: does the report cite a primary source, or is it a secondary synthesis?

Do NOT synthesize from index.json summaries alone. Summaries are navigation aids, not authoritative content.

### Step 3 — Build a Claim Map

For each substantive claim you plan to include:

```
Claim: [statement]
Source: [filename, section heading if helpful]
Confidence: confirmed | likely | uncertain
Primary source: [URL or citation if available in the report]
Conflicts with: [other report + how it conflicts, if applicable]
```

### Step 4 — Identify Tensions and Gaps

Before writing the synthesis, explicitly check:
- Do any reports contradict each other? (If so, note both positions and their sources)
- Are there claims that appear in one report but are absent from others where you would expect them?
- Are there questions that the reports together still do not answer?

Flag gaps with: `[Gap: no report in this corpus addresses X]`

Pay particular attention to the GPS infrastructure constraint — reports may differ on timeline or scope. Always flag: GPS is incomplete as of March 2026 per `research/A2_problem_landscape_fleet_operations.md`.

### Step 5 — Write the Synthesis

Structure:
1. **Scope**: which files were read, which were not
2. **Main findings**: 3–7 bullet points with inline citations
3. **Tensions**: any conflicting information and its sources
4. **Gaps**: what the corpus does not cover
5. **Confidence summary**: overall confidence in the synthesis

### Citation Format

Use inline citations:
- `(per research/A1_problem_landscape_infrastructure_visibility.md)`
- `(per evidence_log.md, E-001)`
- `[Unverified: not found in files read]`
- `[Uncertain: mentioned in summary but not verified in source]`

Never blend claims from different sources into a single uncited sentence.

### Step 6 — State What Was NOT Read

Always end the synthesis with:

```
Files read for this synthesis:
  - research/[FILE].md
  - research/[FILE].md

Files not read (possibly relevant):
  - research/[FILE].md — reason it may contain relevant information
```

This allows the user or a future agent to know the synthesis is incomplete if additional files exist.

## Anti-Patterns to Avoid

- **Never** synthesize from index.json summaries alone
- **Never** blend claims from different reports without attribution
- **Never** omit tensions or contradictions to make the answer cleaner
- **Never** claim the synthesis is complete if relevant unread files exist
- **Never** invent figures or statistics not present in the source files
- **Never** claim GPS fleet data is available — flag the D3=2 constraint explicitly

## Example Output Structure

```
**Synthesis: Data Availability for a DPW Project Finder**

Files read: A1, D1, D2, C2, 02_data/source_inventory.csv
Files not read (possibly relevant): D3 (grant documentation), D4 (GPS schema)

**Main Findings**
1. Capital Project Dashboard aggregates active, funded projects across departments, updated quarterly, and is accessible via ArcGIS public dashboard (per D1; confirmed in evidence_log E-001).
2. Road centerlines are available through Richmond GeoHub and as a reliable fallback via VGIN quarterly updates (per D1).
3. VDOT crash data is publicly accessible via REST API and is already consumed by Richmond's Vision Zero dashboard (per D1).
4. Construction permit data is NOT available as a public GIS layer — likely managed internally or through non-GIS portals (per D1; confirmed gap).
5. Socrata-based Open Data Portal at data.richmondgov.com contains DPW-relevant datasets (per D2; confirmed in evidence_log E-002).

**Tensions**
- D1 identifies road centerlines as available but notes city attributes and currency are unknown; VGIN is the recommended reliable fallback [Uncertain — D5 data quality report not yet read].

**Gaps**
- [Gap: no report read addresses whether the Capital Project Dashboard exposes a public REST API for direct queries vs. requiring manual dashboard interaction]

**Confidence: Moderate** — core data layers confirmed; D5 and D3 not read, so data quality and grant context are incomplete.
```
