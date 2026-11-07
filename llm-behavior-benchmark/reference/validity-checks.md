# Validity checks

Run all of these before publishing. Each is a block, not a note.

| Check | Red when | What it means |
|---|---|---|
| Spread | All composites within 0.15 of the mean on a 0-1 scale | The rubric isn't discriminating. Fix bands, not weights |
| Identical values | Any field returns one value across all units | That field is dead, or the judge is defaulting |
| Top saturation | Most units in the top band | Bands are too generous; the ranking is noise at the top |
| Error rate | >5% of units errored | The ranking is over a biased subsample |
| Field independence | Two fields move together across all units | They are one field; the composite double-counts it |
| Rerun stability | Re-judging the same stored artifacts reorders the top candidates | Judge temperature too high, or bands underspecified |
| Ordering plausibility | Ordering contradicts a strong prior with no readable explanation | Read the transcripts before publishing, then either explain it or find the bug |

Rerun stability is cheap because you kept the raw artifacts: re-judge, don't
re-run.
