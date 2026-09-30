---
name: regression-test-credibility
description: "Investigate tests that pass despite observed failures, unrealistic fakes, or assertions that may never exercise the intended behavior."
---

Start from the observed failure and identify the test that should detect it.

- Confirm the test reaches the relevant code and observes its outcome.
- Pair rejection assertions with a valid control that must succeed.
- Check swallowed exceptions, missing sandbox bindings, skipped callbacks,
  and fixtures that accidentally erase important distinctions.
- Make fakes match observed contracts, readiness, lifecycle, and failures.
- Exercise application composition when a defect crosses component boundaries.
- For a suspect regression test, break the relevant guard in an isolated copy
  and confirm the test fails for the expected reason.
- Treat setup failures separately from behavioral failures.
- Use dependency probes as evidence about tested assumptions, not automatic
  proof that every downstream failure belongs to the dependency.

Report the original symptom, detection evidence, correction, and limits.
Use targeted checks; do not require mutation testing for every small change.
