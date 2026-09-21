# Your AI development kit, file by file

**Current choices: Cognee for memory; your own voice application.** This folder is a reusable starter kit of instructions, templates, setup recipes and helper programs. It is not an already-installed all-in-one application. Cognee itself and your voice app are not bundled or running.

You do not have to maintain every file by hand. Start with START-HERE.md, rules/core.md and the skills relevant to your work. Use the rest when the corresponding need appears.

## How the pieces fit together

1. **Rules** provide the common working expectations.
2. **Skills** provide task-specific workflows, such as debugging or reviewing.
3. **Adapters and the preparation helper** put copies in a project's client-discovery folders.
4. **Templates** give those workflows useful documents to produce.
5. **Checks and evaluations** help establish whether the tools and workflows work.
6. **Cognee**, after separate setup, can provide persistent retrieval across clients. The kit supplies a reviewed-record convention and connection examples.
7. **Your voice application**, once you build it, can provide another way to supply input. This kit provides a specification workflow and testing worksheet.

**Active context** means the material actually supplied to the model for its current response: conversation, loaded instructions, relevant code, tool results and any retrieved memories. A file being somewhere in this folder does not automatically put its contents in active context. A memory stored in Cognee likewise only helps a response when relevant information is retrieved and supplied to the model. Loading everything every time would add noise and cost.

**Adopt** means use a tool or approach substantially as supplied. **Adapt** means modify an idea or workflow for your needs. The skills here are original concise adaptations, not copies of entire upstream projects.

## Reading the file types

- `.md`: readable text instructions or worksheets. A `SKILL.md` is a specially named instruction document.
- `.json` and `.toml`: structured data or configuration. A program/client must explicitly read them for them to have an effect.
- `.py`: Python code that runs when invoked.
- `.html`: a browser-readable document.
- `.env.example`: an example settings worksheet; not active credentials or a running configuration.
- `.gitignore`: Git's exclusion patterns; `VERSION` and `LICENSE` are plain text.

## Complete walkthrough

## 1. The top level — start here

These files explain the kit and record its version, sources and checks.

| File | What it does |
|---|---|
| [README.md](README.md) | The front door: links to the starting instructions, this walkthrough and current decisions. |
| [START-HERE.md](START-HERE.md) | Your first-use instructions, including how to preview preparing a project and then explicitly apply it. |
| [DECISIONS.md](DECISIONS.md) | Records your choices: Cognee for memory and a voice application you will build. These choices override the older report. |
| [WALKTHROUGH.md](WALKTHROUGH.md) | This guide. Explains every delivered file and how the parts fit together. |
| [CONTENTS.md](CONTENTS.md) | A generated clickable inventory. Use it to find a file quickly. |
| [VERSION](VERSION) | The kit release number, currently 0.2.0. It is not a model or application version. |
| [LICENSE](LICENSE) | MIT terms for the original material created for this kit. Referenced third-party software keeps its own license. |
| [SOURCES.md](SOURCES.md) | Explains the source/adaptation policy. These are original concise instructions informed by research; upstream projects are not bundled. |
| [sources.lock.json](sources.lock.json) | A structured list of research references. Despite its name, this is NOT a resolved dependency lockfile: upstream commits are not pinned and links may change. |
| [kit-manifest.json](kit-manifest.json) | SHA-256 hashes of delivered files other than itself. Helps detect changes to this snapshot; it is not a signed guarantee of safety. |
| [VALIDATION.md](VALIDATION.md) | What was tested, what passed, what was skipped, and what has not been tested in real clients. |
| [.gitignore](.gitignore) | Tells Git to leave out common local environments, secrets, caches and private runtime data. It neither encrypts files nor removes anything already committed. |

## 2. rules/ — the shared ground rules

This is the short common policy used when preparing a project.

| File | What it does |
|---|---|
| [rules/core.md](rules/core.md) | Guides teaching, dependency restraint, privacy, verification and reviewed memory. The preparation helper uses it for the project AGENTS.md. These are AI instructions, not operating-system permissions. |

## 3. skills/ — the 12 everyday workflows

Every child folder contains one SKILL.md. Its opening metadata describes when the skill is relevant; the body tells the AI how to handle that work. Merely keeping this library on disk does not activate it in a client.

| File | What it does |
|---|---|
| [skills/mentor-mode/SKILL.md](skills/mentor-mode/SKILL.md) | Explains decisions at your level, gives useful hints, and helps you understand the code you are building. |
| [skills/clarify-and-spec/SKILL.md](skills/clarify-and-spec/SKILL.md) | Turns an unclear request into requirements, boundaries and observable acceptance conditions. |
| [skills/plan-slices/SKILL.md](skills/plan-slices/SKILL.md) | Breaks a feature into small pieces that can each be implemented and checked. |
| [skills/architecture-and-data/SKILL.md](skills/architecture-and-data/SKILL.md) | Reasons about components, data ownership, boundaries and consequential design choices. |
| [skills/dependency-decision/SKILL.md](skills/dependency-decision/SKILL.md) | Checks whether another package or service earns its maintenance, cost and security burden. |
| [skills/tdd/SKILL.md](skills/tdd/SKILL.md) | Uses a meaningful failing test, the implementation, and cleanup when test-driven work fits the task. |
| [skills/systematic-debugging/SKILL.md](skills/systematic-debugging/SKILL.md) | Reproduces a failure, tests explanations and verifies the actual cause before declaring it fixed. |
| [skills/review/SKILL.md](skills/review/SKILL.md) | Reviews changes for concrete defects and missing evidence, with actionable findings. |
| [skills/verify/SKILL.md](skills/verify/SKILL.md) | Requires evidence from relevant checks before claiming a change works; reports unavailable checks honestly. |
| [skills/prototype-ui/SKILL.md](skills/prototype-ui/SKILL.md) | Uses a small visual prototype to resolve layout and interaction questions before larger implementation. |
| [skills/browser-check/SKILL.md](skills/browser-check/SKILL.md) | Checks user flows in a browser while respecting private sessions and recording relevant evidence. |
| [skills/security-and-legal-triage/SKILL.md](skills/security-and-legal-triage/SKILL.md) | Identifies security concerns and legal questions, separates evidence from assumptions, and flags questions requiring qualified review. |

## 4. specialist-library/ — 13 workflows to add when needed

These have the same file format as the core skills, but preparation does not copy them unless explicitly selected. They do not install their related applications.

| File | What it does |
|---|---|
| [specialist-library/release-and-deployment/SKILL.md](specialist-library/release-and-deployment/SKILL.md) | Plans release checks, rollout and recovery for a real deployment. |
| [specialist-library/auth-and-payments/SKILL.md](specialist-library/auth-and-payments/SKILL.md) | Handles identity and payment boundaries, including authorization and failure cases. |
| [specialist-library/database-migration/SKILL.md](specialist-library/database-migration/SKILL.md) | Plans safe data/schema changes, validation and recovery. |
| [specialist-library/rag-and-evaluation/SKILL.md](specialist-library/rag-and-evaluation/SKILL.md) | Designs retrieval-assisted answers and evaluates whether retrieval and answers actually improve. |
| [specialist-library/mobile-release/SKILL.md](specialist-library/mobile-release/SKILL.md) | Guides mobile packaging, platform requirements and release checks. |
| [specialist-library/unity-workflow/SKILL.md](specialist-library/unity-workflow/SKILL.md) | Guides changes and verification in a Unity project; Unity itself is not included. |
| [specialist-library/blender-workflow/SKILL.md](specialist-library/blender-workflow/SKILL.md) | Guides reproducible Blender work and checks of resulting assets; Blender is not included. |
| [specialist-library/refactor-boundaries/SKILL.md](specialist-library/refactor-boundaries/SKILL.md) | Improves code structure while controlling scope and preserving behavior. |
| [specialist-library/memory-curation/SKILL.md](specialist-library/memory-curation/SKILL.md) | Decides what is worth retaining, checks its source and handles corrections. It does not automatically save conversations. |
| [specialist-library/current-source-research/SKILL.md](specialist-library/current-source-research/SKILL.md) | Finds current primary sources and distinguishes verified facts from inference. |
| [specialist-library/skill-evolution/SKILL.md](specialist-library/skill-evolution/SKILL.md) | Turns repeated, evidenced workflow problems into reviewed improvements to a skill. |
| [specialist-library/design-system/SKILL.md](specialist-library/design-system/SKILL.md) | Keeps reusable visual styles and components consistent as the product grows. |
| [specialist-library/voice-workflow/SKILL.md](specialist-library/voice-workflow/SKILL.md) | Helps specify, build and test YOUR voice tool: capture, transcription, optional cleanup, review and text insertion. There is no finished voice application or selected speech engine here. |

## 5. agents/ — job descriptions for focused reviews

These three Markdown files describe roles. They are not running agents, native client agent definitions, or an automatic delegation system.

| File | What it does |
|---|---|
| [agents/explorer-researcher.md](agents/explorer-researcher.md) | A bounded research/exploration assignment with expected evidence and a useful handoff. |
| [agents/independent-reviewer.md](agents/independent-reviewer.md) | A separate review perspective that challenges implementation assumptions and reports concrete findings. |
| [agents/security-architecture-reviewer.md](agents/security-architecture-reviewer.md) | A focused review of trust boundaries, permissions and consequential architecture risks. |

## 6. adapters/ — instructions for each coding client

The preparation helper copies skills into project folders. The kit remains the editable source; these copies do not automatically synchronize when you change the kit.

| File | What it does |
|---|---|
| [adapters/codex/README.md](adapters/codex/README.md) | Explains the Codex project layout and preparation steps. |
| [adapters/cursor/README.md](adapters/cursor/README.md) | Explains the Cursor project layout and preparation steps. |
| [adapters/claude/README.md](adapters/claude/README.md) | Explains the Claude Code layout and shared-policy import. |
| [adapters/claude/CLAUDE.md](adapters/claude/CLAUDE.md) | A tiny @AGENTS.md import so Claude can read the shared project policy. |

## 7. scripts/ — the five executable helpers

These are Python programs. Nothing runs merely because the files exist. Setup previews by default; applying setup and executing project checks are explicit actions.

| File | What it does |
|---|---|
| [scripts/doctor.py](scripts/doctor.py) | Reports the local environment and whether selected tools are on PATH. Does not install tools or prove their configurations work. |
| [scripts/prepare_client.py](scripts/prepare_client.py) | Previews copying the policy and 12 core skills into an existing project. With --apply it creates those files, selected optional skills and a receipt. Refuses conflicting existing contents; identical files are left alone. Guards against duplicate skill discovery and path escape. Does not configure Cognee or global client settings. |
| [scripts/run_checks.py](scripts/run_checks.py) | Reads a checks JSON file and previews its commands. With --run it executes them and reports failures/timeouts. Uses argument arrays without shell interpolation; the programs it runs still have their normal permissions. |
| [scripts/validate_memory.py](scripts/validate_memory.py) | Checks curated memory records for required fields, types and supported values. Does not establish whether a statement is true or send it to Cognee. |
| [scripts/validate_kit.py](scripts/validate_kit.py) | Checks skill counts/frontmatter, structured files, the example memory and delivered-file hashes. Does not prove the AI follows instructions or a client loads them correctly. |

## 8. memory/ — portable records plus your Cognee connection recipe

There are two separate parts: a convention for carefully reviewed facts, and examples for connecting clients to Cognee. The convention is not Cognee’s native storage schema, and no importer, database or running server is included.

| File | What it does |
|---|---|
| [memory/README.md](memory/README.md) | Explains reviewed intake, retention and the split between portable records and the chosen Cognee backend. |
| [memory/record.schema.json](memory/record.schema.json) | Defines a portable record: identity, namespace, kind/status, statement, source, dates, confidence, supersession, review/expiry, sensitivity and links. This is the contract for the kit’s records. |
| [memory/examples/preference.json](memory/examples/preference.json) | A synthetic example of a preference record. It is demonstration data, not a claim about your real preferences. |
| [memory/cognee/README.md](memory/cognee/README.md) | Lists setup choices and an upstream-documented server command, then acceptance checks for connecting multiple clients. It is a recipe, not a completed installation. |
| [memory/cognee/MAPPING.md](memory/cognee/MAPPING.md) | Explains how portable record concepts could map to Cognee ingestion, datasets, sources, corrections and deletion. This design has no implemented importer; a dataset label alone is not access control. |
| [memory/cognee/.env.example](memory/cognee/.env.example) | An entirely commented worksheet for model/provider/embedding settings. No credentials or model choice is supplied. Copying it alone will not configure a working system. |
| [memory/cognee/claude.mcp.example.json](memory/cognee/claude.mcp.example.json) | An unapplied Claude MCP connection example pointing to the proposed local Cognee endpoint. |
| [memory/cognee/cursor.mcp.example.json](memory/cognee/cursor.mcp.example.json) | An unapplied Cursor MCP connection example for that same endpoint. |
| [memory/cognee/codex.config.example.toml](memory/cognee/codex.config.example.toml) | An unapplied Codex MCP example, disabled by default. None of these fragments starts the server or supplies endpoint authentication. |

## 9. model-profiles/ — how much work to give a model

These describe task scope and when to escalate. They are planning data, not a live router, subscription, model download or native client setting.

| File | What it does |
|---|---|
| [model-profiles/README.md](model-profiles/README.md) | Explains using the profiles while keeping teaching and safety expectations consistent. |
| [model-profiles/lightweight.json](model-profiles/lightweight.json) | A narrow task profile for simpler work with clear escalation boundaries; model_id is intentionally unset. |
| [model-profiles/standard.json](model-profiles/standard.json) | A profile for ordinary implementation work; model_id is intentionally unset. |
| [model-profiles/frontier.json](model-profiles/frontier.json) | A profile for harder reasoning and broader uncertainty; model_id is intentionally unset. |

## 10. setup/ — putting the pieces into use

Read these as staged guidance. The software inventory is not a request to install everything.

| File | What it does |
|---|---|
| [setup/CLIENTS.md](setup/CLIENTS.md) | Project destinations, preview/apply instructions, handling existing files and duplicates, and client smoke checks. Codex/Cursor use .agents/skills; Claude uses .claude/skills. |
| [setup/PHASES.md](setup/PHASES.md) | A gradual adoption order: foundation, engineering workflows, visual/custom voice work, Cognee, safety checks, improvements and optional specialties. |
| [setup/WSL.md](setup/WSL.md) | Windows/WSL environment planning and tool placement. It does not create a Linux environment. |
| [setup/CHECKS.md](setup/CHECKS.md) | How to choose and run appropriate checks, including optional scanners and avoiding accidental downloads. |
| [setup/software.json](setup/software.json) | A structured inventory of referenced software, categories and source links, now reflecting Cognee and your custom voice project. It is not a package-manager lockfile or installer. |

## 11. templates/ — worksheets you copy into actual projects

Most are blank Markdown forms: copy one when the task calls for it and replace its prompts with real information. The two checks JSON files are executable command configurations when explicitly passed to run_checks.py --run.

| File | What it does |
|---|---|
| [templates/adr.md](templates/adr.md) | Records a consequential architecture decision, its rationale, alternatives and consequences. |
| [templates/architecture.md](templates/architecture.md) | Documents components, data and boundaries, with an editable Mermaid diagram example. |
| [templates/checks.python.json](templates/checks.python.json) | Example Python check commands for Ruff, mypy and pytest through an already prepared uv environment. Requires the matching project tools and paths. |
| [templates/checks.web.json](templates/checks.web.json) | Example web check commands for local TypeScript and Playwright installations. Requires the matching project structure; avoids a download-on-demand command. |
| [templates/client-smoke-test.md](templates/client-smoke-test.md) | A manual check that a real coding client discovers the prepared instructions and behaves as expected. |
| [templates/context-budget.md](templates/context-budget.md) | Plans which instructions, code and retrieved memories belong in a task and keeps retrieval bounded. |
| [templates/controlled-update.md](templates/controlled-update.md) | Records why to update a dependency/tool, the proposed change, checks and rollback. |
| [templates/debug-log.md](templates/debug-log.md) | Tracks reproduction steps, hypotheses, experiments, the cause and verification. |
| [templates/dependency-budget.md](templates/dependency-budget.md) | Tracks packages, transitive dependencies, services/providers and their costs. |
| [templates/dependency-decision.md](templates/dependency-decision.md) | Justifies one proposed dependency, including alternatives and an exit plan. |
| [templates/feature-spec.md](templates/feature-spec.md) | Defines user behavior, scope, exclusions and acceptance criteria for one feature. |
| [templates/implementation-plan.md](templates/implementation-plan.md) | Lists small implementation steps, affected files, dependencies and checks. |
| [templates/learning-event.json](templates/learning-event.json) | Structured example of a candidate learning event. Replace sample content with evidence; it is not automatically accepted into memory. |
| [templates/learning-note.md](templates/learning-note.md) | A human-readable reflection on what you learned, in your own words, with a revisit prompt. |
| [templates/legal-triage.md](templates/legal-triage.md) | Records applicability questions, claims and primary sources without pretending a checklist establishes legal compliance. |
| [templates/release-checklist.md](templates/release-checklist.md) | Tracks readiness, verification, required authorization and recovery for a release. |
| [templates/review-request.md](templates/review-request.md) | Gives a reviewer the scope, change context and evidence needed for a useful review. |
| [templates/threat-model.md](templates/threat-model.md) | Lists actors, trust boundaries, misuse cases and proposed controls. |
| [templates/ui-brief.md](templates/ui-brief.md) | States the UI question, users, states and criteria a prototype should resolve. |
| [templates/verification.md](templates/verification.md) | Records what was actually checked, on which revision, with results and remaining limits. |
| [templates/voice-trial.md](templates/voice-trial.md) | Tests your future voice app against phrases, negations, paths, pauses, corrections and latency. This is a test worksheet, not audio-processing code. |

## 12. evals/ — checking whether the AI workflow helps

These evaluate assistant behavior, separately from the Python helper tests. They require actual trial runs and human assessment; no model benchmark has been run for you.

| File | What it does |
|---|---|
| [evals/README.md](evals/README.md) | Explains baseline-versus-candidate trials, grading and keeping some cases held out. |
| [evals/cases.json](evals/cases.json) | 16 prompts with criteria covering teaching, restraint, debugging, verification, privacy, memory, migrations and voice transcription errors. |
| [evals/result-template.json](evals/result-template.json) | A blank result record marked not_run, with unfilled metrics. Copy it for an actual trial. |
| [evals/fixtures/task_app.py](evals/fixtures/task_app.py) | Intentionally flawed sample code for evaluation: ownership is not enforced and an empty collection can cause division by zero. Do not reuse it as production code. |

## 13. tests/ — testing the helper programs

These checks concern the kit’s local mechanics, not the quality of an AI model.

| File | What it does |
|---|---|
| [tests/test_helpers.py](tests/test_helpers.py) | 16 deterministic tests covering preview/apply behavior, conflicts, optional skills, path safety, check execution and memory validation. Uses temporary folders and no network. The recorded run has 15 passes and one skipped symlink test because Windows did not allow creating that link. |

## 14. docs/research/ — the report you already read

Preserved as a historical research snapshot. Its old Basic Memory and Handy recommendations are superseded by DECISIONS.md, rather than silently rewriting the original research.

| File | What it does |
|---|---|
| [docs/research/README.md](docs/research/README.md) | Explains that historical status and points to your current decisions. |
| [docs/research/ai-development-system-report.md](docs/research/ai-development-system-report.md) | The full original research report in editable plain text. |
| [docs/research/ai-development-system-report.html](docs/research/ai-development-system-report.html) | The same report formatted for browser reading. |
| [docs/research/research-audit.md](docs/research/research-audit.md) | The research audit in plain text, including evidence and limitations. |
| [docs/research/research-audit.html](docs/research/research-audit.html) | The browser-readable version of that audit. |

## What appears in a project after preparation

The helper creates a project AGENTS.md, copies the 12 core skills plus explicitly selected specialists into the chosen client location, and writes `.ai-dev-system/<client>.json` as a preparation receipt. Claude also gets the small CLAUDE.md import. The receipt records the kit version and copied-file hashes. These are generated project files, so they are not extra source files in this kit.

Existing conflicting files stop preparation instead of being replaced. Editing this library later does not update project copies automatically; inspect and reconcile differences. Cognee connection examples are a separate manual setup step.

## A sensible first pass

Read START-HERE.md and setup/CLIENTS.md, then preview preparation for one existing project. Inspect the proposed files before applying. Run the client smoke-test worksheet. Start using the core workflows; copy templates as useful. Set up and test Cognee separately using synthetic records first. Develop your voice app as its own project using the voice workflow and trial worksheet.

The original report and previous ZIP remain reference snapshots. Use this version’s DECISIONS.md for the current memory and voice choices. See VALIDATION.md for the exact verification boundaries.
