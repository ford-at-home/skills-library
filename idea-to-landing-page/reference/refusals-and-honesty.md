# What this does not produce, and what the page may claim

## What this does not produce

This is the gate. It is written before the process because a scope boundary
written afterward is written to permit whatever already happened.

A demand test does not include, and this skill refuses to add:

| Refused | Why |
|---|---|
| A complete MVP or working product | That is the thing the test exists to avoid committing to |
| User authentication | Accounts imply a product behind the login. There isn't one |
| Payment processing | Requires business setup and compliance, and charging for the undeliverable is a different category of problem |
| Complex backend logic | Needs time and testing that a demand test does not have |
| A production database with real relationships | A capture destination is not a data model |
| A dashboard, settings page, or logged-in area | Routes with nothing behind them |

All six are refused for one reason: they cost real time and return no additional
signal. A visitor who would submit an email will not submit a *better* email
because the page has a login screen.

The pressure to add them arrives late, framed as almost done — "it just needs
auth", "add a Stripe button so we can see if they'd pay". A payment button that
cannot deliver is not a stronger signal; it is a promise with a receipt attached.
If the question is genuinely whether they would pay, state planned pricing and
measure who submits anyway.

Deployment and hosting are out of scope too. Any host giving you a real HTTPS URL
is sufficient and the choice does not affect the signal. Standing up real
infrastructure is different work; use your deployment tooling.

## Honesty constraints

The page may only claim what `exists_today` supports. Check each claim against
it, in writing, before the page goes up.

- **Tense is the tell.** "Track every invoice in one place" describes a product.
  "We're building a way to track every invoice in one place" describes an
  intention. If nothing is built, only the second is available to you.
- **No invented social proof.** No subscriber or user counts you cannot name, no
  customer logos of people who are not customers, no written testimonials, no
  star ratings. A trust section with nothing true to put in it gets deleted, not
  filled. Generic page templates ship with placeholder proof — "Join 1,000+
  subscribers" — and it survives into production because it reads as copy rather
  than as a claim.
- **No manufactured scarcity.** No countdowns, no limited spots, no closing-soon,
  unless the limit is real and you will honor it.
- **Pricing may be stated as planned pricing, labeled as such.** A working
  checkout for an undeliverable product is out of scope, not a stretch goal.
- **Collect the minimum.** An email address and at most one qualifying field the
  follow-up genuinely needs. Every extra field costs submissions and creates
  something you now have to hold. Never collect payment details, government
  identifiers, health information, or credentials.
- **State what happens to the address, then do it.** If the page says you will
  write when it launches, that is a commitment. If you will never write, say the
  list is for launch notification only and keep it to that.
- **Never quote a conversion or performance benchmark you did not measure.**
  Round improvement figures circulate through landing-page advice with no source
  attached. Repeating one puts a fabricated number in your own reasoning.

A coming-soon page is honest. A page a visitor would reasonably read as
"this exists, I can use it today" is not, and no amount of small print in the
footer repairs it.
