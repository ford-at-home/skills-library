# The assertion ladder

Six rungs. Each catches a class the one above it misses. The middle two are the
point of the skill.

**1 — Structural separation.** Two types, two loaders. The feature type has no
field for the target; the feature loader never reads the section the target lives
in.

**2 — Constructor rejection.** Make the feature type reject unknown keys, so
target data cannot be injected at load time even if it appears in the source.

```python
def test_construction_rejects_injected_target() -> None:
    raw = json.loads(SUBJECT_JSON.read_text())["subject"]
    raw["accepted_price"] = 1_000_000
    with pytest.raises(TypeError):
        Subject(**raw)
```

**3 — Denylist over field names.** Catches the names you thought of, and is the
rung everyone stops at.

```python
FORBIDDEN_FIELDS = frozenset(
    {"accepted_price", "sold_price", "pending_price", "final_price", "ground_truth"}
)

def test_dataclass_has_no_forbidden_fields() -> None:
    field_names = {f.name for f in dataclasses.fields(Subject)}
    leaked = field_names & FORBIDDEN_FIELDS
    assert not leaked, f"Subject leaks ground-truth fields: {sorted(leaked)}"
```

**4 — Allowlist over field names. This is the mechanism.** Take every field whose
name matches the target's semantic family and assert the set equals exactly the
one field allowed to be there:

```python
price_fields = {n for n in field_names if "price" in n.lower()}
assert price_fields == {"list_price"}, (
    f"Subject must only expose list_price, but found: {sorted(price_fields)}"
)
```

The inversion is the whole idea. A denylist fails silently the moment someone
adds a column nobody thought to forbid — `settlement_amount`, `final_number`,
`px_close`, `contract_value`. The allowlist fails the moment the set changes at
all, so it fails on names nobody anticipated. Same number of lines, strictly
stronger assertion: it converts "did we remember to forbid this?" into "did
anyone widen the surface?".

Two things make it work. The membership test must be `==`, never `<=` or
`issubset` — the point is that the set cannot grow. And the message must print
the offending names, because the failure will be read by whoever added the
column, who does not know this rule exists.

Write one rung-4 assertion per semantic family of the target: price, date,
outcome, score, status. Pick match substrings wide enough to catch a synonym.

**5 — Value scan over outputs.** Rungs 1–4 all reason about names. This one
does not, so it survives any renaming and catches leakage through a derived
feature. Assert the ground-truth value does not appear in the model's inputs or
outputs, in any of its string formats, and that no output row equals it exactly:

```python
def test_prediction_does_not_contain_target_value(prediction) -> None:
    serialized = repr(prediction)
    for form in (str(TARGET), f"{TARGET:,}", f"{TARGET:.0f}"):
        assert form not in serialized
    for row in prediction.output_rows:
        assert row.value != TARGET, (
            "no output row should equal the actual target exactly; a coincident "
            "value must arrive from the model's own arithmetic, not from a join"
        )
```

Scan the artifacts a human will see too — logs, exported CSVs, UI cards,
generated reports. Leakage that reaches a display is still leakage.

**6 — Fixture integrity.** The hiding guarantee is vacuous if the target is not
actually present in the source file being loaded. Assert it is:

```python
def test_target_is_present_in_fixture() -> None:
    raw = json.loads(SUBJECT_JSON.read_text())
    assert raw["ground_truth"]["accepted_price"] == EXPECTED
```

Without rung 6 the suite passes brilliantly against a file from which someone
removed the target for unrelated reasons, and you learn nothing.

## Derived columns are re-derived, never trusted

If a flag, bucket, or quality marker is computed upstream and cached in the data
file, re-derive it on every load and ignore the cached value. A hand-edited or
stale flag can otherwise move a row into or out of the baseline population,
shifting the model's reference point without touching a line of model code. Keep
the cached column for triage; never let it reach a computation.
