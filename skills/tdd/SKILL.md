---
name: tdd
description: "Use red-green-refactor for deterministic behavior changes and reproducible bugs, with realistic integration boundaries and practical exceptions for exploration."
---

# Tdd

Agree the behavior and useful test boundary. Work one vertical slice at a time rather than writing a large speculative test suite. Assert public behavior using independent expected values; avoid assertions copied from implementation logic.

RED: write a focused test and run it. Confirm it fails for the intended missing behavior, not an unrelated import/setup error. For a bug, reproduce the original symptom. GREEN: implement the simplest correct behavior and run the relevant checks. REFACTOR: improve structure without changing behavior and rerun affected tests. Repeat.

Mock external/nondeterministic boundaries when appropriate, not every internal collaborator. Use database integration tests when transactions, constraints or database-specific semantics matter. Test permissions and error cases, not only happy paths.

For visual exploration, prototype and establish design acceptance before committing regression tests. For LLM behavior, combine deterministic tool/schema checks with a labeled evaluation set and human review; exact text matching alone is not adequate. State a reason when strict TDD adds little value to a trivial/reversible edit.

Explain what each test proves and what it misses. Tests should survive a sound internal refactor. Do not enforce arbitrary coverage percentages or add another runner if the project already has a suitable one.
