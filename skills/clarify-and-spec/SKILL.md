---
name: clarify-and-spec
description: "Resolve material requirement ambiguity and define acceptance criteria for a new feature or application; scale down for small, already clear changes."
---

# Clarify And Spec

Inspect existing behavior, conventions and the user's request before asking questions. Separate known facts, assumptions and decisions. Ask only questions whose answers materially change scope, data, risk or user experience; recommend a default with its tradeoff. Continue independent work while awaiting required facts.

For a meaningful feature, produce a short specification: user/problem; desired behavior; non-goals; examples and failure states; data/permissions; acceptance checks; open decisions. For tiny edits, a sentence and a check suffice. Use the user's terminology and define ambiguous entities.

Read current primary documentation for unstable capabilities. Label research conclusions and uncertainty. Do not invent repository behavior. Record an ADR only for a consequential or surprising choice, not every implementation detail.

Resolve decision dependencies in order: who and what before interface, interface/data before implementation sequence. Treat a specification as what and why; leave execution order to the plan. Reuse existing documents instead of creating parallel sources of truth. Obtain the user's requested design/scope review before committing to dependent implementation, without adding redundant approval steps to already authorized work.
