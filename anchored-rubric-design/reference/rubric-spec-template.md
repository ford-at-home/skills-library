# Rubric spec template

The shape of the document this skill produces.

```markdown
# Rubric — <behavior>
**Consumer:** <who acts on the score, and how>
**Internal scale:** <e.g. 0.00-1.00> · **Converted at:** <the one boundary>
**Calibrated against:** <n> samples on <date>

## Fields
### <field_name>
- Type: deterministic | llm-bool | llm-scalar
- Range: <values or bounds>
- Measures: <one sentence>
- In tension with: <field, and the output that trades one for the other>

## Bands — <scalar field>
| Range | An output here |
|---|---|
| … | … |

## Judge prompt — <judged field>
<the literal prompt text, including the exclusions and the required JSON shape>

## Composite
<the arithmetic, as code>

| Field | Penalty cap | Weight | Max influence on composite |
|---|---|---|---|

## Calibration
| Sample | Field scores | Composite | Expected band | Agreed? |
|---|---|---|---|---|

Spread across samples: <min>-<max>, mean <x>

## Gaming audit
| Field | Cheapest output that scores well on it | Its composite | Verdict |
|---|---|---|---|

## Error value
<what is recorded when a judge call fails, and why it is not the bottom score>
```
