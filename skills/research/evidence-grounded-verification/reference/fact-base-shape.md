# Clearance levels and the fact base template

## Clearance levels

Every cleared claim carries one of these, and the level determines how the claim
may be phrased in the document.

| Level | Meaning | How to attribute |
|---|---|---|
| `primary` | The originating body stated it — statute, filing, published paper, their own release | Cite directly |
| `secondary` | A reputable third party reported it | Cite the reporter, not the origin |
| `vendor-self` | The subject said it about itself | Attribute explicitly: "X states that…" |
| `internal` | Your own document or measurement | Never counts as corroboration of your own claim |
| `private` | Told to you, not public | Not citable externally under any framing |

Advocacy outlets, trade associations, and aggregators can't carry a load-bearing
claim. A trade outlet summarizing a press release is not a primary source for
that release — go to the release.

## The fact base

```markdown
# Fact Base — <document>
**Audience:** <who reads this>
**Cleared as of:** <date> · **Decays first:** <what, and by when>

## Unresolved (read first)
- <what isn't settled, and what would settle it>

## Block 1 — Do not cite
### <claim>
- Believed because: <where it came from>
- Searched: <where you looked>
- Found: <what, or "nothing">
- Re-anchor to: <nearest documented fact, or "no adjacent fact exists">

## Block 2 — Correct before use
### <short name>
- Stated: <the wrong version>
- Correct: <the accurate version>
- Source: <where the correct version comes from>

## Block 3 — Cleared
| Claim | Level | Source | Date | Phrasing that survives |
|---|---|---|---|---|

## Contradictions
| Claim | Source A | Source B | Unresolved because |
|---|---|---|---|

## Measured vs derived
| Finding | Which | If derived: assumption, and was the method ever checked? |
|---|---|---|

## Relationship-risk flags
| Claim | Verified? | Risk | Sign-off needed from |
|---|---|---|---|
```

Unresolved sits at the top rather than the bottom. It holds the claims nobody
settled, including the ones where a source existed and you could not reach it —
which is a different statement from Block 1, and must not be filed there.
