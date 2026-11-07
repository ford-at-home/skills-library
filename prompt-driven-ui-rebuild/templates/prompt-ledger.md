# Prompt Ledger — <target>

**Builder:** <what executes the prompts>
**Observation:** <how each step's result is seen: dev server, preview URL, screenshot, typecheck, test run>
**Design system:** <path to the single artifact holding tokens and primitive names>
**Out of scope:** <what this sequence will not touch>

## Blocked (read first)

- <step, what it is waiting on, what would unblock it>

## Rejection list

Applies to every step below. Grows only. No per-step exemptions.

```yaml
- pattern:  raw palette value instead of a design-system token
  check:    grep the diff for hex literals and framework palette classes
            outside the design-system file
  action:   reject; re-prompt naming the token that should have been used

- pattern:  new component duplicating an existing primitive
  check:    every added component file — does a primitive already cover it?
  action:   reject; re-prompt to compose the existing primitive

- pattern:  second implementation of a concern that already has one
            (error handling, fetching, state, validation, logging)
  check:    search for existing modules owning that concern before accepting
  action:   reject; extend the existing one or delete the old one in the same step

- pattern:  debug or test scaffolding on a shipped path
  check:    grep the diff for deliberate throws, query-param triggers,
            console logging, comments saying remove before production
  action:   reject unconditionally

- pattern:  files touched outside the step's declared surface
  check:    diff file list against the step's declared surface
  action:   reject the out-of-scope files

- pattern:  backend, auth, payments, or persistence introduced by a UI step
  check:    added dependencies, network calls, credentials, schema files
  action:   reject; out of scope for this sequence

- pattern:  placeholder content, invented sample data, or a stub handler
            standing in for real behavior
  check:    grep for lorem, TODO, mock, placeholder, hardcoded arrays feeding the UI
  action:   reject; wire the real source or make the empty state explicit

- pattern:  documentation describing structure that does not exist
  check:    every directory or file named in added docs — does it exist?
  action:   reject the doc, not the code

# additions discovered during the sequence, each noting the step it came from
```

## Steps

### 1. Design system — status: not started

- Depends on: nothing
- Surface: <the single design-system file>
- Prompt sent: <verbatim, or path>
- Acceptance criteria:
  - [ ] Every visual value the later steps need resolves to a name here
  - [ ] Primitive names are listed, not implemented
  - [ ] <project-specific observation>
- Rejection list additions from this step:
- Observed:
- Rejections:

### 2. <name> — status: not started

- Depends on: 1
- Surface: <files this step may touch>
- Prompt sent:
- Acceptance criteria:
  - [ ] <observation, not an adjective>
- Rejection list additions from this step:
- Observed:
- Rejections:

<!-- Repeat. Suggested dependency order: shell and layout, shared primitives,
     screens, states (loading, empty, error), behavior. -->

## Deferred

| Wanted | Why refused here | Where it belongs |
|---|---|---|
|  |  |  |

## Declared limits

What this sequence will not produce. Stated before it starts, so it is a boundary
and not a defect.

- <e.g. no authentication>
- <e.g. no payment processing>
- <e.g. no production data model>
