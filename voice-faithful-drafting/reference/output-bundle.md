# The output bundle and the report

One directory per channel:

```text
output/<piece>/<channel>/
├── post.md            # the piece. Filename per the channel definition
├── to-research.md     # gaps, each with a hint about where to look
├── tighten.md         # questions whose answers make the next pass shorter
├── unresolved.md      # any instruction that could not be carried out
└── synthesis-map.md   # weave mode only: paragraph → source
```

The three auxiliary files are written **even when empty**. An empty
`to-research.md` records that the dimension was considered and nothing was found.
A missing one records nothing.

Then report:

```markdown
## <Piece> — <mode> · voice: <name> · channel: <name>

<the piece, complete>

---

## What changed (top-down)
- <3–5 structural bullets: what moved, what was cut, what framing was added.
  Not sentence diffs>

## Voice notes
- <which accent layers, where, and why>

## Picks I made
- <every parameter chosen because the voice file was silent>

## Unresolved
- <or "none">
```
