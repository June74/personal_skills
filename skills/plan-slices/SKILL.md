---
name: plan-slices
description: "Turn agreed requirements into small, testable implementation slices with file responsibilities and verification; use for multi-step features or refactors."
---

# Plan Slices

Inspect the current project and acceptance criteria. Match plan depth to risk: a tiny task needs no plan document; a small feature needs a few outcomes; a new app or large change needs diagrams, interfaces, risks and milestones.

Each slice should identify observable behavior, files and responsibilities, the test or evidence that proves it, required dependencies, and ordering constraints. Prefer a vertical path through UI/API/data over building every layer in isolation. Include migration/rollback steps where data or deployments are affected.

Do not duplicate complete implementation code in the plan. Include essential interface examples only when they settle ambiguity. Avoid a compulsory framework, agent fleet, issue tracker or commit per microstep. Plans are revised when evidence changes; explain material deviations.

For refactors, characterize existing behavior, define the target boundary and migrate incrementally. For uncertain problems, plan a bounded experiment with a decision criterion before production work. Respect explicit user review gates; otherwise execute the authorized plan and report meaningful evidence.
