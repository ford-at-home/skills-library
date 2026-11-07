# The checkpoint record, the completeness marker, and write ordering

## The checkpoint record

Inline this shape. Every field is load-bearing.

```yaml
key: <sha256 of item_identity + sorted transform_config>  # the resume decision
item_identity: {source_id: A-104, section: 3}  # human-readable, for triage
status: completed | failed                    # never absent, never a third value
config: {model: <id>, prompt_version: <v>, temperature: 0.7, mode: <m>}
attempt: 2                                    # which attempt produced this
cost: {input_tokens: 4210, output_tokens: 5533, usd: 0.0041, source: measured}
                                              # source: measured | estimated
output_ref: <path or row id>                  # where the record actually is
error: <message, or null>
written_at: <iso8601>
```

`config` is duplicated inside the record even though it is already in the key.
The key decides resume; the copy lets you diagnose a mixed corpus after the
fact, when all you have is the output.

`cost.source` exists because a cost derived from a character-count heuristic and
a cost read off the provider's response will otherwise sit in the same column at
the same apparent precision. Label it or the estimate becomes a measurement.

## Completeness marker

Partial output must be distinguishable from complete output by something that is
**absent on success**, not present on success. A flag you have to remember to
set will not be set on the run that crashes.

The strongest pattern found in practice: a progress file that exists for the
duration of the run and is deleted only after the final output write returns.
Its presence means incomplete. Nothing has to remember anything.

Whatever consumes the output must check for the marker. A marker nobody reads is
decoration.

## Atomic write

A partially-written record is worse than a missing one: it parses far enough to
look real. Write to a temporary path in the **same directory**, then rename.
Same-directory rename is atomic, so a reader sees the old bytes or the new
bytes, never a truncated file.

```python
import json, os, tempfile
from pathlib import Path

def write_atomic(path: Path, payload: dict) -> None:
    """Write JSON so a crash mid-write cannot leave a half-parsed file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())        # rename is atomic; content is not durable without this
        os.replace(tmp, path)           # same-filesystem rename
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise
```

Apply this to the final aggregate write too. The write most often left
unprotected is the last one, which is also the one that costs the whole run.

## Validation position

Validate **before** the write, never after.

A validate-after pipeline needs a repair pass, and a repaired record is
indistinguishable from a record that was right the first time. Validation before
the write means a bad record never enters the corpus, and its failure record
names why.

Validate three things, in this order:

1. **Parse** — is it the format you asked for
2. **Shape** — required keys present, types correct, no empty required values
3. **Conservation** — does the output account for every unit of the input. If the
   input had 31 rows, paragraphs, or segments, the output has 31 keys. Missing
   units reject the record. Extra units are a warning and are dropped, after
   logging which ones.

Conservation catches truncation, and truncation is the failure mode that passes
shape validation cleanly.
