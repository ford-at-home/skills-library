---
name: research-grounded-outreach
description: "Draft SME outreach emails that lead with confirmed research findings and ask only the questions that genuinely remain unanswered. Replaces the generic `sme-outreach` skill template with a research-heavy format that earns credibility before making asks."
---

# Research-Grounded Outreach — Draft Emails That Show You Did Your Homework

**Purpose:** Draft SME outreach emails that lead with confirmed research findings and ask only the questions that genuinely remain unanswered. Replaces the generic `sme-outreach` skill template with a research-heavy format that earns credibility before making asks.

**Predecessor:** `jtbd-research` (Phase 3 of pillar-pipeline) — research answers must be integrated before drafting
**Successor:** Manifest & Handoff update (Phase 7 of pillar-pipeline)

---

## When to Use

After Phase 3 (JTBD Research) and Phase 5 (New Ideas + Grading) are complete. You need:
- JTBD files with `## Answered Questions` section containing `[Confirmed]`, `[Partial]`, `[Still Unknown]` tags — in `_shared-*` dirs or per-idea dirs (per-idea versions often have research answers appended)
- Research answer files in `ideas/{pillar}/_research-answers/` (or the pillar repo's `post-event-research/_research-answers/` if from the initial research round)
- Graded ideas in `NEW_IDEAS_RUBRIC_GRADES.md` with tier rankings

## Why This Replaces Generic Outreach

The original `sme-outreach` skill drafts emails that say "we don't know much — can you answer 5 broad questions?" This skill drafts emails that say "here's everything we've confirmed through deep research — we just need 4-5 specifics only your team can answer." The second format gets responses because it respects the reader's time and demonstrates seriousness.

---

## Process

### Step 1 — Identify Contact Groups

Read the JTBD files and gap analyses. Check both `_shared-*` dirs and per-idea dirs for JTBD files — per-idea versions may contain additional answered questions. Group the `[Still Unknown]` and `[Partial]` questions by the SME who can answer them. Typical groupings for a pillar:

| Contact Type | Example | Questions they answer |
|-------------|---------|----------------------|
| System operator | 311 Operations, Procurement Office | API access, taxonomy, internal metrics |
| Data/IT team | City IT, Digital Services | Content structure, data publishing, integration |
| Policy/equity | OIRE, OMBD, community organizations | Language access, MBE tracking, equity barriers |

Aim for **2-4 emails per pillar** (not 1 per question — group related questions).

### Step 2 — Gather Confirmed Findings for Each Email

For each contact, collect everything from the research that is relevant to their domain:

1. **Systems confirmed:** Name the specific platforms, versions, vendors (e.g., "AvePoint Citizen Services on Dynamics 365, launched June 2017")
2. **Data confirmed:** Name datasets with IDs, row counts, field lists, last update dates
3. **Scale confirmed:** Cite specific numbers (e.g., "208,216 requests in 2025", "32 FTE staff")
4. **Policy confirmed:** Reference specific policies by name and date (e.g., "AR 5.24, effective July 2023")
5. **Comparable cities:** Name what peer cities do differently
6. **Recent events:** Reference audits, resets, IG reports with dates

### Step 3 — Identify Genuinely Unanswered Questions

From the JTBD `[Still Unknown]` items, plus any `[Partial]` items where the missing piece requires insider knowledge:
- Maximum **5 questions per email**
- Each question must be specific enough that it has a yes/no or short factual answer
- Never ask questions the research already answered — this wastes the reader's time and undermines credibility

### Step 4 — Include Pilot Recommendations

From `NEW_IDEAS_RUBRIC_GRADES.md`, include the top 2-3 graded ideas relevant to this contact's domain:
- Name and 1-sentence description
- Rubric score (e.g., "scored 99/105 on Mayor's Choice")
- What it needs from them (if anything)
- Emphasize what does NOT require their involvement (e.g., "uses only public Socrata data")

### Step 5 — Write the Email

Use this structure:

```markdown
# Outreach: {Contact Role} — {Topic}

**To:** [CONTACT NEEDED] — {Title}, {Department}
**Email:** [CONTACT NEEDED — ask {referrer}]
**Re:** RVA Hacks 2026 {Pillar} Demos — {Topic}
**Status:** Draft — not yet sent

---

## Subject
RVA Hacks 2026: {N} {topic} prototypes — research findings and a few questions only your team can answer

## Body

Hi [First Name],

I'm writing from the RVA Hacks civic hackathon team. During our March 2026 event, {N} teams built {topic} tools for the "{Pillar}" pillar: {list}. All aimed at {problem statement paraphrase}.

We've completed an extensive post-event analysis. I want to share what we've confirmed before asking for your help on the specifics we can't verify publicly.

### What we've confirmed through public sources

{Bulleted list of 10-20 confirmed findings, grouped by category:}
- **Systems:** ...
- **Data:** ...
- **Scale:** ...
- **Equity:** ...
- **Comparable cities:** ...

### What we still need your help with

{N} specific questions only your team can answer:

1. **{Topic}:** {Specific question}
2. ...

### What we're recommending

Based on the rubric scores and feasibility analysis, our top pilot recommendations for {domain} are:

1. **{Idea name}** ({Idea #}, scored {X}/105 {Award}) — {1-sentence description}. {What it needs or doesn't need from them}.
2. ...

We're not asking for any commitment — just verifying data claims and understanding priorities. Happy to share any prototypes or our full analysis.

Thank you,
[Your name]
RVA Hacks Team

---

## Context for the SME
{2-3 sentences for internal reviewer}

## Why This Person
{1-2 sentences}

## Data Questions (internal tracking)
- [ ] Q1: {question}
- [ ] Q2: {question}

## Research Sources
- `ideas/{pillar}/_research-answers/{file}` — {what it covers}
- Pillar repo `post-event-research/_shared-{problem}/jtbd_analysis.md` — {what it covers} (e.g. `https://github.com/hack4rva/pillar-{slug}/tree/main/post-event-research/`)
- `ideas/{pillar}/NEW_IDEAS_RUBRIC_GRADES.md` — scored ideas

## Follow-Up Status
- Sent: PENDING
- Response: AWAITING
```

### Step 6 — Cross-Reference

After writing all emails for the pillar:
1. Check that every `[Still Unknown]` question from the JTBD files appears in at least one email
2. Check that no email asks a question the research already answered
3. Check that every email references at least 5 confirmed findings
4. Verify all dataset IDs, row counts, and dates are accurate (they came from the research files)

---

## Output

```
outreach/{pillar}/
├── {contact-slug-1}.md
├── {contact-slug-2}.md
└── {contact-slug-3}.md
```

## Quality Bar

A good research-grounded outreach email:
- Makes the reader think "they've really done their homework" in the first 30 seconds
- Asks no more than 5 questions, all specific and answerable
- Includes numbers the reader can verify (dataset IDs, dates, system names)
- Offers something in return (prototypes, analysis, recommendations)
- Can be forwarded to a colleague without losing context
