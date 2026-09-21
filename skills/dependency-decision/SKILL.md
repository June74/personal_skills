---
name: dependency-decision
description: "Evaluate, explain and record meaningful package, runtime, model, service or infrastructure additions, replacements and upgrades."
---

# Dependency Decision

Before adding a dependency, state the missing capability. Check the standard library, existing packages and a simpler architecture. Choose a default and explain when one serious alternative would win; do not hand the beginner an undifferentiated list.

For the chosen dependency explain: runtime/dev/build/system/service/model role; where it is installed; direct versus meaningful transitive dependencies; native/browser/model downloads; license; required accounts/API charges; compatibility; maintenance/advisories; permissions/install scripts; lock-in and removal consequence. Use current primary evidence for changing facts and distinguish source-main from released versions.

Keep application packages project-local. Prefer uv for new Python projects and bundled npm for new JS projects, but preserve a functioning project's manager/lockfile. Do not add competing formatters, database servers or orchestration frameworks without a demonstrated gap.

For a significant choice, update the project's dependency decision record: capability, choice/version, why, alternative, roles, costs, source/date, rollback and revisit trigger. For a minor utility, a short explanation suffices. Show manifest and lockfile diffs, surprising new branches and applicable checks.

Never run a copied installer or npx/uvx command as a harmless discovery step. Pin reviewed tool versions; inspect provenance/install hooks, use least privilege and do not blindly update everything. A clean vulnerability scan does not establish trust or license compatibility.
