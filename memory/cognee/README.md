# Cognee shared-memory setup guide

This recipe reflects inspected current source, not a tested installation or a promise about every release. Choose and pin a compatible release/commit and resolved dependencies before setup.

Use **one local Cognee MCP endpoint** for the three clients. Begin in an isolated WSL environment with synthetic data. The inspected MCP server supports direct local operation; a separate cloud deployment is not required. Its package graph is substantial, so inspect the MCP manifest and chosen storage/model configuration instead of installing every extra from a development quickstart. [MCP source and setup](https://github.com/topoteretes/cognee/blob/main/cognee-mcp/README.md), [manifest](https://github.com/topoteretes/cognee/blob/main/cognee-mcp/pyproject.toml).

After deliberately obtaining the reviewed source and installing its required dependencies, the documented direct command, **from its cognee-mcp directory**, is:

```text
python src/server.py --transport http --host 127.0.0.1 --port 8000 --path /mcp
```

This command is not run by the kit. Resolve port conflicts and Windows/WSL reachability without casually binding to the LAN. Client fragments point to this endpoint: Claude project .mcp.json, Cursor .cursor/mcp.json, and the chosen Codex config scope. Merge manually; never replace existing configuration wholesale. Codex's example is disabled. The examples do not implement server authentication.

Before installation choose: exact package/source version; local storage and backup paths; extraction route; embedding model/provider/dimensions; desired search behavior; network/authentication requirements. Core Cognee advertises a keyless local path, but verify that your chosen MCP version and recall mode support it. Do not assume an existing coding subscription supplies a separate API key or MCP sampling capability. [Cognee overview](https://github.com/topoteretes/cognee), [provider configuration](https://github.com/topoteretes/cognee/blob/main/.env.template).

The .env.example file is an inactive worksheet, intentionally not filled with model names, credentials or guessed telemetry controls. Review the selected version's actual telemetry/logging/remote-routing settings. Passing an API token from the MCP bridge to a backend is a different boundary from authenticating callers of the MCP endpoint. Review both before exposing anything beyond trusted local use. [Server implementation](https://github.com/topoteretes/cognee/blob/main/cognee-mcp/src/server.py).

Acceptance: same dummy memory retrieved from all three clients; completed ingestion before recall; evidence/source preservation; correction and deletion with understood scope; concurrent writers; restart and restore; relevant scoped retrieval; measured token/cost budget; confirmed network and permission boundaries. The portable intake convention is not automatically enforced by Cognee. No auto-capture plugin/hooks are enabled.
