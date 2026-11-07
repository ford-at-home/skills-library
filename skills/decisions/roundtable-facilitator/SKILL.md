---
name: roundtable-facilitator
description: "Orchestrate a multi-turn, multi-persona evaluation of a civic innovation idea. Each persona takes a separate turn with real research, writes to a persistent conversation log, and the facilitator manages phase transitions, challenge routing, and consensus detection."
---

# roundtable-facilitator

**Purpose:** Orchestrate a multi-turn, multi-persona evaluation of a civic innovation idea. Each persona takes a separate turn with real research, writes to a persistent conversation log, and the facilitator manages phase transitions, challenge routing, and consensus detection.

**Depends on:**
- `agents/CIVIC_EVAL_PERSONAS.md` — persona definitions, phase model, fatal flaw test
- `agents/skills/roundtable-persona/SKILL.md` — per-turn persona template (loaded by subagents)
- `PARALLEL_API_KEY` from workspace `.env` — for deep research via Parallel AI
- `2026-annual-hackathon/ideas/RICHMOND_TECH_STACK_2026.md` — Architect grounding
- `2026-annual-hackathon/ideas/IMPLEMENTATION_REALITY_SYNTHESIS.md` — survivability data
- `pillar-repos/pillar-[slug]/research/` — 51 deep-research reports per pillar (A–I sections)
- `pillar-repos/pillar-[slug]/post-event-research/` — per-idea and shared post-event research

---

## When To Use

- Evaluating any civic idea (hackathon demo, NEW_IDEA, BLUESKY, or new proposal) through the seven-persona framework
- When you need a structured, evidence-based deliberation — not a single-pass assessment
- When the user says "run a roundtable on [idea]" or "evaluate [idea] with the personas"

## What This Is NOT

- This is not a single-response evaluation. Each persona turn is a separate inference with its own research.
- This is not the facilitator generating all seven perspectives at once. Subagents are isolated — they see the conversation log, not the facilitator's plan.

---

## Prerequisites

```bash
# Source the API key — required for Parallel AI deep research
source .env
# or: export PARALLEL_API_KEY=$(grep PARALLEL_API_KEY .env | cut -d= -f2)
```

Verify the key is set before proceeding. If missing, warn the user and halt.

---

## Inputs

The user provides one of:
1. **An idea slug** that maps to `2026-annual-hackathon/ideas/[pillar]/[idea-slug]/`
2. **An idea description** (freeform text — a new proposal not yet in the repo)
3. **A reference** to an entry in `IMPLEMENTATION_REALITY_SYNTHESIS.md`

### Idea File Structure (Required for existing ideas)

Every evaluated idea lives at `2026-annual-hackathon/ideas/[pillar]/[idea-slug]/` and contains at minimum these three core files:

| File | Contents | What the roundtable uses it for |
|------|----------|--------------------------------|
| **`IDEA.md`** | Structured card: pillar, problem statement, source, implementation reality score, rank, description, data sources, prior art summary, build estimate, rubric grades (6 categories × scores), bundle membership, recommendations | **All personas** — this is the primary input. Provides pillar alignment, data sources, prior art summary, rubric grades, and bundle context. |
| **`RESEARCH_RESULT.md`** | Deep research output: executive summary, comparative city data, confirmed examples, adoption evidence, equity implications, failure modes, implementation playbook, metrics, citations with URLs | **Architect** (integration & platform guidance), **Activist** (comparable cities, ecosystem), **Funder** (implementation phases & cost), **Citizen** (adoption evidence, equity gaps) |
| **`INNOVATION_ANALYSIS.md`** | Six lenses: Blue Ocean ERRC grid, 8 divergent approaches, design sprint, opportunity mapper (patterns A/B/C), problem scoping (5 dimensions), assumption mapping (risk × uncertainty matrix) | **Innovator** (ERRC reframe, divergent approaches, assumption map), **Mayor** (problem scoping alignment), **Frontliner** (user journey, adoption assumptions) |

Additional files that may exist in some idea dirs:

| File | Contents | Notes |
|------|----------|-------|
| **`README.md`** | Metadata card: pillar, problem statement, source type, team, links to shared research and external URLs | Use to find the correct `_shared-*` dir and external demo links |
| **`lifecycle_review.md`** | Post-event lifecycle review (demos only) | Additional context for roundtable if present |
| **`gap_analysis.md`** | Gap analysis by JTBD (demos only) | Additional context for roundtable if present |
| **`solution_ideas.md`** | Next-step solution ideas (some demos) | Additional context for Innovator and Funder if present |
| **`jtbd_analysis.md`** | Per-idea JTBD (may differ from `_shared-*` version) | Load if present — may contain research answers not in the shared version |
| **`pain_points.md`** | Per-idea pain points (may differ from `_shared-*` version) | Load if present |
| **`demo.mp4`** or **`demo.mov`** | Demo video (demos only) | Standardized filenames |

**All three core files MUST exist before running a roundtable on an existing idea.** If any are missing, halt and tell the user which file(s) need to be created first.

### Key Fields Extracted from IDEA.md

The facilitator parses these from the IDEA.md front-matter table:

```
Pillar              → routes to Mayor (MAP alignment) and pillar context
Problem Statement   → grounds all personas in the actual civic problem
Source              → Demo / NEW / BLUESKY — sets expectations for evidence level
Implementation Reality Score → Architect's starting point (Tier S/A/B/C/D)
Overall Rank        → context for relative priority
```

And from the body:

```
Description         → the idea itself — distributed to all personas
Data Sources        → Architect validates; Funder estimates data costs
Prior Art           → Activist cross-references against ecosystem scan
Build Estimate      → Funder and Architect use for cost modeling
Rubric Grades       → Mayor uses for MAP alignment; all personas see existing scores
Bundle Membership   → Architect and Funder evaluate shared infrastructure value
Recommendations     → Mayor uses for timeline; Funder uses for phasing
```

### Key Fields Extracted from RESEARCH_RESULT.md

```
Comparable cities   → Activist uses for ecosystem scan (avoids re-researching what's known)
Adoption metrics    → Citizen uses for archetype assessment
Equity implications → Citizen (Invisible Resident) and Mayor (MAP equity goals)
Failure modes       → Architect and Frontliner use for risk assessment
Implementation playbook → Funder uses for phasing and cost modeling
Citations           → All personas can cite these directly (no re-searching known facts)
```

### Key Fields Extracted from INNOVATION_ANALYSIS.md

```
ERRC Grid           → Innovator starts here — what to eliminate/reduce/raise/create
Divergent approaches → Innovator evaluates which reframes are most promising
User journey        → Frontliner validates against real workflow
Assumption map      → All personas check their assessments against flagged assumptions
Problem scoping scores → Mayor cross-references against rubric grades
```

### For New Ideas (No Existing Files)

If the user provides a freeform description instead of a slug:
1. Skip file reading — proceed with the description as the sole input
2. Note `[No existing research — all claims require fresh verification]` in the log header
3. The Activist and Architect MUST do heavier research to compensate for missing `RESEARCH_RESULT.md`
4. The Innovator generates their own ERRC reframe rather than building on `INNOVATION_ANALYSIS.md`

---

## Output

A single conversation log file that builds incrementally:

```
agents/roundtables/[idea-slug].md
```

Plus a final structured verdict appended at the end in the output schema from `CIVIC_EVAL_PERSONAS.md`.

---

## Execution Protocol

### Step 0 — Setup

**0a. Load the persona framework:**
```
Read: agents/CIVIC_EVAL_PERSONAS.md
```

**0b. Load the idea's three files** (or halt if missing):
```
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/IDEA.md
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/RESEARCH_RESULT.md
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/INNOVATION_ANALYSIS.md
```

Optional (load if present):
```
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/README.md
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/lifecycle_review.md
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/gap_analysis.md
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/solution_ideas.md
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/jtbd_analysis.md
Read: 2026-annual-hackathon/ideas/[pillar]/[idea-slug]/pain_points.md
```

If any file is missing → halt and report:
```
Cannot start roundtable for [idea]. Missing:
  - [file] — needed for [which personas and why]
```

**0c. Load Richmond context:**
```
Read: 2026-annual-hackathon/ideas/RICHMOND_TECH_STACK_2026.md
Read: 2026-annual-hackathon/ideas/IMPLEMENTATION_REALITY_SYNTHESIS.md
```

**0d. Load shared research:**
Check `README.md` for links to `../_shared-*/`. If present:
```
Read: 2026-annual-hackathon/ideas/[pillar]/_shared-[topic]/jtbd_analysis.md
Read: 2026-annual-hackathon/ideas/[pillar]/_shared-[topic]/pain_points.md
Read: 2026-annual-hackathon/ideas/[pillar]/_shared-[topic]/prior_art_research.md
```

Note: Some ideas also have per-idea versions of these files that may contain research answers or project-specific analysis not in the shared version. If present, load those too.

Note: `thriving-built-environment` has no `_shared-*` dirs. Per-idea copies are the only versions.

**0e. Load the pillar research corpus index:**

Each pillar has ~51 deep-research reports generated pre-hackathon. These are a goldmine for grounding persona assessments. The research lives at:

```
pillar-repos/pillar-[slug]/research/INDEX.md       ← read this first
pillar-repos/pillar-[slug]/research/[section].md   ← read specific reports
```

Use the pillar slug mapping:

| Pillar | Slug |
|--------|------|
| A Thriving City Hall | `pillar-thriving-city-hall` |
| Thriving Neighborhoods | `pillar-thriving-neighborhoods` |
| Thriving Families | `pillar-thriving-families` |
| A Thriving Economy | `pillar-thriving-economy` |
| Thriving and Inclusive Communities | `pillar-thriving-inclusive-communities` |
| A Thriving and Sustainable Built Environment | `pillar-thriving-built-environment` |
| A City That Tells Its Stories | `pillar-city-storytelling` |

**Step 1:** Read `INDEX.md` to see all 51 reports.
**Step 2:** Identify which reports are relevant to this specific idea based on the section map:

| Section | Reports | Most relevant to persona |
|---------|---------|------------------------|
| **A** — Problem Landscape | A1–A5 | Mayor (root causes, scope) |
| **B** — Users & Stakeholders | B1–B5 | Citizen (user personas), Frontliner (staff personas) |
| **C** — Services & Programs | C1–C5 | Activist (existing services, gaps) |
| **D** — Data Sources | D1–D5 | Architect (APIs, data quality, access methods) |
| **E** — Prior Art | E1–E5 | Activist (comparable tools, failures) |
| **F** — Opportunities | F1–F5 | Innovator (ranked solution spaces), Mayor (opportunity fit) |
| **G** — Risks | G1–G5 | Citizen (inclusion risks), Architect (technical risks) |
| **H** — MVP Feasibility | H1–H5 | Architect (build constraints), Funder (scope/cost) |
| **Cross-cutting** | 90–93 | All personas (top questions, hypotheses, red flags, gaps) |

**Step 3:** Read the specific reports that match the idea's problem statement. Use the INDEX.md titles to select — most have descriptive titles that indicate relevance. Typically 3–6 reports are directly relevant per idea.

**Step 4:** Also check for post-event research at:
```
pillar-repos/pillar-[slug]/post-event-research/[idea-slug]/
pillar-repos/pillar-[slug]/post-event-research/_shared-[topic]/
```

If post-event research exists for this specific idea, load it (JTBD analysis, pain points, prior art, solution ideas).

**0f. Source the API key:**
```bash
export PARALLEL_API_KEY=$(grep PARALLEL_API_KEY .env | cut -d= -f2)
```

**0g. Parse key fields from IDEA.md:**
Extract from the front-matter table:
- Pillar
- Problem Statement
- Source (Demo / NEW / BLUESKY)
- Implementation Reality Score + Tier
- Overall Rank

Extract from body:
- Description (the idea itself)
- Data Sources (named datasets)
- Prior Art (summary)
- Build Estimate
- Rubric Grades (6 categories × scores, plus weighted award scores)
- Bundle Membership (related ideas)
- Recommendations (timeline + phasing)

**0h. Create the conversation log:**

```markdown
# Roundtable: [Idea Name]

**Initiated:** [timestamp]
**Idea:** [name]
**Pillar:** [pillar]
**Problem Statement:** [verbatim from IDEA.md]
**Source:** [Demo / NEW / BLUESKY]
**Implementation Reality Score:** [score]/25 — Tier [S/A/B/C/D]
**Overall Rank:** #[N] of 73

## Input Materials

| File | Status |
|------|--------|
| IDEA.md | ✅ Loaded |
| RESEARCH_RESULT.md | ✅ Loaded |
| INNOVATION_ANALYSIS.md | ✅ Loaded |
| Shared research (_shared-*) | [✅ Loaded / N/A] |
| Pillar research corpus (INDEX.md) | ✅ Loaded — [N] reports identified as relevant |
| Post-event research | [✅ Loaded / N/A] |
| RICHMOND_TECH_STACK_2026.md | ✅ Loaded |
| IMPLEMENTATION_REALITY_SYNTHESIS.md | ✅ Loaded |

## Existing Rubric Grades (from IDEA.md)

| Category | Score |
|----------|:-----:|
| Impact | [N] |
| Feasibility | [N] |
| User Value | [N] |
| Execution | [N] |
| Innovation | [N] |
| Equity | [N] |

**Pillar Award:** [N] | **Mayor's Choice:** [N]

## Bundle Context

[Bundle name and related ideas from IDEA.md, if any]

---

## Status

- **Phase:** Setup
- **Turns Completed:** 0
- **Challenges Pending:** 0
- **Fatal Flaws Detected:** 0

---
```

6. Create a TodoWrite checklist tracking every turn:

```
Phase 1 — Divergence:
  [ ] Turn 1: Innovator
  [ ] Turn 2: Activist
  [ ] Turn 3: Citizen
Phase 2 — Convergence:
  [ ] Turn 4: Mayor
  [ ] Turn 5: Architect
  [ ] Turn 6: Frontliner
  [ ] Turn 7: Funder
Phase 3 — Challenge Rounds:
  [ ] Route pending challenges
Phase 4 — Validation:
  [ ] Fatal flaw test
  [ ] Temporal assessment
  [ ] Final verdict
```

### Step 1 — Phase 1: Divergence (Parallel)

Launch three subagents simultaneously using the Task tool. Each subagent receives the `roundtable-persona` skill instructions, their persona definition, the `PARALLEL_API_KEY`, and a **persona-specific slice of the idea files**:

**Subagent dispatch (all three in one tool call batch):**

```
Task: "Innovator evaluates [idea]"
  → Persona: THE INNOVATOR
  → Idea files to read:
    - INNOVATION_ANALYSIS.md (primary — start with ERRC grid and divergent approaches)
    - IDEA.md (description + problem statement for context)
  → Pillar research to read:
    - pillar-repos/pillar-[slug]/research/F1_opportunities_ranked.md (ranked solution spaces)
    - pillar-repos/pillar-[slug]/research/F5_opportunities_do_not_build.md (anti-patterns)
    - Any F-section report whose title relates to this idea's problem statement
  → Research mandate: The ERRC reframe and 8 divergent approaches already exist.
    The pillar research has ranked opportunities and "do not build" guardrails.
    Your job is to go BEYOND both. Use WebSearch to find where this pattern
    has worked in non-civic domains. Challenge the assumption map.
    What did the innovation analysis AND the pillar research miss?

Task: "Activist evaluates [idea]"
  → Persona: THE ACTIVIST
  → Idea files to read:
    - IDEA.md (prior art summary + bundle membership)
    - RESEARCH_RESULT.md (comparable cities, ecosystem data, citations)
  → Pillar research to read:
    - pillar-repos/pillar-[slug]/research/E1–E5 (prior art — all five reports)
    - pillar-repos/pillar-[slug]/research/C1–C5 (existing services and gaps)
  → Research mandate: RESEARCH_RESULT.md AND the pillar E/C sections contain
    substantial prior art and ecosystem data. Read them ALL first.
    Start from what's confirmed — do NOT re-research known facts.
    Use Parallel AI deep research (pro-fast) to go BEYOND both sources:
    find nonprofit/coalition/state-level actors not covered in either.
    Apply the decision tree (Adopt/Adapt/Build/Partner/Advocate/Reframe).

Task: "Citizen evaluates [idea]"
  → Persona: THE CITIZEN (all three archetypes)
  → Idea files to read:
    - IDEA.md (description + rubric grades, especially Equity score)
    - RESEARCH_RESULT.md (adoption metrics, equity implications sections)
    - INNOVATION_ANALYSIS.md (user journey from design sprint section)
  → Pillar research to read:
    - pillar-repos/pillar-[slug]/research/B1–B5 (user personas and needs)
    - pillar-repos/pillar-[slug]/research/G3_risks_inclusion.md (inclusion risks)
    - pillar-repos/pillar-[slug]/research/B5_users_digital_equity.md (digital equity)
  → Research mandate: RESEARCH_RESULT.md has some adoption data. The pillar
    B-section has detailed user personas and digital equity analysis.
    Use WebSearch to find ADDITIONAL adoption evidence for comparable tools.
    Evaluate the user journey in INNOVATION_ANALYSIS.md from each
    archetype's perspective, informed by the pillar's user research.
```

**After all three return:**
- Append each persona's output to the conversation log as Turn 1, 2, 3
- Extract any questions directed at other personas
- Extract any challenges or disagreements
- Update the Status section

**Report to user:**
```
Phase 1 complete — Divergence

Key findings:
  - Innovator: [1-sentence summary]
  - Activist: [1-sentence summary]
  - Citizen: [1-sentence summary]

Tensions identified: [count]
Questions pending for Phase 2: [list]

Continue to Phase 2? [y / inject context / pause]
```

Wait for user confirmation before proceeding.

### Step 2 — Phase 2: Convergence (Sequential)

Phase 2 personas run sequentially because each builds on prior output:
- The Mayor needs the Activist's ecosystem scan to assign ownership
- The Architect needs the Innovator's reframe to assess technical feasibility
- The Funder needs the Architect's integration assessment to model costs

**For each persona (Mayor → Architect → Frontliner → Funder):**

1. Read the full conversation log so far
2. Read any questions directed at this persona from Phase 1
3. Launch a subagent with:
   - The persona definition
   - The full conversation log (Phase 1 outputs)
   - The directed questions from Phase 1
   - Richmond-specific context (tech stack, structural walls, implementation data)
   - The `PARALLEL_API_KEY`
   - **Persona-specific file slice + research mandate:**

```
Mayor:
  → Idea files to read:
    - IDEA.md (pillar, problem statement, rubric grades, recommendations timeline)
    - INNOVATION_ANALYSIS.md (problem scoping section — 5-dimension scores)
  → Pillar research to read:
    - pillar-repos/pillar-[slug]/research/A1–A5 (problem landscape — root causes)
    - pillar-repos/pillar-[slug]/research/F1_opportunities_ranked.md (ranked opportunities)
  → Pre-loaded context: IDEA.md already has pillar alignment and rubric grades.
    The pillar A-section has deep problem landscape analysis.
    Your job is to validate or challenge alignment.
  → Research mandate: Use WebSearch to verify MAP alignment. Search
    Richmond city council agendas (Legistar) for related initiatives.
    Check if this is already funded or underway. Cross-reference the
    "Recommendations" section timeline against current city capacity.

Architect:
  → Idea files to read:
    - IDEA.md (data sources, build estimate, bundle membership)
    - RESEARCH_RESULT.md (platform guidance, integration risks, failure modes)
    - RICHMOND_TECH_STACK_2026.md (structural walls, DIT context)
  → Pillar research to read:
    - pillar-repos/pillar-[slug]/research/D1–D5 (data sources — APIs, quality, access)
    - pillar-repos/pillar-[slug]/research/H1–H5 (MVP feasibility — build constraints)
    - pillar-repos/pillar-[slug]/research/G4* or G5* (technical risks, guardrails)
  → Pre-loaded context: IDEA.md names specific data sources. RESEARCH_RESULT.md
    has platform/integration analysis. The pillar D-section has deep data source
    inventories. The implementation reality score is your baseline.
    Your job is to validate the score and find risks the scoring missed.
  → Research mandate: Use WebSearch to check CURRENT status of named data
    sources and systems (Socrata API health, EnerGov RFP status, etc.).
    Cross-reference against the five structural walls.
    If bundle membership exists, assess shared infrastructure viability.

Frontliner:
  → Idea files to read:
    - IDEA.md (description, data sources, build estimate)
    - INNOVATION_ANALYSIS.md (user journey from design sprint, assumption map)
  → Pillar research to read:
    - pillar-repos/pillar-[slug]/research/B2* or B3* (staff user personas)
    - pillar-repos/pillar-[slug]/research/C4_services* or C5* (service gaps)
  → Pre-loaded context: INNOVATION_ANALYSIS.md has a user journey and assumption
    map. The pillar B-section has detailed staff/user personas grounded in research.
    Your job is to validate the journey against real workflow and challenge assumptions.
  → Research mandate: Use WebSearch to find post-launch adoption studies for
    comparable tools. What happened after the demo? Did city staff actually
    use it? Focus on the assumptions flagged "TEST FIRST" in the assumption map.

Funder:
  → Idea files to read:
    - IDEA.md (build estimate, recommendations timeline, bundle membership)
    - RESEARCH_RESULT.md (implementation playbook with phased timeline)
  → Pillar research to read:
    - pillar-repos/pillar-[slug]/research/H1–H5 (MVP feasibility — scope, cost)
    - pillar-repos/pillar-[slug]/research/F1_opportunities_ranked.md (ranked by viability)
  → Pre-loaded context: IDEA.md has a build estimate. RESEARCH_RESULT.md has
    a phased implementation playbook. The pillar H-section has detailed MVP
    feasibility analysis. Your job is to model the full funding lifecycle.
  → Research mandate: Use WebSearch + Parallel AI (pro-fast) to identify
    specific grant programs, budget line items, or cost-avoidance models.
    If the idea is part of a bundle, model shared infrastructure economics.
    Search for [topic] + "civic technology" + "grant" OR "funding".
```

4. Append the output to the conversation log
5. Extract challenges and questions
6. Report to user after each turn

**After all four complete, report:**
```
Phase 2 complete — Convergence

Key findings:
  - Mayor: [decision + rationale]
  - Architect: [recommendation + walls hit]
  - Frontliner: [verdict + adoption risk]
  - Funder: [funding model + sustainability risk]

Challenges raised: [count]
Unresolved tensions: [list]

Continue to Challenge Rounds? [y / skip to validation / pause]
```

### Step 3 — Phase 3: Challenge Rounds

Review the conversation log for:
- Explicit challenges ("I disagree with X because...")
- Directed questions not yet answered
- Contradictions between personas (e.g., Mayor says "Advance" but Architect says "Blocked")
- Claims tagged `[Unverified]` that another persona can verify

**For each unresolved item:**

1. Identify which persona should respond
2. Launch a subagent with:
   - The persona definition
   - The full conversation log
   - The specific challenge or question
   - Research mandate: "Verify or rebut this specific claim. Use WebSearch or Parallel AI if needed."
3. Append the response to the log as a Challenge Round entry

**Loop termination criteria:**
- No new challenges raised in the latest round
- OR three challenge rounds have completed (hard cap to prevent infinite loops)
- OR user says "skip to validation"

**Report after each round:**
```
Challenge Round [N] complete

Resolved: [count]
Still unresolved: [count]
New challenges raised: [count]

Continue? [y / skip to validation]
```

### Step 4 — Phase 4: Validation

This phase does NOT use subagents — the facilitator synthesizes directly from the conversation log.

**4a. Fatal Flaw Test**

Check each kill criterion against the log:

| Fatal Flaw | Source | Result |
|------------|--------|--------|
| No identifiable owner | Mayor + Activist turns | PASS / FAIL |
| Structural wall, no workaround | Architect turn | PASS / FAIL |
| Net negative for frontline | Frontliner turn | PASS / FAIL |
| No funding path beyond pilot | Funder turn | PASS / FAIL |
| Harms Invisible Resident | Citizen turn | PASS / FAIL |

If ANY flaw is FAIL → verdict is KILL (with specific blocker named).

**4b. Temporal Assessment**

For each persona's assessment, tag:
- **Appreciating** — gets easier/more valuable over time
- **Depreciating** — gets harder/less relevant over time
- **Stable** — holds regardless

**4c. Tension Synthesis**

List all tensions identified during the roundtable:

| Tension | Persona A | Persona B | Resolved? | Resolution |
|---------|-----------|-----------|-----------|------------|

**4d. Final Verdict**

Using the full conversation log, produce the 12-section output schema from `CIVIC_EVAL_PERSONAS.md`:

```
1. Problem Definition (Reframed)
2. Solution Concept (MVP + Expanded)
3. MAP Alignment
4. Ownership
5. Technical Feasibility
6. Funding & Sustainability
7. Operational Viability
8. User Impact
9. Ecosystem Context
10. Risks
11. Fatal Flaw Test
12. Final Verdict: GO / REFINE / KILL
```

Append the full schema to the conversation log.

**Report to user:**
```
Roundtable complete for [idea name]

Verdict: [GO / REFINE / KILL]
Rationale: [2-3 sentences]
Temporal: [Appreciating / Depreciating / Stable]
Fatal flaws: [count — 0 if GO]
Key tension: [the most productive disagreement]

Full log: agents/roundtables/[idea-slug].md
```

---

## Research Protocol (For All Subagents)

Every subagent MUST follow this protocol. Include it in every subagent dispatch.

### Mandatory Research Triggers

| Claim Type | Required Action |
|------------|----------------|
| "This already exists" | WebSearch for the tool/org/URL. Cite it or mark `[Unverified]` |
| "This hits a structural wall" | Read `RICHMOND_TECH_STACK_2026.md`. Name the wall. Check current status via WebSearch |
| "Grant funding available" | WebSearch for the specific program. Name it, cite the URL, note eligibility |
| "This worked in [city]" | WebSearch for the implementation. Cite it. Note if it's still live |
| "Residents won't use this" | WebSearch for comparable adoption data. Cite the study |
| "This data exists" | Verify against Socrata, GeoHub, Legistar, or named API. Confirm access method |
| "The city should/shouldn't own this" | Identify the alternative owner by name. Verify they exist and are active |

### Research Tools Available

| Tool | Use For | How |
|------|---------|-----|
| **WebSearch** | Quick fact checks, prior art, adoption data, current system status | Direct tool call |
| **Parallel AI deep research** | Ecosystem scans, comprehensive prior art, funding landscape | Shell: `curl -X POST "https://api.parallel.ai/v1/tasks/runs" -H "x-api-key: $PARALLEL_API_KEY" -H "Content-Type: application/json" -d '{"input": "<research query>", "processor": "pro-fast", "task_spec": {"output_schema": {"type": "text"}}}'` then poll with `curl "https://api.parallel.ai/v1/tasks/runs/{run_id}/result" -H "x-api-key: $PARALLEL_API_KEY"` |
| **WebFetch** | Pull specific pages (Socrata datasets, API docs, grant program pages) | Direct tool call |
| **Read** | Richmond-specific context (tech stack, implementation reality, pillar data) | Direct tool call on repo files |

### Parallel AI Usage Rules

- Use `pro-fast` processor for all roundtable research (fast enough for turn-based flow)
- Deep research queries should be specific and scoped — not "tell me everything about X"
- Poll every 30 seconds, timeout after 5 minutes
- Save raw results to `agents/roundtables/research/[idea-slug]/[persona]-[topic].md`
- Always include the research output in the persona's turn entry in the conversation log

### Loading the API Key

The `PARALLEL_API_KEY` lives in the workspace `.env` file at the repo root. Every subagent that needs Parallel AI must:

```bash
# Read from .env
export PARALLEL_API_KEY=$(grep PARALLEL_API_KEY /Users/williamprior/Development/GitHub/hackathon/.env | cut -d= -f2)
```

Do NOT hardcode the key. Do NOT include it in conversation logs or output files.

---

## Conversation Log Format

Each turn in the log follows this structure:

```markdown
---

## Turn [N] — [PERSONA NAME] ([Phase])

**Research conducted:**
- [Tool]: "[query]" → [1-sentence finding]
- [Tool]: "[query]" → [1-sentence finding]

**Assessment:**
[Persona's evaluation — structured per their output format in CIVIC_EVAL_PERSONAS.md]

**Key claims:**
- [Claim] — [Verified / Unverified / Contradicted by Turn N]

**Questions for the table:**
- → [PERSONA]: [specific question]

**Challenges:**
- To [PERSONA] (Turn [N]): [specific disagreement with rationale]

---
```

Challenge round entries:

```markdown
---

## Challenge Round [N] — [PERSONA] responds to [CHALLENGER] (Turn [M])

**Challenge:** [what was challenged]
**Response:** [the response]
**Research:** [any research conducted to support the response]
**Resolution:** [Resolved / Unresolved / Escalated]

---
```

---

## User Control Points

The facilitator pauses after each phase and after each challenge round. The user can:

| Command | Effect |
|---------|--------|
| **continue** / **y** | Proceed to next phase |
| **inject [text]** | Add context the personas don't have (e.g., "the City just signed a new AvePoint contract"). Injected context is prepended to the next persona's input. |
| **skip** | Jump to the next phase (e.g., skip remaining challenge rounds) |
| **pause** | Save state. The conversation log is the state — resume by re-reading it. |
| **rerun [persona]** | Re-run a specific persona's turn with updated context |
| **deep research [query]** | Fire an ad-hoc Parallel AI deep research query and append results to the log |

---

## Error Handling

| Failure | Recovery |
|---------|----------|
| Parallel AI times out | Fall back to WebSearch for the same query. Note `[Parallel AI timeout — WebSearch fallback]` in the log |
| Subagent returns empty/broken output | Re-run the subagent once. If it fails again, note `[PERSONA turn failed — manual input needed]` and continue |
| API key missing | Halt immediately. Instruct user to set `PARALLEL_API_KEY` in `.env` |
| Idea has no existing files (new proposal) | Proceed with user-provided description only. Note `[No existing research — all claims require fresh verification]`. Activist and Architect must do heavier research. |
| IDEA.md exists but RESEARCH_RESULT.md missing | Halt. Activist and Architect cannot function without research baseline. Run `prior-art-regional-research` skill first. |
| IDEA.md exists but INNOVATION_ANALYSIS.md missing | Proceed with reduced Innovator context. Note `[No innovation analysis — Innovator generating fresh ERRC reframe]`. |
| Conversation log exceeds context limits | Summarize earlier turns (preserving key claims, challenges, and research citations) before passing to later subagents |

---

## Example Dispatch (Phase 1 — Activist evaluating Contract Expiry Dashboard)

```
You are THE ACTIVIST evaluating a civic innovation idea.

## Your Persona
[paste Activist section from CIVIC_EVAL_PERSONAS.md]

## The Idea (from IDEA.md)
Name: Contract Expiry Dashboard
Pillar: A Thriving City Hall
Problem Statement: PS2 — Procurement Risk & Opportunity Review
Source: NEW (AI-generated post-event)
Implementation Reality Score: 24/25 — Tier S (Ship It)
Overall Rank: #1 of 73 ideas

Description: A sortable, filterable dashboard showing City contract
expiration timelines. Load the Socrata xqn7-jvv2 dataset (1,362 records,
updated monthly, 0% missing expiration dates). Display contracts with
quick-filter buttons: expiring in 30/60/90/180/365 days...

Prior Art (from IDEA.md): Tempe Procurement Contracts dashboard;
NYC Checkbook; Portland OCDS dashboards

Bundle Membership: Socrata Contracts Pipeline — foundation for
5 related ideas (Alerts, Drift Scanner, Spend Mirror, Contract Navigator)

## Research Already Done (from RESEARCH_RESULT.md)
- Richmond is the ONLY confirmed mid-sized city with public effective_to dates
- Cambridge, MA has the right fields but no dashboard
- Adoption metrics are weak: Cambridge dataset has 533 views
- No city has documented cost savings from an expiration dashboard
- Equity requires MWBE tagging (not in base dataset)

[Include key sections from RESEARCH_RESULT.md]

## Your Task
The research already covers comparable cities. Your job is to go BEYOND it:

1. Apply the decision tree:
   - Does this already exist? RESEARCH_RESULT.md says no mid-sized city has it.
     Verify — search for any new launches since the research was done.
   - Is the city the right owner? Or should a civic tech org build/host this?
   - Could this scale beyond Richmond? (Other Socrata cities could fork it.)
   - Does the bundle (5 related ideas) change the ownership calculus?

2. Conduct a Parallel AI deep research query:
   "What civic technology organizations, open-source projects, or
   government transparency initiatives focus on procurement contract
   expiration tracking or renewal management in US local government?
   Include Code for America brigades, Sunlight Foundation projects,
   OpenGov initiatives, and any commercial vendors. Note which are
   active vs. sunset as of 2026."

   API key: [loaded from .env — use Shell to source it]
   Processor: pro-fast

3. Use WebSearch to check:
   - Has any Code for America brigade built a contract expiry tool?
   - Is there an open-source procurement dashboard project on GitHub?
   - Has Richmond's Procurement Transparency Dashboard changed since
     the research was done? (check rva.gov/procurement-services/)

## Output Format
Follow the Turn format from roundtable-persona/SKILL.md.

## Rules
- Start from RESEARCH_RESULT.md — do NOT re-research what's already confirmed
- Do NOT claim something exists without citing a URL
- Do NOT claim "the city shouldn't own this" without naming who should
- Tag anything unverified as [Unverified]
- You do not know what the Innovator or Citizen said. Evaluate independently.
```

---

## Completion Criteria

The roundtable is complete when:
- All seven personas have taken at least one turn
- All challenge rounds are resolved (or hard cap reached)
- Fatal flaw test is complete
- The 12-section output schema is written
- The conversation log file is finalized

The facilitator should NOT claim completion until the log contains the final verdict section.
