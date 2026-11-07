# Five ways a cycle produces a confident wrong result

Each of these leaves a cycle that looks complete.

**Silent misbinding — the one this exists to catch.** An action is matched to a
tracked item by title, the write succeeds, and it lands on the wrong item or opens
a duplicate. There is no error and no signal. Both items then hold half the
context, the next agenda double-counts, and the owner of the real item never sees
the update. Binding on agenda item IDs is the only defense, which is why the IDs
are assigned in phase A before anyone knows which lines will produce actions.

**The unclosed cycle.** The room agrees, everyone leaves, nothing is created, and
two weeks later the same item is raised as if new. The tell is an agenda line with
no tracked number and no `new` marker. This is why the cycle, not the document, is
the unit of work — an agenda that produced no tracked work has not succeeded at
anything.

**Attribution laundering.** "We decided to defer the migration" replaces the person
who decided it. Six weeks on there is nobody to ask, so it is re-litigated from
scratch. The speaker field is cheap to fill at the time and impossible to
reconstruct later.

**Confident assignment.** The room said "someone should", the domain mapping said
who probably should, and the item got assigned. A guess wearing an assignee field
is never re-examined — the field format is identical whether it holds a decision
or an inference, and only one of those is true.

**Stale roster.** Someone's domains changed a month ago and the config did not.
Every sync since routed their work to the previous owner, correctly according to
the file. This is what the phase-A mismatch report is for, and why it runs before
the agenda rather than as a warning attached to it.
