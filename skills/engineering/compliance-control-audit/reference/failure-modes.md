# Six ways this produces a confident wrong answer

Every one of these yields a report that looks finished. That is why the
corresponding rules in SKILL.md are rules and not preferences — nothing
downstream signals that one was violated.

**Clean because nothing was looked at.** The scope filter defaulted to
non-production and nobody read the header. Every control passed against zero
production resources. *Caught by:* resource counts and the active filter in the
header, and zero-resources being not-determined rather than a pass.

**Errors swallowed as passes.** A check wraps its API call and continues on error,
so a permissions gap reads identically to a satisfied condition. *Caught by:* the
third state. This is the failure most likely to already be present in inherited
checking code.

**Trusting the marker.** A resource is skipped because it carries a tag saying it
was already remediated. The remediation was reverted, the tag was applied by hand,
or it landed on the wrong resource. *Caught by:* verifying the condition rather
than the claim about it.

**Exception creep.** A name-prefix exclusion added for a few service accounts
silently covers everything later named with that prefix, including human accounts.
Nobody approved those, and nothing flags them. *Caught by:* exclusions matching
exact identifiers, and patterns being reported with their current matches.

**Coverage laundering.** A failing check is deleted or marked inactive and the pass
rate rises. *Caught by:* counting against the full control set, which surfaces the
gap as declared-but-not-implemented.

**Accurate and useless.** Findings grouped by control ID, no resource identifiers,
no owner hints, no exposure ranking. Nobody can act on it, so nobody does, and the
same report regenerates next quarter with an older `first_seen`. *Caught by:*
ranking by exposure and carrying an owner hint per finding.

This last one is different from the others in kind. It is not a wrong answer — it
is a right answer nobody can use, which fails just as completely and is much
easier to defend in review.
