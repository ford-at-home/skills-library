# Eight ways a corpus becomes unfindable while looking fine

Each of these leaves every individual artifact internally consistent. That is why
the corresponding rules in SKILL.md are rules and not preferences — no defect is
visible from inside any one enumeration.

**The one it exists to catch: the half-applied restructure.** Someone pilots a
new layout on a single capture and leaves the original in place. The promotion
pipeline parses identity out of the filename, so it enriches the copy matching
the old convention and not the new one — or the reverse. Now one capture exists
twice: once enriched and promoted, once a bare stub nothing links to. The
generated index lists both and the corpus double-counts. A hand-maintained index
lists only the old path. The durable note's `sources` field names only the new
path. Three enumerations, three answers, and no defect is visible from inside
any one of them, because each is internally consistent. This is not a filing
error. It is what a naming-convention change does to a pipeline that derives
identity from names, and the only thing that catches it is matching captures on
upstream id instead of path.

**Plan-as-description.** A stored refactor plan gets read as an account of the
corpus. It is a proposal, often explicitly deferred, and the disk may be in a
third state matching neither its "before" nor its "after."

**Index drift from its own generator.** Exclusion rules tighten, the classifier
changes, categories are added, and no successful rebuild has run since — so the
committed index reflects the previous generator. It carries a "do not edit,
auto-generated" banner, which is exactly why nobody rechecks it. The banner
guarantees provenance, not freshness.

**The index indexing itself.** Policy files, READMEs, and taxonomy files appear
as corpus entries, inflating totals and putting navigation documents into search
results as though they were content.

**Query-as-title.** The generator falls back to whatever field is populated and
an ingest pipeline stored the full search query, so index entries become
paragraph-length titles. Technically complete, practically unscannable. Any
fallback chain for a display field needs a length ceiling.

**The sweep that never runs.** Per-write automation looks like full coverage. It
only ever sees files touched by the triggering event, so anything that failed
once is permanently invisible and the backlog grows silently for years.

**Taxonomy inflation.** Rather than make a filing decision, a new category gets
added, until there is roughly one category per note and the taxonomy carries no
information. A closed set that is expensive to extend is the point.

**Restructure by fiat.** The layout is treated as presentation and moved for
tidiness. It was an API: bots wrote to those paths, workflows filtered on them,
prompts referenced them, the generator hard-coded them. The tidier corpus is the
one nothing can write to any more.
