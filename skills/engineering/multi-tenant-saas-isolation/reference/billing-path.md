# Webhook ordering and entitlements

## Webhook handling order

Each step assumes the previous one passed.

1. **Verify the signature against the raw bytes.** First statement in the
   handler. Nothing may transform the body first.
2. **Reject stale events**, 300-second tolerance. A replay from yesterday must
   not re-grant access to a since-cancelled subscription.
3. **Claim idempotency.** Write `SK = PROVIDER_EVENT#<id>` with
   `ConditionExpression: attribute_not_exists(SK)` and a TTL. Condition failure
   means already processed: return 200, do nothing else. Providers retry for days.
4. **Identify the tenant from provider state**, not from the payload.
5. **Write an audit row** on every plan or status mutation, sort key
   `AUDIT#<iso-timestamp>` so it sorts chronologically and only ever appends.

The signature scheme is the auth boundary, so an API gateway in front of the
handler adds no protection against a forged event — a direct function URL is
sufficient, and cheaper. Whichever fronting you choose, cap its concurrency: a
leaked URL is otherwise a cost-denial-of-service.

## Entitlements

Two operations, deliberately different. Conflating them is the bug:

- **A read-only preview** for UI ("you have N runs left"). Reserves nothing;
  another caller can consume the remainder before the next call.
- **An atomic reservation** that increments usage and checks the cap in a single
  conditional write. Two concurrent callers at `max - 1` must produce exactly
  one success. Only this one may gate a run.

```ts
// The gate. One write, or it is not a gate.
ConditionExpression: 'attribute_not_exists(PK) OR #count < :max'
// ConditionalCheckFailedException means denied, not failed.
```

Denied means no quota was consumed and the work does not start. A *throw* also
means the work does not start. Denying a legitimate run is recoverable; billing
for something not bought, or running work for a cancelled subscription, is not.

Add a compensating release for the case where the reservation succeeds and the
work then fails to start. Without it, crashed starts leak quota permanently.

Keep the entitlement interface as the boundary between billing and product. The
work engine must not know which provider paid. New billing channels are new
implementations of that interface, never branches inside the existing one.
