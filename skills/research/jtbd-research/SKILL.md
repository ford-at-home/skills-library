---
name: jtbd-research
description: "After JTBD analysis produces open questions for a pillar, this skill groups them into efficient Parallel AI research queries, fires them, polls for results, and integrates answers back into the JTBD files."
---

# JTBD Research Skill — Answer Open Questions with Parallel AI

**Purpose:** After JTBD analysis produces open questions for a pillar, this skill groups them into efficient Parallel AI research queries, fires them, polls for results, and integrates answers back into the JTBD files.

**Predecessor:** `INNOVATION_LIFECYCLE` Steps 1-5 (Phase 2 of pillar-pipeline)
**Successor:** `INNOVATION_LIFECYCLE` Steps 6-11 per-demo (Phase 4 of pillar-pipeline), then `research-grounded-outreach` (Phase 6)

---

## When to Use

After completing Steps 1-3 of the Innovation Lifecycle (JTBD Analysis + Question Generation) for a pillar's problem statements, and **before** moving to per-demo evaluation (Steps 6-11).

## Prerequisites

- `PARALLEL_API_KEY` available in environment (source from parent workspace `.env` if needed)
- JTBD analysis files exist with an "Open Questions" section
- Existing research corpus in each pillar's GitHub repo has been read — e.g. `https://github.com/hack4rva/pillar-{name}/tree/main/research/`

---

## Step 1: Extract Open Questions

Read the `jtbd_analysis.md` files from the `_shared-*` dirs for the pillar. Also check per-idea dirs — some have their own versions with different or enhanced content. Collect all questions from the "Open Questions" section. Typical categories:

- **Data Questions** — What systems exist? What data is published? What APIs are available?
- **User Questions** — Who uses the system? How many? What are the usage patterns?
- **Integration Questions** — Can tools connect? What procurement/security process applies?
- **Equity Questions** — Who is excluded? What languages? What digital access gaps?
- **Prior Art Questions** — What have comparable cities done? What has Richmond tried before?

## Step 2: Group into Research Queries (3 per problem statement)

For each problem statement, create 3 queries:

| Query | Content | Maps to |
|-------|---------|---------|
| `{prefix}_q1_system_data` | Systems, platforms, APIs, data sources, taxonomies | Data + Integration questions |
| `{prefix}_q2_usage_equity` | Usage patterns, demographics, digital divide, LEP, equity | User + Equity questions |
| `{prefix}_q3_prior_art` | Comparable cities, tools, failure modes, prior attempts | Prior Art questions |

**Naming convention:** `{problem_area_short}_q{n}_{topic}`

Example for Thriving City Hall:
- `sn_q1_system_data` (service navigation)
- `sn_q2_usage_equity`
- `sn_q3_prior_art`
- `proc_q1_system_data` (procurement)
- `proc_q2_staffing_equity`
- `proc_q3_prior_art`

## Step 3: Fire Queries

```bash
export PARALLEL_API_KEY=<key>
mkdir -p ideas/{pillar}/_research-answers

parallel-cli research run "<query text with numbered questions>" \
  --no-wait \
  -o ideas/{pillar}/_research-answers/{query_name}
```

- Use `pro-fast` processor (default) — good balance of depth and speed
- Use `--no-wait` to fire all queries in parallel
- Each query should list its sub-questions explicitly and numbered
- Include "Specifically answer ALL of these questions with sourced evidence" in the prompt

## Step 4: Poll and Save Results

```bash
parallel-cli research poll <task_id> \
  -o ideas/{pillar}/_research-answers/{query_name}
```

- Poll every 60-90 seconds
- pro-fast typically completes in 2-5 minutes
- Results save as `{name}.md` and `{name}.json`

## Step 5: Integrate Answers into JTBD Files

For each JTBD analysis file:
1. Read the corresponding research answer files
2. Add a new "## Answered Questions" section below "## Open Questions"
3. For each question, provide:
   - The sourced answer from Parallel AI
   - Confidence level: `[Confirmed]`, `[Partial]`, or `[Still Unknown]`
   - Citation to the research file
4. Move fully answered questions from "Open Questions" to "Answered Questions"
5. Leave genuinely unanswered questions in "Open Questions" with a note on what's needed

**Note:** Historically, research answers have been appended to per-idea copies of `jtbd_analysis.md`, creating enhanced versions that differ from the `_shared-*` originals. This is expected — per-idea files serve as the enriched reference for that specific idea.

## Step 6: Update Idea Grounding

For each surviving idea in `NEW_IDEAS.md`:
- Check which JTBD questions are now answered
- Update any assumptions that are confirmed or refuted
- Flag ideas whose feasibility changed based on new evidence

---

## Repeatable Pattern per Pillar

```
1. Read JTBD files → collect open questions
2. Group into 3 queries per problem statement (system, equity, prior art)
3. Fire all queries with --no-wait
4. Poll and save results
5. Integrate answers into JTBD files
6. Update idea grounding if needed
```

## Output Files

```
ideas/{pillar}/_research-answers/
├── {prefix}_q1_system_data.md
├── {prefix}_q1_system_data.json
├── {prefix}_q2_usage_equity.md
├── {prefix}_q2_usage_equity.json
├── {prefix}_q3_prior_art.md
└── {prefix}_q3_prior_art.json
```
