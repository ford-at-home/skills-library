---
name: research-corpus-navigation
description: "Map a user question to the correct pillar section and specific research reports before attempting to answer."
---

> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# research_corpus_navigation

Purpose: Map a user question to the correct pillar section and specific research reports before attempting to answer.

## When To Use
- A user asks any research question about Richmond's built environment problem space
- A user asks about a specific problem domain (infrastructure project visibility, fleet operations, DPW data, accessibility)
- A user asks what reports to read
- An agent needs to determine which files are relevant before answering

## Inputs
- User question or information need (natural language)

## Outputs
- Identified section(s) from the research corpus
- List of specific files to read (in recommended order)
- Brief explanation of why each file is relevant
- Any files that must be read before answering (prerequisites)

## Process

### Step 1 — Load Navigation Artifacts

Before looking at any research file, load:
1. `research/index.json` — scan all summaries and key_terms
2. If the corpus is unfamiliar: read `CORPUS_GUIDE.md` first

Do NOT skip this step and dive directly into research files.

### Step 2 — Classify the Question

Determine which category the user question falls into:

| Question Category | Relevant Sections |
|------------------|------------------|
| "What problems exist in this space?" | Section A (A1–A5) |
| "Who are the users or stakeholders?" | Section B (B1–B5) |
| "What services or programs exist?" | Section C (C1–C5) |
| "What public data is available?" | Section D (D1–D5), `02_data/` |
| "What has been built elsewhere?" | Section E (E1–E5) |
| "What should we build?" | Section F (F1–F5) |
| "What could go wrong?" | Section G (G1–G5) |
| "Is this feasible for a weekend?" | Section H (H1–H5) |
| "How should we demo this?" | Section I (I1–I5) |
| "What is the overall picture?" | `research/00_pillar_summary_context.md` |
| "What datasets or APIs are mentioned?" | D1, D2, D3, `02_data/source_inventory.csv` |
| "Transportation Project Visibility specific" | A1, A3, A4, B1, D1, D2, F2, H1, H2 |
| "Fleet Operations specific" | A2, A3, B2, D4, D5, F3, H3, H4, G2 |
| "GPS or synthetic data" | D4, D5, G2, H4 |
| "Accessibility concerns" | B5, G3 |
| "Risk or guardrails" | G1–G5, `research/92_red_flags.md` |
| "Transparency theory / asymmetry / private-sector paradigms" | J1–J3 |
| "Utility outages, work orders, smart-city sensing, predictive restoration" | K1–K4 |
| "Data models for service tracking (requests, assets, workforce, context)" | L1–L4 |
| "Simulation: ETA, queues, routes, outage duration" | M1–M2 |
| "Cross-city open data, 311 APIs, free-tier utility/weather/geo" | N1–N2 |
| "GIS + work-order or realtime / digital-twin architecture" | O1–O2 |
| "Consumer-grade civic tracking UX (Domino's-style)" | P1 |
| "Ghost dashboards, gaps, innovation synthesis" | Q1, E4, `research/92_red_flags.md` |

### Step 3 — Search `research/index.json`

Scan the `key_terms` and `summary` fields for matches to the user's question. Identify:
- High-confidence matches (3+ matching key_terms)
- Medium-confidence matches (1–2 matching key_terms)
- Files worth reading despite no term match (based on section relevance)

### Step 4 — Build a Reading List

Order files by:
1. Direct relevance to the question
2. Section order (earlier sections provide context for later ones)
3. Files mentioned in `CORPUS_GUIDE.md` recommended reading orders

Limit the initial reading list to 5 files maximum. If more are needed after reading, say so.

### Step 5 — Identify Prerequisites

Some questions require reading prerequisite files:
- Any question requiring context about Richmond's built environment -> read `00_pillar_summary_context.md` first
- Any question about specific DPW services -> read C1 before C2–C5
- Any question about data -> read D1 before D2–D5
- Any question requiring problem framing -> read A1 or A2 before F or H sections
- Any fleet or GPS question -> flag D3=2 constraint (GPS infrastructure incomplete as of March 2026)

Flag prerequisites explicitly.

### Step 6 — Output the Navigation Result

Return:
```
Relevant section(s): [X, Y]
Files to read (in order):
  1. research/[FILE].md — [one-sentence reason why]
  2. research/[FILE].md — [one-sentence reason why]
  3. ...

Prerequisites (read these first if not yet read):
  - research/[FILE].md — [reason]

Files to skip (and why):
  - [Section] — not relevant because [reason]
```

### Step 7 — Confirm Scope Boundaries

After delivering the reading list, state:
- What sections were NOT included and why (to confirm you didn't miss something)
- Whether cross-report synthesis will be needed
- Whether any answer requires verified facts from `evidence_log.md`

## Important Domain Constraints

When navigating questions about fleet or GPS topics, always flag:
- GPS infrastructure for Richmond DPW fleet is **explicitly incomplete as of March 2026**
- Any fleet visibility MVP should use synthetic or schedule data, not live GPS
- Reference: `research/A2_problem_landscape_fleet_operations.md` and `research/G2_risks_gps_dependency.md`

## Example

**Question:** "What ArcGIS data can we use to build a project finder?"

**Navigation result:**
```
Relevant sections: D (Data Sources), C (Services & Programs)

Files to read (in order):
  1. research/D1_data_arcgis_dpw.md — primary source on GeoHub layers for project data
  2. research/C2_services_arcgis_landscape.md — public inventory, quality, and API playbook
  3. research/H1_mvp_48hr_framework.md — how to wire ArcGIS FeatureService to a Leaflet map
  4. 02_data/source_inventory.csv — verified data source list with access details

Prerequisites: none (D1 is the logical starting point)

Files to skip: B, E, F, G, I — not directly relevant to data availability question

Verified facts to check: evidence_log.md (E-001 covers GeoHub; E-002 covers Open Data Portal)
```
