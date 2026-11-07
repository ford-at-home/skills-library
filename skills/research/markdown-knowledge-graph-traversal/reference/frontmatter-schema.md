# The frontmatter schema this skill reads

Notes in a well-formed corpus carry typed YAML frontmatter. This is the schema
the skill expects.

```yaml
---
type: source | entity | concept | decision | synthesis | evaluation | claim
      | open-question | goal | value | research | plan
domain: <topic area, e.g. finance, health, product/pricing>
status: active | archived | superseded | draft | needs-review
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_quality: firsthand | secondhand | inferred | unverified | ai-generated
sensitivity: public | personal | private | sensitive
related:
  - "[[Note Title]]"
claims:
  - "one discrete, falsifiable assertion this note makes"
tags:
  - "#topic/subtopic"
---
```

**Fallback for notes with no frontmatter:** treat them as
`source_quality: unverified`, `status: draft`, and rank them below typed notes.
Do not upgrade a note's standing because its prose sounds authoritative.

`claims:` is a **cache**, not a summary — a list of discrete assertions. If a
note's body has clearly moved past its `claims` array, the cache is stale: trust
the body and flag the note in Notes to Update.

## Source quality

The axis that makes this skill work. It is orthogonal to confidence: *how sure
am I* and *where did this come from* are different questions, and collapsing
them is what makes an agent treat every note as equally true.

| Value | Meaning |
|---|---|
| `firsthand` | The corpus owner wrote, experienced, or directly confirmed it |
| `secondhand` | From a named, traceable external source |
| `inferred` | Derived from other notes; not directly stated anywhere |
| `unverified` | Asserted, not confirmed |
| `ai-generated` | Produced by a model; needs human review before it is trusted |

## Uncertainty labels in the answer text

A metadata column is not enough — the label goes in the prose a reader actually
reads.

| Label | Applied to |
|---|---|
| `[Unverified]` | `source_quality: unverified` or `ai-generated` |
| `[Inference]` | `source_quality: inferred` |
| `[Speculative]` | A hypothesis with no source note |
| `[Superseded]` | A claim overtaken by a newer note |

A corpus that has been answered from for a while will contain your own prior
syntheses. Model-written synthesis notes are starting points for review; do not
let them corroborate themselves.
