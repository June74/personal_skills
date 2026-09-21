---
name: verify
description: "Gather and report actual evidence before claiming a change or task is complete, including the original symptom and acceptance criteria."
---

# Verify

Map acceptance criteria to observable evidence. Select the relevant test, lint, type, build, runtime/browser or manual check; avoid treating one check as all of them. Inspect the actual exit status and meaningful output against the current revision/diff.

For a bug, repeat the original reproduction. For UI work, inspect the rendered states and interactions, not only compilation. For migrations/deployment, verify data/rollback/recovery as appropriate. Explain untested platforms, skipped tools and unresolved failures.

Record command or procedure, revision/diff state, result and artifact when useful. Existing evidence for unchanged code remains valid within its scope; repeat after consequential changes rather than mechanically on every message. Never claim tests ran when they were only proposed or could not execute.

Report the outcome, what changed, evidence and material limits. If checks fail, investigate or clearly state the remaining failure. Do not hide missing tools by marking them as passed. Do not broaden or rerun testing without a changed risk, failure or requirement.
