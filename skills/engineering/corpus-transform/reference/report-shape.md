# Run plan and run manifest

```markdown
# Run Plan — <corpus>
**Items:** <n> · **Key:** <formula> · **Config:** <model, prompt version, ...>
**Cost:** <n> x $<per item> = $<total> · **Ceiling:** $<ceiling>
**Single-item failure:** record and continue
**Run-level failure:** halt, in-flight item not marked failed
**Completeness marker:** <path>, deleted after final write

## Resume analysis (if resuming)
| State | Count | Action |
|---|---|---|
| Key matches current config | | reuse |
| Key present, config differs | | reprocess — list the differing values |
| Failed in prior run | | retry |
| Never attempted | | process |

# Run Manifest — <corpus>
**Started / ended:** <iso8601> · **Config:** <as above>
**Complete:** yes | no — <why not>

| | Count |
|---|---|
| Corpus items | |
| Completed this run | |
| Reused from prior run | |
| Failed | |
| Never attempted | |
| **Reconciles to corpus total** | yes / no |

**Spend:** $<actual> of $<ceiling> · estimated $<estimate> · ratio <a/e>
**Cost basis:** measured | estimated — <which, and how>

## Failures
| Key | Item | Attempts | Error | Retryable |
|---|---|---|---|---|

## Provenance warnings
- <records in the output produced by a different config, and which>
```
