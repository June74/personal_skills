---
name: architecture-and-data
description: "Reason about component boundaries, data models, APIs, failure modes and maintainable refactoring for a new or changing application."
---

# Architecture And Data

Start from existing code and actual functional/nonfunctional requirements: users, data volume, latency, privacy, availability, budget and operational skill. Estimate only enough to distinguish alternatives. Default to a modular single application; queues, caches and services require a concrete need.

Draw one readable context/component diagram and trace one request through it. Label external services and trust boundaries. Describe each module's responsibility, public interface and dependency direction. Prefer small interfaces hiding cohesive work; do not add abstractions only to imitate a pattern.

For data, identify entities, keys, constraints, ownership, deletion/retention and transaction boundaries. For APIs, define inputs, validation, authentication versus authorization, error responses, retries/idempotency and compatibility. Explain failures, logs, backups, deployment and rollback proportional to the feature.

Compare the simple default with one justified alternative. State dependency/service count, cost and removal difficulty. Show why an awkward structure hurts a specific change or test instead of labeling it bad architecture. Refactor after behavior is protected; split a file by responsibility, not an arbitrary line limit.

Use ordinary Mermaid flow/sequence/state/ER syntax when supported, or plain boxes/arrows. Keep diagrams near code/ADRs. Verify inferred architecture against entry points and callers. An automatically generated code graph is evidence to inspect, not authoritative memory.
