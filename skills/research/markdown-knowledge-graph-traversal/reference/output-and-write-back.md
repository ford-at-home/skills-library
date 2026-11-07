# The seven sections, and how a write-back is proposed

## Output

```markdown
## Answer
<1-3 sentences. The direct answer. No hedging theater.>

## Evidence Map
<Nodes and typed edges from step 4, human-readable, with exact file paths.>

## Key Nodes
<The 3-5 that carry the answer. Each with: type, source_quality, confidence.>

## Conflicts and Gaps
Conflict: <both statements, both paths, both dates, which wins and why>
Gap: <what is missing that would materially change the answer>

## Evaluation
<The claim YAML from step 5, one block per major claim.>

## Recommendation
<What the evidence supports doing or believing. If confidence is low, say so in
the first sentence. Do not smooth it.>

## Notes to Update
<Proposed new, edited, or newly linked notes. Proposal only.>
```

The Evidence Map is the section that proves step 4 happened. An answer with no
node list was written by blending retrieved text, whatever the other six
sections say.

## Write-back rules

Only if `write_back` was given, and only after the user has read the answer.

- A new synthesis note goes in the drafts folder with `type: synthesis`,
  `source_quality: ai-generated`, `status: needs-review`, and `related:` links to
  every note cited in the Evidence Map.
- A change to an existing canonical note is written as a **separate proposed-
  update note** in the drafts folder, never as an edit to the note itself.
- A new open question becomes its own note with `type: open-question`.

Nothing leaves the drafts folder without human approval.

If `write_back` is "none", still emit the Notes to Update section. It is a
proposal, not a write.
