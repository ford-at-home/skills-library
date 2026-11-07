---
skill_number: "03"
skill_id: stakeholder-map
name: Stakeholder Map
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 2-4 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/01-civic-alignment/city-sponsor-brief.md
    - artifacts/02-event-charter/event-charter.md
  optional:
    - artifacts/00-plugin-orientation/planning-state.md
    - artifacts/02-event-charter/scope-boundaries.md
outputs:
  - artifacts/03-stakeholder-map/stakeholder-map.md
  - artifacts/03-stakeholder-map/partner-register.csv
  - artifacts/03-stakeholder-map/partner-register.csv.meta.yaml
  - artifacts/03-stakeholder-map/decision-maker-map.md
downstream_skills:
  - 04-governance-model
  - 05-track-strategy
  - 06-problem-statement-development
  - 08-partnership-and-sponsor-plan
  - 09-community-outreach-plan
  - 11-mentor-volunteer-ops
  - 14-judging-system
  - 16-post-event-pipeline
  - 17-open-source-handoff
templates_used:
  - templates/03-stakeholder-map/stakeholder-map.template.md
  - templates/03-stakeholder-map/partner-register.template.csv
  - templates/03-stakeholder-map/partner-register.meta.template.yaml
  - templates/03-stakeholder-map/decision-maker-map.template.md
search_paths:
  - artifacts/03-stakeholder-map/
  - templates/03-stakeholder-map/
  - examples/*/03-stakeholder-map/
  - ../**/CONTACTS.md
  - ../**/CONTACTS.csv
  - ../**/POST_HACKATHON_CONTACTS*
  - ../**/stakeholder*.md
  - ../**/partners*.csv
  - docs/contacts/
  - outreach/
---

# Skill 03 — Stakeholder Map

## Purpose

Identify every category of stakeholder, every named partner, and
every decision maker the event will engage. Produce the contact
backbone the rest of planning depends on.

Three artifacts:

1. **`stakeholder-map.md`** — categorical view: who matters, why
   they matter, how engaged they should be.
2. **`partner-register.csv`** — operational view: a flat table of
   real people and organizations with contact info, status, and
   ownership.
3. **`decision-maker-map.md`** — domain-specific view: for each
   decision domain (city alignment, sponsor commitments, judging,
   public communications, legal, technology), who decides.

The three are not redundant. They serve different reader modes:
the strategy reader, the operational reader, and the escalation
reader.

## When to use

- Immediately after Skill 02
- When onboarding a new organizer who needs the lay of the land
- When a new partner appears and needs categorizing
- Periodically (every 4-6 weeks) to confirm the partner register is
  current

## Who should use it

The partnership lead + city-side liaison. The agent's job is to
structure and check, not invent.

## Prerequisites

**Required:**

- `01/city-sponsor-brief.md` at `draft` or higher
- `02/event-charter.md` at `draft` or higher

**Optional:**

- `02/scope-boundaries.md` — useful for deciding which stakeholders
  are in/out of scope

If the charter is at `not-started`, the stakeholder map has nothing
to anchor to. Stop.

## Inputs

- Upstream artifacts
- Any existing contact list, CRM export, or prior-event partner
  roster
- The user's knowledge of who is in the room

## Outputs

| Artifact | Status | Human review |
| -------- | ------ | ------------ |
| `stakeholder-map.md` | `needs-review` | yes |
| `partner-register.csv` | `needs-review` | yes |
| `partner-register.csv.meta.yaml` | mirrors the CSV | n/a |
| `decision-maker-map.md` | `needs-review` | yes |

All three require human review because they name real people whose
agreement matters.

## Search behavior

1. `artifacts/03-stakeholder-map/*` — existing?
2. `templates/03-stakeholder-map/*` — load.
3. `examples/*/03-stakeholder-map/*` — reference only.
4. Parent repo, looking for:
   - `CONTACTS.md` or `CONTACTS.csv`
   - `POST_HACKATHON_CONTACTS.csv` / `POST_HACKATHON_CONTACTS.md`
   - `outreach/` — any directory of outreach emails is a goldmine
     for "who has been contacted" data
   - Any directory of kickoff emails
   - Any prior partner register
5. User-supplied content.

## Validation behavior

Run the three artifacts' validation blocks from
`validation/checks.md`.

Additional checks:

- Every partner in the CSV must appear in at least one category in
  `stakeholder-map.md`
- Every decision domain in `decision-maker-map.md` has exactly one
  decider
- PII handling: emails and phone numbers are allowed in the CSV
  (it is intentionally a contact register), but not in the
  stakeholder-map or decision-maker-map (those are summary
  documents)
- No row claims `commitment status: confirmed` without a date

## Normalization behavior

`CONTACTS.md`-style documents commonly exist from prior events.
Normalize them into `partner-register.csv` with the schema:

```
name, organization, role, email, phone, category, pillar_or_track,
commitment_status, last_contact_date, owner, notes
```

`POST_HACKATHON_CONTACTS.csv` or similar may already be in tabular
form; map columns onto the schema and flag missing columns.

A prior year's contact list is **not** the current year's partner
register. Carry over names that the user explicitly confirms still
apply; do not carry over commitments without re-confirmation.

## Step-by-step procedure

1. **Search.** Inventory candidates.
2. **Read upstream.** Confirm the sponsor brief and charter exist
   and are usable.
3. **Categories first.** Walk the user through the stakeholder
   categories:
   - city government (executive, departments, council)
   - civic / nonprofit partners
   - sponsors (corporate, foundation, in-kind)
   - subject-matter mentors
   - judges
   - participants and participant communities
   - vendors (venue, AV, food, swag)
   - press / media
4. **Build `stakeholder-map.md`.** For each category, state
   interest, engagement level, and owning organizer.
5. **Build `partner-register.csv`.** One row per named person.
   Normalize from any source documents found. Fill `owner` (who on
   the organizing team owns the relationship) for every row;
   blank owner is not allowed.
6. **Write the CSV's `.meta.yaml` sidecar** with the frontmatter
   and a `columns:` declaration.
7. **Build `decision-maker-map.md`.** For each decision domain
   (listed in `validation/checks.md`), name the decider, the
   recommender(s), and the informed parties.
8. **Cross-check.** Every commitment in `partner-register.csv` that
   has `commitment_status: confirmed` must be traceable to a
   meeting note, email, or other record. If not, downgrade to
   `verbal` and flag.
9. **Write artifacts** at `needs-review`.
10. **Report.**

## User interaction rules

- Never invent a contact. If the user does not know who owns a
  category, leave it blank and flag in `open_questions`.
- Confirmed commitments require evidence. Verbal "they said yes" is
  `commitment_status: verbal`, not `confirmed`.
- PII handling: confirm with the user before publishing
  `partner-register.csv` outside the organizing team. The artifact
  itself is in the repo; whether the repo is public matters.
- Decision domains should not have shared deciders. If two people
  share authority, the team has not actually decided — surface
  this.

## Completion criteria

- [ ] Three artifacts exist at canonical paths
- [ ] Every partner has an owner
- [ ] Every category has an owning organizer
- [ ] Every decision domain has exactly one decider
- [ ] No PII appears outside the partner register
- [ ] CSV sidecar is present and validates against schema

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| User doesn't know who decides a domain | Mark the row `decider: TBD` and add an `open_question` blocking on resolution. Skill 04 will revisit. |
| Two people claim to be the decider for a domain | Stop and surface. The team must resolve before the map is `approved`. |
| Prior year's contact list is huge and stale | Normalize but mark every row `commitment_status: stale` until the user confirms each one. |
| User wants to put a verbal commitment into the register | Allow it, but the row gets `commitment_status: verbal`, not `confirmed`. |
| A partner appears in the map but has no owner on the team | The team is over-committed. Flag and ask the user to drop the partner or assign an owner. |

## Templates used

- `templates/03-stakeholder-map/stakeholder-map.template.md`
- `templates/03-stakeholder-map/partner-register.template.csv`
- `templates/03-stakeholder-map/partner-register.meta.template.yaml`
- `templates/03-stakeholder-map/decision-maker-map.template.md`

## Downstream skills

- **04 (Governance Model)** consumes all three.
- **05, 06** read `stakeholder-map.md` and `partner-register.csv`
  to ensure track and problem-statement work has civic anchors.
- **08, 09, 11, 14, 16, 17** all draw from the partner register.

## Example invocation

> "Build the stakeholder map. I have CONTACTS.md and
> POST_HACKATHON_CONTACTS.csv from last year."

Expected steps:

1. Skill normalizes CONTACTS.md into the partner-register CSV.
2. Skill cross-references POST_HACKATHON_CONTACTS.csv for any new
   names not in CONTACTS.md.
3. Skill asks the user to confirm category for each partner and
   assign owners.
4. Skill walks decision domains.
5. Skill writes artifacts at `needs-review`.

## Changelog

- 1.0.0 (initial) — First version. CSV sidecar pattern enforced;
  prior-year contacts carried over only on explicit confirmation.
