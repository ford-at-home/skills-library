/**
 * The only place tenant-scoped key strings are constructed.
 *
 * Every partition key begins with `TENANT#<tenantId>` so the
 * `dynamodb:LeadingKeys` IAM condition can enforce the boundary that the
 * application layer is merely expected to respect. That enforcement compares
 * against the literal key, which is why hand-building a key elsewhere — even
 * correctly — is forbidden: the next variant will differ, and the resulting
 * AccessDeniedException surfaces nowhere near its cause.
 *
 * This is the DynamoDB form of the rule, not the rule itself. Against another
 * store — a tenant column under a row-level security policy, say — the
 * equivalent is one module producing that value and no other place producing it.
 * The single construction site is the rule; the key syntax is this store's
 * expression of it.
 *
 * Adapted from a deployed implementation. Extend the entity list; do not add a
 * second construction site.
 */

export type TenantKey = { PK: string; SK: string };

const tenant = (tenantId: string) => `TENANT#${tenantId}`;

export const Keys = {
  /** Tenant record: plan, status, billing provider ids. */
  tenantMeta: (tenantId: string): TenantKey => ({
    PK: tenant(tenantId),
    SK: 'META',
  }),

  /** Membership. `subjectId` is the identity-provider subject, not an email. */
  tenantUser: (tenantId: string, subjectId: string): TenantKey => ({
    PK: tenant(tenantId),
    SK: `USER#${subjectId}`,
  }),

  /** One unit of billable work. */
  run: (tenantId: string, runId: string): TenantKey => ({
    PK: tenant(tenantId),
    SK: `RUN#${runId}`,
  }),

  /**
   * Quota counter for one billing period. The atomic reservation targets this
   * item; see the entitlement rules. `period` is `yyyy-mm` so counters are
   * naturally partitioned by month and old ones can simply be left in place.
   */
  usageCounter: (tenantId: string, period: string): TenantKey => ({
    PK: tenant(tenantId),
    SK: `USAGE#${period}`,
  }),

  /**
   * Webhook idempotency marker. Written with
   * `ConditionExpression: 'attribute_not_exists(SK)'` before any state change;
   * a condition failure means the event was already processed.
   */
  providerEvent: (tenantId: string, eventId: string): TenantKey => ({
    PK: tenant(tenantId),
    SK: `PROVIDER_EVENT#${eventId}`,
  }),

  /**
   * Append-only audit trail. ISO-8601 timestamps so the sort key orders
   * chronologically. Written on every plan or status mutation, by the webhook
   * handler and by any manual override tool.
   */
  audit: (tenantId: string, isoTimestamp: string): TenantKey => ({
    PK: tenant(tenantId),
    SK: `AUDIT#${isoTimestamp}`,
  }),
} as const;

/** UTC, because a billing period must not depend on where the code runs. */
export function currentBillingPeriod(now: Date = new Date()): string {
  const year = now.getUTCFullYear();
  const month = String(now.getUTCMonth() + 1).padStart(2, '0');
  return `${year}-${month}`;
}

/**
 * S3 counterpart. The prefix mirrors the DynamoDB key so one session tag scopes
 * both stores.
 */
export function tenantObjectKey(tenantId: string, ...segments: string[]): string {
  return ['tenants', tenantId, ...segments].join('/');
}
