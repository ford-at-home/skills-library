# How an anchored rubric goes wrong

**The one it exists to catch.** Every candidate scores between 7 and 8 on an
unanchored 1-10 scale and the ranking is noise. The fix is never more precision
in the instruction ("be strict", "be discriminating") — it is band text
describing what a 4 actually looks like. Instructions to be harsh move the whole
distribution; anchors spread it.

**LLM-authored composite.** The judge returns fields plus an overall. The overall
is what everyone reads, no one checks that it follows from the fields, and it
silently doesn't.

**Penalty that can't reach.** A field is described as a "50% penalty" and carries
weight 0.3, so its actual maximum effect on the composite is 0.15. Nobody
notices, because the number in the code and the number in the comment are both
true about different things.

**Instructed penalties read as enforced.** A judge prompt lists automatic
deductions. Six months later a document describes them as applied. They were
always advisory — a stronger model honors them, a weaker one doesn't, and the
difference shows up as inexplicable variance between judge models.

**Correlated fields.** Three fields a good output satisfies together. The
composite is one number reported three times, gameable by whatever produces
that one property.

**Errors scoring zero.** A failed judge call is stored as 0.0 and enters the
mean. Downstream code grows a filter like `if score < 0.01: skip`, which then
also drops genuinely terrible outputs, and the ranking quietly improves.

**Stale rubric outliving its replacement.** A superseded rubric survives in
backup files, old harnesses, test fixtures, and diagnostic tooling long after
the live one changed. Anyone reading those finds a coherent, wrong description.
When you replace a rubric, grep for its field names and delete every hit that
isn't the live path.

## What the scale rule costs when it is skipped

The scale rule looks pedantic until you count the cost. In the project this
skill was extracted from, nine separate commits are scale-conversion fixes, and
several corrected the previous one — one multiplies chart values by 10, the next
by 100 "(10x again)", a later one removes a duplicate conversion because the API
had started doing it. Every one of these was cheap to prevent and expensive to
notice, because a score that is wrong by 10x still renders.
