---
name: multi-tenant-saas-isolation
description: Enforce tenant boundaries in a multi-tenant application so that no single bug leaks another tenant's data. Covers where tenant identity may come from, the scoping shape that makes isolation enforceable in the storage layer, why tenant context must never travel through an LLM prompt, signature-then-parse ordering for billing webhooks, fail-closed entitlement checks, and the four tests that are the only evidence the layers compose. Use when writing or reviewing a handler that reads tenant-scoped data, wiring IAM for a tenant-facing role, invoking a model on customer data, handling a Stripe or billing webhook, gating a feature by plan, or auditing a multi-tenant app before production traffic. Trigger phrases include multi-tenant, tenant isolation, tenant spoofing, LeadingKeys, cross-tenant leak, entitlement check, quota, webhook signature, prompt injection, is this safe for real customers.
---

# Multi-Tenant SaaS Isolation

Tenant boundaries fail one bug at a time. The defense is that each layer
enforces the boundary independently, so no single mistake in the application
layer becomes a data leak. Three layers, numbered as the rest of this folder
refers to them: **layer 1** is the application — one authoritative tenant
identity and every access scoped by it; **layer 2** is the storage layer, which
refuses a request the application scoped wrongly; **layer 3** is the model
boundary, where tenant context travels only in channels the model cannot read.
This skill is the rule set plus the audit that proves the rules hold.

The rules are cheap to follow and expensive to learn. Tenant identity in a
request body is a vulnerability, not a convenience. An entitlement check that
returns "allowed" on error will bill a customer for a plan they cancelled.
Neither is discoverable from the code working on the happy path.

## Use when

- Writing or reviewing any handler that reads or writes tenant-scoped data
- Wiring the IAM role or row-level security policy a tenant-facing path runs under
- Invoking a model, agent, or tool chain on customer data
- Handling a billing webhook, or gating any feature or quota by plan
- Auditing a multi-tenant application before it takes production traffic
- Changing a key shape, a token claim, or an entitlement interface

## Don't use when

- The application has one tenant and no plan to add another. Say so and stop.
- The question is which AWS resources to create and in what order. That is
  provisioning work, not this skill.
- The boundary is per-user within one customer rather than per-customer. The
  mechanisms transfer; the threat model does not. A user seeing a colleague's
  record is a permissions bug, not a breach.

## Inputs

Ask for these. Do not infer them.

```yaml
tenant_id_source:      # exact path, e.g. the verified JWT claim name.
                       # If the answer includes "request body", stop
data_store:            # DynamoDB single-table | Postgres | other, and whether
                       # tenant scoping is already in place
key_helper:            # the one module that builds the scoping value, or "none"
llm_path:              # how tenant data reaches the model, and what the model
                       # is allowed to call afterwards
billing_provider:      # stripe | marketplace | manual | none
entitlement_behavior:  # what happens today when the entitlement check throws
audit_status:          # which of the four isolation tests have been run
```

**If `tenant_id_source` is not a verified token claim, stop and fix that first.**
Every rule below assumes an authoritative tenant identity. Without one they are
decoration.

## Process

1. **Establish one authoritative tenant identity.** A signature-verified token
   claim, written by exactly one code path, re-injected from the source of truth
   on every login so a stale attribute cannot outlive a migration. Never a body,
   path parameter, query string, or caller-controlled header. If more than one
   code path sets the claim, name every writer and reduce to one.

2. **Put the tenant identifier in the field the storage layer can enforce on**,
   built in one module and nowhere else. On DynamoDB that is the partition key
   `TENANT#<tenantId>`, with the sort key naming the entity; on Postgres it is a
   tenant column the row-level security policy compares against. See `keys.ts`.

3. **Add the store-level enforcement that makes step 2 hold**, in that order —
   enforcement compares against the literal value the store sees, so a second
   construction site is what breaks it, loudly and far from its cause. On AWS
   that enforcement is the IAM condition. See `reference/iam-conditions.md`.

4. **Route tenant context around the model, never through it.** Table below.

5. **Verify webhook signatures before reading the body**, then apply a replay
   window, then an idempotency row, then the state change. See
   `reference/billing-path.md`.

6. **Make entitlement checks fail closed and the quota gate atomic.** A
   read-then-write quota check double-allocates the last unit under concurrency.

7. **Bound the blast radius of each mutation path.** A webhook mutates only the
   tenant it can identify from provider state, never one named in the payload.

8. **Run the audit.** Four tests. They are the only evidence the layers compose.
   Without them you do not know isolation works; you hope it does.

## Layer 3: keeping tenant context out of the model

An LLM can be prompt-injected. The storage layer cannot. So identity and
credentials ride in deterministic channels only.

| Tenant context may ride here | It must never ride here |
|---|---|
| Lambda or container environment | The system prompt |
| IAM session tags | The user prompt |
| Step Functions or workflow execution input | Tool descriptions exposed to the model |
| Agent session attributes | Knowledge-base or retrieval query strings |
| Key construction inside the handler | Anywhere the model can read it back |

Treat model output as untrusted text. Every tool call the model requests is
validated server-side against that tenant's plan and explicit grants before
execution. The model does not get to self-elevate by asking.

## Hard rules

Each of these prevents a failure that leaves the happy path working. That is why
they are rules rather than advice — a leaked boundary and an enforced one return
the same response until someone goes looking.

```text
Tenant identity comes from a verified token claim. Never from a body, path,
  query string, or caller-controlled header.
Exactly one code path writes the tenant claim.
The tenant identifier lives in the field the storage layer enforces on, written by
  the shared helper — a TENANT#<tenantId> partition key on DynamoDB, a tenant
  column under row-level security on Postgres.
Never hand-build that value.
Tenant context never enters a prompt, a tool description, or a retrieval query.
Model output is untrusted. Validate every requested tool call server-side.
Verify the webhook signature before parsing the body.
A webhook mutates only the tenant it can identify from provider state.
Entitlement checks fail closed. A throw denies.
The quota gate is one conditional write.
Stores holding tenant data carry a retain-on-delete policy. A typo must not
  delete a customer.
No default plan, no placeholder tenant, no fallback identity. A missing tenant
  record is a condition to handle, not a value to invent.
Key shapes, claim shapes, and the entitlement interface change by written
  decision record with a migration plan. They are integration seams.
```

The last-but-one rule gets argued with, and one of the implementations this skill
came from breaks it — a `?? 'free'` on a missing plan field, in a codebase whose
own rules forbid exactly that. Absence of a plan record is `tenant_not_found`.

## The audit — the gate to production

Four tests. Nothing else is evidence.

| # | Test | Pass condition |
|---|---|---|
| 1 | Tenant A's token requests Tenant B's record through the public API | 200 with empty result, or 403. Never B's data |
| 2 | A handler issues a deliberately mis-scoped query for another tenant | The storage layer itself denies it — an authorization error from the enforcement layer, not a successful read. On AWS, `AccessDeniedException` from IAM |
| 3 | Webhook called with an invalid signature | Rejected, and no write occurred |
| 4 | The same webhook event delivered twice | Second delivery is a no-op |

Test 2 is the one that gets skipped, because passing test 1 feels like it covers
it. It does not: test 1 exercises the application layer, test 2 exercises what
happens when the application layer is wrong. That is the whole point of layer 2.

## Output

An isolation review, in the shape given in `reference/review-shape.md`.

## Stop instead of guessing

- **Tenant id is read from a request body anywhere** → stop. Report every call
  site. This is the finding; do not continue the review around it.
- **`tenant_id_source` cannot be named exactly** → stop and ask. "From the JWT"
  is not an answer; the claim name is.
- **Asked to certify isolation without running the four tests** → refuse. Name
  the tests not run and what each would have covered. A verdict without test 2
  is a statement about the application layer only.
- **Asked to add a default plan, placeholder tenant, or fallback identity so a
  flow stops erroring** → refuse and name the input flow that should exist
  instead. A filled gap is indistinguishable from real data downstream.
- **Asked to relax fail-closed "temporarily" for a demo** → refuse. Every
  documented instance of this was never restored, and the comment explaining the
  temporary state is what stops anyone looking again.
- **A key shape, claim shape, or entitlement signature needs to change** → stop
  and require a written decision record plus a migration plan. Write both shapes
  for one release; never cut over in place.

## Further reading in this folder

- `keys.ts` — the key-helper module the rules assume. Copy it, adapt the entity
  list, and route every key through it. In another language or against another
  store, write the equivalent as one module with no key strings anywhere else —
  that constraint, not the syntax, is the rule
- `reference/iam-conditions.md` — layer 2 in AWS form: the DynamoDB and S3
  policies, session tags versus a role per tenant, and why the helper lands first
- `reference/billing-path.md` — the five-step webhook order and the difference
  between an entitlement preview and an atomic reservation
- `reference/review-shape.md` — the isolation review template
- `reference/failure-modes.md` — six ways tenant isolation fails while looking
  correct, and which rule above catches each
