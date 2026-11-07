# Nine ways an orientation produces a confident wrong model

Each of these yields a model that reads as complete. That is why the
corresponding rules in SKILL.md are rules and not preferences — the model looks
the same whether or not one was violated.

**The failure this exists to prevent.** An agent reads a README describing 28
serverless functions and plans around that. The deployed infrastructure
definition declares four. Every downstream decision — where to add a handler,
what to reuse, what the cost model is, how to test — was made against a system
that does not exist. The check that would have caught it took thirty seconds:
count the declarations in the infrastructure definition and compare.

**Believing the config file.** A configuration file for the previous major
version of a tool sits in the repository, unread by the current toolchain. It
looks authoritative. Changes made to it do nothing, silently.

**Directory names as evidence of coverage.** A `tests/` directory is taken as
proof the code is tested. Opened, it covers one narrow pipeline and nothing else.
A change ships because "tests pass".

**Framework transposition.** Conventions from a similar framework get applied —
a directory structure, a config file, a layout file — none of which the actual
framework reads. The result looks correct and is inert.

**Hand-editing generated output.** A generated router or type file is edited to
register something. It works locally until the next build regenerates it.

**The second implementation.** A helper is written because a grep for its
intended *name* found nothing. The existing one was named differently. Now two
exist, they drift, and bugs get fixed in one.

**Wrong-layer writes.** A mutation is added on the client to a table where client
writes are revoked by policy. It fails only against the real backend, often only
in production, and the fix is a rewrite rather than a patch.

**External reported as done.** A dashboard setting, a secret, or a deployed
function is described as configured. Nobody configured it. The gap surfaces at
launch.

**Stale trust.** A document that was accurate when written, and was verified once
with a date attached, is trusted two years later. Check the date; a verification
without a date is not a verification.
