# The orientation report

```markdown
## Orientation — <task>

### Model
| Fact | Label | Evidence |
|---|---|---|
| <statement> | Verified | <file:line or command> |
| <statement> | Partial | <what exists, what doesn't> |
| <statement> | Missing | <where it was claimed, why absent> |
| <statement> | External | <where it actually lives> |

### Documentation vs code
- <doc claim> → <what the code shows> → <which is right, what to fix>

### Layers affected
- <layer> → <files to modify> / <files to create>

### Existing pattern to follow
- <named file> — <why it is the right model>

### Already exists?
- <concept> → <found at path, extend it> | <ruled out: searched for X, Y, Z>

### Hands off
- <generated or vendored paths>

### Validation commands
- <command> — <why this change needs it>

### Manual actions required (External)
- <action, and who must do it>

### Unverified
- <claim I could not check, and what would settle it>
```

The `Unverified` section is mandatory and may not be empty by default. If you
verified everything load-bearing, say so explicitly.
