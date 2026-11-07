# Six ways this produces a confident wrong answer

Every one of these yields an answer that reads as finished and cited. That is why
the corresponding rules in SKILL.md are rules and not preferences — nothing in
the output signals that one was violated.

**The one it exists to catch — the fluent average.** Retrieval succeeds, six
relevant notes come back, and the answer is a smooth paragraph blending all six
at uniform confidence. Nothing in it is quite wrong and none of it is traceable.
The graph in step 4 is the only thing that prevents this, and it is the step
that gets dropped under time pressure. If your draft answer has no node list,
you skipped it.

**Self-corroboration.** A model-written synthesis note from three months ago is
retrieved as a source and treated as `firsthand`. Its claims came from the same
reasoning you are doing now. Check `source_quality` on every hub note.

**One-pass retrieval.** Keyword search alone misses everything phrased
differently; semantic search alone misses exact identifiers, figures, and names.
Each pass fails in a way the other catches, which is the only reason to run two.

**Recency mistaken for authority.** The most recently edited note wins by
default, even when an older `firsthand` note contradicts it. The override exists
because a fresh guess is still a guess.

**Confidence borrowed from source quality.** A single `firsthand` note gets
`high` confidence because `firsthand` sounds strong. One source is `medium`.

**Answering the whole question.** The corpus covered 70% and the remaining 30%
came from general knowledge, unmarked, in the same voice as the cited part. This
is the failure mode users cannot detect from the outside.
