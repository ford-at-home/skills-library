---
name: evidence-grounded-answering
description: "Answer user questions using only content actually present in this repository corpus, with explicit grounding and uncertainty marking."
---

> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# evidence_grounded_answering

Purpose: Answer user questions using only content actually present in this repository corpus, with explicit grounding and uncertainty marking.

## When To Use
- Any time a factual claim about Richmond programs, data, services, or DPW operations is being made
- When a user asks: "Does X exist?" "Is Y available?" "What does the City do about Z?"
- When an agent is about to state something it cannot directly verify from files it has read
- Before asserting that a dataset, API, program, service, or policy exists
- Before making any claim about GPS fleet data availability (D3=2 — infrastructure incomplete)

## Inputs
- User question
- Files read in current context
- Optional: `evidence_log.md` for verified claims

## Outputs
- Answer grounded in specific file content
- Inline citations for each substantive claim
- Explicit uncertainty markers for unverified statements
- "Not found" statements when information is absent

## Process

### Step 1 — Establish What Has Been Read

Before answering, state (internally or explicitly) which files have been read. Only make claims from those files. Do not interpolate from general knowledge about Richmond or civic tech.

### Step 2 — Classify Each Claim

For every substantive claim in your answer, classify it:

| Status | Meaning | Marker |
|--------|---------|--------|
| `Confirmed` | Present in a source file AND verified in `evidence_log.md` | No marker needed; cite source |
| `Stated in corpus` | Present in a research file but not independently verified | `(per [filename])` |
| `Uncertain` | Implied or summarized but not directly stated in a file read | `[Uncertain: implied by X but not stated directly]` |
| `Not found` | Not present in any file read | `[Not found in files read]` |
| `Requires reading` | Likely in a specific file that has not been read | `[Requires reading: filename]` |

### Step 3 — Check the Evidence Log

For claims about:
- Specific portal URLs and their capabilities (GeoHub, Open Data Portal, ArcGIS dashboards)
- GPS infrastructure status (incomplete as of March 2026)
- Data update cadences (e.g., Capital Project Dashboard updates quarterly)
- DPW operational facts (e.g., 832 center-lane miles of streets)
- Hackathon details (e.g., March 27–29, 2026 at VCU Snead Hall)

Cross-check `evidence_log.md`. If the claim has an `E-` entry with `Confirmed` status, you can cite it with high confidence. If the claim is not in the log, mark it `[Stated in corpus: not independently verified]`.

### Step 4 — Formulate the Answer

Structure:
1. Direct answer to the question
2. Supporting evidence with citations
3. Explicit uncertainty statements
4. What is NOT covered (to set expectations)

### Step 5 — Apply the Anti-Fabrication Check

Before finalizing the answer, run this check:

- Does every named government program or portal actually appear in a file I have read?
- Does every dataset I mentioned actually appear in D section files or `02_data/`?
- Does every URL I mentioned appear in `evidence_log.md` or a research file?
- Am I inventing specificity (exact percentages, exact dates, specific API endpoints) not present in the source?
- Am I claiming GPS fleet data is available? (It is NOT — flag D3=2 constraint)

If any check fails -> remove or mark the claim as `[Unverified]`.

### Step 6 — State Scope Limits

At the end of the answer, state:
- What files were used to answer this question
- What topics the answer does NOT cover because relevant files were not read

## Required Language

When information is absent, use:
- "This repository does not contain that information."
- "I cannot verify that from the files I have read in this session."
- "That would require reading [specific file] which I have not yet loaded."
- "[Unverified]: this appears in a summary but I have not read the source file."

Do NOT use:
- "Likely..." (without a citation)
- "Generally..." (as a hedge for an ungrounded claim)
- "It is common for cities to..." (implies external knowledge not in corpus)
- "I believe..." (implies opinion substituting for evidence)
- "Richmond probably has..." (speculative without a source)

## Critical Domain Constraint

GPS fleet data for Richmond DPW is **explicitly incomplete as of March 2026**. Any answer about fleet GPS tracking must include:
- `(per research/A2_problem_landscape_fleet_operations.md; confirmed evidence_log.md E-004)`
- Explicit statement that live GPS feeds are not available for hackathon prototypes
- Recommendation to use synthetic or schedule data instead

Failure to include this constraint when answering fleet-related questions is a fabrication error.

## Example

**Question:** "Is there a public ArcGIS layer showing Richmond DPW capital projects?"

**Grounded answer:**

Yes. Richmond's Capital Project Dashboard is a publicly accessible ArcGIS-based tool that centralizes capital project information from all city departments (per `research/D1_data_arcgis_dpw.md`; confirmed in `evidence_log.md` entry E-001). It is updated quarterly and displays projects that have received funding in planning, design, or construction phases (per D1). The dashboard includes project descriptions, locations, project managers, phases, and estimated completion dates (per D1).

Road centerlines are also available through the Richmond GeoHub as a "Centerlines" dataset, with VGIN Road Centerlines as a quarterly-updated fallback (per `research/D1_data_arcgis_dpw.md`).

However, construction permit activity does NOT appear to be available as a public GIS layer — `research/D1` notes it may be managed internally or through non-GIS portals. `[Requires reading: research/D2_data_open_data_portal.md for fuller assessment of Socrata-based datasets]`

*Files read for this answer: D1, evidence_log.md*
*Not covered: D2 (Open Data Portal), D3 (grant documentation), C2 (GeoHub landscape)*

## Anti-Patterns

- Never state a City program or portal exists without a source file citation
- Never quote a statistic (lane miles, percentage, processing time) without a source
- Never say "Richmond has X data" based only on index.json summaries
- Never blend confirmed and uncertain claims in the same sentence without differentiation
- Never claim GPS fleet data is available or will be available without citing a confirmed timeline
