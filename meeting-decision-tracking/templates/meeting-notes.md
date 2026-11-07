# Notes — <meeting> — <date>

<!--
Fill this during or immediately after the meeting.

One thing makes it syncable: every line sits under an agenda item ID. The sync binds
actions to tracked items through those IDs and is forbidden from matching by title
similarity, so a line with no ID and no explicit item number is returned as unresolved
rather than guessed at.

Tag each line with exactly one of:
  decision     — something was settled. Names the speaker and what it rules out.
  action       — someone will do something. Becomes a tracked item.
  blocker      — work is stopped. Names the other side.
  information  — worth writing down, becomes nothing.

Do not resolve ambiguity while writing. If the room said "someone should", write that.
An invented owner is unrecoverable once it reaches the assignee field.
-->

Present: <names as they appear below>
Agenda: <path or link>

## A1 — <agenda line, copied>

- decision · <speaker> · <what was decided> · rules out: <what is now off the table>
- action · <what> · owner: <name, or UNASSIGNED — ambiguity: "<the words used>">
- blocker · <what is stopped> · other side: <who owes the work>
- information · <what>

## A2 — <agenda line, copied>

-

## Off-agenda

<!--
Raised with no agenda item, so it has no binding key. Same tags. These become new
tracked items and need an owner or an explicit ambiguity like everything else.
-->

-

## Unresolved ownership

<!--
Every action whose owner the room did not settle. Copy the ambiguity in the words used
and name who can resolve it. These become unassigned items carrying this text, not
assigned items carrying a guess.
-->

| Agenda ID | Ambiguity, as stated | Who can resolve it |
|---|---|---|
|  |  |  |

## Discussed without converging

<!--
Not decisions. These are needs-decision items. Record what the disagreement is about
and what would settle it.
-->

-

## Synced items

<!--
Filled in during the sync, so the next agenda can tell tracked work from discussed
work. An empty column here after the sync deadline is the failure this format exists
to prevent.
-->

| Agenda ID | Tracked as | Bound by | Assignee | Labels |
|---|---|---|---|---|
|  |  |  |  |  |
