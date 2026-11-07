# Claim tags, and the shape of the log

## Claim discipline

Every persona tags each factual claim:

| Tag | Meaning |
|---|---|
| `[Verified]` | A source was found. Cite it. |
| `[Unverified]` | No source found. The claim stands as belief, labelled. |
| `[Contradicted]` | Research contradicts an earlier turn. Name the turn. |
| `[Requires SME]` | Only a specific named human can settle this. |

Seven claims cannot be asserted untagged. A persona making one searches first or
tags it `[Unverified]`: this already exists (name the tool, cite it) · this data
is available (name the endpoint, confirm access) · this is structurally blocked
(name the system) · funding exists (name the program and eligibility) · this
worked elsewhere (name where, and whether it still runs) · people won't use this
(cite adoption data) · someone else should own this (name them, verify they exist).

Fabricated citations are worse than no citations, and they are what a persona
under pressure to sound grounded produces.

## Log template

```markdown
# Roundtable: <proposal>
**Date:** <date> · **Evidence loaded:** <list> · **Missing:** <list>
**Unresolved at start:** <criteria that cannot be checked, and why>

## Turn N — <PERSONA> (<phase>)
**Assessment:** <through this persona's lens only, in its output categories>
**Research conducted:** table of tool, query, finding
**Key claims:** each tagged [Verified | Unverified | Contradicted by Turn N | Requires SME]
**Questions for the table:** → <PERSONA>: <answerable in one turn>
**Challenges:** To <PERSONA> (Turn N): <the disagreement and why>
**Temporal tag:** <Appreciating | Depreciating | Stable> — <one sentence>

## Challenge Round N — <PERSONA> responds to <PERSONA> (Turn N)
**Challenge:** <what was contested> · **Response:** <evidence-based>
**Resolution:** <Conceded | Rebutted with evidence | Unresolved, needs SME | Escalated>

## Verdict
**Ship | Refine | Kill** · **Temporal:** <tag>

| Kill criterion | Result | Evidence in log |
|---|---|---|

### Tensions
| Tension | Persona A | Persona B | Resolved? | How |
|---|---|---|---|---|

- Reframed problem: <what the proposal is actually about after deliberation>
- Owner: <named, or the reason none exists>
- If refine: what specifically must change
- If kill: which criterion, and what would have to change to revisit
- The most productive disagreement: <which one, and what it revealed>
```
