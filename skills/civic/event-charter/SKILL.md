---
description: "Convert civic alignment into a small set of documents the"
skill_number: "02"
skill_id: event-charter
name: Event Charter
version: 1.0.0
status: initial
lifecycle_stage: pre-event
estimated_duration: 1-2 weeks
requires_human_review: true
prerequisites:
  required:
    - artifacts/01-civic-alignment/civic-priority-map.md
    - artifacts/01-civic-alignment/success-definition.md
  optional:
    - artifacts/01-civic-alignment/city-sponsor-brief.md
outputs:
  - artifacts/02-event-charter/event-charter.md
  - artifacts/02-event-charter/operating-principles.md
  - artifacts/02-event-charter/scope-boundaries.md
downstream_skills:
  - 03-stakeholder-map
  - 04-governance-model
  - 05-track-strategy
  - 08-partnership-and-sponsor-plan
  - 09-community-outreach-plan
  - 10-participant-experience-plan
  - 12-event-operations-plan
  - 13-technology-setup
  - 14-judging-system
  - 17-open-source-handoff
  - 18-retrospective-and-next-year-plan
templates_used:
  - templates/02-event-charter/event-charter.template.md
  - templates/02-event-charter/operating-principles.template.md
  - templates/02-event-charter/scope-boundaries.template.md
search_paths:
  - artifacts/02-event-charter/
  - templates/02-event-charter/
  - examples/*/02-event-charter/
  - ../**/CHARTER*.md
  - ../**/MISSION*.md
  - ../**/event-brief*.md
  - docs/charter/
---

# Skill 02 — Event Charter

## Purpose

Convert civic alignment into a small set of documents the
organizing team and external stakeholders can read in 5 minutes:

1. **`event-charter.md`** — the event's mission, dates, venue,
   expected scale.
2. **`operating-principles.md`** — three to seven principles that
   break ties throughout planning. Each principle is action-oriented
   and includes an example tie.
3. **`scope-boundaries.md`** — explicit "we will do this / we will
   not do this" list, justified by the principles.

These three documents make the rest of planning legible. Most
downstream skills cite one or more of them.

## When to use

- Immediately after Skill 01 completes
- When the event is being publicly announced for the first time
- When a stakeholder asks "what is this event for?" and the
  organizers cannot answer in two sentences

## Who should use it

Executive lead + city-side liaison + the operations lead. This is a
group exercise, not a solo agent task. The agent's role is to
record, structure, and stress-test.

## Prerequisites

**Required:**

- `artifacts/01-civic-alignment/civic-priority-map.md` at status
  `draft` or higher
- `artifacts/01-civic-alignment/success-definition.md` at status
  `draft` or higher

**Optional:**

- `artifacts/01-civic-alignment/city-sponsor-brief.md` (strongly
  recommended; the charter cites the sponsor)

If `success-definition.md` is at `draft`, the charter goes to
`needs-review` and notes the soft dependency. If
`success-definition.md` is missing, **stop** — the charter has
nothing to align to.

## Inputs

- The two upstream artifacts above
- A proposed date range and venue (or an explicit "TBD" with a
  target)
- The expected scale: number of participants, number of teams,
  number of tracks (latter likely "TBD" until Skill 05)

## Outputs

| Artifact | Status when emitted | Human review |
| -------- | ------------------- | ------------ |
| `event-charter.md` | `needs-review` | required |
| `operating-principles.md` | `draft` | optional |
| `scope-boundaries.md` | `needs-review` | required |

## Search behavior

1. `artifacts/02-event-charter/*` — existing artifacts?
2. `templates/02-event-charter/*` — load templates.
3. `examples/*/02-event-charter/*` — read for reference only.
4. Parent repo for `CHARTER*.md`, `MISSION*.md`, `event-brief*.md`,
   `kickoff-emails/`.
5. User-supplied content.

Kickoff emails from a prior event are excellent input for the
charter's "what this event is" framing — the prose has already been
externally tested.

## Validation behavior

Run the `event-charter.md`, `operating-principles.md`, and
`scope-boundaries.md` blocks from `validation/checks.md`.

Additional checks:

- The charter's mission sentence must be one sentence. Reject
  multi-paragraph "missions."
- The charter must cite both upstream artifacts by path.
- Operating principles must be **action-oriented** ("we anchor every
  track to a named public priority") rather than aspirational ("we
  value impact"). Reject the aspirational form.
- Scope boundaries must list **both** what the event will do and
  what it will not do. A scope document with only positives is
  rejected.

## Normalization behavior

If the user provides existing charter-like content (a deck, a
kickoff email, a sponsor pitch), normalize per the guide.

Special case: kickoff emails are excellent source material but are
**not** the charter. Normalize their content into the charter
template; do not copy the email verbatim into the artifact.

## Step-by-step procedure

1. **Search.** Run search paths.
2. **Confirm upstream.** Read `civic-priority-map.md` and
   `success-definition.md`. If either is missing or `not-started`,
   stop and report.
3. **Draft the mission sentence.** One sentence: "The <event name>
   is a <duration> <event type> that <action> <civic outcome>
   anchored in <strategic plan>."
4. **Capture event facts.** Dates, venue, scale (participants,
   teams, tracks). Note "TBD" where genuinely unknown.
5. **Draft the operating principles.** With the user, write 3-7
   action-oriented principles. For each, write one example tie the
   principle breaks. Tie examples come from real planning
   tradeoffs the team has already encountered.
6. **Draft scope boundaries.** Two columns: "will do" and "will
   not do." Each row references at least one operating principle.
7. **Cross-check.** Every success goal in `success-definition.md`
   must be addressable by something in the charter. Every priority
   in `civic-priority-map.md` marked "yes, this event will work on
   it" must appear in the charter's scope.
8. **Write artifacts** at `needs-review` (charter, scope) or
   `draft` (principles).
9. **Report** with summary, open questions, next skill (03).

## User interaction rules

- The mission sentence is the highest-leverage paragraph in the
  entire planning corpus. Push the user to make it concrete. Reject
  vague drafts.
- Operating principles must be derived from real tradeoffs the team
  has already faced, not aspirations. If the user cannot name a tie
  a principle has broken, the principle is probably aspirational and
  should be dropped or rewritten.
- Scope boundaries should make at least one organizer
  uncomfortable. If the "will not do" column has zero items that
  feel like sacrifices, the boundaries are too soft.

## Completion criteria

- [ ] All three artifacts exist at canonical paths
- [ ] Charter cites both upstream artifacts
- [ ] Mission sentence is one sentence and concrete
- [ ] 3-7 operating principles, each action-oriented with an
      example tie
- [ ] Scope has at least 3 "will do" and 3 "will not do" entries
- [ ] Charter is at `needs-review` with named reviewer
- [ ] Scope boundaries are at `needs-review`

## Failure modes & recovery

| Failure | Recovery |
| ------- | -------- |
| `success-definition.md` is missing | Stop. Skill 01 must complete first. |
| Mission sentence won't compress to one sentence | The team likely has not picked an anchor. Send them back to `civic-priority-map.md` to confirm which priorities are in scope. |
| Operating principles are aspirational | Push for tie examples. If no tie example exists, drop the principle. |
| Scope boundaries are too soft | Ask the team: "What did we already say no to?" Those are the boundaries. |
| Dates/venue are unknown | Allow "TBD" but require a target date for resolution; record in `open_questions`. |
| Multiple organizers disagree on the charter | The charter is the place where this disagreement must resolve before downstream skills run. Surface the disagreement; do not paper over it. |

## Templates used

- `templates/02-event-charter/event-charter.template.md`
- `templates/02-event-charter/operating-principles.template.md`
- `templates/02-event-charter/scope-boundaries.template.md`

## Downstream skills

Skill 02's outputs gate roughly 10 downstream skills. In practical
terms: nothing else can run cleanly until the charter exists at
`draft` or higher.

## Example invocation

> "Write the event charter. The anchor is the Mayor's Action Plan;
> success goals are in `success-definition.md`. We're aiming for
> March 27-29 at VCU Snead Hall, 200-300 participants, 7 tracks."

Expected steps:

1. Skill reads upstream artifacts.
2. Skill drafts a one-sentence mission and asks the user to confirm.
3. Skill walks the user through 3-7 operating principles, with tie
   examples for each.
4. Skill walks scope boundaries; pushes back on "will not do"
   entries that don't feel like sacrifices.
5. Skill writes the three artifacts at `needs-review` / `draft`.
6. Skill reports: "02 complete. Next: 03 (Stakeholder Map)."

## Changelog

- 1.0.0 (initial) — First version. Three artifact outputs. Charter
  and scope at `needs-review`; principles at `draft` because
  principles change throughout the year.
