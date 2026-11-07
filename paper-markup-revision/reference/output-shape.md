# Output shape

```text
<draft>.v2.md        # the new version. Auto-increment: .v3.md, .v4.md
unresolved.md        # written every run, even when empty
```

```markdown
## v2 — <draft> · <n> instructions applied, <m> unresolved

<the full updated document>

---

## What I changed
- <mark or anchor> → <resolution method> → <what was done>. One line per
  instruction. Name the runner-up candidate where there was one.

## Unresolved
- <instruction, verbatim> — <why: no match / two equal candidates / directive
  needs a voice file / contradicts another instruction>. Closest candidates:
  <named>.

## Picks I made
- <any parameter chosen because the dictation was silent>
```

The change log names the resolution method per instruction because that is what
lets the writer override a bad match on the next pass. "Applied" without a method
is not reviewable: a content match that landed in the wrong paragraph and a block
anchor that landed in the right one look identical in the output.
