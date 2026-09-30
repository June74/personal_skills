---
name: desktop-project-delivery
description: "Coordinate a desktop application through platform feasibility, runtime integration, real-host verification, and final delivery. Resume ongoing work at its current stage; skip for isolated edits."
---

Read [the delivery workflow](references/workflow.md) and execute only the
stages relevant to the task. Existing user decisions and authorization apply.

When available, use `desktop-boundary-probes` for uncertain native behavior,
`prototype-runtime-wiring` for accepted UI integration, `async-side-effect-delivery`
for delayed external effects, and `regression-test-credibility` when green tests
miss observed failures. Load only the needed skill; otherwise follow the workflow
directly. Automatic selection does not grant new execution permissions.
