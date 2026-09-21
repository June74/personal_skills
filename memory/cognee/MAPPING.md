# Map our records to Cognee deliberately

The JSON record schema describes what we want to preserve. It does not replace Cognee's internal relational, vector or graph schema. No importer/synchronizer is implemented in this kit.

| Our concept | Proposed usage / check |
|---|---|
| user/global and project/ID | Choose explicit dataset/scoping conventions and test actual access boundaries; names are not ACLs |
| statement + source_ref + dates | Include a stable ID and provenance in approved ingested text/metadata; verify retrieval preserves them |
| candidate vs accepted | Keep candidates outside durable ingestion until reviewed |
| valid_to / supersedes | Maintain an explicit correction link; test that outdated claims are not presented as current |
| retention / deletion | Document the exact record/dataset removal path and derived-data behavior before promising granular deletion |
| links | Let Cognee derive graph relationships, then treat inferred relations as hypotheses unless supported |

Current MCP surface exposes remember, recall, forget and an ingestion-status helper. Remember can distinguish session cache from permanent graph work; completion and dataset scope must be checked. Forget can have broad dataset/owned-memory scope, so do not translate a request to remove one fact into a broad purge. Inspect the actual selected version's tool schema. [MCP tool documentation](https://github.com/topoteretes/cognee/blob/main/cognee-mcp/README.md).

Pilot sequence: ingest one approved synthetic record; wait for processing; retrieve its claim and provenance; add a correction; query again; exercise deletion at a known safe scope; restart and restore. Record failures honestly. Keep the original reviewed source records for portability, with a clear decision about which copy is authoritative.
