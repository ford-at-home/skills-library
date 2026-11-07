# What the document looks like, and what you report back

## The document

```markdown
# <Short title>

<One sentence: what this document is for.>

## <The core mental model>

...prose, linking terms to the glossary on first use...

## What this document deliberately omits

- <Adjacent topic> — <why not here> → <where it belongs, or open question ref>
```

The omissions section is the load-bearing part of the shape. It is what stops the
next reader mistaking a scoped document for an incomplete one, and stops the next
author padding it out to look finished.

## The report to the requester

```text
Classified as:      <shape> → <destination>
Action:             created <path> | extended <path>
Glossary delta:     <terms added or amended, or "none needed, because …">
Gaps left open:     <what the fragment did not say, and where it is now logged>
Contradictions:     <document that disagrees, or "none">
Entropy fixed:      <what else you corrected in the same pass>
Split into:         <if the fragment went to more than one place>
```

`Glossary delta` has no empty state. Either terms changed, or you state the
reason none needed to — a blank line there is the same as not having checked.

`Gaps left open` is the field that makes invented detail visible. If the fragment
did not specify a runtime and the document does not either, this field says so,
and the next reader knows the gap is deliberate rather than resolved.
