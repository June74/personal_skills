# Usable stages, not one giant installer

| Phase | Install or enable | Depends on | Completion check |
|---|---|---|---|
| 0 Foundation | WSL/Ubuntu if chosen; Git, ripgrep; reviewed uv and project Python; Node/npm only when needed | Supported host, disk, accounts already chosen | Explain paths, interpreter, package manager, Git diff and recovery |
| 1 Engineering | 12 skills/policy; pytest, Ruff, mypy for Python project | One working client and project environment | One red-green-refactor slice plus evidence and teach-back |
| 2 Visual | Existing browser or Playwright CLI; project Playwright tests; your own voice tool when ready | Node/browser OS dependencies for Playwright | Responsive UI, keyboard/error-state check; dictation preserves negation |
| 3 Memory | Curated intake records + isolated Cognee endpoint | Private storage, backups, explicit scope | Three-client dummy-data retrieval/correction/delete/concurrency/restore checks; network review |
| 4 Safety | Gitleaks before publishing; OSV; relevant security rules | Lockfiles and advisory refresh | Controlled fixtures detected, license reviewed, update rollback demonstrated |
| 5 Evolution | Manual learning events and paired evals | Stable skills and meaningful feedback | Evidence-backed candidate passes held-out cases, human review and rollback |
| 6 Specialists | One selected project-specific skill/tool set | Concrete project requirement | Explain dependencies, permissions, costs and removal; test actual target |

Use `software.json` as an inventory, not an install-all list. Review official installation instructions and selected versions before executing anything. The research report in `docs/research/` explains alternatives, costs, context and exact source evidence.
