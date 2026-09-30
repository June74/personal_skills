# Desktop delivery lessons

Recorded September 30, 2026 from the Wispr_clone repository through `ba5b691`.
This is a bounded historical record, not a fresh application verification.
Raw conversations, machine-specific paths, and private runtime data are omitted.

| Stage | Repository evidence | Reusable lesson |
|---|---|---|
| UI design and retention | `02eeb60` through `7604ad6`, September 23 | Preserve accepted decisions through iteration and final packaging |
| Platform feasibility | `f58d351`, `2437efa`, `fcae1ec`, September 24 | Probe uncertain host, model, focus, and destination assumptions early |
| Foundation | `b903fe7` through `984ab46`, September 25 | Contracts, fakes, probes, import checks, and CI serve different evidence needs |
| Component integration | `f884cf6` through `f9d3177`, September 25–26 | Test application wiring, cancellation, recovery, retention, and delivery |
| Transcription revision | `fadda31`, `d750c6a`, September 26 | Remove superseded implementation and reconcile capabilities and settings |
| Real-host corrections | `9ecb12a`, `85aaaab`, `e7d010a`, September 26–27 | Fakes missed native threading, readiness, and input-layout constraints |
| Final runthrough | `a28af3a` through `ba5b691`, September 28 | Exercise controls and prove regression tests can detect their target failure |

The UI and backend runthrough work orders exposed ineffective controls,
same-version recovery-event rejection, clock-domain mismatch, and a passing
test whose swallowed exception prevented either event from being exercised.
These findings motivate the four focused skills and the delivery entry skill.
The original planning pipeline and role profiles describe intended process;
their existence alone does not establish execution or success.

The project README labels v0 complete. The September 27 desktop checklist
records skipped microphone-disconnection testing and insertion findings whose
closure was not established during this retrospective. No current runtime,
release readiness, or comparative model-performance claim follows from it.

Source records: project `README.md`, Git history, `backend_dev/web/README.md`,
and `backend_dev/agents/work_orders/{desktop-checklist-H,WO-fix-v0-backend,WO-fix-v0-web}.md`.
