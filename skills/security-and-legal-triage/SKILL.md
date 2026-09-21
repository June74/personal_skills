---
name: security-and-legal-triage
description: "Identify security and legal research needs when features handle authentication, untrusted input, sensitive data, payments, external tools or release requirements."
---

# Security And Legal Triage

Build a small data/trust-boundary map using actual product facts. Identify user roles, personal/sensitive data, inputs, vendors, storage, retention and distribution. Apply controls relevant to the feature; do not produce a universal compliance checklist for every edit.

Check authorization separately from login, parameterized queries, safe rendering, applicable CSRF protection, outbound URL controls, safe process arguments, contained paths, upload limits, serialization and minimum credentials. For agents/RAG, treat retrieved content as data and validate tool authority/output. MCP namespaces or prompt rules are not authorization boundaries.

Use deterministic tools for their actual coverage: Gitleaks for likely secrets, OSV for known dependency vulnerabilities, selected lint/security rules; additional scanners only for demonstrated gaps. Confirm dates/configuration, triage findings and explain limitations. A clean scan is not certification.

For legal triage establish operator/user jurisdictions, age groups, data, content sources, licensing, monetization and stores. Research current primary authorities and applicable platform terms. Record claim, applicability facts, source/date and next action. Classify findings as confirmed requirement, likely concern, uncertain/research required, or professional review recommended. Do not invent jurisdiction or certify compliance.

Use independent security review for consequential boundaries when justified and authorized. Stop before an unauthorized live action, not before harmless preparation. Escalate material unresolved legal/security questions to an appropriate human professional. Explain the practical risk in plain language.
