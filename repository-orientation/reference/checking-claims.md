# Cheap checks by claim shape

Load-bearing means your change is wrong if the claim is false. These are in
rough order of value returned per second spent.

| Claim shape | Check |
|---|---|
| "There are N of X" | Count the declarations in source and in the infrastructure definition. Compare both to the doc. |
| Names a file, table, env var, or endpoint | Confirm it exists, and that something references it. |
| Names a framework or version | Read the dependency manifest and the lockfile, not the prose. |
| "Configured in `<file>`" | Confirm the toolchain actually reads that file. Config files for the wrong major version are inert and invisible. |
| Implies test coverage | Open the tests. Note what they actually assert, not what the directory is called. |
| Describes what is deployed | Compare against the infrastructure definition. Prose describes intent; the deployment definition describes reality. |
| Describes a boundary or permission | Find the enforcement — the migration, the policy, the guard. An unenforced boundary is a convention. |

Label each claim. When a document and the code disagree, the code wins and the
disagreement is a finding you report.
