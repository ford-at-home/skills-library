# What each decision commits to, and the shape of the review

| Per initiative | Meaning |
|---|---|
| **continue** | Allocation stays. It survived the zero-based check |
| **wind down** | Stopped or de-prioritized over the next period |
| **amplify** | Allocation grows, with cited triggering evidence |
| **hold** | Allocation stays pending a named forthcoming decision, with a due date |
| **pivot** | Continues with a revised hypothesis; needs re-authorizing |

`hold` is not a softer `continue`. `continue` is a decision made now; `hold` names a
decision coming, and carries the date it is due.

| Per candidate | Meaning |
|---|---|
| **fund** | Enters the portfolio. Requires a named source of the capacity |
| **park** | Stays in the backlog. Only if zero-based authoring would not include it *and* it has not aged out |
| **reject** | Leaves the backlog. Rationale required |

| Drift severity | Meaning |
|---|---|
| **blocking** | The zero-based check fails materially; the portfolio must change this period |
| **significant** | Drift named; deferring the change needs justification |
| **acceptable** | Within tolerance; documented, forces no change |

## Review template

```markdown
# Reallocation Review — <period>
**Total capacity:** <n> <unit>
**Changes made:** <true | false> · **Zero-based check passed:** <true | false>
**Built blind:** <true | false> · **Masked ranking run:** <true | false>

## Zero-based portfolio — built first
| Initiative or candidate | Allocation | Rationale (cite the current case, risks, return) |
|---|---|---|

## Masked ranking differences
<Any initiative whose position changed when origins were stripped.>

## Drift from actual
| Initiative | Current | Zero-based | Delta | Reason for the gap | Pattern |
|---|---|---|---|---|---|

## Initiative decisions
| Initiative | Decision | New allocation | Triggering evidence |
|---|---|---|---|

<For each pivot: the revised hypothesis, what would validate it, revised capacity.>
<For each hold: the decision that is coming, and its due date.>

## Candidate decisions
| Candidate | Decision | Allocation | Draws capacity from | Rationale |
|---|---|---|---|---|

## Drift detected
| Pattern | Initiatives affected | Evidence | Severity |
|---|---|---|---|

## Considered for stopping
<Every initiative weighed for wind-down, including those not recommended for it.>

## Narrative
<Three to five sentences. Surfaces the stops and the amplifications, not the totals.>

## If nothing changed
<Why each initiative individually survives zero-based authoring. "We reviewed and
chose to keep everything" is not an answer to this.>
```

Tag every claim: `[fact]` (sourced), `[assumption]` (believed, untested),
`[inference]` (derived from facts above), `[open question]`.
