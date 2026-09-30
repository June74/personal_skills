# Desktop delivery skills

The canonical instructions live in `skills/`, alongside the discoverable core
skills. `workflows/desktop-project-delivery.md` links to the bundled procedure;
there is only one editable workflow body.

| Skill | Selection boundary |
|---|---|
| desktop-boundary-probes | Uncertain native focus, input, overlay, device, or webview behavior |
| prototype-runtime-wiring | Connect an accepted prototype to real application behavior |
| async-side-effect-delivery | Deliver delayed results to a destination that may have changed |
| regression-test-credibility | Observed failures despite passing tests |
| desktop-project-delivery | Coordinate multiple desktop delivery stages |

## Automatic selection

Each skill has descriptive portable frontmatter and Codex metadata with
`policy.allow_implicit_invocation: true`. Claude's default model invocation
remains enabled: no `disable-model-invocation: true` flag is set. The workflow
has its own entry skill because a standalone workflow file is not a skill catalog
entry. Selection is model-driven when relevant, not a background process.

Official references checked September 30, 2026:
[Codex skills](https://learn.chatgpt.com/docs/build-skills) and
[Claude skills](https://code.claude.com/docs/en/skills).

## Discovery and deployment

The existing `scripts/prepare_client.py` includes all five folders in core
snapshots. Use `--client codex` for `.agents/skills` or `--client claude` for
`.claude/skills`, with an existing project directory outside this kit. Preview
first; `--apply` creates the snapshot. See [client setup](CLIENTS.md) for existing
files and duplicate discovery. References and metadata travel with each skill.

For personal discovery on this machine, follow the existing library-link
convention: `~/.agents/skills/<name>` and `~/.claude/skills/<name>` link to
the canonical library folder. `~/.codex/skills/<name>` is a compatibility alias;
avoid duplicate entries if a client discovers both Codex locations.
New local sessions should refresh their skill catalogs. Other machines require
their own deployment; editing the library does not refresh copied snapshots.

No hooks, services, permissions changes, or additional packages are required.
Automatic selection preserves the task's existing authorization boundaries.

## Verification limits

Helper tests check complete snapshots for both clients, metadata, and bundled
workflow availability. Fresh-client model selection and task quality require
separate behavioral evaluation; packaging checks do not prove either.
