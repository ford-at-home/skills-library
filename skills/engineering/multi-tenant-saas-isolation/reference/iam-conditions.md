# Layer 2: enforcement inside the storage layer

The application layer cannot be fully trusted because bugs happen. Layer 2 is
whatever makes the store itself refuse a mis-scoped request, so that "the handler
forgot to scope its query" is stopped below the application rather than returning
another tenant's data. On AWS that is the IAM conditions below, and the refusal
arrives as `AccessDeniedException`. On Postgres it is a row-level security policy
the query cannot escape, comparing the tenant column against the tenant set for
the session. The AWS form is worked through here because it is the one the
implementations behind this skill used.

DynamoDB, scoped by session tag:

```jsonc
{
  "Effect": "Allow",
  "Action": ["dynamodb:GetItem", "dynamodb:Query", "dynamodb:PutItem", "dynamodb:UpdateItem"],
  "Resource": "arn:aws:dynamodb:*:*:table/<table>",
  "Condition": {
    "ForAllValues:StringEquals": {
      "dynamodb:LeadingKeys": ["TENANT#${aws:PrincipalTag/TenantId}"]
    }
  }
}
```

S3, scoped by prefix:

```jsonc
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::<bucket>/tenants/${aws:PrincipalTag/TenantId}/*"
}
```

The handler reads the tenant id from the verified claim, calls `sts:AssumeRole`
on a tenant-scoped role passing `Tags: [{Key: "TenantId", Value: tenantId}]`, and
uses the returned credentials for every subsequent call.

**Session tags, not a role per tenant.** A role per tenant means role creation on
signup, an IAM quota ceiling per account, and a cleanup path on deletion. Session
tags scale without limit against one role.

The condition and the key shape are coupled: `LeadingKeys` compares against the
literal partition key, so a handler that hand-builds `"TENANT#" + id` with
different casing gets denied, and the failure surfaces far from its cause. That
is why the central key helper has to be in place before the condition is added.

The coupling is not AWS-specific. Any enforcement that compares a stored value
requires exactly one place to produce that value, whichever store holds it.
