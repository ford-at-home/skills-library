# Six ways tenant isolation fails while looking correct

None of these breaks the happy path, which is why each survives review.

**The one it exists to catch: documented and unenforced.** In the estate this
skill came from, the `LeadingKeys` condition appears in five documents and in
exactly one deployed stack — and that one scopes by user identity, not tenant.
The repo whose rules describe it best ships a handler running with a table-wide
role and the isolation audit filed as a future task. Documentation reads like
implementation. Grep stacks, not prose.

**A fallback that looks like caution.** `plan ?? 'free'`, `status ?? 'active'`,
`tenantId ?? 'default'`. Each reads as defensive coding and converts a missing
record into a silent grant. They survive review because the failure is a
business-logic error, not an exception.

**Layer 2 skipped because layer 1 passes.** The API correctly returns nothing
for a cross-tenant request, so isolation looks proven. Nothing has been proven
about what a mis-scoped query does, which is the only thing layer 2 is for.

**Tenant name in the prompt for a legitimate reason.** Personalized output is a
real requirement, and it is how tenant identifiers reach prompts. Pass a display
name if the product needs one; never pass anything that scopes an access
decision. What the model can echo, it can be induced to echo wrongly.

**Signature verification after a "harmless" parse.** A log line or an early
field read gets added above the verification call. The check still runs and
still passes, and attacker-controlled bytes were parsed and acted on first.

**Two code paths for one boundary.** Duplicated trees diverge predictably: the
newer one gains features, the older one keeps the IAM condition, and the deployed
entry point is the one without it. When two paths enforce one boundary, one of
them is wrong and you do not know which.
