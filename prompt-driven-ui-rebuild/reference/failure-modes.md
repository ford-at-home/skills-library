# How this goes wrong

**The one it exists to catch.** The design system gets defined, then bypassed. In
the pair of front ends this was extracted from, `tailwind.config.ts` defined a
full set of semantic tokens — `primary`, `accent`, `muted`, `card` — and the main
page used `text-muted-foreground` alongside hardcoded `from-blue-50 via-purple-50
to-pink-50` and `from-purple-500 to-pink-500` in the same file, with `primary`
and `accent` unused. Raw palette classes appeared across roughly two dozen source
files. Gate 1 held; Gate 2 was never enforced. Both branches of that codebase
carry the identical drift, which is what happens when nothing checks it: the
tokens become decoration and the real design system is whatever the last prompt
felt like.

**Additive duplication.** Nobody deletes. The same codebase ended up with three
overlapping error-monitoring surfaces — one of them a React component filed under
`lib/` — and three error-handling implementations side by side. Each was a
reasonable answer to the prompt that produced it. The rejection list is the only
thing that catches the fourth.

**Debug scaffolding that ships.** That codebase carried a deliberate
`throw new Error(...)` fired by a URL query parameter, with the comment "remove in
production", in a page component that shipped. "Remove later" is not a mechanism.

**Docs that describe a structure that isn't there.** Its README documented two
source directories that did not exist. Generated documentation describes what was
asked for, not what was built.

**Rejection list written after the fact.** Written once output exists, it will be
written to accept that output. If a step's list is empty before the prompt goes
out, the step is not ready.

**Compounding on unverified output.** Step 3 looks fine, so nobody checks it.
Step 7 fails and the cause is in step 3. By then five steps sit on top of it and
reverting costs more than the whole sequence did.

**The plausible improvement.** The builder returns something genuinely nicer than
you asked for, using values that aren't in the design system. Accepting it makes
the design system advisory. Reject it, then add the value to the design system in
its own step, or defer it.

## Evidence, and its limit

The failure modes above were read out of a shipped generated front end and its
fork, not imagined. But those two are **not** a controlled comparison of gated
versus ungated building — they descend from the same generated base and share most
of their UI code byte for byte. They show what unreviewed additive prompting
accumulates, and that a factored design system survives forking while an
unenforced reference rule does not. They do not measure how much the gates
prevent. Don't claim they do.
