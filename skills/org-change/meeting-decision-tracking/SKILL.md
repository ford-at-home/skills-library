---
name: meeting-decision-tracking
description: Run one cycle of a recurring team meeting as a single unit — agenda, notes, tracker sync — where the agenda gives every line a stable item ID and the sync binds actions to tracked items only through that ID, never through title similarity. Exists because title-matching an action against an active tracker silently half-updates two near-duplicate items, and because a cycle that produces an agenda but no tracked work leaves the same decision to be made again in two weeks. Use when a recurring status round-table needs its decisions tracked within hours. Trigger phrases include meeting prep, agenda for tomorrow, weekly sync, turn these notes into issues, sync meeting decisions, nothing got tracked, we decided this already.
---

# Meeting Decision Tracking

Close the loop from tracker activity to agenda to attributed notes to tracked
work, in one cycle of a recurring meeting.

Extracting action items with owners, attributing decisions to whoever said them,
and declining to invent an owner the room never named are all things you can
already do, and several published tools do them. The part that is routinely wrong
is the **binding**: matching an action from the notes to the item it belongs to.
Similarity matching against an active tracker opens a duplicate or updates the
wrong item, and both failures are silent — each item then holds half the context
and nothing reports an error.

So the agenda is generated first and every line gets a stable ID. The notes are
written under those IDs. The sync binds on them. That ordering is the mechanism.

The unit of work is a **cycle**, not a document. A cycle that produces an agenda
but no tracked work is the failure this exists to prevent.

## Use when

- A recurring meeting produces decisions and action items that must become
  tracked work
- You are preparing an agenda for a round-table where each owner reports on their
  own domain
- Notes exist and nothing has been created or updated in the tracker yet
- Action items from previous cycles need a status check before the next one

## Don't use when

- There is no roster and no tracker. There is nowhere for output to land, and
  this is note-taking
- One meeting, one action item, one obvious owner. Create the item directly
- The job is telling stakeholders about a decision rather than tracking it
- You want several viewpoints on a proposal before deciding. This records
  decisions; it does not make them

## Inputs

```yaml
phase:           # agenda | notes | sync. Required — it sets the write posture
tracker:         # the project or repository holding the tracked items. Required
config:          # roster and label taxonomy. See reference/configuration.md
cycle:           # activity window, e.g. "since 2026-07-20". Required for agenda
notes:           # path to raw meeting notes. Required for sync
```

**If `config` is missing, stop and ask.** Every wrong answer this can give comes
from guessing an owner, and the roster is what makes that unnecessary.

**If `notes` is missing in the sync phase, stop.** Do not reconstruct a meeting
from the agenda, the item history, or what usually happens.

**Read the label taxonomy from the tracker, never assume it.** If a label the
notes call for does not exist, propose it and stop.

## Process

### Phase A — Agenda (read-only)

1. **Load the config, then read the tracker's real labels and handles.** Report
   every roster domain with no matching `area/*` label and every handle that does
   not resolve. A roster that has drifted produces an agenda that looks complete.
2. **Pull activity in the cycle window**: opened, closed, commented, relabeled,
   reassigned, milestone changed.
3. **Group by owner, then by domain**, since the agenda is read aloud one person
   at a time. Within each owner, split by state: in progress, ready to start,
   blocked, needs decision.
4. **Give blockers and cross-team dependencies their own section, naming both
   sides.** A dependency listed only under the person waiting is invisible to the
   person who owes the work.
5. **Carry forward unresolved items with their age in days.** An item that has
   survived three cycles is no longer a status line.
6. **Assign every agenda line a stable item ID** (`A1`, `A2`, …) and record the
   tracked item number it refers to, or `new`. These IDs are the binding key for
   the whole cycle.
7. **Time-box each owner** and flag anyone whose item count will not fit. Say it
   before the meeting, not during.

### Gate before phase C

Sync runs only if the notes reference agenda item IDs or name owners explicitly.
Notes that do neither cannot be synced without guessing. Say so and stop.

### Phase B — Notes

8. **Record each decision with its speaker**, what was decided, and what it rules
   out. A decision nobody owns cannot be revisited or reversed.
9. **Tag every line `decision`, `action`, `blocker`, or `information`.** Only
   actions become tracked items. Decisions become a comment, or an item of their
   own if they bind future work. Information becomes nothing.
10. **Where the room was ambiguous about ownership, record the ambiguity in the
    words used.** "Someone should look at the deploy script" is the data;
    inventing a someone destroys it.

### Phase C — Sync (writes)

11. **Resolve each action's target before writing anything.** Match by agenda item
    ID first, then by an explicit item number stated in the notes. If neither key
    resolves, the action is unresolved output, not a best guess.
12. **Write through the tracker's configured API or tooling.** If it is
    unavailable, stop, emit the sync report, and say so — a human can apply it by
    hand.
13. **Apply labels only from axes that exist.** Unstated priority means no
    priority label.
14. **Assign only where the notes name a person, or where exactly one roster
    domain covers the work.** Otherwise create it unassigned with an `Ownership:`
    line stating the ambiguity and naming who can resolve it.
15. **Cross-reference both directions.** The item body carries the meeting date,
    the agenda item ID, and the speaker. The notes get the item number written
    next to the line.
16. **Emit the sync report, then reconcile**: every `action` line appears exactly
    once, in exactly one of created, updated, skipped with reason, or unresolved.

## Hard rules

Each of these prevents a failure that produces a plausible-looking result. That is
why they are rules and not advice — nothing downstream signals a violation.

```text
Bind an action to a tracked item by agenda item ID or an explicitly stated item
  number. Never by title similarity, at any confidence.
Two agenda items plausibly matching one action is an unresolved output, not a pick.
Every action line lands in exactly one bucket: created, updated, skipped with a
  reason, or unresolved.
Never invent an assignee. Ambiguous ownership ships unassigned, with the ambiguity
  written down.
Never invent a priority. Unstated means unlabeled.
Never record a decision nobody made. A room that did not converge produces a
  needs-decision item.
Never resolve an owner from commit history. Authorship is not ownership.
Never create a label the tracker does not have. Propose it and stop.
Never close an item on a verbal "that's done". Comment the claim and who made it.
Never edit the raw notes. Annotate a copy.
```

The binding rule carries the skill and is the one that looks safe to soften.
Near-duplicate titles are normal in an active tracker — "fix the deploy script"
exists three times with different scopes — and a similarity match produces a
confident write to the wrong item.

The assignee rule is the one that gets argued with. The roster says who is
*likely* to own a thing; the assignee field reads as fact. Once a guess is in that
field nobody re-examines it and the real owner never sees the item.

## Stop instead of guessing

- **A name matches no roster entry or alias** → stop for that item, listing every
  unmatched name at once alongside the roster names that exist
- **Two agenda items plausibly match one action** → stop and name both
- **An action references no item ID and no item number** → unresolved. Do not
  search the tracker for something that looks similar
- **The notes are a raw transcript with nothing marked** → ask whether the meeting
  produced decisions. Do not mine a transcript for implied ones
- **The notes are older than the current cycle** → flag it. The tracker has moved,
  and a stale sync reopens settled work
- **Asked to "just create the items" without the notes** → refuse. Items invented
  from an agenda carry the authority of a meeting that did not happen

## Further reading in this folder

- `reference/configuration.md` — the roster and label-axis schema, and why
  `area/*` values must correspond one-to-one with roster domains
- `reference/artifacts.md` — the three output shapes: agenda, notes, sync report
- `reference/failure-modes.md` — five ways a cycle produces a confident wrong
  result, and which rule catches each
- `templates/meeting-notes.md` — the notes template to fill in
