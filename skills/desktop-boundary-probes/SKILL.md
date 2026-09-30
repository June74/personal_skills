---
name: desktop-boundary-probes
description: "Validate uncertain native desktop behavior before implementing or releasing features involving focus, input, overlays, devices, or embedded webviews."
---

Identify the platform assumption whose failure would change the design.
Use a bounded probe in the intended OS, runtime, and receiving application.

- Define observable success, failure, and the decision each result enables.
- Exercise the real boundary early; imports and mocked calls prove less.
- Check thread ownership, initialization order, readiness, and native data
  layouts where the chosen APIs depend on them.
- For overlays and insertion, observe focus, target identity, and actual
  delivery; successful API returns alone do not establish success.
- Separate unattended checks from interactive and physical-device checks.
- Record revision, environment, command, observation, and untested limits.
- When reality contradicts a fake, repair the fake and add a boundary check.

Keep probes disposable and narrow. Preserve user data and shared services.
Stop once the uncertainty is resolved; do not build a parallel application.
