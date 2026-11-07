---
name: sme-outreach
description: "Draft a ready-to-send email to a subject matter expert (city staff, nonprofit professional, or community organization) asking specific questions that only a human with lived experience or institutional access can answer."
---

# sme-outreach

**Purpose:** Draft a ready-to-send email to a subject matter expert (city staff, nonprofit professional, or community organization) asking specific questions that only a human with lived experience or institutional access can answer.

**Note:** For pillar pipeline use (Phase 6), prefer `skills/research-grounded-outreach/SKILL.md` instead — it produces emails that lead with confirmed research findings. This skill is still useful for one-off outreach during per-demo evaluation (Phase 4, Step 7) when you need a quick email for a specific data blocker.

## When To Use
- A data source requires a city department relationship to access
- A question cannot be answered by web research (e.g., "does DPW currently have GPS on their plow trucks?")
- A team needs to validate an assumption about how a city system actually works
- A prior art project exists and you need to understand whether it could apply to Richmond

## Hard Rules
- Never fabricate a contact. Use only entries in `CONTACTS.md`. If no appropriate contact exists, write the email with `[CONTACT NEEDED]` in the To field and add a note to CONTACTS.md.
- Never ask vague questions. Every email must include a specific list of data questions.
- Always include the context: what was built, what problem it solves, what specific thing you need.
- Keep it short. City staff are busy. Aim for 5–7 sentences of context, then a bulleted list of asks.

## Inputs
- Problem statement (verbatim)
- The specific gap or data question to be answered
- CONTACTS.md (to identify the right person)
- Demo transcript (to give context about what was built)

## Output
One markdown file written to `outreach/[pillar]/[contact-slug].md`

---

## Process

### Step 1 — Identify the right contact
Read `CONTACTS.md`. Find the person whose role and topics best match the data question.
If no match exists, write the email to `[CONTACT NEEDED]` and flag for CONTACTS.md update.

### Step 2 — Write the email

Use this template:

```markdown
# Outreach: [Contact Name / Role]

**To:** [Name] — [Title], [Organization]
**Email:** [email from CONTACTS.md, or CONTACT NEEDED]
**Re:** [Project Name] — [Pillar] — [One-line subject]
**Status:** Draft — not yet sent

---

## Subject
RVA Hacks 2026: [Project Name] — Quick question about [topic]

## Body

Hi [First Name],

I'm [your name] from the RVA Hacks civic hackathon team. During our March 2026 event, a team built [project name] — a [one-sentence description] aimed at [problem statement, paraphrased].

We're now doing a post-event review to understand what it would take to move this from a prototype to something the City could actually pilot. We've hit a point where we need someone with your expertise to answer a few questions that web research can't resolve.

Would you be willing to have a 20-minute call, or respond to the questions below by email?

**Our questions:**
1. [Specific, concrete question about data access, system integration, or operational reality]
2. [Second specific question]
3. [Third specific question — no more than 5 total]

We're not asking for a commitment of any kind — just trying to understand what's real and what would need to change. Happy to share the full prototype if that's helpful.

Thank you,
[Your name]
[Your role]
[Contact info]

---

## Context for the SME
[2–3 sentences explaining what the team built and what gap this outreach is trying to close. Written for the reviewer of this file, not the SME.]

## Why This Person
[1–2 sentences explaining why this contact is the right person for these questions.]

## Data Questions (internal tracking)
- [ ] Q1: [question]
- [ ] Q2: [question]
- [ ] Q3: [question]

## Follow-Up Status
- Sent: [date or PENDING]
- Response: [summary or AWAITING]
```

### Step 3 — Update the lifecycle rubric
After writing the email, update the `gap_analysis.md` for the project (in `ideas/<pillar>/<project>/`) to note that outreach is pending.

---

## Output Naming Convention
Files are named `[contact-slug].md` where the slug is `[first-name-last-name]` or `[role-slug]` if no contact is identified yet.

Example: `outreach/thriving-built-environment/dpw-fleet-operations.md`
