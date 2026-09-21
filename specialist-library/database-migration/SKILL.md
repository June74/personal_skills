---
name: database-migration
description: "Plan and verify schema or data migrations with compatibility, backups and rollback constraints."
---

# Database Migration

Inspect the actual database/version, schema, production size and migration history. Identify constraints, transaction/locking behavior and consumers. Use the project's migration system; generated migrations are drafts. Prefer expand, migrate/backfill, then contract for changes requiring compatibility. Test realistic data including nulls/duplicates and failure/restart. Establish backup restore evidence before destructive changes. Distinguish app rollback from irreversible data loss. Prepare commands and evidence; run production mutations only within explicit scope.
