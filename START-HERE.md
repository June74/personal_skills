# Your AI development folder kit

This is the actual first version of the portable layer proposed in your report.
The 12 core skills have been written as concise, original adaptations. They are not copies of entire upstream frameworks.

## What works as files

- `skills/`: 12 portable skills. Each folder contains a real `SKILL.md`.
- `rules/core.md`: the small shared mentoring/engineering policy.
- `agents/`: three portable role contracts; no automatic agent spawning.
- `specialist-library/`: 13 optional skills. Kept outside client discovery until needed.
- `templates/`: project specs, diagrams, dependency decisions, debugging, reviews and learning records.
- `scripts/`: standard-library Python utilities for inspection, validation, safe client preparation and checks.
- `memory/`: schemas, synthetic examples, lifecycle and a unapplied Cognee connection recipe.
- `evals/`: 16 realistic cases, fixture files, grading rubric and result template.
- `model-profiles/`: three client-neutral profiles. They do not select or buy a model automatically.
- `setup/`: phased instructions and per-tool installation/dependency inventory.
- `docs/research/`: your complete report and evidence appendix.

## First use

1. Keep this folder as your canonical kit. For Linux tools later, copy it into your WSL home, e.g. `~/ai-dev-system`. Do not maintain two editable copies.
2. Open a small disposable learning project in one coding client. Start with one client; connect the others after it works.
3. Read `setup/CLIENTS.md`. The helper below previews every new file and never overwrites existing content.
4. Activate the core skills for that project, then ask: “Build one small feature with me. Explain the files and dependencies; show the failing test, fix, and verification.”
5. Use the phase checklist in `setup/PHASES.md`. Keep optional services off until needed.

With Python 3.11+ already available, from this kit folder:

```text
python scripts/doctor.py
python scripts/validate_kit.py
python scripts/prepare_client.py --client codex --project /absolute/path/to/learning-project
```

The last command is a **preview only**. Use your real existing project path (the example is not a literal target). On Windows quote paths containing spaces and use the Python launcher/interpreter installed on your machine; in WSL the command may be `python3`.

After reviewing the preview, repeat it with `--apply` to create the listed files. Use `--client claude` or `--client cursor` for those clients. Do not activate all three into the same project without reading the duplicate-discovery guidance.

The helper does not install Python, packages, applications, MCP servers or hooks. It does not change your home/global client settings. If a file already differs, it stops before writing; merge intentionally using the displayed source/destination and rerun. It does not auto-update deployed copies.

## What is not just a folder

Python/Node, a browser, PostgreSQL and Cognee are running software. This kit supplies their selected recipes/configuration examples, not bundled executables, model weights or subscriptions. Optional software that the report rejected is not included.

Memory examples are synthetic. Live private records belong outside this distributable kit. No live memory endpoint, telemetry hook or automatic observer is enabled. Cognee configuration still requires installation, a model/storage choice and privacy/concurrency/restore checks. Voice is your own future project; the kit supplies guidance and acceptance examples only.

Read [WALKTHROUGH.md](WALKTHROUGH.md) to understand every file, and [DECISIONS.md](DECISIONS.md) for your current choices.

See `VALIDATION.md` for exactly what was tested. File/schema/helper validation is not proof that all three installed clients behave identically or that an AI model follows every instruction.
