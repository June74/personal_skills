---
name: refactor-boundaries
description: "Perform a substantial behavior-preserving refactor when coupling or architecture drift obstructs a concrete change."
---

# Refactor Boundaries

Show the current dependency direction and the specific change that is difficult. Characterize observable behavior and callers with meaningful tests. Define one target responsibility/interface and migrate in small steps. Avoid generic abstraction layers without multiple real uses. Compare coupling, duplication and clarity after the change; do not equate fewer lines with better design. Keep public behavior stable unless scope explicitly includes a change. Use import-boundary tooling only when a maintained rule earns its dependency.
