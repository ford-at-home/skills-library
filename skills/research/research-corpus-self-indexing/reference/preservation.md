# Preservation: the only conditions under which a note may go

The default answer to "should I delete this?" is no. Deletion is the only
operation here that is irreversible at the content level, and "cleanup" is how
people lose years of notes.

**Do not delete a note unless it is verifiably persisted, byte-for-byte,
elsewhere.** All four must hold:

1. **Byte-exact superset.** The destination contains the original text verbatim,
   allowing only an added frontmatter block and a title heading. No paraphrase,
   no summary, no lossy migration.
2. **Different durable location.** A different path in the corpus. Moving a note
   inside the corpus is a rename, not a deletion, and is fine.
3. **Persisted where the loss of this machine cannot take it.** Pushed to a
   remote, or synced and confirmed present at the destination. A copy that exists
   only on this machine does not count.
4. **Audit trail.** The removal is recorded somewhere durable, naming where the
   content went — the removing commit message where the corpus is under version
   control, and otherwise a dated line in a log the corpus keeps.

Verify mechanically: read both files, strip the destination's frontmatter,
confirm the source body is a substring of the destination body with nothing lost.
If that check is not clean, the migration is lossy and the source stays.

Narrow exceptions are not research deletions: **secrets, personal data that was
never meant to be here, and third-party copyrighted material** are removed as a
security action. **Generated artifacts are not notes** and may be rewritten at
any time.

An orphan is not a deletion candidate. It is an unfiled note, and the repair is
a link.
