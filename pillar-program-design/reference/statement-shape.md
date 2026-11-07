# The statement file, and the three roll-up files

One file per problem statement, in this shape.

```markdown
# <Title — 4-8 words, plain English>

**Pillar:** <pillar> · **Type:** practical | open-ended
**Status:** draft | blocked | approved · **Frozen:** <date or "not frozen">
**Institutional ally:** <name, title, office>
**Commitment on record:** <where the ally's agreement is recorded>

## Problem
<Current state. Who is stuck and on what. No solution language.>

## User
<The specific cohort. Not a demographic — a situation.>

## Why this matters
<Tie to a named priority in the anchor, with the section reference.>

## Data needed
| Dataset | Owner | Access path | Refresh cadence | Known limits |
|---|---|---|---|---|

## What good looks like
<Success conditions, not specifications. What is true afterward.>

## Prior art
<What exists elsewhere, how well it works, and whether this is adapt or build.>

## Constraints
<Legal, privacy, and platform limits. Name systems that cannot be integrated.>

## Out of scope
<At least one entry.>

## Open questions
<Unanswered, each tagged to the office that can answer it.>
```

`Commitment on record` is a path or a reference, never a characterization. "Ally
confirmed by email" is not the field's value; the email is.

Plus three roll-up files:

- `pillar-list.md` — pillar, description, the priorities it maps to, its
  committee, its ally. Every merge and split recorded with its reason.
- `dataset-inventory.md` — one row per dataset across all statements. This is the
  file where you find out two pillars depend on the same locked system.
- `open-questions.md` — grouped by the recipient office, so each group can be sent
  as-is.
