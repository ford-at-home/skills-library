# How this goes wrong

Each of these leaves a corpus that reconciles by count and is wrong in a way
nothing downstream reports. That is why the corresponding entries in SKILL.md are
rules rather than preferences.

**The one it exists to catch.** The model changes, someone re-runs the job to
pick up the stragglers, and the resume skips every item the old model produced
because the checkpoint key is item identity alone. The corpus is now half one
model and half another, the counts are perfect, and nothing in the output says
which record came from which. Six months later the only way to find out is to
read the text.

**The checkpoint that stores progress but not output.** A resume marks
previously-completed items as done, skips them, and returns an in-memory result
containing only the current run's work. The returned object has exactly the
shape of a complete corpus and is missing everything the earlier runs produced.
Observed in practice.

**Permanently skipped failures.** A resume skips both completed and
previously-failed items so the run finishes cleanly, and the failed items are
never revisited. The final output is short by the failure count and reports
success. Observed in practice.

**The destructive failure write.** Marking an item failed uses a full-row
upsert that supplies only the identity and error columns. On a database whose
upsert deletes and reinserts the conflicting row, retrying a batch and hitting
an error on an item that previously succeeded erases the stored output. Observed
in practice — check what your upsert does to unlisted columns before trusting a
retry pass.

**The fabricating fallback.** When the model output fails validation, the code
constructs a record from the source text — a prefix, a case change, a copy — so
the pipeline does not stall. That record passes validation, lands in the corpus,
and is now permanently indistinguishable from real output. Observed at two
levels in the same codebase. A validator paired with a fabricating fallback is
worse than no validator: it converts a loud failure into a silent one.

**Two behaviors for one failure class.** A provider error inside the per-field
try block sets the field to empty and marks the item processed; the same error
one line outside re-raises and leaves the item unprocessed. Both are defensible;
having both is not. Decide once, per failure class.

**Estimated cost recorded as measured.** Token counts derived from
`len(text) // 4`, multiplied by a price table, stored in a `cost_usd` column
beside a code comment admitting the real counts were available on the response.
The number is a character count wearing a dollar sign.

**Cost known and unenforced.** Every implementation reviewed estimated total cost
before starting and printed it; none stopped at a threshold. The only circuit
breaker that existed fired on the provider's insufficient-credit error — correct
behavior, and it fires when the money is gone rather than at a limit you chose.
