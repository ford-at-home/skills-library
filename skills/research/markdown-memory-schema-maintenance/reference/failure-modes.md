# Six ways a metadata audit makes the corpus worse

Each of these leaves a corpus that validates clean. That is why the
corresponding rules in SKILL.md are rules and not preferences — the repaired
corpus is indistinguishable from a correct one.

**The one it exists to catch — the stale claim cache.** A note's `claims:` array
was written eight months ago and the body has moved on. Retrieval reads the array
first, for good reason: it's cheap. So the corpus now confidently serves an
assertion its own note no longer makes, and the paths cited all check out. Nobody
finds this by reading answers.

**Backfill inflation.** Two hundred notes lack `source_quality`, so they all get
set to `firsthand` in one pass. Validation goes green. The calibration signal is
now permanently gone, and it looks like it was always there.

**Enum drift laundering.** An illegal `type: note` value gets mapped to `source`
across forty files. The distinction the author was reaching for is deleted, and
the schema never learns it was needed.

**Orphan cleanup as deletion.** Orphan notes look like garbage. They are usually
the notes nobody has linked *yet*, which is a link defect, not a content defect.

**Auto-linking at scale.** Five hundred unlinked mentions get linked in one
commit. Some are homonyms, and the traversal graph now contains false edges that
later look like real evidence.

**Mistaking well-formed for correct.** Every field validates and the note is
still factually wrong. This skill cannot see that, and should not claim to.
