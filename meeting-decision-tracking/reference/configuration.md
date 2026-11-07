# Configuration

Fill this in once per meeting. It is the reason the skill never has to guess an
owner.

```yaml
meeting:
  name:
  cadence:              # e.g. weekly, Tuesday
  sync_deadline:        # how long after the meeting the sync must finish.
                        # Hours, not days — decisions not tracked the same day
                        # get re-decided
  minutes_per_person:
tracker:
  project:              # where tracked items live
  notes_location:       # where notes live, so items can link back to them
  access:               # which API or tooling has write access
roster:
  - person:             # the name as it appears in the notes
    handle:             # tracker username
    domains: []         # the area label values this person owns
    aliases: []         # first name, initials, any other form the notes use.
                        # Required — the alternative is fuzzy-matching a person
```

## The four questions every item answers

Which domain owns it (exactly one, and it must correspond to a roster domain —
see below). How urgent it is, never inferred. Where it stands. What kind of work
it is.

Encode them however your tracker already does. The table below is one encoding,
using label namespaces, which is what a tracker without typed fields forces. If
yours has first-class priority, status, and type fields, use those and keep only
the domain correspondence.

| Axis | Answers | Cardinality |
|---|---|---|
| `area/*` | which domain owns it | exactly one |
| `priority/*` | how urgent | zero or one, never inferred |
| `status/*` | where it stands | exactly one |
| `type/*` | what kind of work | zero or one |

Read the real taxonomy from the tracker before the first write. Nothing here
authorizes creating a label to make the table fit.

## The one correspondence that has to hold

`area/*` values must map one-to-one with roster `domains`.

That correspondence is the only reason an agenda can be grouped by owner without a
human sorting it. When it drifts — someone's domains change and the config does
not — every sync since routes their work to the previous owner, correctly
according to the file and wrongly according to the team. Nothing errors, because
the label exists and the assignee exists; they just no longer describe reality.

Phase A reports these mismatches before the agenda is built, which is the only
point in the cycle where the drift is cheap to fix.

## Aliases are not optional

The roster carries every form a person's name takes in the notes: first name,
initials, nickname. The alternative to an explicit alias list is fuzzy-matching a
human being against a roster, which fails in exactly the cases where two people
have similar names — the cases where being wrong matters most.
