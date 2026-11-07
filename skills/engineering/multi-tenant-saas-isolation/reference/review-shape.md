# The isolation review

```markdown
# Isolation Review — <app>

## Verdict
production-ready | not production-ready
### Not production-ready because
<one bullet per broken hard rule or unrun audit test. Nothing else in this section>

## Identity
- Claim: <exact name> · Writers: <every code path that sets it>
- Authoritative: yes | no (if no, stop here)

## Tenant scoping
| Entity | Field carrying the tenant id | Built by |
- Scoping values built outside the helper: <file:line, or none>

## Layer 2 — enforcement inside the storage layer
- Store-level condition present: yes/no · Mechanism: IAM `LeadingKeys` | row-level security | none
- If IAM · Role model: session tags | per-tenant | none
- Paths still running with store-wide access: <list>

## Layer 3 — the model boundary
- Channel carrying tenant context to the model: <channel>
- In-prompt tenant references: <file:line, or none>
- Tool-call validation: server-side | absent

## Billing path
| Step | Present | Evidence |
signature-first · replay window · idempotency · provider-side tenant lookup · audit row

## Entitlements
- Preview and reservation distinct: yes/no
- Reservation is one conditional write: yes/no
- On throw: deny | allow (defect) · Compensating release: yes/no

## Audit
| # | Test | Run? | Result |

## Unverified
<anything asserted from prose rather than from code>
```
