# The default schema

Use this if the corpus has no declared one, and record in the report that you
did.

```yaml
---
type: source | entity | concept | decision | synthesis | evaluation | claim
      | open-question | goal | value | research | plan
domain: <topic area>
status: active | archived | superseded | draft | needs-review
created: YYYY-MM-DD
updated: YYYY-MM-DD           # add when content materially changes
source_quality: firsthand | secondhand | inferred | unverified | ai-generated
sensitivity: public | personal | private | sensitive
related:
  - "[[Note Title]]"
claims:
  - "one discrete, falsifiable assertion this note makes"
supersedes: "[[Old Note]]"    # only when this note replaces another
tags:
  - "#topic/subtopic"
---
```

`source_quality` values, since the whole point of the field is calibration:

| Value | Meaning |
|---|---|
| `firsthand` | The owner wrote, experienced, or directly confirmed it |
| `secondhand` | From a named, traceable external source |
| `inferred` | Derived from other notes; not directly stated |
| `unverified` | Asserted, not confirmed. Body must carry `[Unverified]` |
| `ai-generated` | Model-produced. Needs human review before trust rises |

Inline body labels that must be present where the field implies them:
`[Unverified]`, `[Inference]`, `[Speculative]`, `[Superseded]`.

## A note with no frontmatter is not a defect to be silently fixed

It is treated as `source_quality: unverified`, `status: draft`, and ranked below
typed notes at retrieval time. That ranking penalty is the incentive to maintain
the schema; removing it by backfilling guesses removes the incentive too.
