# Leakage audit report shape

```markdown
# Leakage Audit — <model>
**Target:** <quantity> · **Knowable at:** <moment>
**Claim to be presented:** <accuracy figure, to whom>
**Holdout:** <how, or "none — stated as a limit">

## Verdict
clean | leakage found | cannot determine — <one line>

## Field classification
| Field | Knowable before target? | Derived from post-target data? | Verdict |
|---|---|---|---|

## Assertion ladder
| Rung | Present | Passes | File |
|---|---|---|---|
| 1 structural separation | | | |
| 2 constructor rejection | | | |
| 3 denylist | | | |
| 4 allowlist (==) | | | |
| 5 value scan over outputs | | | |
| 6 fixture integrity | | | |

## Leaks found
### <field or path>
- Reaches the model via: <call path>
- Knowable only after: <moment>
- Effect on the validation figure: <measured, or "not measured">
- Fix: <structural change, not a filter>

## Calibration freeze
**Frozen:** <date> · **Values:** <metrics> · **Tolerance:** <bounds>
**Known biases asserted visible:** <which, by which test>

## Known limits
| Limit | Cause | What would fix it | Fabrication risk it creates |
|---|---|---|---|

## Could not verify
- <claim, and why>
```
