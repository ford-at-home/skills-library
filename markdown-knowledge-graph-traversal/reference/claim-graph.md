# The claim graph, and the claim block

## Node types

`person`, `place`, `concept`, `decision`, `claim`, `risk`,
`evidence` (path + quote), `open-question`.

## Typed edges

The types are the point. An untyped "related to" edge carries no more information
than the two notes being retrieved together, which is what the graph exists to
improve on.

| Edge | Meaning |
|---|---|
| `supports` | Evidence supports a claim |
| `contradicts` | One contradicts another |
| `depends_on` | Holds only if the other is true |
| `caused_by` | Causal |
| `owned_by` | A decision or goal belongs to a person |
| `blocks` | One prevents another |
| `updates` | Newer note revises an older one without invalidating it |
| `supersedes` | Newer note fully replaces an older one |

`updates` and `supersedes` are distinct on purpose. An updated note is still
citable for the parts that stand; a superseded one is not citable as current at
all.

## The claim block

One per major claim, with both axes recorded separately.

```yaml
claim: <plain-language statement>
source_notes:
  - path/to/note.md          # exact path, always
confidence: high | medium | low | speculative
source_quality: firsthand | secondhand | inferred | unverified | ai-generated
supporting_evidence:
  - <quote or reference from a cited note>
contradicting_evidence:
  - <quote, or "none found">
open_questions:
  - <what would have to be known to raise confidence>
```

`contradicting_evidence` has no empty state: it is either a quote or the literal
"none found". Omitting the field is indistinguishable from not having looked.

## Confidence

Confidence is about the weight of evidence. `source_quality` is about where the
evidence came from. Neither substitutes for the other.

| Value | Set when |
|---|---|
| `high` | Several `firsthand` or `secondhand` sources agree, no contradiction |
| `medium` | One good source, or several `inferred` ones, with minor gaps |
| `low` | A single `unverified` source, or sources that disagree |
| `speculative` | No source; reasoning alone. Label it `[Speculative]` |

One source is `medium`, however strong that one source is.
