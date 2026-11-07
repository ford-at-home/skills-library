# Run record shape

The document this skill produces.

```markdown
# Run Record — <benchmark>
**Manifest:** <hash> · **Run date:** <date>
**Rubric:** <name and version> · **Internal scale:** <e.g. 0.00-1.00>
**Judge:** <exact identifier> @ temperature <x>
**Candidate params:** <temperature, max tokens> — identical across candidates
**Matrix:** <n candidates> × <m scenarios> = <n×m> units
**Cost:** <actual, or the token counts it is derived from>

## Validity checks
| Check | Result | Value | Blocks publication? |
|---|---|---|---|

## Ranking
| Rank | Candidate | Composite (internal) | n | Excluded | Field breakdown |
|---|---|---|---|---|---|

## Excluded units
| Candidate | Scenario | Reason | Error text |
|---|---|---|---|

## Candidate set changes since last run
| Candidate | Added / removed | Reason |
|---|---|---|

## Comparability
- Same manifest hash and same judge as the previous run? <yes / no, what changed>
- What would invalidate comparison to the next run: <list>

## What the ranking does not tell you
- <behavior this rubric doesn't cover>
- <the depth actually exercised, if less than the config declares>
```
