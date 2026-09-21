---
name: review
description: "Review a meaningful code or architecture change against requirements, focusing on evidenced defects and risks; use independent context when available and justified."
---

# Review

Establish the scope: intended behavior, base/current revision or uncommitted diff, constraints, tests and reported evidence. Read the relevant code and callers before making claims. Prefer a separate read-only reviewer for consequential changes when authorized and available; otherwise perform an explicit review pass and state its limits.

Look for concrete correctness, data-loss, security, compatibility and maintainability issues. Follow changed behavior across boundaries. A test pass does not prove authorization, migration safety or business correctness. Avoid speculative low-value style comments.

Return actionable findings with severity, file/line, trigger scenario, consequence and suggested direction. Distinguish verified facts from questions. If no issues are found, say so and state coverage limits. Do not invent findings to fill a quota.

The reviewer does not edit, merge, deploy or access production credentials merely because it can. Client-side tool restrictions must enforce read-only access where supported; prose is not a sandbox. Review once per meaningful change rather than every tiny step. Verification remains execution evidence, not a replacement for reasoning.
