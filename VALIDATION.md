# Validation and limits — kit 0.2.0

Cognee replaces the previous memory recipe; voice guidance now targets your own implementation. Client fragments remain unapplied and Cognee has not been runtime-tested.

This kit was created as deliverable files. No global client configuration, application dependency, model, server, hook, scheduled task or production resource was installed or enabled.

## Completed checks

- Parsed all 25 skills using the kit's controlled frontmatter validator: matching names/folders, descriptions and nonempty bodies; 12 core and 13 optional.
- Parsed JSON and TOML resources, validated the synthetic memory record and tested negative memory cases.
- Ran 16 deterministic helper tests: **15 passed, 1 skipped**. Covered preview without writes, idempotent preparation, no overwrite/partial writes on pre-existing conflicts, explicit specialist activation, duplicate-discovery guard, path-escape rejection, check preview versus execution, literal shell metacharacters, nonzero exit propagation, missing tools and timeout failure.
- The skipped test would create a directory symlink to check escape rejection. This Windows session lacked the permission to create that link. Direct traversal rejection was tested; the symlink/reparse protection is present but not proven by that test here.
- The bundled Skill Creator quick validator could not run because its PyYAML dependency is unavailable. No dependency was installed just for it. The supplied standard-library validator checks the deliberately narrow generated frontmatter format; it is not a general YAML parser or a behavioral benchmark.

## Not claimed

- Live discovery, permission enforcement or model behavior in your installed Codex, Cursor or Claude Code versions. Run `templates/client-smoke-test.md` in each actual client.
- Automated model/profile evaluations. The 16 cases and fixtures are supplied, with results initially marked `not_run`; no paid model calls were made for them.
- A running shared memory endpoint, authentication layer, enforced namespace isolation or cross-client backup/concurrency success. Memory connection examples are disabled/unapplied recipes.
- A resolved application lockfile, installed transitive-package count or proof that every referenced upstream release is secure today.
- A sandbox for arbitrary check commands. `run_checks.py` avoids shell interpolation, but a configured executable can still perform any action its permissions allow. Review configurations before `--run`.
- Atomic multi-file writes against hostile concurrent filesystem changes. The setup helper preflights conflicts and uses exclusive creation, but is intended for a normal local project, not an adversarial shared filesystem. A mid-run race or disk failure can leave some newly created files; rerun after inspecting them. It never intentionally overwrites existing files.

## Reproduce local checks

With Python 3.11+ from this folder:

```text
python -B scripts/validate_kit.py
python -B scripts/validate_memory.py memory/examples/preference.json
python -B tests/test_helpers.py
```

The helper tests use disposable directories under the OS temp directory, verify their cleanup boundaries, and do not access the network. After you intentionally customize files, integrity hashes will differ; review the changes before making a new release/manifest. Do not treat a checksum as a signature or security assessment.
