---
description: "Anchor the event in a real, public, government-owned strategic plan"
skill_number: "01"
skill_id: civic-alignment
name: civic-alignment
display_name: "Civic Alignment"
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 2-6 weeks
requires_human_review: true
prerequisites:
  required: []
  optional:
    - artifacts/00-plugin-orientation/planning-state.md
outputs:
  - artifacts/01-civic-alignment/civic-priority-map.md
  - artifacts/01-civic-alignment/city-sponsor-brief.md
  - artifacts/01-civic-alignment/success-definition.md
downstream_skills:
  - 02-event-charter
  - 03-stakeholder-map
  - 05-track-strategy
  - 06-problem-statement-development
  - 08-partnership-and-sponsor-plan
  - 14-judging-system
  - 16-post-event-pipeline
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/01-civic-alignment/civic-priority-map.template.md
  - templates/01-civic-alignment/city-sponsor-brief.template.md
  - templates/01-civic-alignment/success-definition.template.md
search_paths:
  - artifacts/01-civic-alignment/
  - templates/01-civic-alignment/
  - examples/*/01-civic-alignment/
  - ../**/MAYORS_ACTION_PLAN*.md
  - ../**/PILLARS.md
  - ../**/COMPREHENSIVE_PLAN*.md
  - ../**/CIP*.md
  - ../**/strategic-plan*.md
  - docs/civic-priorities/
  - planning/civic/
---

# Skill 01 — Civic Alignment

## Purpose

Anchor the event in a real, public, government-owned strategic plan
and confirm the executive sponsor inside city government. Without
this, every downstream skill drifts.

Produce three artifacts:

1. **`civic-priority-map.md`** — which public priorities the event
   serves and who owns each one in city government.
2. **`city-sponsor-brief.md`** — the named executive sponsor, what
   they have publicly committed to, and the meeting/correspondence
   that records the commitment.
3. **`success-definition.md`** — at most three measurable success
   goals that downstream skills (especially 02, 14, 18) will hold the
   event to.

## When to use

- Starting a civic hackathon from scratch
- Resuming after a year-long gap (re-confirm; do not assume year N's
  alignment still applies in year N+1)
- A new mayor / city manager / DCAO has taken office and the
  political ground may have shifted
- Considering anchoring to a different strategic document than last
  year

## Who should use it

The hackathon's executive lead **with** the city-side liaison. This
skill is not a solo agent task — its outputs are the agent's
synthesis of conversations with named human stakeholders.

## Prerequisites

None required. Optional input: Skill 00's `planning-state.md`.

External inputs (not produced by the plugin, must exist in the world):

- A public strategic plan owned by the local government
- A named executive sponsor inside city government willing to be
  publicly associated with the event

If either external input does not exist, **stop**. The event is not
yet civic-aligned, and producing any artifact in this skill would be
a fiction.

## Inputs

- The public strategic plan (URL, PDF, web page, or document)
- The sponsor's name, title, office, and a record of their
  commitment (meeting note, email, public statement)
- The agent or user's draft of what success looks like

## Outputs

| Artifact | Status when emitted | Human review |
| -------- | ------------------- | ------------ |
| `civic-priority-map.md` | `needs-review` | required |
| `city-sponsor-brief.md` | `needs-review` | required |
| `success-definition.md` | `needs-review` | required |

The skill emits all three at `needs-review`. The named human review
owner (typically the city-side liaison plus the hackathon's executive
lead) marks them `approved` when ready.

## Search behavior

Before generating anything, search for prior alignment material:

1. `artifacts/01-civic-alignment/*` — if the artifacts already exist
   at `draft` or higher, read them and confirm with the user whether
   to revise or supersede.
2. `templates/01-civic-alignment/*` — load the templates.
3. `examples/*/01-civic-alignment/*` — read worked examples for
   reference. Do **not** copy content from examples into the user's
   artifacts.
4. Parent repository, looking for any of:
   - `PILLARS.md`, `MAP.md`, `MAYORS_ACTION_PLAN*.md`,
     `COMPREHENSIVE_PLAN*.md`, `CIP*.md`, `strategic-plan*.md`
   - Markdown files at the parent repo root
   - `docs/`, `planning/`, `research/` directories
5. User-supplied URL or pasted document.

If multiple candidate strategic documents are found, **list them all
and ask the user which is the canonical anchor.** Do not pick one.

## Validation behavior

Run the `civic-priority-map.md`, `city-sponsor-brief.md`, and
`success-definition.md` blocks from `validation/checks.md`.

Specifically, refuse to mark any of the three artifacts as `draft`
(let alone `needs-review`) if:

- The strategic document is not actually public
- The strategic document is not actually owned by city government
- The sponsor is not actually named
- "Success" is a list of feelings rather than measurable outcomes

In those cases, write the artifact body but leave `status:
not-started` and add a blocker explaining the gap.

## Normalization behavior

If the user has prior alignment work — last year's pillar document,
a prior event's mission statement, a previous mayor's strategic plan
— normalize per `normalization/normalization-guide.md`. The
normalized artifact carries `normalized_from` pointing at the
source. **Status starts at `needs-review`**, never `approved`, even
if the source was previously approved. Civic alignment is
time-sensitive.

If the prior source is from a previous administration, flag this
explicitly in `open_questions` and ask the user to confirm the new
administration endorses the same anchor.

## Step-by-step procedure

1. **Search.** Run the search paths above. Inventory candidates.
2. **Confirm the anchor.** Ask the user: which public strategic
   document does the event anchor to? If multiple, the user picks
   one (or names one parent document if the others are derivative).
3. **Read the anchor.** Read the chosen document. Extract:
   - Its name, owner, publication date, URL
   - Its named priorities (pillars, focus areas, goals)
   - The public-sector owner of each priority
4. **Build `civic-priority-map.md`.** One row per priority. Columns:
   priority name, public owner, plan section reference, will this
   event work on it? (yes/no with rationale).
5. **Confirm the sponsor.** Ask the user: who is the named executive
   sponsor? Capture name, title, office, and a record of their
   commitment.
6. **Build `city-sponsor-brief.md`.** Single page. Sponsor identity,
   committed level of engagement, communications protocol, and any
   public statements the sponsor has made about the event.
7. **Draft success.** Ask the user: what would make this event a
   success? Constrain to at most three goals. For each goal, capture
   the measurement, who decides, and the time horizon.
8. **Build `success-definition.md`.** At most three goals. For each:
   measurement, decider, horizon.
9. **Write all three artifacts** at `status: needs-review` with
   review owners named.
10. **Report** to the user with a summary of what was produced,
    which open questions remain, and the next skill (02).

## User interaction rules

- Ask each question once, plainly. Do not interview-style probe.
- If the user cannot answer a question (e.g. "we don't have a sponsor
  yet"), do not invent one. Write the artifact with the section
  blank and `status: blocked` with the blocker recorded.
- If the user names a sponsor who has not actually committed, ask
  what record exists of the commitment. If none, status is
  `needs-review` and the open question is "confirm sponsor
  commitment in writing."
- Never write claims like "the Mayor supports this event" without a
  cited public statement or meeting note.

## Completion criteria

- [ ] `civic-priority-map.md`, `city-sponsor-brief.md`, and
      `success-definition.md` exist at canonical paths
- [ ] All three have frontmatter with `status: needs-review` (or
      higher if a reviewer has signed off)
- [ ] The strategic plan is named with URL or document reference
- [ ] The sponsor is named with title, office, and a citation of
      their commitment
- [ ] At most three success goals exist, each with a measurement,
      decider, and horizon
- [ ] No open question is left blank — either the artifact answers
      it or the artifact records it as open

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| No public strategic plan exists | Stop the skill. The event must wait until a plan exists or the organizers anchor to an alternative public document (e.g. a city council resolution). Write a blocker note explaining the gap. |
| Strategic plan is owned by an NGO, not government | Anchoring is weaker but possible if the NGO is government-adjacent and the executive sponsor accepts. Record as `needs-review`. Flag in `open_questions` for the sponsor to confirm. |
| The sponsor is willing in conversation but has not committed in writing | Write the brief with `status: needs-review` and `open_question: "Obtain written commitment from <sponsor> before Skill 08 (sponsor plan) proceeds."` |
| Success can only be defined in feelings ("we want a good event") | Stop and push the user to one measurable proxy (e.g. "X teams submit," "Y city departments engage in post-event review"). Do not write a vague success-definition.md. |
| Last year's alignment is being reused without re-confirmation | Refuse to mark `approved`. Status remains `needs-review`. Add `open_question: "Re-confirm year-N alignment with the current administration."` |

## Templates used

- `templates/01-civic-alignment/civic-priority-map.template.md`
- `templates/01-civic-alignment/city-sponsor-brief.template.md`
- `templates/01-civic-alignment/success-definition.template.md`

## Downstream skills

Once `01` artifacts are at `draft` or higher:

- **02 (Event Charter)** can run, consuming `civic-priority-map.md`
  and `success-definition.md`.
- **03 (Stakeholder Map)** can run, consuming `city-sponsor-brief.md`.
- **05, 06, 08, 14, 16, 18** all eventually depend on this work.

## Example invocation

> "Run civic alignment. The anchor is Richmond's Mayor's Action Plan
> (May 2025). The sponsor is Michael Kolbe in the Mayor's Office of
> Strategic Initiatives."

Expected steps:

1. Skill searches; finds `2026-annual-hackathon/PILLARS.md` as a
   normalization candidate.
2. Skill offers: "Normalize PILLARS.md into
   `civic-priority-map.md`?" User confirms.
3. Skill reads PILLARS.md, maps the seven pillars onto the
   civic-priority-map template, writes the artifact at
   `needs-review`.
4. Skill asks for the sponsor brief: title, office, written
   commitment record.
5. Skill asks for success: three goals, each measurable.
6. Skill writes all three artifacts at `needs-review` with
   `review_owner: Michael Kolbe (Mayor's Office of Strategic
   Initiatives)`.
7. Reports: "01 complete (pending review). Next: 02 (Event Charter)."

## Changelog

- 1.0.0 (initial) — First version. Three artifact outputs, all
  `needs-review` by default.
