# Connect one client to one project first

Keep the source skills in this kit. The helper produces project-scoped snapshots with file hashes; it does not install global copies, run downloaded code, alter hooks or grant tool permissions.

| Client | Helper destination | Rules |
|---|---|---|
| Codex | `.agents/skills/` | project `AGENTS.md` |
| Cursor | `.agents/skills/` | project `AGENTS.md` |
| Claude Code | `.claude/skills/` | project `CLAUDE.md` importing `@AGENTS.md` |

Official documentation checked September 20, 2026: [Codex](https://learn.chatgpt.com/docs/build-skills), [Cursor](https://cursor.com/docs/skills), [Claude skills](https://code.claude.com/docs/en/skills), [Claude project instructions](https://code.claude.com/docs/en/memory).

Preview using `python scripts/prepare_client.py --client codex --project PATH`.
For a single optional skill add `--specialist mobile-release`; repeat the option to select more. This adds only the selected specialist, not the entire library. Then rerun with `--apply` after reviewing paths.

For all three clients in ONE project, first prepare Codex or Cursor (they share `.agents`). Claude needs its own discovery adapter. Cursor may also discover `.claude` compatibility folders, creating duplicate names. The helper blocks preparing Claude beside existing `.agents` copies, and the reverse, unless you explicitly pass `--allow-duplicate-discovery`. Do not use that option until you have inspected your client's inventory and chosen how to avoid duplicates (separate project/worktree scopes, selective client configuration if supported, or a documented manual linking strategy). This kit does not pretend there is one universally deduplicated cross-client layout.

When project instructions already exist, review and merge the policy rather than replacing them. The helper stops on conflicting files. It does not append content secretly. Rerunning after a successful apply is idempotent; future kit updates require a reviewed diff and intentional snapshot refresh, never edits to both source and deployed copies.

For native Windows versus WSL, paths refer to the environment where the client runs its tools. Keep Linux project environments in Linux. Use copies initially to avoid Windows symlink permissions/path-resolution surprises. A future symlink setup can expose canonical folders directly where every client can resolve them; validate inventory and permission semantics first.

Smoke test each client: see the 12 skill names exactly once; request an explicit skill; make a tiny feature; report a deliberate failing test honestly; confirm no specialist or MCP service was automatically enabled. Record client/model/version and results in `templates/client-smoke-test.md`.

Role files in `agents/` are task prompts, not portable permission manifests. Apply native read-only restrictions when invoking a reviewer. Model profiles are similarly guidance, not executable client settings. No subagent compatibility or model availability is assumed.
