# Mark vocabulary

Six symbols. The right-hand column is what the dictation must supply.

| Mark | Means | Needs content |
|---|---|---|
| `✓` | keep verbatim | no |
| `✗` | cut | no |
| `~` | rework | yes — how |
| `★` | expand | yes — with what |
| `→` | move | yes — where to |
| `?` | weak, challenge, suspect | optional — why |

**Numbered handles.** `① ② ③ …`, continuous across the document, not per page.
Use them when a block anchor is too coarse — one phrase inside a long paragraph —
or when printing without anchors.

**Highlighter, one colour, one meaning: use this as-is.** When editing your own
draft, that means preserve it verbatim. When pulling from sources, it means this
passage goes in the new piece. Do not invent a second colour.

**Directives** are short uppercase tokens in the margin. Voice supplies the
parameter.

| Directive | Does | Needs a voice file |
|---|---|---|
| `SLOP` | scrub the tells listed in the voice's anti-slop file | yes |
| `DEEPEN` | expand using a named accent layer | yes |
| `TIGHTEN` / `TIGHT` | compress, keep the claim | no |
| `HOOK` | rework as the opener | yes |
| `LAND` | rework as the closer | yes |
| `PIVOT` | bridge between sections | no |
| `STAKES` | make the stakes explicit | no |
| `CLAIM` | restate as one sharp declarative line | no |
| `SCENE` | turn an abstraction into a specific moment | yes |
| `EXAMPLE` / `EX` | insert a concrete example | content must come from dictation |
| `EVIDENCE` / `EV` | add a citation | content must come from dictation |
| `CALLBACK` / `CB` | tie back to something earlier in the document | no |
| `ASIDE` | parenthetical in the writer's register | yes |
| `VISUALIZE` / `VIZ` | insert a placeholder: `[Diagram: …]`, `[Sketch: …]` | no |
| `KSP` | restructure to Pulse, Catalyst, Context, Handoff | no |

Paper carries the directive; dictation carries the parameter. `DEEPEN` on the
page, "the deepen on page two — the terse one" in the dictation. A
prose-generating directive with no voice file and no dictated parameter goes to
`unresolved.md`. Do not pick an accent the user never named.

`EXAMPLE` and `EVIDENCE` never invent their content. No dictated example means an
`[Example needed: …]` marker and an unresolved entry.
