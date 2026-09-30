---
name: async-side-effect-delivery
description: "Design or review delayed operations that deliver results to an external destination after focus, settings, or application state may change."
---

Define the destination, operation identity, cancellation boundary, expiry,
and recovery behavior before dispatching an external side effect.

- Capture the intended destination and relevant settings at operation start.
- Revalidate destination identity and eligibility immediately before dispatch.
- Reject late results after cancellation, deletion, expiry, or replacement.
- Keep clock domains explicit: compare timestamps only within a compatible
  clock domain; test composition with distinct wall and monotonic clocks.
- Separate not attempted, dispatched, confirmed, and uncertain outcomes.
- Do not automatically retry an uncertain non-idempotent operation.
- Choose deduplication or recovery according to the destination's capabilities;
  do not promise exactly-once delivery without supporting evidence.
- Test cancellation races, destination loss, timeout, and restart where relevant.

For text insertion, never infer permission to submit or execute the text.
Expose a recoverable held state when safe delivery cannot be established.
