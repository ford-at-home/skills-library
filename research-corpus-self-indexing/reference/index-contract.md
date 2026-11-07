# The typed fields the index reads

The index consumes these. Per-field validity belongs to
`markdown-memory-schema-maintenance`, not here. What matters for indexing is that
the fields exist and carry values the generator can classify on.

```yaml
type: source | entity | concept | synthesis | decision | claim | goal | value | research | plan
domain: <a value the taxonomy file declares>
status: active | archived | superseded | draft | needs-review
source_quality: firsthand | secondhand | inferred | unverified | ai-generated
sensitivity: public | personal | private | sensitive
related:  ["[[Durable Note]]"]     # outbound edges
sources:  ["<path/to/capture.md>"] # backward edges, on durable notes
tags:     ["#domain/subdomain"]
```

Two rules make this indexable rather than decorative. **The generator classifies
on frontmatter first and path second**, so moving a file cannot silently retype
it. And **the note template exists to satisfy the extractor** — if the generator
pulls summaries from a `## TL;DR` section, that section is mandatory in the
template, and a note without one gets an arbitrary first paragraph. Template and
generator are one contract; changing either alone breaks the index quietly.
