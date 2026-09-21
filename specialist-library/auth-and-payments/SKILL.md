---
name: auth-and-payments
description: "Design or review authentication, authorization, billing or payment boundaries using established framework/provider primitives."
---

# Auth And Payments

Map actors, roles, ownership and trust boundaries. Choose established identity/session/payment primitives fitting the current framework rather than hand-writing cryptography or card storage. Test cross-user denial, expiry/revocation, CSRF where relevant, webhook signature verification, replay/idempotency and failure recovery. Keep test/live credentials and events separate. Check current provider terms, fees, refunds and geographic requirements. Explain the data flow and dependency cost. Do not create charges or modify live billing without authorization.
