# Defect classes, ordered by retrieval impact

Impact is what a defect does to an agent retrieving from the corpus later, not
how many notes carry it. A misspelled `type` in one note that a filter depends on
outranks a missing `created` date in two hundred.

| Class | Retrieval impact | Repair |
|---|---|---|
| Missing `type` / `status` / `source_quality` | Note is invisible to filtered retrieval, or silently downranked | Owner supplies the value. Never guess |
| Illegal enum value | Same as missing, and it hides as valid | Owner decides: correct the note, or widen the schema |
| Stale `claims` cache | Worst case in the set — retrieval reads the cache and answers from superseded content | Regenerate from the body, propose as a draft |
| Malformed `claims` entry | Fragment retrieval returns prose instead of assertions | Rewrite as one assertion per entry |
| Broken supersede chain | Superseded content is served as current | Set target `status`, add `[Superseded]` + forward link |
| Broken wikilink | Traversal dead-ends | Repoint or remove the link, keep the note |
| Orphan note | Unreachable by traversal; only keyword search finds it | Link it from a hub or map note |
| Unlinked mention | The edge exists in prose and not in the graph | Propose the link, with the snippet as evidence |
| Missing `[Unverified]` | Agent overtrusts the note | Add the label. Do not raise `source_quality` |
| Missing `sensitivity` | Private content can leak into an external draft | Owner supplies it. Default to the most restrictive value pending an answer |
