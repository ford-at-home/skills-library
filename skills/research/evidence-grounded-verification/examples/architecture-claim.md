# Worked example — a README's own architecture claim

A real fact base, produced by running this skill against a project README. Kept
because it shows the process catching something a careful proofread would not.

**Audience:** a technical evaluator — prospective collaborator, acquirer, or
employer — who can open the repository and read the deployment config.

**Cleared as of:** 2026-07-27 · **Decays first:** infrastructure counts, which
change on every deploy.

## Unresolved (read first)

- Two handler directories exist on disk with implementations but aren't
  referenced by the deployment stack. Whether they're pending, abandoned, or
  deployed by another mechanism is unsettled, and it changes the correct count
  below. Resolved by asking the author.

## Block 1 — Do not cite

None. Every claim traced to something real. The defect here is magnitude, not
fabrication — which is the more common case.

## Block 2 — Correct before use

### Lambda function count

- **Stated:** "28 Lambda Functions", in the headline architecture diagram at
  `README.md:15`.
- **Correct:** four are declared in the deployed stack. Six handler directories
  exist on disk; two aren't wired in.
- **Source:** the CDK stack file. This is the executable definition of what
  actually deploys, which makes it primary.
- **Searched:** every `lambda_.Function` and `PythonFunction` constructor call
  across the project. Nine further matches exist, all inside `docs/*.md` guides
  — illustrative code samples, not infrastructure.
- **Re-anchor to:** "four Lambda functions across a Python serverless stack."
- **Why it survived internally:** the number sits in the most prominent position
  in the README, inside an ASCII diagram, where it reads as a specification
  rather than as a claim someone once made.

## Block 3 — Cleared

| Claim | Level | Source | Date | Phrasing that survives |
|---|---|---|---|---|
| Uses AWS Lambda, DynamoDB, API Gateway, CDK | `primary` | the CDK stack file | 2026-07-27 | "Serverless AWS stack deployed via CDK" |
| Handlers are Python | `primary` | `PythonFunction` constructs | 2026-07-27 | "Python Lambda handlers" |
| Integrates a third-party search API | `primary` | the service handler | 2026-07-27 | "Search API integration for market intelligence" |

## Measured vs derived

| Finding | Which | If derived: assumption, and was the method ever checked? |
|---|---|---|
| 4 declared functions | measured | Counted from constructor calls in the stack |
| 6 handler directories | measured | Counted from disk, deduplicated across a mirrored tree |
| 28 | derived, method unvalidated | No counting method reproduces this figure |

---

## What this demonstrates

The README is self-authored, so under *never clear a claim by citing a document
your own team wrote*, it can't clear its own architecture claim. That rule is
what pushes the check past the prose and into the deployment config, where the
real number is.

Without it, you read a confident, specifically-numbered, diagram-formatted claim
and move on. The formatting is exactly what makes it read as more sourced than
it is — "28" looks like the output of a count, and nobody re-ran the count.

This is the ordinary form of the failure this skill exists for: not a lie, but a
figure that became load-bearing without anyone re-deriving it.

A note on the check itself. An earlier manual review of this same repository
recorded three functions rather than four. The conclusion held — the README was
badly overstated either way — but the count didn't, which is the argument for
treating a count as a documented search rather than a recollection.
