---
name: prototype-runtime-wiring
description: "Connect an accepted UI prototype to application commands and events while preserving its design and verifying real behavior."
---

Map each actionable control to its command, persisted value, returned state,
and visible success or failure. Identify controls without runtime support.

- Preserve accepted presentation; replace simulated outcomes explicitly.
- Establish one authoritative owner for application state and resources.
- Specify event ordering, duplicate handling, and stale-event rejection.
  Related events may legitimately share a version.
- Preserve unsaved edits during background renders.
- Distinguish valid zero values from missing values.
- Refresh authoritative state after reconnect; do not blindly replay mutations.
- Exercise actual UI wiring: edit → enable → submit → persist → reload.
- Check recovery and cancellation controls in every applicable state,
  including visibility, focus, and clickability under the actual CSS.
- Disable or label unsupported behavior instead of implying it works.

Deliver the working flow and remaining gaps. Pure helper tests supplement
browser and host checks; they do not establish that controls are connected.
