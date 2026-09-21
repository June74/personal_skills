# A small AI development system that teaches you

**Research date: September 20, 2026.** Prepared for a junior developer using Windows, WSL/Ubuntu, Cursor, Claude Code, and Codex.

This is a design and research report, not an installation. “Recommended” expresses my judgment for your profile. Linked capability, licensing, and release statements come from primary sources inspected during this research. The custom skills are proposed work, and the recommended Basic Memory integration has not been tested in your environment.

Read sections 1, 3, 5, and 20 first. The remaining sections explain the choices and their dependencies. The companion research audit preserves more detailed source-file findings without turning the recommended stack into a shopping list.

Freshness has limits: a page retrieved today may still describe an older release; `main` and `develop` can contain unreleased features. Release evidence is labeled separately. I have not installed the candidates, benchmarked their token consumption, or certified every transitive dependency as safe. Exact resolved dependency counts require the eventual lockfiles and target platform.

## 1. Executive Recommendation

**Build a small, versioned collection of engineering procedures around the coding clients you already use. Begin with no new memory server, no agent framework, and no mandatory paid service.** Use one client to lead each change. Use a second client for an independent review only when the risk justifies it.

Your most valuable addition is a mentoring contract: the AI explains the next small step, names the files and their responsibilities, shows the architecture when needed, explains new dependencies, verifies its work, and asks you to explain an important decision back in your own words. This behavior matters more than installing another collection of expert personas.

```text
YOU: explain the problem → sketch → predict → critique → explain back
                              │
                  one active coding client
                 Cursor / Claude Code / Codex
                              │
                 shared rules + 12 small skills
                              │
           design → plan → tests → code → verification
                              │
            local terminal + browser + project tools
                              │
           reviewed notes → shared memory, added later
```

My defaults are **WSL2 + Ubuntu 24.04 LTS, Git, uv-managed Python, Node 24 LTS with npm when web tooling is needed, pytest, Ruff, mypy, and Playwright**. Most application choices stay inside the application, not in your global AI environment. Ubuntu 24.04 is a conservative compatibility choice, not a claim that it is the newest Ubuntu. Node’s current release table identifies 24 as LTS and 26 as Current. [Microsoft WSL guidance](https://learn.microsoft.com/en-gb/windows/wsl/setup/environment), [Ubuntu 24.04](https://releases.ubuntu.com/24.04/), [Node release policy](https://nodejs.org/en/about/previous-releases).

For sketches, start with paper or Excalidraw and disposable HTML/CSS. Add Penpot only when editable design systems and collaboration become useful. For voice, try Handy on Windows with a local model. For shared memory, start with curated files; pilot Basic Memory as one local MCP endpoint in phase 3. It has a heavier package footprint than its simple storage model suggests, but avoids making you maintain a custom protocol server. A graph database is unnecessary at your initial scale.

**Expected additional recurring software cost: $0 for the local foundation**, beyond whichever AI subscriptions you already choose, existing hardware, electricity, and backups. Hosted model calls, production hosting, email delivery, domains, and app-store accounts are separate costs. Local storage does not make a cloud coding model private: any retrieved memory inserted into its prompt can leave your computer.

## 2. My Capability Map

The numbered groups cover all 54 categories in your brief. “Core” means a routinely available procedure; it does not mean every tool or full skill body is loaded every session.

| Capability | Needed? | Core / On-demand | Best choice | Why |
|---|---|---|---|---|
| 1–3 Requirements, planning, specification | Yes | Core | Clarify/specify + short implementation plan | Make acceptance criteria visible before coding |
| 4–5 System design, architecture | Yes | Core, depth varies | One component diagram, data model, failure cases, short ADR | Teach boundaries without defaulting to distributed systems |
| 6–8 UI, prototypes, sketch-to-UI | Yes | Core for UI work | Sketch → local HTML → screenshot critique | Fast visual feedback with minimal setup |
| 9 Frontend engineering | Yes | Project-specific | HTML/CSS/JS first; React + TypeScript + Vite for substantial app state | Match complexity to the product |
| 10–11 Backend, Python | Yes | Project-specific | Python + FastAPI for APIs; Django for integrated business apps | Avoid assembling an authentication/admin platform unnecessarily |
| 12 JavaScript/TypeScript | Yes | Project-specific | Node LTS + npm; TypeScript when the UI grows | One package-manager convention |
| 13–14 Databases, API design | Yes | Core procedure; packages on demand | SQLite for local apps; PostgreSQL for shared production data; OpenAPI | Learn constraints, transactions, ownership, and contracts |
| 15–16 Security, legal awareness | Yes | Tiny rule + triggered skill | Threat/risk triage + scanners + current official research | Prompts alone cannot enforce security or establish law |
| 17–19 TDD, testing, browser/E2E | Yes | Core | pytest; Playwright; Vitest only for meaningful JS logic | Separate logic, integration, visual, and user-flow evidence |
| 20 Debugging | Essential | Core | Reproduce → evidence → hypothesis → regression | Prevent random patching |
| 21–23 Review, refactoring, code structure | Essential | Core; deeper audit on demand | Independent review + responsibility map; import checks later | Catch design problems as they become concrete |
| 24–25 Documentation, research | Yes | Core habit; specialist when useful | README, ADRs, dependency records, dated primary sources | Keep knowledge beside the code |
| 26–28 AI/ML, RAG, LLM evaluation | Sometimes | On-demand | Plain SDK calls + evaluation fixtures; retrieval baseline before vectors | Establish value before adding orchestration |
| 29–30 Deployment, DevOps | Yes when shipping | On-demand | One application + one database; local scripts before CI | Learn deploy, rollback, backups, logs, and secrets |
| 31–32 Mobile and store releases | Sometimes | On-demand | React Native/Expo if React skills transfer; official store checklists | Store policies and native builds add their own dependencies |
| 33–34 Unity, Blender | Occasionally | On-demand only | Editor tests/profilers; Blender Python; narrowly scoped MCP when useful | Large permissions and toolchains should not become global defaults |
| 35 Linux/WSL learning | Yes | Core mentoring | Bash + man/help; ShellCheck for scripts | Explain actual commands as they appear |
| 36 Voice | Desired | Optional host app | Handy, local model, push-to-talk | Keeps microphone integration on Windows |
| 37 Diagrams | Yes | Core habit | Mermaid text or Excalidraw | A diagram can be a file, not another server |
| 38–39 Shared memory, knowledge graphs | Yes, staged | Phase 3 | Curated files → SQLite FTS + explicit relationships | Relational rows can represent a small graph |
| 40 Interoperability | Essential | Core | Agent Skills + common scripts + small adapters | Shared knowledge, separate client permissions |
| 41–44 Learning, evolution, evals, model adaptation | Yes, later | Manual review first | Git + learning-event records + fixture-based evals | Improve from evidence, never self-rewrite silently |
| 45–46 Context and MCP security | Essential | Core policy | Narrow retrieval, selective skills, allowlisted tools | Minimize both prompt noise and authority |
| 47–52 Dependency discovery, management, packages, security, updates, visualization | Essential | Core skill + local tools | uv/npm, lockfiles, OSV, dependency records, tree commands | Every addition must have a reason |
| 53–54 Licensing and supply chain | Essential | Triggered review | License evidence + provenance + reviewed installs | “Open source” does not mean no obligations |
| Accessibility | Yes | Core design/test criterion | Keyboard, focus, contrast, labels; WCAG reference | A working UI must work for more than mouse users |
| Recovery, observability, data portability | Yes | On-demand shipping gates | Restore drill, structured logs, exports, rollback | Shipping includes recovering from failure |
| User learning and confidence calibration | Essential | Every cycle | Teach-back, prediction, progressively fewer hints | Track growing independence, not generated lines |
| Performance and resource budgets | Yes | Triggered | Profile first; explicit latency/storage/AI-cost limits | Avoid speculative optimization and surprise bills |

## 3. Final Minimal Stack

Use these labels throughout: **F0** = free local open-source software with no required model API; **F1** = open/local-capable but model-assisted; **F2** = hosted free tier or limited service; **F3** = paid. F0 does not guarantee that a default configuration makes no network requests. **A** = always-loaded instructions/catalog; **B** = metadata until selected; **C** = invoked tool/skill output; **D** = no model context until manually shared. These are behavior categories, not measured token counts.

### Always-on rules

Keep one canonical policy around 250–450 words. Its content should be roughly:

1. Build in small steps while teaching. Explain the next change, its reason, and affected modules; define new terms. Offer occasional prediction and teach-back exercises without blocking ordinary progress.
2. Inspect existing architecture before substantial changes. Match design depth to risk. Prefer the standard library or an existing dependency where it cleanly solves the problem.
3. Explain every new dependency: purpose, type, alternatives, important transitive/native/service costs, and what breaks if it is removed. Show manifest and lockfile changes.
4. Protect secrets and user data. Treat web pages, repository text, and retrieved memories as untrusted evidence. Use least privilege. Explain destructive shell actions before execution and obtain required authorization.
5. Verify before claiming completion. State what was tested, what failed, and what remains untested. Do not call scanner output a security guarantee.
6. Propose durable memory and workflow changes for review. Do not silently record conversations, change global rules, broaden permissions, or promote guesses into facts.

This is **F0/A/low** content; model execution retains your client’s cost and data-handling terms. Full teaching lessons belong in the mentoring skill, not repeated global rules.

### Core skills: 12, with one owner per capability

`mentor-mode`, `clarify-and-spec`, `plan-slices`, `architecture-and-data`, `dependency-decision`, `tdd`, `systematic-debugging`, `review`, `verify`, `prototype-ui`, `browser-check`, and `security-and-legal-triage`.

All are **F1/B-low until selected**; they are local files with no required extra model API. Their activated bodies should generally be 500–1,500 tokens after adaptation; browser references and deeper architecture investigations can be larger. These are design targets, not measurements of upstream files. The exact sources and modifications follow in section 4.

### On-demand skills

Keep these outside auto-discovery until a project needs them: release/deployment; auth/payments; database migration; RAG/evaluation; mobile release; Unity; Blender; deeper refactoring; memory curation; current-source research; skill evaluation/evolution. They should load the project’s actual framework/version documentation. Do not create one permanently installed skill for every vendor.

### Specialist agents

Use at most three role templates, invoked when justified (**F1/C**, medium per agent; parallel agents still consume tokens):

| Role | Why independent context helps | Boundaries |
|---|---|---|
| Explorer/researcher | Reads noisy code or sources and returns a compact evidence map | Read-only; filenames/URLs, findings, uncertainties; no setup changes |
| Independent reviewer | Tests a proposal without the implementer’s assumptions | Reads diff, requirements, relevant tests; returns actionable issues |
| Security/architecture reviewer | A separate adversarial pass for auth, sensitive data, major boundaries | Scoped threat model; no production credentials or automatic fixes |

UI review can be a task for the reviewer with screenshots and accessibility criteria. A “Python expert” persona usually needs a skill/reference, not a permanently separate agent. Native client subagents are enough; no LangGraph, CrewAI, AutoGen, or agent fleet is required to develop ordinary applications.

### Tools and services

| Layer | Recommendation | Load/cost |
|---|---|---|
| Shell and source control | Git, Bash, ripgrep, existing editor; normal help/man pages | F0/C-low |
| Python | uv + one project Python; pytest, Ruff, mypy in dev groups | F0/C-low, larger failures only on demand |
| Web | Node 24 LTS + bundled npm when needed; project-local tooling | F0/C-low |
| Browser | Playwright CLI + curated skill for exploration; Playwright Test for repeatable tests | F0 tool/F1 skill; C-low to high for snapshots/images |
| Security | Gitleaks + OSV-Scanner; Ruff selected security rules | F0/C-low; vulnerability data needs updates |
| Sketch/design | Paper/Excalidraw + local HTML; Mermaid text | F0/D until shared |
| Voice | Handy on Windows, selected local speech model | F0/D until transcript enters chat |
| MCP | **Zero required initially**; later one shared memory endpoint | Catalog cost A or deferred, client-dependent; outputs C |
| Background services | **Zero required initially** | App/browser servers run only while needed |
| Memory | Reviewed Markdown/JSON records; SQLite service only in phase 3 | F0 storage; F1 agent-assisted curation |
| Local model | Optional Ollama, local-only mode; no default model download | F1; hardware and model-license constraints |

The source evidence for visual and memory choices appears in sections 6 and 9 and the companion audit. Core language, package, and scanner documentation is linked in sections 12–18.

### One source of truth, with client adapters

```text
~/ai-dev-system/                 private versioned configuration repository
├── skills/                     the 12 selected/adapted skill directories
├── specialist-library/         not automatically discovered
├── agents/                     3 short role definitions
├── rules/core.md               source for tiny client-visible instructions
├── adapters/{claude,codex,cursor}/
├── scripts/                    the same deterministic checks for every client
├── evals/                      task fixtures, assertions, baseline results
├── model-profiles/             routing and work-size settings
└── sources.lock.json           upstream URL, commit, license, audit date

~/.local/share/ai-dev-memory/    private data; separate from distributable skills
~/projects/<project>/docs/      requirements, architecture, ADRs, decisions
```

The separate memory directory avoids accidentally publishing personal facts with configuration. A repository named `memory/` may contain schemas and examples; private live records should not be committed there by default.

| Mechanism | Claude Code | Codex | Cursor | Portable choice |
|---|---|---|---|---|
| Skills | `.claude/skills`, `~/.claude/skills`; symlink folders supported | `.agents/skills`, `~/.agents/skills`; symlink folders supported | `.agents/skills` and `.cursor/skills`; also compatibility directories | One canonical body; publish/link selected folders into discovered locations |
| Rules | `CLAUDE.md`; current AGENTS support has version/configuration caveats | `AGENTS.md`, scoped guidance | `AGENTS.md`, `.cursor/rules` | Project `AGENTS.md`; minimal Claude import where necessary |
| MCP | stdio and HTTP configuration | stdio and Streamable HTTP configuration | stdio, SSE, Streamable HTTP | Same server/protocol; separate small configuration files |
| Hooks | Claude-specific events/config | Current Codex supports lifecycle hooks and explicit hook trust | Cursor events/config | Shared executable checks, translated event wrappers |
| Subagents/plugins | Native configuration and packaging | Native configuration and packaging | Native configuration and packaging | Share task contracts, not assumed identical manifests |

These capabilities are documented, but do not imply every tool-specific frontmatter field or permission has identical semantics. The Agent Skills standard defines a portable file shape; `allowed-tools` remains implementation-dependent. [Agent Skills specification](https://agentskills.io/specification), [Claude skills](https://code.claude.com/docs/en/skills), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Cursor skills](https://cursor.com/docs/skills).

Use individual symlinks inside WSL for clients running there. Cursor can discover several compatibility directories, so check its skill inventory for duplicates rather than copying skills into every supported location. If a Windows-hosted client cannot resolve Linux paths, generate a read-only snapshot from the canonical source and record its hash; never edit both copies. Cloud clients require an explicit deployment/sync path and cannot be assumed to see your home directory. [Cursor discovery and sync behavior](https://cursor.com/docs/skills).

For Claude, a small `CLAUDE.md` containing `@AGENTS.md` remains a documented compatibility fallback. Current direct `AGENTS.md` support depends on version, built-in plugin, and feature-flag conditions; privacy configurations can affect availability. Do not rely on the fallback-free path without testing. [Claude memory/instruction documentation](https://code.claude.com/docs/en/memory).

Do not follow old advice that Codex lacks hooks: current official documentation describes `hooks.json` or inline configuration and requires trust of changed non-managed hooks. Start with no AI lifecycle hooks anyway. Use explicit checks, then a Git pre-commit check if useful. Git hooks are local conveniences; repeat required checks in CI because hooks can be bypassed. [Codex hooks](https://learn.chatgpt.com/docs/hooks), [Claude hooks](https://code.claude.com/docs/en/hooks), [Cursor hooks](https://cursor.com/docs/hooks).

**Adapter acceptance test:** each client discovers each selected skill once, explains the same core policy, runs the same check script in the same project, reports a deliberate failing test, and cannot read an unrelated private directory through the memory tool. Record the tested client versions. That is the evidence needed before calling the setup interoperable.

## 4. Exact Skill Selection

**These are twelve proposed local adaptations, not twelve unmodified installations.** Store each under `~/ai-dev-system/skills/<name>/SKILL.md`. Preserve upstream license notices and record the reviewed commit in `sources.lock.json`. The links below identify the actual source files inspected; a link to `main` is a reference, not a version pin. No reviewed source covered your entire dependency-teaching or legal-triage requirement, so those two are explicitly custom.

Every skill has B/low discovery cost. The table estimates **activated** cost after curation; costs include only skill instructions, not the eventual code, images, research, or tool results. None needs another model subscription by itself.

| Skill | Repo and exact file/path | Adopt/Adapt | Trigger | Active context | Actual behavior, useful part, and required change |
|---|---|---|---|---|---|
| `mentor-mode` | Matt: [skills/productivity/teach/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) | **ADAPT** | Meaningful development/learning step | Low–medium | Upstream creates a multi-session course with retrieval practice. Keep prediction, explanation and spaced revisits; embed them in real project work instead of generating a course workspace for every edit. Upstream explicit teaching trigger needs adaptation for routine mentoring. |
| `clarify-and-spec` | Matt: [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md), [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md), [to-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md) | **ADAPT**, merge | New feature, ambiguous requirement | Low–medium | Resolves decision dependencies, defines vocabulary, synthesizes requirements. Bound questions to decisions that affect the result; recommend defaults; write one acceptance spec. Use ADRs only for consequential tradeoffs. |
| `plan-slices` | Superpowers: [skills/writing-plans/SKILL.md](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) | **ADAPT** | Agreed scope needs several changes | Low–medium | Identifies files, responsibilities and test steps. Remove required full implementation code in plans and mandatory framework/subagent handoffs. Plan outcomes and interfaces so the plan does not become a second copy of the program. |
| `architecture-and-data` | Matt: [skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md) | **ADAPT** | New app, significant boundary/data change, refactor | Medium | Uses module interfaces and testability to reason about design. Add data model, API contract, failure paths, trust boundaries and one diagram; remove rigid vocabulary bans and automatic multiple design agents. |
| `dependency-decision` | **Custom proposed:** `skills/dependency-decision/SKILL.md` | **ADAPT/create** | Before a meaningful dependency addition, replacement or upgrade | Low + research | Apply sections 12–16: capability first, existing/standard-library option, default vs alternative, dependency types, manifest/lock change, maintenance/license/advisory evidence, removal consequence and rollback. |
| `tdd` | Matt: [skills/engineering/tdd/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md), [tests.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/tests.md), [mocking.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/mocking.md) | **ADAPT** | Behavior change or reproducible bug | Low–medium | One vertical slice, behavioral assertions, independent expected values. Current upstream defers refactoring to review; restore your **red → green → refactor** loop. Avoid tests that merely repeat implementation. |
| `systematic-debugging` | Superpowers: [skills/systematic-debugging/SKILL.md](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md), [root-cause-tracing.md](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/root-cause-tracing.md); Matt [diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md) | **ADAPT**, merge | Unexpected result or failing check, before patching | Medium | Reproduce, trace, compare, test a hypothesis, fix cause. Merge Matt's tight feedback loop. Replace environment-dumping examples with redacted/presence-only checks. Do not copy the Bash/npm helper unchanged. |
| `review` | Superpowers: [requesting-code-review/SKILL.md](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md), [code-reviewer.md](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/code-reviewer.md) | **ADAPT** | Meaningful diff, risky feature, merge | Low + reviewer C/medium | Send requirements, bounded diff and evidence to a fresh reviewer. Keep severity and file/line evidence. One useful review per change; support uncommitted diffs and enforce read-only review tools. |
| `verify` | Superpowers: [verification-before-completion/SKILL.md](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | **ADAPT** | Before claiming a task is complete | Low | Requires execution evidence rather than confidence. Keep revision-aware test/build/runtime evidence and untested limits. Avoid rerunning unchanged checks just because another message is sent. |
| `prototype-ui` | Matt [prototype/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md), [UI.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/UI.md), [LOGIC.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/LOGIC.md); Anthropic [frontend-design/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md); Impeccable [entry skill](https://github.com/pbakaus/impeccable/blob/main/.agents/skills/impeccable/SKILL.md) | **ADAPT**, merge | New or changed UI, including production redesign/polish | Medium; screenshots extra | Intentional design and critique; disposable HTML alternatives when a visual question needs exploration. Keep typography, hierarchy, accessibility and realistic states. Mine Impeccable references; omit its full engine/hooks and long critique workflow. |
| `browser-check` | Microsoft: [skills/playwright-cli/SKILL.md](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md) | **ADAPT** | Inspect UI, console/network, forms, responsive layout or screenshot | Low–medium; page-dependent | Operates named browser sessions, snapshots, screenshots and traces. Remove broad npm/npx permission grants and automatic global `@latest` installation. Pin versions, scope output, use test accounts, and keep exploration separate from saved regression tests. |
| `security-and-legal-triage` | **Custom proposed:** `skills/security-and-legal-triage/SKILL.md`; [OWASP ASVS](https://github.com/OWASP/ASVS), [MCP security guidance](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) | **ADAPT/create** | Auth, personal data, public input, payments, uploads, external tools, release | Medium + current research | Identify threat/data flow, select checks and current legal sources, classify uncertainty and escalation. Never claim certification or store legal rules as timeless facts. |

**Dependencies and overlap:** the first nine use existing file/terminal/Git tools; TDD and verification invoke the project's existing test tools. Design needs a browser, browser-check needs the Playwright toolchain, and security triage invokes the selected scanners only when relevant. Architecture owns module/data/API explanations; mentoring owns how they are taught; planning owns execution order. Review reasons independently; verification establishes what actually ran. This division prevents three skills from producing three competing plans.

Important support-file findings: Superpowers' inspected `find-polluter.sh` assumes Bash and `npm test`, splits filenames on whitespace and suppresses test output; it is **REFERENCE ONLY**. Matt's interactive HITL template echoes supplied values, so it must not collect secrets. Codebase-design's deeper referenced design files were identified but not fully audited; do not copy them automatically. Anthropic's frontend skill is a short prose skill; its individual license is Apache-2.0, while the repository as a whole has mixed licensing. [Debug helper](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/find-polluter.sh), [HITL template](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh), [Anthropic repository licensing](https://github.com/anthropics/skills#about-this-repository).

### On-demand material worth retaining as a library

| Source and exact path | Classification | When useful / dependency and context implications |
|---|---|---|
| Anthropic [skills/skill-creator/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | **ADAPT** | Phase 5 eval methodology. Its `run_eval.py` invokes Claude-specific commands, so Codex/Cursor require adapters. Python and model calls; C/medium–high. Use safe text/JSON review rather than the unchanged HTML viewer. |
| ECC [skills/continuous-learning-v2/SKILL.md](https://github.com/affaan-m/ECC/blob/main/skills/continuous-learning-v2/SKILL.md) | **REFERENCE ONLY** | Evidence-linked small learning candidates. Bash/Python and Claude hooks/background assumptions make it nonportable unchanged. Keep manual events; no blanket observation hooks. |
| Compound [skills/ce-compound/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/main/skills/ce-compound/SKILL.md) | **REFERENCE ONLY** | Its filter for verified, non-obvious lessons is useful. One lesson, update existing errors, avoid duplicating recoverable code facts. Do not load its whole workflow for this policy. |
| wshobson [python-testing-patterns/SKILL.md](https://github.com/wshobson/agents/blob/main/plugins/python-development/skills/python-testing-patterns/SKILL.md) | **REFERENCE ONLY** | Look up fixtures, async/database testing after an actual need. Example plugins are optional; no arbitrary 80% coverage gate. |
| K-Dense [skills/scikit-learn/SKILL.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scikit-learn/SKILL.md) | **REFERENCE ONLY** | Classical ML project: pipelines, metrics and leakage. Installing `scikit-learn` (import name `sklearn`) brings NumPy/SciPy; unrelated scientific packages remain absent. References/scripts not fully audited. |
| Understand Anything [understand/SKILL.md](https://github.com/Egonex-AI/Understand-Anything/blob/main/understand-anything-plugin/skills/understand/SKILL.md) | **REFERENCE ONLY initially** | Unfamiliar large repository where a persistent interactive map earns its cost. Seven-phase workflow, many reads/agents, parser/build dependencies; high first-run context. Adapt automatic output/build/update behavior first. |

Use source directories as a specialist index, not a startup manifest. An agent earns its separate context only when it can independently explore or challenge a bounded question:

| Candidate inspected | Decision | Why an agent, or why not |
|---|---|---|
| Agency [engineering-codebase-onboarding-engineer.md](https://github.com/msitarzewski/agency-agents/blob/main/engineering/engineering-codebase-onboarding-engineer.md) | **ADAPT** into explorer | Many noisy reads can be compressed into a cited map. Small repositories use the architecture skill instead. Remove persona claims of memory. |
| Superpowers reviewer above | **ADAPT** into independent reviewer | Independent assumptions and fresh context help reveal missed behavior. |
| VoltAgent [security-auditor.md](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/security-auditor.md) | **REFERENCE** for threat reviewer | Independent adversarial pass for high-risk changes. Remove fictional context-manager dependencies, template metrics and implied compliance guarantees. |
| Agency [engineering-mobile-release-engineer.md](https://github.com/msitarzewski/agency-agents/blob/main/engineering/engineering-mobile-release-engineer.md) | **REFERENCE**, usually a skill | Signing/store checklist needs current facts, not continuous autonomy. Independent audit only before a consequential release; no automatic fastlane install. |
| VoltAgent [architect-reviewer.md](https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/architect-reviewer.md) | **SKIP unchanged** | Inspected permissions include writing/editing and its breadth exceeds your default needs. Use your architecture skill and read-only reviewer. |

### Planning: one light path and one deeper path

These judgments concern fit, not universal quality. The maintenance appendix records dated activity and known limitations.

| Approach | Planning quality / learning value | Context and complexity | Portability / solo fit | Decision |
|---|---|---|---|---|
| Matt discovery + compact Superpowers plan | Strong questions, explicit files and testable slices; good teaching after adaptation | Low–medium | Plain Markdown, excellent small solo fit | **Default** |
| Full Superpowers | Disciplined end-to-end process; more prescribed execution | Medium–high | Client-specific integrations; useful if the complete method is intentionally chosen | Mine selected parts |
| [Spec Kit](https://github.com/github/spec-kit) | Strong specification/requirements traceability | Medium–high; generated workflow artifacts | Multi-agent integrations; useful for larger requirements-heavy work | Borrow templates for deeper path |
| [ECC](https://github.com/affaan-m/ECC) | Broad practical procedures and learning machinery | High if broad rules/hooks are enabled | Adapters exist, behavior still client-dependent | Reference individual ideas |
| [BMAD](https://github.com/bmad-code-org/BMAD-METHOD) | Structured product roles and lifecycle | High | More process than a solo small feature needs | Skip default install |
| [GSD Core](https://github.com/open-gsd/gsd-core) | Persistent phases and execution management | Medium–high | Another workflow owner; current migrated home | Reference if managing a long project becomes difficult |
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | Good feedback-to-learning emphasis | Medium–high depending on modes | Current skills-first structure; additional conventions | Borrow durable-learning filter |

| Task | Appropriate depth and artifacts |
|---|---|
| Tiny task | State outcome and relevant check; edit; verify. No formal document. |
| Small feature | Short acceptance spec, sketch if visual, 3–7 vertical slices, tests. |
| Large feature | Requirements/risks, component and data diagrams, API/state contracts, dependency decisions, milestones, rollout/rollback; independent review. |
| New application | One-page product brief, threat/data map, one walking skeleton from UI to database, then feature slices. Estimate users/data/latency before choosing infrastructure. |
| Major refactor | Map current dependencies, characterize existing behavior, define target boundary, migrate incrementally; preserve externally visible behavior. |
| Unknown/research problem | Time-boxed experiment, primary sources, alternatives, explicit success/failure criterion; decide after evidence. |
| Bug | Reproduce → minimize → observe → hypothesis → instrument → test → root cause → fix → regression → explanation. No speculative rewrite. |

The deeper path uses the same skills and files; it does not require another orchestration framework. Add queues, caches or services only when an identified load, latency, reliability or asynchronous-work requirement explains them. Record the simpler alternative and what evidence would justify revisiting it.

## 5. What NOT to Install

| Overlapping capability or attractive addition | Keep | Skip / reason |
|---|---|---|
| Multiple discovery/planning systems | Clarify/spec + plan-slices | Full Superpowers + Spec Kit + BMAD + GSD + ECC together: competing routers, duplicated artifacts and instructions |
| Several TDD/debugging prompts | Adapted Matt TDD; Superpowers debugging with one Matt feedback-loop idea | Duplicate TDD, diagnosing-bugs, build-fixer and debugger triggers; compiler repair is part of diagnosis |
| Many design assistants | One prototype-ui skill | Simultaneous full Impeccable, frontend-design, rapid-prototyper and UI-designer systems |
| Hundreds of expert personas | Three bounded role templates | Agency, VoltAgent and wshobson wholesale; a title supplies neither verified expertise nor isolation |
| Scientific mega-collection | Needed topic as an on-demand reference | Bio/chem/data packages and hundreds of descriptions for ordinary app development |
| Multiple memory engines | Files first; Basic Memory pilot later | Graphiti + Cognee + Mem0 + vector DB + graph DB together |
| Old OpenMemory or Penpot bridge links | Verify current projects | Mem0's old OpenMemory was sunset; old standalone Penpot MCP repository archived/moved. This does **not** mean Mem0 core or Penpot is abandoned. [OpenMemory maintainer notice](https://github.com/mem0ai/mem0/issues/3238), [current Penpot MCP](https://github.com/penpot/penpot/blob/develop/mcp/README.md) |
| Letta as a neutral shared-memory addon | Existing client + shared protocol | Current Letta Code is another agent harness; archived Letta V1 architecture is not a current recommendation |
| Multiple browser agents | Playwright CLI + project tests | Playwright MCP, DevTools MCP, agent-browser and browser-use all permanently connected |
| Automatically observing everything | Explicit short learning events | Raw transcript/tool recording, unreviewed global instincts, self-editing rules |
| Full Anthropic eval viewer unchanged | Eval concepts + safe text/JSON | Inspected scripts are Claude-specific; current issue reports concern viewer HTML injection and process handling. Reports are not reproduced exploits. [Issue #1788](https://github.com/anthropics/skills/issues/1788), [#1789](https://github.com/anthropics/skills/issues/1789) |
| Many Python managers | uv; existing pip/venv projects remain valid | Poetry, pip-tools and Conda in the same ordinary project without a specific reason |
| Many JS managers/runtimes | Bundled npm | Adding pnpm, Yarn and Bun because a tool's repository uses them to develop itself |
| Duplicated code-quality tools | Ruff + mypy; Biome for new JS projects | Black + isort + Flake8 alongside Ruff; Biome plus full ESLint/Prettier unless a needed rule justifies it |
| Premature platform | One app/database | Kubernetes, service mesh, Redis, Kafka, generic repository layers, agent framework or model proxy before requirements demand them |
| Heavy local ML environment for dictation | Handy release binary + one model | Python Whisper + PyTorch + ffmpeg, Rust/Bun/CMake source build toolchains for a downloaded Handy app |
| Paid design/voice by default | Excalidraw/HTML, Handy | Figma or cloud dictation subscription unless collaboration or accuracy testing demonstrates enough benefit |
| Cloud-only dependency for a local prototype | Local app, SQLite, captured test email | Hosted auth/database/email just to answer a layout question |
| Browser/server telemetries left implicit | Review and configure selected tool | “Local” alone does not establish zero outbound traffic; inspect each selected version |

This is not a claim that the rejected tools are bad. They fail your current test: **does this capability justify another concept, dependency, permission, running service, or persistent prompt?**

## 6. Shared Memory Architecture

**Use curated, portable records first. For the requested single endpoint, pilot Basic Memory in phase 3 with lexical search and semantic search explicitly disabled. Do not add a graph database.** Basic Memory is the best practical fit among the inspected existing products, but it is a conditional choice: its dependency weight and unauthenticated HTTP transport are real disadvantages. If those exceed your risk/maintenance budget, keep the files until a better-fitting endpoint is available.

“Memory” has several meanings. An **episode** records what happened; a **fact** records a supported statement; a **relationship** connects two records; **temporal** fields say when a statement was valid. Semantic search finds similar meaning using embeddings. None of these concepts inherently requires a separate graph or vector server.

### Candidate comparison

Versions below are observed releases as of September 20, 2026, not a promise that future installs resolve the same graph. Release evidence and capability descriptions inspected on current branches are distinguished in the appendix; not every main-branch feature is established for the named tag. All model-assisted candidates can send data to a model if configured to use one.

| Candidate | Storage, models and service cost | Fit, drawbacks and decision |
|---|---|---|
| **[Basic Memory](https://github.com/basicmachines-co/basic-memory), v0.23.2, Aug 25; AGPL-3.0-or-later** | Human-readable Markdown plus SQLite indexing/relations; MCP. Tagged manifest has **43 direct runtime requirements**, Python ≥3.12, including FastMCP `4.0.0b1`, FastEmbed/ONNX-related components and provider integrations. F0 local lexical use; F1 agent-assisted curation. | **Conditional winner:** inspectable/exportable content, no separate DB required, existing multi-client entry point. Heavier than expected; prerelease dependency; HTTP/SSE has no native authentication. Semantic search defaults must be overridden for the proposed baseline. [Tagged manifest](https://github.com/basicmachines-co/basic-memory/blob/v0.23.2/pyproject.toml), [transport security](https://docs.basicmemory.com/reference/docker/) |
| **[Graphiti](https://github.com/getzep/graphiti), v0.30.2, Sep 8; Apache-2.0** | Temporal knowledge graph; current MCP defaults to FalkorDB, Neo4j alternative; extraction/model and embedding endpoints. Local models possible; one small Python manifest does not reflect service/model burden. F1. | Strong if time-aware multi-hop relationships measurably improve retrieval. **Reference for later**, too much initial infrastructure. Kuzu option is deprecated rather than a good lightweight new default. Disable telemetry deliberately. |
| **[Cognee](https://github.com/topoteretes/cognee), v1.6.0, Sep 18; Apache-2.0** | Default local graph/vector stack includes SQLite, LanceDB, Ladybug and FastEmbed/ONNX; >50 direct requirements. New local ingestion can be keyless. F1; endpoint choice determines cloud use. | Rich ingestion/retrieval but a larger pipeline to debug. **Reference**, not core. Do not repeat obsolete claims that every path requires OpenAI. Provenance behavior needs acceptance testing. |
| **[Mem0](https://github.com/mem0ai/mem0), core 2.1.0, Sep 18; Apache-2.0** | Default core path uses OpenAI LLM/embeddings, local Qdrant and SQLite history; providers can change. Server examples use a different PostgreSQL/pgvector arrangement. F1 with local replacement; default external API path can be F3. | Useful extracted personalization, but an extra adapter is needed for our neutral shared endpoint. **Reference**. The old OpenMemory project was sunset, not a maintained turnkey shortcut. [Maintainer notice](https://github.com/mem0ai/mem0/issues/3238) |
| **[Letta Code](https://github.com/letta-ai/letta-code), 0.32.14, Sep 20; Apache-2.0** | Current full coding-agent harness with persistent context; service/model configuration matters. F1/F3 according to deployment. | **Skip as a memory addon.** It is not simply one neutral memory layer beneath three existing clients. Letta V1 is retired/archived; avoid designing around its old server requirements. |
| **[Official MCP memory server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory), release 2026.8.31; MIT** | Node/MCP SDK/Zod; JSONL entities, relations and observations; no inference required. F0. | Very small useful demonstration, but sparse provenance/time/retention controls. Its in-process write queue is **not** cross-process coordination. Never point three independent stdio processes at one file and call it a safe shared service. |
| **[QMD](https://github.com/tobi/qmd), v2.8.3, Aug 16; MIT** | Local document search; SQLite, native `better-sqlite3`, `sqlite-vec`, `node-llama-cpp`, parser/model dependencies; CLI and HTTP MCP. F0 local search after downloads. | **Optional retrieval alternative**, not memory lifecycle management. Useful for a large existing notes corpus; too much merely to search a few curated facts. |
| **[Hindsight](https://github.com/vectorize-io/hindsight), v0.10.0, Sep 14; current LICENSE MIT** | Structured retain/recall, embedded PostgreSQL option plus inference/embedding requirements. F1. | Stronger purpose-built lifecycle, higher operational burden. **Reference**. Current LICENSE takes precedence over stale Apache wording in older material. |
| **Custom SQLite FTS5 + MCP service** | Python `sqlite3`, one MCP SDK and its transitives; no graph/embedding model needed initially. F0 service/F1 curation. | Smallest controllable dependency design, but **not implemented or production-ready here**. You would own transport security, tests, migrations, concurrency and packaging. Optional future exercise, not a beginner prerequisite. |

The companion audit records exact source paths and release evidence. Do not compare only top-level dependency counts: a seven-package library plus a database and two model endpoints can be operationally heavier than a larger single-process tool.

### Proposed shared endpoint

```text
Claude Code ─┐       small client adapters
Cursor ──────┼───── MCP Streamable HTTP ──────┐
Codex ───────┘                               │
                          LOCAL, SINGLE USER │
                          one Basic Memory process
                          bound to loopback explicitly
                                      │
                     ┌────────────────┴───────────────┐
                     │                                │
             private Markdown notes           SQLite index/relations
             canonical human content          local text retrieval
                     │                                │
          user-global / project namespaces     no graph DB; no model
                     │                         required for search
                     └──────── backups + restore test ┘

Model-assisted curation/retrieval → chosen coding model
If that model is hosted, selected content crosses the cloud boundary.
```

Use a single supervised process for HTTP, not a stdio process per client writing to one shared JSON file. The tagged Basic Memory CLI supports `--transport streamable-http`, `--host`, `--port` and `--path`; explicitly choose `127.0.0.1` because the inspected default is `0.0.0.0`. Pin the reviewed package in an isolated environment. The exact starting command is **proposed, unexecuted configuration**, not a validated integration:

```text
basic-memory mcp --transport streamable-http --host 127.0.0.1 --port 8000 --path /mcp
```

Set these documented/tagged controls deliberately for the local lexical pilot, then verify actual network behavior and effective configuration:

```text
BASIC_MEMORY_SEMANTIC_SEARCH_ENABLED=false
BASIC_MEMORY_RERANKER_ENABLED=false
BASIC_MEMORY_AUTO_UPDATE=false
BASIC_MEMORY_LOGFIRE_ENABLED=false
BASIC_MEMORY_LOGFIRE_SEND_TO_LOGFIRE=false
```

Disabling a feature does **not** uninstall its declared Python dependencies. Explicitly disable reranking too, so an older enabled setting does not conflict with semantic search being off. `main` has different dependencies from the audited tag; resolve, inspect and scan the chosen version before adopting it. [Tagged configuration](https://github.com/basicmachines-co/basic-memory/blob/v0.23.2/src/basic_memory/config.py), [defaults and validation](https://github.com/basicmachines-co/basic-memory/blob/v0.23.2/src/basic_memory/config_models.py), [tagged MCP command](https://github.com/basicmachines-co/basic-memory/blob/v0.23.2/src/basic_memory/cli/commands/mcp.py).

**Security limitation:** Basic Memory documents that its HTTP/SSE endpoint is unauthenticated. Loopback reduces network exposure; it does not isolate the service from other local processes. Namespaces are organizational filters, not authorization boundaries. A bearer token in a client configuration does nothing unless the server or an added proxy validates it. Use only trusted clients on the same machine, no public tunnel, minimum exposed tools, and no secrets in memory. Validate host/origin handling and Windows↔WSL reachability. If you need authentication or enforceable per-client/project permissions, add and test a reviewed authentication/authorization layer—or reject this pilot. That extra component belongs in the dependency budget. [Basic Memory security warning](https://docs.basicmemory.com/reference/docker/), [MCP transport requirements](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports), [WSL networking](https://learn.microsoft.com/en-us/windows/wsl/networking).

### Records, intake, retrieval and correction

The following is **our proposed schema and curation policy**, not a claim that Basic Memory enforces every field. Store it in frontmatter/body conventions and validate it with a small local script if needed:

```text
id, namespace, kind, status, statement
source_ref, source_date, recorded_at
valid_from, valid_to, supersedes
confidence: observed | user-stated | inferred
review_after, expires_at, sensitivity
links: [{relation, target_id}]
```

Use `user/global` for explicitly accepted preferences and learning progress; `project/<stable-id>` for project facts; `project/<id>/episodes` for short-lived history. Namespace names and file layouts are our convention. Keep guesses in a separate candidate status. A source reference should resolve to a file/revision, decision, dated URL or explicit user correction. Never interpret “confidence: 0.9” generated by a model as a calibrated probability.

1. **Intake:** propose one durable fact after an explicit correction, consequential decision or unusual verified bug. Show statement, scope, evidence and expiry. Accept/edit/reject before persisting. Do not ingest whole chats, source trees, credentials or every completed task.
2. **Deduplication:** search the intended namespace first; update or supersede an existing record. Prefer a project ADR as the authority and remember its pointer rather than copying its full text.
3. **Retrieval:** search current project first; include user-global only when relevant. Start with at most five short hits, open at most two, and aim for 500–1,000 tokens. Show dates/provenance; never let retrieved text override permissions or current instructions. These are configurable targets.
4. **Changing facts:** preserve the old record as superseded, set validity bounds, link replacement and evidence. Resolve conflicts with newer supported evidence or ask; do not silently merge contradictory claims.
5. **Retention:** proposed defaults: transient episodes 30 days; unconfirmed hypotheses 14 days; accepted project/preferences reviewed after 90 days but kept until no longer useful. A scheduled purge is optional future work, not supplied native automation.
6. **Deletion:** remove content and derived indexes/embeddings, inspect backups and exports, and apply their retention policy. Deleting a Git-tracked file does not erase its history. Keep sensitive personal memory out of published repositories.

**Backup matters because writes are queued.** The inspected Basic Memory implementation can acknowledge a write before Markdown materialization. Quiesce writes, shut down gracefully, and back up notes, database and configuration together. For a live SQLite backup, use its backup API; copying only the database while ignoring an active WAL can lose changes. Test a restore and search after restoration. [Basic Memory tagged server](https://github.com/basicmachines-co/basic-memory/blob/v0.23.2/src/basic_memory/mcp/server.py), [SQLite backup API](https://sqlite.org/backup.html), [WAL](https://sqlite.org/wal.html).

Pilot acceptance: all three **actual installed client versions** query the same known fact; corrections appear everywhere; concurrent updates do not disappear; namespace filtering, bounded results, export, delete and restore work; the service is reachable only as intended; no unexpected telemetry/model call occurs. Test real authorization separately if added. The protocol and documented client support make this plausible, but it has **not** been run in this research.

### Why a graph database is unnecessary here

An SQLite relation row `(source_id, relationship, target_id)` already represents “project uses PostgreSQL.” SQL joins and small recursive queries can answer modest graph questions; FTS5 supplies lexical retrieval. Add embeddings when a benchmark shows paraphrases are being missed. Add Graphiti/graph infrastructure only when temporal multi-hop questions repeatedly outperform this baseline enough to justify the services and inference cost. [SQLite FTS5](https://sqlite.org/fts5.html), [recursive queries](https://sqlite.org/lang_with.html).

## 7. Self-Improving Skill Architecture

**Start with manual capture and reviewed Git changes. The system may propose improvements; it must not silently rewrite its own rules.** Repetition can mean a bug in one project rather than a universal preference.

```text
explicit feedback / verified unusual failure
                 ↓
redacted learning event with evidence
                 ↓
manual pattern review → candidate instinct, not a fact
                 ↓
small proposed skill/profile diff
                 ↓
baseline vs candidate evaluation
                 ↓
held-out regressions + three-client adapter checks
                 ↓
your approval → Git commit/tag → rollback available
```

Use **Git, JSONL and Python's standard library**, plus the clients you already have. Suggested event fields: timestamp, project/scope, client/model, skill version, observed problem, evidence path/revision, correction, outcome, sensitivity, expiry and review status. Do not place raw credentials or complete prompts in the learning log. One accepted lesson can link to memory; the released skill remains authoritative in the canonical repository.

Borrow ECC's evidence-linked, scoped “instinct” concept and Compound's durable-learning filter: preserve verified, non-obvious knowledge that cannot easily be reconstructed from final artifacts. ECC's inspected observer/hook implementation is Claude-specific; its background observer has a documented native Windows limitation. Broad capture also has privacy costs independent of whether analysis is enabled. Use WSL only if later adopting that implementation, and review every hook first. [ECC actual skill](https://github.com/affaan-m/ECC/blob/main/skills/continuous-learning-v2/SKILL.md), [Windows issue](https://github.com/affaan-m/ECC/issues/2489), [Compound learning skill](https://github.com/EveryInc/compound-engineering-plugin/blob/main/skills/ce-compound/SKILL.md).

Borrow Anthropic skill-creator's paired evaluation design, not an assumption that its scripts run unchanged in every client. Inspected `run_eval.py` invokes `claude -p`; its browser review helper embeds evaluation data into generated HTML and has process-management behavior that requires review. Current issue reports reinforce using plain text/JSON first. [Skill creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), [run_eval.py](https://github.com/anthropics/skills/blob/main/skills/skill-creator/scripts/run_eval.py), [review generator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/eval-viewer/generate_review.py).

Create 10–20 small fixtures before investing in a framework. Include correct triggers and near-miss non-triggers; a real failing-test-first case; a bug needing evidence; a dependency that should be rejected; incomplete evidence that must not be called success; a secret that must not be printed; a misleading memory; a screenshot critique; and a beginner explanation graded for accuracy and usefulness. Run baseline and candidate with the same repository state, model, tool permissions and task. Repeat important stochastic cases, keep held-out regressions, and record outcome, human comprehension, tokens, time and tool calls. Use model graders only as supplementary evidence.

An improvement must help a real case without damaging held-out tasks or teaching. A smaller prompt with the same quality is valuable. No measured improvement is claimed in this report; the evaluation system and adapters are proposed implementation work.

## 8. Model Adaptation Architecture

Keep one portable skill body and small profiles that adjust **task size, evidence requirements and escalation**, not three duplicated prompt libraries. Model names, pricing and capabilities change; map your currently available models to these profiles after testing them.

| Profile | Suitable work | Instructions and tool scope | Escalate when |
|---|---|---|---|
| Lightweight | Bounded mechanical edit, classify a short result, summarize a cited diff | One small goal, explicit expected output, few relevant files, clear stopping condition; same verification and privacy rules | Ambiguous requirements, repeated failed hypothesis, unfamiliar API or multi-module reasoning |
| Standard | Normal feature slice, test-first implementation, debugging | Relevant spec and diagram, bounded tool loop, tests, explain decisions | Authentication/data-loss risk, unresolved architecture tradeoff, repeated failure |
| Frontier | Architecture alternatives, difficult root cause, independent high-risk review | Broader evidence with an explicit budget; challenge assumptions; return compact findings and teach tradeoffs | Missing facts, professional legal/security expertise, inability to verify |

A conceptual profile can contain `task_scope`, `max_parallel_roles`, `retrieval_limit`, `supports_images`, `tool_schema_constraints`, `verification_contract` and `escalation_conditions`. Token limits are tuning targets, not proof of capability. Do not reduce security or teaching requirements to make a weak model appear successful.

For a new model, first run the unchanged core/eval suite. Include actual coding, tool use, instruction conflicts, visual interpretation if needed, and honest failure reporting. Compare against the old model and a no-skill baseline; otherwise a stronger model may receive credit for a skill change it did not need. Change a profile before rewriting all skills. Record model/provider/version when available and retest after meaningful provider changes.

For fully local experimentation, **one optional Ollama installation** is easier than adding several inference engines. Explicit local-only controls exist; model files have their own licenses and hardware requirements. A local engine does not establish that an arbitrary model is good enough for coding or image interpretation. [Ollama local-only controls](https://docs.ollama.com/faq). OpenCode with a local provider is an optional replacement path with documented skills/provider support, not a fourth default coding client. Aider, Goose and Cline are also alternatives; none earns an additional permanent installation merely to access another agent harness. [OpenCode skills](https://opencode.ai/docs/skills/), [providers](https://opencode.ai/docs/providers/), [Aider](https://github.com/Aider-AI/aider), [Goose](https://github.com/aaif-goose/goose), [Cline](https://github.com/cline/cline).

Hosted frontier assistance can remain the pragmatic choice for difficult work. Use your selected subscriptions where supported, but do not assume a subscription covers separate API evaluations. Local and hosted profiles should pass the same acceptance criteria.

## 9. UI / Design Workflow

**Default: sketch → disposable local HTML → real browser → critique → production.** The prototype answers a visual or interaction question. It should not acquire authentication, a database or a deployment platform just to render a screen.

```text
paper/photo or Excalidraw sketch
              ↓
AI states layout interpretation + uncertain parts
              ↓
brief: audience, main action, content, key states
              ↓
2–3 meaningfully different HTML/CSS alternatives
              ↓
browser at desktop + mobile widths; screenshots
              ↓
your marked corrections → one focused iteration
              ↓
approved direction + recorded design decisions
              ↓
production slices → functional + visual + accessibility checks
```

Choose variants that explore a real tradeoff—navigation location, information density or primary action—not three colors on the same layout. Use realistic mock content, empty/loading/error/success states, keyboard focus and readable contrast. Explain one useful design principle per iteration. Keep source sketches editable and save the chosen design rationale beside the project.

| Tool | Decision and tradeoff | Dependencies, privacy and context |
|---|---|---|
| **Local HTML/CSS** | Default, quickest faithful browser preview; reuse an existing framework only if simpler | Existing browser; optional Python standard-library static server. F0; C when code/screenshots read |
| **[Excalidraw](https://github.com/excalidraw/excalidraw)** | Manual sketching/architecture; MIT | F0 local/self-hosted option; hosted web delivery separate. D until shared; no MCP required |
| **[Excalidraw MCP](https://github.com/excalidraw/excalidraw-mcp)** | Optional if live canvas editing matters | Node/server or remote endpoint; embedded canvas needs MCP Apps support, not merely generic MCP. F0/F2; A/deferred catalog + C |
| **[Penpot](https://help.penpot.app/technical-guide/getting-started/)** | Best open-source upgrade here for reusable vector design/components; MPL-2.0 | F0 self-host/F2 hosted. Self-hosting brings frontend/backend/exporter, PostgreSQL and supporting services; medium operational cost |
| **[Current Penpot MCP](https://github.com/penpot/penpot/blob/develop/mcp/README.md)** | On-demand live design-file integration | Match Penpot/MCP versions; active plugin connection; powerful Plugin API operations. Old standalone repo archived Feb 3, 2026; do not use stale setup guides |
| **[Storybook](https://storybook.js.org/docs/writing-tests)** | Add when a reusable component catalog earns its maintenance | Project framework/build/addon dependencies. F0 locally; Chromatic F2/F3 optional. A simple component page may suffice first |
| **Frontend-design + selective Impeccable** | Merge into prototype-ui, as section 4 | The former is compact prose; current Impeccable also invokes a native engine/download launcher and optional hooks. Do not call the complete modern package dependency-free. [Launcher](https://github.com/pbakaus/impeccable/blob/main/.agents/skills/impeccable/scripts/impeccable) |
| **[Figma](https://www.figma.com/pricing/)** | Proprietary F2/F3 exception when collaborators need it or demonstrated features save enough work | Hosted account and plan limits. Free/local substitute: Excalidraw + HTML; Penpot for a sustained design workspace |

For architecture, use Mermaid flow, sequence, state and entity-relationship diagrams where they explain the problem. C4 is a way to choose levels of detail, not a required server. Start with system context, components/containers, and one request sequence. Mermaid's dedicated C4 syntax is still labeled experimental; ordinary flowcharts using C4 concepts are a more conservative documentation choice. [C4](https://c4model.com/diagrams), [Mermaid C4 status](https://mermaid.js.org/syntax/c4.html).

For an unfamiliar large repository, Understand Anything can generate a local navigable code graph, but its parser/build stack, multi-agent analysis and initial token use are substantial. Its `.ua/knowledge-graph.json` is an analysis artifact, not automatically accurate long-term memory. Default to a small cited architecture diagram; use the larger tool only when it helps answer concrete navigation questions. [Inspected skill](https://github.com/Egonex-AI/Understand-Anything/blob/main/understand-anything-plugin/skills/understand/SKILL.md).

That optional MIT/F1 tool currently adds Node ≥22, pnpm ≥10, Python/Git and native/WASM parser/build components in its own environment. It is an exception to the default npm-only convention, not a reason to add pnpm globally. Review automatic builds, update hooks and main-worktree output redirection before enabling it.

### Browser control: one family of tools

| Option | Use it when | Context and dependency judgment |
|---|---|---|
| **[Playwright CLI + skill](https://github.com/microsoft/playwright-cli)** | Default interactive frontend inspection | Node, browser binaries and OS libraries. Named sessions persist; file-backed/scoped snapshots can reduce inserted output. B/C, low–high depending on what is read |
| **[Playwright Test](https://playwright.dev/docs/intro)** | Saving repeatable functional and screenshot checks | Project dev dependency and matching browser revision; C concise results, traces on failures. Complements exploration |
| **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** | Shell unavailable or structured browser tools work better in measured trials | Same browser family, another interface. Catalog A or deferred depending on client; C outputs. Persistence alone is not a reason: CLI also persists |
| **[Chrome DevTools MCP/CLI](https://github.com/ChromeDevTools/chrome-devtools-mcp)** | Detailed performance/trace investigation | Node/Chrome and supporting packages; current CLI is experimental and has a daemon. Scope workspace, disable unwanted statistics/CrUX use, stop afterward |
| **[agent-browser](https://github.com/vercel-labs/agent-browser)** | Alternative if compact/delta snapshots outperform the default on your tasks | Browser/daemon, current source requires Node ≥24. Compare, then substitute; do not add alongside every controller |
| **[browser-use](https://github.com/browser-use/browser-use)** | Building a browser-agent product | Python, browser and another LLM loop; more dependencies/context than necessary for ordinary coding QA. Local library possible; cloud optional |

**Version caveat:** observed Playwright CLI v0.1.21 (September 18) depends on an exact Playwright 1.64 alpha build, while observed stable Playwright Test is v1.63.0 (September 4). Reuse the project's CLI if its installed version exposes the needed commands; otherwise isolate a pinned CLI installation. Do not upgrade stable tests to a prerelease just to match a tool's package. [CLI manifest](https://github.com/microsoft/playwright-cli/blob/main/package.json), [CLI releases](https://github.com/microsoft/playwright-cli/releases), [Playwright releases](https://github.com/microsoft/playwright/releases).

Explore one named session with test identities: inspect relevant elements, fill a form, observe console/network failures, check narrow and wide viewports, and capture a focused screenshot. Persist useful flows as tests. Keep authentication state and traces outside source control: traces can include network bodies, headers and private DOM content. Stable screenshot comparisons need controlled OS/browser/fonts/viewport/data; approving every changed golden blindly defeats the test. [Session reference](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/tools/skills/playwright-cli/references/session-management.md), [tracing](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/tools/skills/playwright-cli/references/tracing.md), [visual comparisons](https://playwright.dev/docs/test-snapshots).

Measure CLI versus MCP on the same login/form/responsive/failure task, using the same model and success criteria. Count tokens where available, tool output, retries, total time and correctness. File-backed output saves context only when the agent reads selected parts. A screenshot still consumes vision context. No universal savings percentage was established here.

For a DevTools investigation, current CLI file access is unrestricted by default and usage statistics are enabled by default. Use `--workspace`, `--no-usage-statistics` and `--no-performance-crux` as appropriate; update checks have separate controls. Inspect the chosen version's effective configuration. [DevTools CLI](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/cli.md).

### Voice: Windows capture, ordinary text into WSL tools

Use **Handy on Windows**, hold-to-talk or toggle, one local model and your technical vocabulary. The Windows microphone/hotkey/text-insertion path is simpler than maintaining separate WSL audio integration. Pauses should not submit a message. Review inserted text before sending, particularly shell commands or destructive instructions. Cross-app paste reliability must be tested on your actual clients. Handy v0.9.7, released September 18, includes relevant audio/hotkey/Windows fixes. [Handy](https://github.com/cjpais/Handy), [releases](https://github.com/cjpais/Handy/releases).

```text
microphone → local Handy speech model → optional cleanup → review → focused client
                                             │
                              reuse existing local LLM only if needed
```

| Option | Recommendation / constraints |
|---|---|
| Handy, MIT | **Default F0:** release binary + microphone + one model; no mandatory cloud API, Rust/Bun/CMake or Python Whisper installation |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp), MIT | F0 alternative for batch/embedded speech; executable + model. You still need capture/hotkey/paste integration; source builds need compiler/CMake |
| [Python Whisper](https://github.com/openai/whisper), MIT | Good research library, excessive dictation setup: PyTorch, NumPy, Numba and ffmpeg among dependencies |
| [Superwhisper Windows](https://superwhisper.com/windows) | Proprietary comparison with advertised local/offline options. Trial if Handy fails your accuracy/workflow test; current exact price not verified |
| [Wispr Flow](https://wisprflow.ai/pricing) | F2/F3 cloud convenience comparison; observed Pro $15/month or $12/month billed annually. Privacy options do not establish local inference. Handy is the local alternative |

Optional Handy post-processing can send a transcript to an OpenAI-compatible local **or cloud** endpoint; the chosen endpoint controls that privacy boundary. Begin without it. Trial “use SQLite—no, PostgreSQL,” “do **not** delete production,” `user_id`, a path with spaces, a ten-second pause, numbers and corrections. Cleanup may remove fillers and clearly superseded false starts; it must preserve identifiers, negation and uncertainty. Measure hotkey-to-text latency and correction burden before choosing a larger model. [Handy post-processing](https://handy.computer/docs/post-processing), [Wispr data controls](https://docs.wisprflow.ai/articles/9609615338-Private-Cloud-Sync-and-Data-Sharing-preferences-in-Wispr-Flow).

### Occasional games and 3D

**Unity:** use the Windows editor, project-matched packages, console, profiler and edit/play-mode tests first. The community [CoplayDev Unity MCP](https://github.com/CoplayDev/unity-mcp) is a reasonable on-demand bridge when live editor state matters; it is not official Unity software. It adds Python/uv and bridge packages plus Unity package dependencies. Pin compatible server/editor package versions and enable only needed tool groups. Its inspected [orchestrator skill](https://github.com/CoplayDev/unity-mcp/blob/main/unity-mcp-skill/SKILL.md) teaches inspect → edit → compile → console → tests → screenshot. Adapt scene-creation examples so they do not replace existing work; checkpoint first. Teach GameObjects/components, asset references and frame timing as those concepts appear.

**Blender:** begin with its built-in `bpy` scripting and saved scripts for deterministic geometry/render/export. Live [MCP for Blender](https://github.com/ahujasid/blender-mcp), now packaged as `mcp-for-blender`, is optional for an open scene. Arbitrary Python execution carries filesystem/process authority, not just canvas permissions. Disable its default telemetry using `DISABLE_TELEMETRY=true` and the addon consent setting; leave external asset/AI generation integrations off unless needed. Asset licenses are separate. [Telemetry terms](https://github.com/ahujasid/blender-mcp/blob/main/TERMS_AND_CONDITIONS.md). Connector-specific skills from [jithinolickal](https://github.com/jithinolickal/blender/blob/main/skills/blender/SKILL.md) and [vinhelysia](https://github.com/vinhelysia/blender-mcp/blob/master/skill/blender-mcp/SKILL.md) are reference material, not interchangeable bridge instructions.

Game debugging uses the same disciplined loop: create a minimal scene, reproduce at known settings, inspect logs/profiler/state, change one hypothesis, repeat, save evidence. For shaders/assets, compare controlled lighting/camera/material inputs. Turn off bridges outside the active project; no global game agent collection.

Keep both bridges beside their Windows GUI applications initially. Their MIT licenses do not relicense Unity itself or downloaded assets. Bridge Python ≥3.10/uv requirements are separate from Blender's embedded Python, which already supports native scripting. Avoid duplicating those host bridge packages inside unrelated WSL application environments.

## 10. Learning Workflow

**The deliverable is working software plus your ability to explain it.** A fast result that leaves you unable to change or debug it has missed half the goal.

For each meaningful slice, the AI should state the outcome, explain the reason, identify files and responsibilities, introduce only the needed concept/dependency, implement a small change, explain its important code, show verification, and occasionally invite a prediction or teach-back. Keep routine messages short; increase explanation where your questions or mistakes reveal a gap. Do not force a quiz before every action.

Example: add a “complete task” action to a small application.

1. **Design:** sketch incomplete/completed states and decide what should happen on a failed save. Show `button → HTTP route → task service → database`. Explain that the route translates network requests while the service owns the business rule.
2. **Scope:** “Only the owner can complete a task; repeating the action is safe; a failed save shows an error.” Define *idempotent* using the repeat-click example. Ask what should happen if another user's task ID is supplied.
3. **Plan files:** `api/tasks.py` handles request/response; `services/tasks.py` enforces ownership/state; `db/tasks.py` persists; the UI component displays status; tests assert the behavior. For a very small app these may be fewer modules—responsibility matters more than folder count.
4. **Dependency lesson:** if an HTTP client is newly needed for API tests, explain why HTTPX exists, that it is dev-only unless application code uses it, what appears in `pyproject.toml`/`uv.lock`, and what breaks if removed. Do not add an ORM just to satisfy a preferred diagram.
5. **Red:** write one behavioral test that a non-owner cannot update the record. Run it and explain the failure. A syntax/import error is not proof that the behavioral test is effective.
6. **Green:** make the smallest correct implementation, then test owner success and repeated completion. Explain the ownership check and transaction boundary; avoid dumping hundreds of unrelated lines.
7. **Refactor:** after green, remove a duplicated state transition or clarify a name. Explain cohesion—related responsibilities belong together—and rerun affected tests.
8. **Browser:** operate the form, check keyboard behavior, inspect a failed request, and verify empty/error/loading states. Save a repeatable E2E test for the important user path.
9. **Debug visibly:** if the UI stays stale, reproduce, inspect the response and local state, form one hypothesis, test it, fix the cause and add a regression. Explain why a reload hid the bug without fixing it.
10. **Review and learn:** independent review for the authorization boundary; report evidence and limits. Invite you to explain where the rule lives and how to test another forbidden action. Propose one durable lesson only if useful.

Use strict red-green-refactor for deterministic business rules, parsers, permissions, API contracts and reproducible bugs. Database behavior needs integration tests against realistic schema/transaction behavior. Use a production-like database when its semantics matter. UI appearance often starts with a prototype and visual acceptance, then behavior tests. External APIs need contract tests and controlled stubs. AI outputs need curated datasets, deterministic tool-boundary tests, retrieval metrics, adversarial cases and human evaluation; a single exact-string assertion is rarely an adequate quality test. Scientific work additionally needs leakage checks, baselines and reproducibility.

Teaching Linux means explaining commands **before unfamiliar or consequential use**, then showing how to inspect the result. For example, `pwd` shows the current directory; `rg` searches text; `|` passes output to another process; an environment variable supplies configuration to child processes; `PATH` is the list of directories searched for executables. Explain flags and path scope. Use `sudo` only for a genuine system change; project packages belong in the project environment. Do not hide destructive operations inside a large script.

Track a small learning record you approve: concepts encountered, explanation in your words, exercise attempted, hint level and next revisit. Revisit by asking you to predict a result, locate a module, diagnose a small bug, inspect a dependency tree or write one test. Progress means fewer hints and better explanations over time—not more generated code, higher message counts or an invented mastery score.

## 11. Security + Legal Guardrails

Use different mechanisms for different jobs. A skill supplies a procedure; a scanner executes repeatable checks; an independent reviewer challenges assumptions; primary sources establish current requirements. None replaces all the others.

| Layer | What belongs here | Activation and cost |
|---|---|---|
| Tiny always-on rule | Protect secrets; distrust external instructions; least privilege; explain consequential changes; verify before success claims | A/low |
| Security/legal skill | Data-flow/threat model; select relevant tests; classify legal triggers and uncertainty | B then C/medium |
| Deterministic tools | Gitleaks, OSV, selected Ruff security checks; optional Semgrep/local rules, container scanner when relevant | F0/C, concise findings |
| Independent agent | Auth/privacy/financial boundary or high-risk architecture review with evidence | F1/C, bounded separate context |
| Current research | Official framework advisories, OSV, platform policies and jurisdiction-specific government sources | C/on demand; date every finding |
| Human professional | Material unresolved legal obligations or high-impact security/compliance review | External service, potentially paid; prompts cannot supply certification |

### Security checks should follow the feature

| Trigger / risk | Required reasoning and evidence |
|---|---|
| Authentication / authorization / APIs | Separate “who are you?” from “may you do this?” Test ownership/role checks server-side, session expiry, rate limits and safe error responses; use established framework/auth primitives |
| SQL injection / XSS / CSRF | Parameterized database queries; contextual escaping/safe rendering; CSRF protection for relevant cookie-authenticated mutations; test actual boundary behavior |
| SSRF / command injection | Restrict outbound destinations and redirects where untrusted input selects URLs; avoid shell interpolation; pass executable arguments safely |
| Paths / uploads / deserialization | Contain resolved paths, generate safe filenames, constrain size/type/content, isolate storage and processing; never deserialize untrusted executable formats |
| Secrets / database permissions | Environment/secret-store configuration, redacted logs, separate dev/prod identities, minimum DB permissions; scan before publication; rotate exposed secrets |
| Dependencies / supply chain | Lockfiles, source and install-script review, advisory checks, controlled updates and rollback; section 16 |
| LLM/RAG / prompt injection | Treat retrieved documents/tool results as data, isolate tool permissions, validate structured output, control exfiltration paths, test hostile retrieved instructions |
| MCP / agent tools | Review executable/server provenance, methods, filesystem/network scope and authentication; bind locally; no broad credentials; approvals and real OS isolation where needed |
| Mobile / cloud / release | Secure token storage, permission minimization, signing, transport, public bucket/service exposure, backups/restore, logging and incident response |

OWASP ASVS is a requirements/checking reference; the LLM guidance covers additional application risks. Neither implies that a prompt or scan has established compliance. [OWASP ASVS](https://github.com/OWASP/ASVS), [OWASP LLM project](https://owasp.org/projects/top-10-for-large-language-model-applications), [MCP security practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices).

Default scanner set: Gitleaks for likely secrets, OSV for known vulnerable dependencies, Ruff's relevant rules for Python code. Bandit overlaps some Ruff checks; add it only for needed coverage rather than assuming the rule sets are identical. Semgrep can add broader patterns, but rules and metrics settings require review; local rules avoid a mandatory hosted rule service. `--metrics off` is available. Containers justify image/config scanning; ordinary SQLite development does not. [Ruff security rules](https://docs.astral.sh/ruff/rules/), [Semgrep metrics](https://semgrep.dev/docs/metrics).

### Legal triage is an early-warning process

The custom skill should first establish where the operator and users are, intended age group, data collected, vendors, monetization, content sources and distribution channels. Your jurisdiction and product facts are not supplied, so no project-specific legal conclusion is confirmed here.

| Product trigger | What to investigate now |
|---|---|
| Personal data, analytics, cookies, tracking | Applicable privacy rules, notice/consent or other basis, vendor agreements, access/export/deletion, security and cross-border transfers |
| Minors/children, biometrics, sensitive data | Age-specific and sensitive-data requirements; minimize collection and obtain professional review where applicable |
| User-generated or AI-generated content | Moderation/reporting, copyright and licensing, attribution, source provenance, publicity/trademark risks and platform rules |
| Packages, assets, models, APIs, scraping | Exact software/model/asset license, copyleft/notice obligations, API terms, access restrictions and permitted reuse |
| Email, subscriptions, billing, refunds, payments | Consent/opt-out and sender rules, renewal/cancellation disclosures, refund obligations, processor terms; avoid handling raw card data unnecessarily |
| App Store / Google Play | Current review/privacy/account-deletion rules, permission declarations, SDK behavior, signing and release requirements |
| Accessibility / regional launch | Applicable accessibility duties and technical target; WCAG is a technical standard, not a universal legal determination |
| Retention / deletion / exports | Match promises to real databases, logs, processors and backups; test the deletion/export path |

Each finding records **claim, applicability facts, jurisdiction, authoritative source, publication/effective/access date, practical implication, unresolved question and owner**. Classify it as **confirmed requirement** only when both the rule and its applicability are supported; otherwise **likely concern**, **uncertain / research required**, or **professional legal review recommended**. Static skill text should tell the agent what to research, not pretend yesterday's legal summary is timeless.

Current primary starting points include the [European Commission data-protection framework](https://commission.europa.eu/law/law-topic/data-protection/legal-framework-eu-data-protection_en), [FTC children's privacy](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy), [FTC commercial email guidance](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business), [OSI licenses](https://opensource.org/licenses), [Apple review guidelines](https://developer.apple.com/app-store/review/guidelines/), [Google Play policy center](https://play.google.com/about/developer-content-policy/), and [W3C WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/). They are research entry points, not interchangeable laws or legal advice for an unspecified product.

## 12. Dependency Architecture

**A runtime executes your program; a package manager installs its libraries; a framework supplies an application structure; an SDK is a library for a particular platform; a service is a separately running system.** One tool can occupy several roles. Python is a runtime; uv is a package manager; FastAPI is a framework; a model provider's SDK is a library; PostgreSQL is a database service.

The tables describe capabilities you may enable, not one giant install command. “Conditional” means required only after selecting that feature. If an entry is removed, the capability named in its purpose disappears; it should not break unrelated layers. Every optional application package belongs to that application's environment, never the global skill collection.

### System and AI environment

| Dependency | Required? | Purpose | Type | Installed where | Depends on | Alternative | Why chosen |
|---|---|---|---|---|---|---|---|
| Windows + WSL2 + Ubuntu 24.04 LTS | Chosen foundation; native Windows remains possible | Linux development environment | System | Windows host / WSL | Virtualization, disk, supported Windows | Native Linux or native Windows | Fits your Linux learning and existing computer |
| Git | Yes | Version history, diffs, rollback | System/dev | WSL; host only for host-native projects | OS, HTTPS/SSH for remotes | None recommended | Shared evidence and recovery mechanism |
| Bash, coreutils, man, CA certificates | Mostly supplied by Ubuntu | Shell, file operations, help, trusted TLS | System | WSL | OS packages | PowerShell on Windows | Learn existing tools first |
| ripgrep | Yes for agent work | Fast scoped source search | Dev/system | WSL | Prebuilt executable | Existing grep | Reduces irrelevant output |
| uv | Yes for Python | Python versions, environments, package resolution | Dev/build | WSL user tools | Prebuilt binary; no Python/Rust needed to run it | pip + venv + pip-tools | Replaces several independent management tools |
| Project Python, initially 3.13.x | For Python work | Executes app/tests/tools | Runtime/system | uv-managed; separate from Ubuntu's Python | Compatible wheels and OS libraries | 3.14 when whole project supports it | Conservative AI/native-library compatibility baseline |
| Node 24 LTS + npm | When browser/frontend tooling begins | JS tools, builds, package management | System/dev; runtime for Node apps | WSL | Prebuilt Node distribution | pnpm as later replacement | npm is already bundled; one convention |
| Existing coding clients | At least one | AI editing and review | Dev/model/service | Cursor on host with WSL workspace; CLIs in WSL | Account/model access and client runtime | Optional OpenCode + local inference | No fourth client required |
| Selected skills + adapter files | Yes | Portable procedures | Dev/config | Canonical private repository | Client skill support | Manual prompts | No new service or framework |
| ShellCheck | Once writing shell scripts | Finds common Bash errors | Dev | WSL package/binary | OS | Manual shell review | Useful targeted check; not a shell sandbox |
| tldr/tealdeer | Optional | Short command examples | Dev/help | WSL user tools | Cached community pages; network to update | `man`, `--help` | Convenience, no need to install immediately |

Use Python's supported-version table and the project's wheel availability together; a newer language release is not automatically the least troublesome choice. Do not replace `/usr/bin/python3`. uv's standalone binary does not depend on a Python installation; it can download project Python afterward. [Python status](https://devguide.python.org/versions/), [uv installation](https://docs.astral.sh/uv/getting-started/installation/), [uv project model](https://docs.astral.sh/uv/guides/projects/).

### Application dependencies: Python, APIs, data, AI

| Dependency | Required? | Purpose | Type | Installed where | Depends on | Alternative | Why chosen |
|---|---|---|---|---|---|---|---|
| Python standard library | Yes with Python | Files, JSON, logging, SQLite, simple HTTP calls | Runtime | Python installation | Python | Third-party packages only for a gap | Start here |
| FastAPI | Conditional API default | HTTP routing, validation, OpenAPI | Runtime | Project `.venv` | Starlette, Pydantic and their dependencies | Django; Flask for a smaller existing service | Good fit for your Python/AI APIs |
| Uvicorn | With deployed FastAPI | Runs ASGI application | Runtime | Project `.venv` | Python, HTTP/event-loop packages | Another supported ASGI server | FastAPI itself is not the server process |
| Pydantic | Direct if your code imports it | Validates boundary data | Runtime | Project `.venv` | Native `pydantic-core` wheel | Dataclasses for trusted internal data | Already in FastAPI's graph; make direct use explicit |
| HTTPX | For API tests or outbound HTTP | HTTP client, sync/async | Dev or runtime according to usage | Project `.venv` | HTTP core, AnyIO, certificate packages | `urllib`; requests; aiohttp | Reuse one client for tests and genuine HTTP needs |
| SQLite via `sqlite3` | Local app / foundation memory | Embedded relational data | Runtime storage | Local filesystem | Python's SQLite build | PostgreSQL | No database daemon |
| PostgreSQL | Shared production relational app | Concurrency, constraints, transactions | Service/runtime | Local native service or chosen host | OS/storage/backups | SQLite for small local deployments | One general-purpose durable database |
| Psycopg 3 | With Python + PostgreSQL | Database driver | Runtime | Project `.venv` | `libpq`; binary extra can bundle native libraries | Another driver only if framework requires it | Explicit database connection layer |
| SQLAlchemy 2.0 | When app data grows | Query construction / optional ORM | Runtime | Project `.venv` | Driver; optional/native extensions and greenlet in some modes | Parameterized SQL | Adds value for substantial schemas; avoid wrapper on wrapper |
| Alembic | With evolving SQLAlchemy schemas | Versioned schema changes | Dev/deployment | Project environment + release job | SQLAlchemy, Mako and supporting packages | Django migrations when using Django | Avoid hand-tracking production schema history |
| One model-provider SDK | Only for AI app features | Supported API interface | Runtime/model | Project `.venv` | HTTP/validation packages + model endpoint | HTTPX for a simple stable protocol | One SDK per actual provider; no generic routing framework yet |
| Local Ollama | Optional privacy/local-model path | Runs model weights | Service/model | Windows OR WSL, one installation | RAM/VRAM, disk, optional GPU driver | llama.cpp server | Easier starting operation; disable cloud features |
| Embedding model + pgvector | Only after lexical baseline fails | Similarity retrieval | Model/runtime/database extension | Inference host + existing PostgreSQL | Model weights, compatible extension/server versions | SQL full-text search; Qdrant later | Reuse database instead of adding a new server |
| Promptfoo | Optional larger evaluation matrix | Compare prompts/models against cases | Dev | Project or isolated Node tool environment | Node, packages, chosen model endpoints | pytest + JSON fixtures | Helpful UI/reporting once evaluation management is burdensome |
| Mailpit | Optional email feature development | Captures test SMTP messages in a local inbox | Dev/service | WSL tools, run when needed | Prebuilt executable; local ports/storage | Framework in-memory mail backend | No real email delivery or cloud account needed for tests |

For a small FastAPI service, start with `fastapi` and `uvicorn`, not every optional extra. The official docs distinguish core from `standard` extras, which bring additional convenience dependencies. Python wheels are prebuilt packages: using them avoids compiling Rust/C/C++ locally, but bundled native libraries still need security updates. Psycopg's pure Python installation still needs `libpq`; its binary extra is easier initially but bundles native components. [FastAPI dependencies](https://fastapi.tiangolo.com/#dependencies), [Psycopg installation](https://www.psycopg.org/psycopg3/docs/basic/install.html), [SQLAlchemy architecture](https://docs.sqlalchemy.org/en/20/intro.html), [Alembic](https://alembic.sqlalchemy.org/en/latest/).

Keep business decisions in plain modules and side effects at the edges. For example: `api/` translates HTTP, `services/` applies a business rule, `db/` persists it. Do not automatically build generic repositories, dependency-injection containers, microservices, or an interface for every class. Add a boundary when it explains a responsibility or makes a real change/test easier.

For Python diagnostics, start with standard-library `logging`, debugger support and pytest's captured logs. Coverage.py or pytest-cov is optional for finding untested branches; coverage percentage does not establish test quality. The `pre-commit` framework is optional convenience once several checks need orchestration; begin with one explicit check script and repeat required checks in CI. [pytest logging](https://docs.pytest.org/en/stable/how-to/logging.html), [Coverage.py](https://coverage.readthedocs.io/en/latest/), [pre-commit](https://pre-commit.com/).

For an AI/RAG application, start with a small evaluated pipeline: documents with source IDs → simple chunks → lexical retrieval → selected context with citations → one model call. Test retrieval separately from answer quality, with relevant-document labels, unanswerable questions and hostile content. Add one embedding model and pgvector only if this misses important paraphrases; record model/version/dimensions and reindex after incompatible changes. Add a reranker, agent loop, tracing platform or durable workflow engine only for measured failures. Bound model spending, tool calls and latency; keep redacted structured logs before introducing an observability stack.

### Frontend, testing, browser and design

| Dependency | Required? | Purpose | Type | Installed where | Depends on | Alternative | Why chosen |
|---|---|---|---|---|---|---|---|
| HTML/CSS/JS + browser | Yes for web UI | Prototype and application interface | Runtime | Project files / browser | Browser | Framework when needed | Zero package prototype possible |
| React + React DOM | Conditional | Stateful component UI | Runtime | Project `node_modules`, built output | JS/browser | Vanilla JS, Vue or Svelte | Reasonable larger-app default; transferable to React Native concepts |
| TypeScript + applicable type packages | With larger TS UI | Static checks | Dev/build | Project | Node; compiler | JS with careful tests | Makes data contracts visible; not a runtime validator |
| Vite + React plugin if applicable | With bundled web app | Dev server and production build | Dev/build | Project | Node; current Rolldown/native build components | No bundler for simple HTML | Fast iteration; not a production backend |
| Biome | New JS/TS projects | Formatting/linting | Dev | Project | Platform binary | Existing ESLint + Prettier | One default tool; retain existing mature setup instead of replacing it gratuitously |
| pytest, Ruff, mypy | Python projects | Tests, formatting/linting, static types | Dev | Project dev group | Python/platform wheels; pytest pluggy etc. | unittest; existing checker | Three different jobs, not three competing linters |
| Playwright CLI | Browser exploration | Operate page, snapshots, screenshots | Dev | Isolated tools workspace | Node + browser engine + OS libraries | Existing client browser; MCP if needed | On-demand instructions and bounded outputs |
| `@playwright/test` | Persistent E2E/visual tests | Repeatable user-flow checks | Dev | App project | Node + matched browser revision | Existing test runner | Tests become part of the repository |
| Chromium initially | With Playwright | Actual browser execution | Dev/system | Playwright browser cache | Linux shared libraries/fonts | Firefox/WebKit added by target | One engine first; add others deliberately |
| Vitest | Conditional JS logic/component tests | Fast frontend tests | Dev | App project | Node; Vite ecosystem | Existing framework runner | Do not install for a static sketch |
| Testing Library / axe integration | When component/a11y tests need them | User-oriented assertions / automated accessibility checks | Dev | App project | Framework adapters / Playwright | Manual keyboard checks still required | Targeted tests, no claim of complete accessibility coverage |
| Excalidraw | Optional | Sketches and diagrams | Design | Local/self-hosted app or chosen web app | Browser; Node only if hosting/building | Paper; Mermaid | Useful without MCP |
| Penpot | Optional heavier design stage | Editable components/design handoff | Design/service | Self-hosted stack or hosted account | Backend/frontend, PostgreSQL, supporting services per pinned compose | Excalidraw + HTML | Add only for durable design work |
| Storybook | Optional established component system | Component states and documentation | Dev/build | UI project | Framework, builder and addons | A `/dev/components` page | Too much setup for one disposable screen |

Modern Vite documentation now describes Rolldown; do not mechanically copy old “Vite always means esbuild plus Rollup” dependency maps. Pin the chosen version and inspect its manifest. Playwright's browser binaries and Linux libraries are real dependencies even though `package.json` alone does not show them. [Vite guide](https://vite.dev/guide/), [Biome](https://biomejs.dev/), [Vitest guide](https://vitest.dev/guide/), [Playwright browser installation](https://playwright.dev/docs/browsers).

### Memory, security, voice and specialist dependencies

| Dependency | Required? | Purpose | Type | Installed where | Depends on | Alternative | Why chosen |
|---|---|---|---|---|---|---|---|
| Curated notes + Git for nonsensitive records | Yes, files only | Share decisions and lessons | Data/dev | WSL project/private folders | Existing file tools | Basic Memory later | Immediate useful memory |
| Basic Memory | Phase 3 conditional pilot | Shared MCP + indexed notes | Dev/service | Isolated WSL environment | Python >=3.12; 43 direct tagged requirements + transitives; SQLite | Files; optional custom FTS service | Existing product avoids writing a memory server |
| Gitleaks executable | Yes before publishing code | Detect likely secrets | Dev/security | WSL tools | Prebuilt binary | Another existing secret scanner | Local check distinct from dependency auditing |
| OSV-Scanner executable + data | Phase 4; manual audit earlier | Known vulnerable package versions; license inventory support | Dev/security | WSL tools | Binary, manifests, advisory data | pip-audit + npm audit | One cross-language entry point |
| Semgrep CE + reviewed local rules | Optional higher-risk app | Pattern-based security checks | Dev/security | Isolated tool environment | Runtime/native engine + rules | Ruff security rules for small Python work | Adds coverage only where useful |
| Syft | Optional release/container inventory | SBOM | Dev/release | Tools | Binary + artifact to inspect | Existing package-manager inventory | Separate inventory from vulnerability analysis |
| Trivy | Optional container/IaC project | Image/config scanning | Dev/security | Tools | Binary, databases, container artifacts | OSV plus targeted config review | Not an initial prerequisite; review current advisories |
| Handy + one speech model | Optional voice | Offline dictation | Host app/model | Windows | Microphone, app runtime, downloaded weights | whisper.cpp command-line workflow | Host hotkeys and microphone are simpler |
| Unity Editor/Hub + project packages | Unity only | Game authoring/builds | System/build/runtime | Windows | C# tooling, platform modules, licenses | Godot for a new project if suitable | Respect current Unity projects; don't load everywhere |
| Unity MCP bridge | Unity only, optional | Editor state/actions | Dev/service | Editor + local bridge | Specific editor version, bridge runtime | Native editor tests/logs/CLI | Stateful editor access can justify MCP |
| Blender | Blender only | 3D authoring/rendering | System/build | Windows | Bundled Python, graphics hardware | Existing DCC tool | Native Python automation first |
| Blender MCP | Optional | Interactive scene operations | Dev/service | Blender addon + local process | Python/uv bridge; optional asset services | Blender Python script | More authority and attack surface; on demand |
| Expo/React Native + Android tools | Mobile only | Native Android app | Runtime/dev/build | Explicit Windows toolchain or supported Linux setup | Node, JDK, Android SDK, Gradle, emulator/device | Flutter/Dart or native Kotlin | Reuse JS/React knowledge when it fits |
| Xcode + macOS | iOS native builds | Build, simulator, signing | System/build | Mac or chosen Mac build service | Supported Mac, Apple account | Hosted Mac build | WSL cannot supply Xcode |
| Tauri + Rust/Cargo + OS build tools | Desktop only | Package web UI as desktop app | Build/runtime | Target OS | Rust, WebView; Windows MSVC/WebView2 | PWA; Electron for Node integration | Consider only when a real desktop capability is needed |

The native mobile/desktop stacks are alternatives to building a web-only product, not foundation installs. Docker is not required by Git, uv, FastAPI, SQLite, PostgreSQL, Playwright, or the file-first memory design. If a selected self-hosted design stack uses Compose, Docker becomes its optional infrastructure dependency. Docker Desktop has license eligibility conditions; “Docker” is not a blanket free/open-source claim. [Expo local build requirements](https://docs.expo.dev/guides/local-app-development/), [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/), [Docker Desktop Windows documentation](https://docs.docker.com/desktop/setup/install/windows-install/).

## 13. Dependency Graph

Branches group components; arrows show a dependency or stated interaction, not a requirement to install every optional component. R = chosen foundation, O = optional/conditional, D = development-only, C = cloud.

```text
Windows [R, existing]
├── Cursor UI [existing] ── WSL workspace connection
├── Handy [O] ── microphone + local speech-model file
├── Unity / Blender / Android Studio [O, only corresponding projects]
└── WSL2 → Ubuntu [R]
    ├── Git + Bash + ripgrep [R]
    ├── uv executable [R; does NOT require Python]
    │   └── downloads/manages project Python [R for Python]
    │       ├── standard library → SQLite / JSON / logging
    │       ├── pytest + Ruff + mypy [D]
    │       ├── FastAPI [O] → Starlette + Pydantic
    │       │   └── Pydantic → pydantic-core native wheel
    │       ├── Chosen ASGI app server [O] → Uvicorn
    │       ├── SQLAlchemy [O] → one chosen driver/database path:
    │       │   ├── sqlite3 → SQLite
    │       │   └── Psycopg → PostgreSQL [O service]
    │       └── Alembic [O deployment tooling] → SQLAlchemy
    ├── Node 24 LTS → npm [O until web/browser work]
    │   ├── React + React DOM [O runtime]
    │   ├── TypeScript + Vite + Biome [D]
    │   ├── Playwright CLI / Test [D] → Chromium + OS libraries
    │   └── Vitest / Storybook [O,D]
    ├── Claude/Codex CLI → selected model provider [C or supported local path]
    ├── shared skill files + deterministic check scripts [R,D]
    ├── Gitleaks + OSV-Scanner [D] → advisory data for OSV
    └── Basic Memory [O, phase 3, isolated environment]
        ├── Python + MCP/HTTP/runtime dependencies
        ├── curated Markdown + SQLite index
        └── optional local embedding weights [OFF initially]

Optional application edges:
AI feature → ONE SDK → hosted model [C] OR local Ollama → weights + hardware
RAG → lexical search first → pgvector [O] inside existing PostgreSQL
Public deployment → ONE host [C] + backup target + optional email provider [C]
iOS native release → macOS/Xcode + signing + Apple developer program
```

Neither PostgreSQL nor Python depends on Docker. Neither the voice app nor local speech recognition requires your WSL Python environment. A tool written in Rust or Go does not require installing that compiler when you use its prebuilt binary.

## 14. Dependency Decision Guide

| Problem | Default | Alternatives and when to switch | Reason / avoid |
|---|---|---|---|
| Python packages and environments | **uv** | pip + venv + pip-tools for an existing compatible project; keep Poetry if already established; Conda for a scientific stack genuinely depending on its native packages | uv covers environments, locking, Python and tool execution; don't stack four managers |
| JavaScript packages | **npm** | pnpm for a substantial workspace or measured disk/performance pain; keep Yarn if a project already uses it; Bun when its runtime/toolchain is an explicit project decision | npm is bundled and familiar; one lockfile owner |
| Backend HTTP API | **FastAPI** for API/AI service | Django for integrated users/admin/forms/data-heavy business app; Flask for small established apps without stronger typed API needs | Smallest total system can be a larger integrated framework; fewer direct packages alone is not the goal |
| HTTP client | **urllib** for a tiny simple request; **HTTPX** for application HTTP | requests for a sync-only existing codebase; aiohttp when its async ecosystem or server/client integration is specifically needed | HTTPX unifies sync/async and API testing; don't install all three |
| Query layer | **Parameterized SQL first; SQLAlchemy for a substantial schema** | Django ORM with Django; raw Psycopg when queries are few and explicit | Teach SQL and transactions before hiding them |
| Schema changes | **Alembic with SQLAlchemy** | Django migrations with Django; explicit numbered SQL for genuinely tiny databases | Automatic generation is a draft; inspect destructive changes and data migrations |
| Database | **SQLite for local/simple apps; PostgreSQL for shared production data** | Other databases only for demonstrated data/access needs | Do not use SQLite as a fake substitute in tests for PostgreSQL-specific behavior |
| Vector search | **No vector database until needed; then pgvector if using PostgreSQL** | Qdrant when isolation, scale, filtering or retrieval operations justify a separate service | Embeddings add model/version/data-rebuild costs |
| AI-development memory | **Curated notes, then Basic Memory pilot** | QMD for search-only pain; Graphiti for measured temporal relationship failures | Memory operations and application RAG are different workloads |
| Python testing | **pytest** | unittest when no third-party runner is warranted or project already uses it | Fixtures and readable failures help mentoring |
| Browser | **Playwright CLI for exploration, Playwright Test for regression** | Existing integrated client browser; MCP for integration-specific state/tools; DevTools for performance/network diagnosis | Exploration is not a committed automated test |
| Formatting/linting | **Ruff for Python; Biome for a new JS/TS project** | Existing ESLint/Prettier or framework plugins when coverage requires them | Avoid two formatters fighting over the same files |
| Type checks | **mypy for Python; tsc for TypeScript** | Keep Pyright/another checker when established; evaluate newer checkers against real code before switching | A linter is not a type checker; type checks are not input validation |
| Public deployment | **No provider in foundation; local first. Static preview: Cloudflare Pages. Python service: one managed host such as Railway when shipping.** | Self-hosted Linux/systemd for control when you're ready for patching, TLS and backups; Vercel for suitable frontend workloads | A VPS is not free to operate and home hosting is not equivalent to managed production |
| Email | **Mailpit or framework mail capture during development; one delivery provider for production** | Resend is a reasonable hosted candidate; self-host SMTP only with operational expertise | A test inbox is not a production delivery service |
| Local inference | **Ollama, optional, local-only profile** | llama.cpp for tighter configuration/control or a single portable server | Benchmark your hardware; model weights have their own licenses |
| Dictation | **Handy** | whisper.cpp if you want to maintain the capture/hotkey/paste plumbing; paid dictation only after a local trial fails | Runtime benchmarks must be measured on your machine |
| Agent/RAG framework | **Plain functions + one SDK + tests** | Pydantic AI for complex typed tool orchestration; LangGraph for durable resumable workflows; LlamaIndex for substantial ingestion/retrieval integrations | Do not install all three, or use one to orchestrate your ordinary coding sessions |
| Mobile | **Expo/React Native when sharing React knowledge helps** | Flutter if its UI/runtime tradeoffs suit the product; native Kotlin/Swift for platform-specific behavior | Decide from product requirements; not every app needs store distribution |
| Desktop | **Web/PWA until native features are needed** | Tauri for web UI + controlled native capability; Electron when Node integration or its ecosystem materially simplifies the app | Tauri adds Rust/native build tools; Electron adds a bundled browser/runtime |

Package-manager alternatives are real tradeoffs: pnpm uses a shared content store and stricter dependency layout; modern Yarn defaults to Plug'n'Play with integration considerations; Bun is also a runtime, so adopting it can change more than package installation. Conda manages non-Python packages as well. [pnpm](https://pnpm.io/motivation), [Yarn PnP](https://yarnpkg.com/features/pnp), [Bun](https://bun.sh/docs/runtime), [Conda packages](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/packages.html), [pip-tools](https://pip-tools.readthedocs.io/en/latest/), [Poetry](https://python-poetry.org/docs/basic-usage/).

For outbound requests, the standard library is sufficient only while code remains clear. A small package can reduce more complexity than it adds. HTTPX offers sync and async APIs; aiohttp is async-oriented. [HTTPX](https://www.python-httpx.org/), [aiohttp](https://docs.aiohttp.org/en/stable/). SQLite and PostgreSQL solve different deployment/concurrency needs. [SQLite use cases](https://www.sqlite.org/whentouse.html), [PostgreSQL support policy](https://www.postgresql.org/support/versioning/), [pgvector](https://github.com/pgvector/pgvector).

An SDK does not remove the model service dependency. “OpenAI-compatible” describes a protocol subset, not guaranteed equivalence in tool calling, structured output, streaming, or context size. Keep the model boundary small and test the features your application uses. [LangGraph scope](https://docs.langchain.com/oss/python/langgraph/overview), [Pydantic AI](https://pydantic.dev/docs/ai/overview/), [LlamaIndex](https://developers.llamaindex.ai/python/framework/), [Promptfoo](https://www.promptfoo.dev/docs/intro/).

### Hosted services: choose for the product, not the agent environment

| Candidate | Useful fit / current constraint | Local or simpler alternative / portability |
|---|---|---|
| [Cloudflare Pages](https://developers.cloudflare.com/pages/functions/pricing/) | F2/F3 static hosting; static assets and Functions have different billing/limits | Local static preview; portable HTML assets. Workers-specific application bindings add migration work |
| [Railway](https://docs.railway.com/pricing/plans) | F2/F3 Python service candidate; current Free plan has limited credits; Hobby is $5/month including $5 resource usage, with additional usage billed | Local Uvicorn + PostgreSQL; later Linux hosting if you can operate TLS, patching and backups. Keep deployment configuration small |
| [Vercel](https://vercel.com/docs/plans/hobby) | F2/F3 useful frontend deployments; Hobby restricts use to personal, non-commercial projects | Local Vite/build output; Cloudflare or a suitable host for the actual workload. Do not assume every hobby-sized business qualifies |
| [Neon](https://github.com/neondatabase/neon) | F2/F3 hosted PostgreSQL candidate when database operations/branching justify another provider. Official repo confirms free-tier availability; exact current pricing pages could not be fetched reliably in this audit | Plain local PostgreSQL for development. Do not self-host Neon's distributed storage stack merely to obtain PostgreSQL; standard SQL/drivers and exports reduce migration cost |
| [Resend](https://resend.com/pricing) | F2/F3 transactional delivery; observed free allowance 3,000/month with 100/day limit; paid service if volume/features require it | [Mailpit](https://github.com/axllent/mailpit), F0/MIT executable, for development only. Bind its SMTP/UI to loopback. Self-host SMTP adds reputation, DNS and delivery operations |

Prices/conditions above were checked September 20, 2026; no free tier is a production uptime promise. Neon quota/price remains explicitly unverified. Choose a database near the application, account for backups, egress, idle/sleep behavior and spending alerts. Do not create a separate provider account for every layer by habit.

For store distribution, budget the currently listed **Apple Developer Program US$99/year** (regional pricing/eligible waivers vary) and **Google Play US$25 one-time registration**; commercial transaction fees and policies are separate. New personal Play accounts have testing and device-verification requirements; current guidance describes 12 opted-in testers for 14 continuous days before applying for production access. WSL cannot replace macOS/Xcode for iOS native builds. [Apple enrollment](https://developer.apple.com/help/account/membership/program-enrollment), [Play registration](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en), [Play testing](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en).

### Manifest literacy

| File/concept | What it tells you | What to teach when it changes |
|---|---|---|
| `pyproject.toml` | Python project metadata, allowed dependencies, dev groups, build backend | Why each direct package belongs and whether it ships |
| `uv.lock` | Exact resolved packages, sources, hashes and platform choices | Direct vs transitive packages; review surprising additions |
| `.python-version` / `.venv` | Selected interpreter / disposable isolated environment | Interpreter and package environment are different things |
| `requirements.txt` | A requirements/install input, sometimes a generated lock-style export | It is not automatically fully pinned or hashed |
| `package.json` | JS direct dependencies, devDependencies, scripts, engine constraints | Scripts execute code; browser build dev tools may still affect production output |
| `package-lock.json` | npm's resolved dependency graph and integrity data | Commit it; `npm ci` checks consistency and performs a clean install |
| `peerDependencies` | A package expects the host app to supply a compatible companion | A plugin asking for React is different from privately bundling it |
| Unity `Packages/manifest.json` and `packages-lock.json` | Direct and resolved Unity packages | Asset Store assets and native plugins may live outside this graph |
| apt packages and `PATH` | OS packages and executable search order | `PATH` finds programs; it does not install them or activate a Python environment |
| `Dockerfile` / image digest | OS base and build/runtime contents | Containers also contain dependencies and need patching |

Version constraints such as `>=x,<y` describe allowed versions; the lockfile records the actual selected ones. Native dependencies can vary by OS and CPU even with one logical lockfile. Runtime imports should be declared directly even when a framework currently installs the package transitively. [uv dependency groups](https://docs.astral.sh/uv/concepts/projects/dependencies/), [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/).

Use a short **dependency decision record** only for architectural choices: capability, chosen dependency/version family, runtime/dev/build/service/model role, considered alternatives, license, source, native/transitive costs, removal difficulty, lock-in, and revisit trigger. “Removed X → API cannot serve requests” teaches more than “X is industry standard.”

## 15. Dependency Budget

Count **declared direct packages**, **transitive resolved packages**, **tool applications**, and **running services** separately. Combining them into one reassuring number hides cost.

| Budget | Foundation | Python + substantial web project | After optional memory phase |
|---|---|---|---|
| Core skill directories | 12 planned; install progressively | Same 12 | Same; memory skill only when needed |
| OS/system packages | WSL2 + Ubuntu; verify supplied Bash, coreutils, man, CA certificates and apt; add Git/ripgrep if missing | Add only the chosen browser's Linux libraries/fonts; PostgreSQL/libpq if selected | No separate database daemon for SQLite; inspect any additional native requirements |
| New Python runtime packages | 0 for the AI procedures | Example: FastAPI, Uvicorn; optional Pydantic direct import, SQLAlchemy, Psycopg, provider SDK | Basic Memory isolated from project; **43 direct runtime requirements in audited tag**, plus transitives |
| Python dev packages | 3 per Python project: pytest, Ruff, mypy | HTTPX only if testing API/outbound client; Alembic if schema needs it | No project contamination |
| JS direct runtime packages | 0 | Example React UI: React + React DOM | No change |
| JS dev packages | 0 until web work | Example 8: TypeScript, `@types/node`, `@types/react`, `@types/react-dom`, Vite, React plugin, Biome, Playwright Test; Vitest optional | No change |
| Agent browser tool | 0 initially | Reuse project's CLI when supported; otherwise 1 isolated Playwright CLI application | No change |
| Security binaries | Gitleaks; OSV added by phase 4 | Same; no redundant scanner suite | Same |
| Package managers | apt + uv; npm when Node needed | 3 roles total, **2 language managers** | Same |
| Always-running additional services | **0** | **0** required; app/database run during work | **1** local memory service if pilot passes |
| MCP servers | **0** | Usually 0 | **1** memory; temporary editor/design MCP only when needed |
| Mandatory new cloud services | **0** beyond existing AI choices | 0 for local work | 0 |
| Production providers | 0 | Target 1 host + database arrangement; email/model service only if app needs it | Memory remains local |

These examples are transparent counts of this proposed manifest, not an installed bill of materials. OS packages supplied by Ubuntu are inventory items, not all new installations; their resolved count depends on the existing distribution and selected features. Tool applications and language packages are counted separately. A frontend scaffold may add packages; remove unused template dependencies deliberately. Count an isolated Playwright CLI application separately when needed; reusing the project's exposed CLI adds no second direct package merely for exploration.

**Complexity alarms:** a second memory engine; a second JS package manager in one project; Redis without a queue/cache requirement; three hosted vendors for a tiny app; Docker solely to run SQLite; semantic indexing before keyword search is inadequate; a graph database for a few relationships; an agent framework for a sequential script.

Show `uv tree` or `npm ls` when a dependency is added, then explain only the meaningful new branches. For architecture drift, add import-linter contracts in Python or dependency-cruiser in JS only when there is a real boundary to enforce. Graphviz is optional for rendered dependency-cruiser graphs, not a requirement to list dependencies. [Import Linter](https://import-linter.readthedocs.io/en/stable/), [dependency-cruiser](https://github.com/sverweij/dependency-cruiser).

## 16. Dependency Safety Strategy

**Use reproducible installs and reviewed updates. Do not mistake a clean vulnerability scan for proof that a package is trustworthy.**

1. **Before adding:** identify the exact owner/package name from official docs; inspect license, current maintenance, supported runtimes, manifest, install hooks and native builds. Compare the standard library and existing packages. Check advisories. Look for unexpected executable downloads or credentials/network access. Write a decision record for major additions.
2. **Lock:** commit `uv.lock` and `package-lock.json`; pin tool versions and browser revisions in the environment record. Pin CI actions to reviewed full commit hashes and container images to digests where appropriate. Preserve licenses/notices when vendoring skills.
3. **Install safely:** prefer publisher releases, verified package registries and signed OS repositories. Download shell installers to a file and inspect them, or use verified release binaries. Do not paste `curl | sh` as the default. `npx`, `uvx`, skill installers and plugin installation also execute downloaded code; they are not harmless lookups.
4. **Check locally:** Gitleaks for secrets; OSV for supported lockfiles; Ruff's selected security rules for Python patterns. OSV currently lists both `uv.lock` and npm lockfiles. Use pip-audit when Python-environment/SBOM coverage specifically helps; npm audit is already available. Do not install both additional auditors merely to produce duplicate alerts. [OSV supported artifacts](https://google.github.io/osv-scanner/supported-languages-and-lockfiles/), [pip-audit](https://github.com/pypa/pip-audit).
5. **Control update intake:** weekly manual review initially; Dependabot on GitHub or Renovate when cross-host/self-host requirements justify it, not both. Limit open update branches. Separate major updates and group low-risk related patches. Do not auto-merge initially. [Dependabot](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates), [Renovate](https://github.com/renovatebot/renovate).
6. **Evaluate:** changelog → affected behavior → small upgrade branch → lockfile diff → clean install → type/lint/tests → relevant browser/security checks → manual review → merge. Security urgency may justify accelerating review, not skipping verification.
7. **Recover:** keep the previous lockfile and deployable artifact. An application rollback does not automatically reverse a destructive database migration. Prefer compatible expand/migrate/contract changes and verify a backup before risky migrations.
8. **Remove:** delete unused direct packages, regenerate the lockfile, inspect remaining dependents, run relevant tests and build. Do not remove a transitive package by editing the lockfile manually.

For untrusted JS packages, use an inspection/sandbox workflow with lifecycle scripts disabled initially; allow required scripts only after understanding them. `--ignore-scripts` can break legitimate native packages and is not a complete sandbox. Python source distributions can run build code too; prefer compatible wheels when practical, but wheels are not a security certification. [npm install behavior](https://docs.npmjs.com/cli/v11/commands/npm-ci/), [uv binary/source behavior](https://docs.astral.sh/uv/pip/compatibility/).

**Scanner privacy:** remote advisory queries can reveal package names/versions. OSV offers offline data mode; refresh its database, record the date, then scan offline when confidentiality matters. Gitleaks can scan locally with redaction. Semgrep registry use enables metrics by default; explicitly disable metrics and use reviewed local rules for the private profile. License rules and engines may have different licenses. [OSV offline mode](https://google.github.io/osv-scanner/usage/offline-mode/), [Gitleaks](https://github.com/gitleaks/gitleaks), [Semgrep metrics](https://docs.semgrep.dev/metrics).

Trivy deserves a current-source caveat: the maintainers documented a **March 19, 2026 supply-chain compromise**, including a malicious release and altered Action tags, followed by remediation. This does not establish that current Trivy is abandoned or unusable. It does mean old pinned-looking tags and generic install snippets are insufficient evidence of safety. Consult the affected-artifact advisory and later fixes before using it; no default container scanner is needed before you use containers. [Trivy advisory](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23), [maintainer conclusion, March 30](https://github.com/aquasecurity/trivy/discussions/10462).

An SBOM is an inventory of software components, not a vulnerability verdict or legal opinion. Generate one with an existing auditor or Syft when distributing a release/container. Inspect license text and distribution context; unresolved/copyleft/asset/model terms go to a human review path. Known-CVE scanners cannot reliably identify new malicious packages or every compromised maintainer account. [Syft](https://github.com/anchore/syft), [OSI license texts](https://opensource.org/licenses).

## 17. WSL / Ubuntu Setup

This is an installation **order**, with reasons before commands. Do not reinstall a working setup just to match a diagram. First inventory the current Windows version, WSL distributions, free disk/RAM, GPU, existing clients, Python/Node locations, and package managers. No hardware assumptions were made in this report.

| Order | What / why | What depends on it | Optional? / verification |
|---|---|---|---|
| 1 | WSL2 and Ubuntu 24.04 LTS provide a stable Linux workspace | Linux CLI development | WSL is the chosen path, not compulsory for all Windows tools; verify distribution/version |
| 2 | Create Linux user; learn home directory and normal permissions | All Linux work | Required; explain why daily coding does not need root |
| 3 | Apply OS updates; confirm Git, certificates, Bash/help; add ripgrep | Secure downloads, history, source inspection | Git/ripgrep useful; most shell tools already exist |
| 4 | Put Linux projects under `~/projects` and configuration under `~/ai-dev-system` | Linux file performance and clear boundaries | Required convention; do not put active Linux `node_modules` on `/mnt/c` |
| 5 | Connect Cursor to the WSL workspace; run Claude/Codex CLIs in that environment as supported | Consistent paths and tool execution | Keep host/WSL configurations distinct; verify where a command actually runs |
| 6 | Install a reviewed uv release binary; let uv manage project Python | Python app/tests | Required for Python; no separate Poetry/pyenv/pipx install needed |
| 7 | Make one learning project; add pytest, Ruff, mypy as dev dependencies | Core engineering cycle | Verify a failing test, fix it, run checks, explain diff |
| 8 | Install Node 24 LTS with npm when frontend/browser work starts | Vite/Playwright/web tooling | Optional until then; use one installation method, no redundant version managers |
| 9 | Add selected skill folders + tiny adapters | Consistent AI behavior | Test discovery per client; no global skill-marketplace dump |
| 10 | Add browser tool, one engine and its documented Linux dependencies | UI verification | Verify local screenshot + intentional console/error check |
| 11 | Add scanners and optional voice | Security and dictation | Gitleaks early; OSV phase 4; Handy on Windows |
| 12 | Pilot shared memory, then other specialists one at a time | Cross-client recall | Only after prior layers work; dummy-data tests first |

Microsoft recommends storing Linux-used project files in the Linux filesystem. Keep host-native Unity, Blender and Android projects where their native tools work reliably; this is not a universal “everything belongs in WSL” rule. Keep `.venv` and `node_modules` separate between operating systems. [WSL environment guidance](https://learn.microsoft.com/en-gb/windows/wsl/setup/environment), [WSL interoperability](https://learn.microsoft.com/en-us/windows/dev-environment/wsl-interop).

A beginner shell lesson should accompany actual use:

| Example | Explanation |
|---|---|
| `pwd` | Shows your current directory; inspect this before file operations |
| `ls -la` | Lists files, including hidden ones; `-l` shows details, `-a` includes dotfiles |
| `command -v python` | Shows which executable your shell would run |
| `git diff` | Shows uncommitted content changes; learn to review before committing |
| `uv sync --locked` | Uses the committed resolution and fails if it needs updating |
| `uv run pytest` | Runs tests in the project's managed environment |
| `npm ci` | Recreates dependencies from the lockfile; replaces `node_modules` |
| `man chmod` | Opens authoritative local permission documentation before changing modes |
| `Ctrl+C` | Requests an interrupt of the foreground process; it does not undo its changes |

Teach `~`, absolute vs relative paths, executable permissions, processes/ports, environment variables, redirects/pipes and quoting as needed. Avoid `sudo pip`, blanket `chmod 777`, and giant setup scripts. Before a destructive action, state the exact target and recovery plan. ShellCheck helps diagnose scripts; man pages remain the detailed reference; tldr offers examples rather than authority. [ShellCheck](https://www.shellcheck.net/), [tldr](https://tldr.sh/).

Installers that add entries to `PATH` should be followed by inspection of the changed shell file. Use release archives/checksums/attestations when available; a checksum hosted beside a compromised artifact alone is not independent proof of authenticity. The uv release page offers binary artifacts and attestation instructions. [uv release artifacts](https://github.com/astral-sh/uv/releases).

## 18. Cost Report

**The proposed local foundation can add $0 in recurring software charges beyond your existing AI choices.** This assumes you already have a suitable Windows computer. Storage, backups, electricity, microphone quality, RAM/VRAM and your time remain costs. A local model that fits in memory may still be too slow or inaccurate for your work; this report contains no hardware benchmark.

The table groups every recommended component, including conditional additions. **F0** means free local open-source software without a required model API; **F1** means open/local-capable software or procedures whose AI use needs a model; **F2** means a hosted free tier; **F3** means paid. Mixed labels describe separate deployment choices, not a promise that an entire product is free.

| Component group | Class / local and open? | API or recurring charge |
|---|---|---|
| Existing Windows and coding clients | Windows/client licenses are separate; existing subscriptions are F3 where applicable | Keep your current account arrangement; subscription access and application API billing are different |
| WSL2/Ubuntu; Git, Bash/coreutils, man, certificates, ripgrep | F0 local development layer on the existing host | No model API; normal package/security updates need network access |
| uv, project Python, Node/npm; optional ShellCheck and tldr/tealdeer | F0, local | No subscription; runtimes and packages occupy disk |
| Rules, adapters, 12 skills, three role templates, scripts, evaluation fixtures | F1 procedures; locally stored, source licenses retained | Use the selected coding model; no additional API is inherent in a skill file |
| pytest, Ruff, mypy; HTTPX when needed; optional Coverage.py/pytest-cov and pre-commit | F0, local | No model/API charge for checks; optional packages solve specific reporting/orchestration needs |
| FastAPI/Uvicorn/Pydantic; SQLite; PostgreSQL/Psycopg; conditional SQLAlchemy/Alembic | F0, local-capable | Hosted database/server optional; backups and administration remain your responsibility |
| HTML/CSS/JS; React/React DOM, TypeScript/types, Vite/plugin, Biome | F0, local development | No deployment provider required for local work |
| Playwright CLI, Playwright Test, Chromium; conditional Vitest, Testing Library, axe | F0 tools; F1 agent operation | Browser downloads and native libraries; model cost only when the agent consumes results |
| Excalidraw, Mermaid; optional Penpot and Storybook | F0 local/self-hosted choices; hosted offerings can be F2/F3 | Penpot self-hosting adds services; commercial visual testing is optional |
| Markdown/JSON notes, SQLite; Basic Memory lexical local pilot | F0 storage/server; F1 curation | No required model API; optional embeddings/cloud features change the cost profile |
| Gitleaks, OSV-Scanner; selected Ruff rules; optional Semgrep CE/local rules, Syft, Trivy | F0 local tools under their respective licenses | Advisory/rule updates; commercial platforms are optional |
| Dependabot **or** Renovate | Hosted service or open-source/self-hosted choice, according to deployment | Hosting/CI quotas or self-host operation may cost; neither is an initial requirement |
| Handy + one local speech model | F0 local app; inspect model terms separately | No transcription API required; optional model-based cleanup adds inference work |
| One AI provider SDK; optional Ollama or llama.cpp; later embeddings/pgvector and Promptfoo | F1/model-dependent; pgvector itself F0 | Hosted inference is usage-billed unless covered by an explicit offer; local weights need hardware and license review |
| Optional import-linter or dependency-cruiser; Graphviz if rendering | F0 local | No API; install only to enforce a real boundary |
| Unity + optional MIT bridge; Blender + optional bridge | Unity proprietary eligibility/paid terms; Blender open source; bridges separately licensed | Native toolchains; external assets/services may cost; no inherent paid LLM API in the bridge |
| Expo/React Native + Android tools; optional Tauri/Rust/native tools | Open-source/local build paths | Devices, signing and stores separate; iOS needs macOS/Xcode or a Mac build service |
| Optional Docker infrastructure | Engine and Docker Desktop have different terms | Desktop may require a paid subscription; containers do not remove host costs |
| Production host/database, domain, email and distribution | F2/F3 depending on actual provider and usage | Cloudflare Pages or one Python host such as Railway only when shipping; verify current limits before choosing |
| Conditional Neon / Resend; local Mailpit for email tests | F2/F3 hosted services; Mailpit F0/MIT | No foundation account needed. Local PostgreSQL substitutes for development DB; Mailpit does not deliver production mail. Current provider prices and store fees appear in section 14 |

The key cost boundaries are documented by the projects: [Playwright browser dependencies](https://playwright.dev/docs/browsers), [Penpot self-hosting](https://help.penpot.app/technical-guide/getting-started/), [Handy](https://github.com/cjpais/Handy), [Basic Memory's tagged license/dependencies](https://github.com/basicmachines-co/basic-memory/blob/v0.23.2/pyproject.toml), [Expo local builds](https://docs.expo.dev/guides/local-app-development/), [Docker Desktop terms and requirements](https://docs.docker.com/desktop/setup/install/windows-install/).

Prefer concrete substitutions over an ideological “all free” promise: Handy before paid dictation; Excalidraw/HTML before hosted design tooling; local notes before cloud memory; pytest fixtures before a hosted evaluation platform; local Playwright before commercial browser infrastructure. These cover learning and local development well. A local mail catcher tests message generation but does **not** provide production delivery, sender reputation or inbox placement. A home server does not automatically replace managed availability, and local models do not guarantee cloud-model capability. Price the production product separately from this development environment.

## 19. Context Budget

These are **relative estimates and operating targets, not measured savings**. Context usage varies with model, client version, skill discovery, tool-search/deferred-loading support, output formatting and conversation length. Money, context-window occupancy, CPU use and latency are different budgets.

| Category | Proposed budget | Relative cost and control |
|---|---|---|
| **A: always present** | One 250–450-word core policy; short skill names/descriptions; minimal project instructions | Low by design. Avoid duplicated rules, copied manuals and full agent rosters |
| **B: discoverable until selected** | Exactly 12 core skills; specialist library outside automatic discovery | Low metadata cost. Target roughly 500–1,500 tokens per adapted skill body when activated; references load separately |
| **C: invoked work** | Usually one primary skill and relevant references; scoped file reads, commands and results | Low to high. Browser snapshots, screenshots, broad searches and verbose errors can dominate |
| **C: memory, phase 3** | Search titles/snippets first; read a few relevant records | Start with a 500–1,000-token retrieval target. This is a workflow target unless an adapter enforces it, not a Basic Memory guarantee |
| **C: specialist agent** | One bounded question with a compact evidence return | Medium to high total consumption. Parallel work can reduce elapsed time while increasing aggregate tokens |
| **D: external/manual artifacts** | Local diagrams, voice recordings, dashboards, reports | No model context until shared; a transcript, screenshot or retrieved section then becomes C |

The Agent Skills format supports progressively loading instructions and references, but clients implement discovery and permissions differently. Check the actual inventory and active context rather than assuming identical behavior. [Agent Skills specification](https://agentskills.io/specification).

**CLI output still costs tokens when read by the model.** It is useful because it supports explicit invocation and narrow output, not because shell access is free. Playwright CLI can save artifacts to files and expose selected results; ask for the relevant region/error instead of repeatedly loading complete page snapshots. Persistent regression tests should print a concise result, with traces opened only after failure. [Playwright CLI skill](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md).

MCP is not automatically expensive either. A client may load catalogs or schemas upfront, or defer detailed definitions until discovery. Measure each of your three clients. Server results, images and repeated calls remain costs even with deferred schemas. Start with zero new MCP servers, later one memory endpoint, and disable specialist endpoints after their task.

For a useful baseline, repeat the same small change in a clean session, recording model/client versions, skills loaded, tool calls, output size, reported token usage where available, elapsed time, correctness and your ability to explain the result. Change one variable. Do not rank tools by a vendor's token-saving percentage from a different workflow.

## 20. Installation Phases

Each phase should produce a working, understandable capability before the next dependency arrives. The phases are an installation proposal; nothing in this report has been installed.

### Phase 0 — Foundation

**Install/confirm:** inventory the existing host first; establish WSL2 + Ubuntu 24.04 LTS, OS updates, Git, shell help, certificates and ripgrep. Add a reviewed uv binary and uv-managed project Python 3.13.x; install Node 24 LTS with npm when web/browser work requires it. Create Linux project/configuration directories. Connect existing clients to the intended workspace. Explain project environments, manifests and lockfiles. Add Gitleaks before publishing code; retain ordinary manual package review from the first install.

**Unlocks:** inspectable files, reproducible history and a clear Windows/WSL boundary. **Gate:** show where commands run, inspect a diff, restore a disposable file from Git, and verify a synthetic secret is detected without exposing a real credential. No new MCP service or always-running background service. [Microsoft's filesystem guidance](https://learn.microsoft.com/en-gb/windows/wsl/setup/environment), [Gitleaks](https://github.com/gitleaks/gitleaks).

### Phase 1 — Core engineering and mentoring

**Install:** pytest/Ruff/mypy in one learning project's dev group, using phase 0's Python environment. Add the tiny core policy and the 12 selected skill directories progressively; add the three role templates without launching them automatically. Record source commits/licenses and create minimal client adapters. Use the standard library before selecting an API framework.

**Unlocks:** clarify → plan → test → implement → review → verify, with dependency explanations and teach-back. **Gate:** complete one small feature with an intentional failing test, passing checks and a reviewed diff; each client discovers every skill once and reports the same deliberate failure. You can explain the module responsibilities and remove a disposable dependency. [uv projects](https://docs.astral.sh/uv/guides/projects/).

### Phase 2 — Visual feedback and voice

**Install:** using phase 0's Node/npm when needed, reuse the project's Playwright CLI if it exposes the required commands; otherwise isolate a pinned CLI installation. Add Chromium and documented Linux libraries/fonts. Add project Playwright Test only for durable flows. Start with HTML/CSS and a paper/Excalidraw sketch; React/TypeScript/Vite/Biome require an actual application need. Adapt the design/browser skills. Optionally install Handy's Windows binary and one speech model; no source-build toolchains for ordinary binary use.

**Unlocks:** sketch → executable screen → browser inspection → revision. **Gate:** verify one responsive screen, keyboard/focus behavior, one error state and a useful screenshot; save a repeatable test if the feature warrants it. Dictation must preserve identifiers and negations in a short trial. Continue with zero new MCP services. [Playwright browser requirements](https://playwright.dev/docs/browsers), [Handy](https://github.com/cjpais/Handy).

### Phase 3 — Shared memory pilot

**Install only after files become awkward:** Basic Memory in its own WSL environment, backed up Markdown and SQLite, keyword retrieval first. The audited **v0.23.2** requires **Python >=3.12**, declares **43 direct runtime requirements plus transitives**, is **AGPL-3.0-or-later**, and pins **FastMCP 4.0.0b1**, a prerelease dependency. Disabling semantic features does not uninstall their packages. Reassess the exact release before installation. [Tagged manifest](https://github.com/basicmachines-co/basic-memory/blob/v0.23.2/pyproject.toml).

**Configuration:** local routing, semantic/reranking features off initially, automatic updating off, telemetry export off; explicitly bind to `127.0.0.1`. The tagged HTTP server does not supply authentication. This is an **unauthenticated loopback pilot for a trusted personal account**, not a production-approved or multi-user service. Do not expose it to the LAN to solve a Windows/WSL connectivity problem. Verify the host-client route separately. [Tagged server](https://github.com/basicmachines-co/basic-memory/blob/v0.23.2/src/basic_memory/mcp/server.py), [HTTP security warning](https://docs.basicmemory.com/reference/docker/).

**Unlocks:** one shared endpoint for Cursor, Claude Code and Codex. **Gate, with dummy data:** bounded retrieval; cross-client read/write; correction/delete behavior; concurrent edits; conflict recovery; backup/restore; path-traversal and out-of-scope-file denial; project scoping; injection-resistance workflow; confirmed network/export settings. Project names are organizational namespaces, not demonstrated authorization boundaries. Review real records before writing them. If any critical gate fails, keep curated files and postpone the server.

### Phase 4 — Security and legal release gates

**Install:** OSV-Scanner and a documented advisory-data refresh process. Add selected Ruff security rules; choose Semgrep CE/local rules only for justified coverage. Use Syft for a release inventory where useful, and a container scanner only after containers appear. Select Dependabot or Renovate when manual updates become burdensome.

**Unlocks:** repeatable secret, dependency and release checks. **Gate:** detect a controlled vulnerable fixture, triage a false positive, inspect a license, produce a dependency inventory and demonstrate rollback. Record scanner/data dates. Use current official policy/legal sources for the product's actual jurisdictions and data; escalate unresolved legal questions. Memory's security gate already applies in phase 3. [OSV supported artifacts](https://google.github.io/osv-scanner/supported-languages-and-lockfiles/), [Syft](https://github.com/anchore/syft).

### Phase 5 — Continuous learning

**Install:** nothing initially. Add Git-reviewed learning-event records, evaluation fixtures and a manual review cadence. Optional Promptfoo follows a real need for larger comparison matrices.

**Unlocks:** evidence-based skill/model changes. **Gate:** reproduce a failure, propose a small procedure change, compare baseline/candidate on several cases, review tradeoffs and revert it. No autonomous global-rule rewriting or indiscriminate conversation capture.

### Phase 6 — Specialists and production

**Install one project-specific set at a time:** production API/database; RAG only after retrieval evaluation; Penpot/Storybook only for enduring design systems; Unity/Blender/editor bridge only during relevant projects; Expo/native builds or Tauri only for required platforms. Choose hosting/email/model providers from the product requirements.

**Unlocks:** a concrete new product capability. **Gate:** explain every runtime, native dependency, service, permission, license and ongoing cost; test export/recovery and removal; then ship a small slice. A specialist that never gets used should be removed from discovery and stopped.

## 21. Architecture of My Final AI Development Environment

```text
YOU: problem + sketch + acceptance criteria + prediction + teach-back
                                  |
             ONE ACTIVE LEAD CLIENT PER CHANGE
         Cursor (Windows/WSL) | Claude Code | Codex
                                  |
       +--------------------------+---------------------------+
       | SHARED LOCAL KNOWLEDGE AND PROCEDURES                 |
       | ~/ai-dev-system/                                     |
       | core rules -> 12 skills -> scripts + eval fixtures   |
       | 3 invoked roles; pinned sources; small adapters      |
       | specialist library stays outside auto-discovery     |
       +--------------------------+---------------------------+
                                  |
  +-------------------------------+--------------------------------+
  | WINDOWS HOST                  | WSL2 / UBUNTU 24.04            |
  | existing editor + browser     | Git, Bash/help, ripgrep        |
  | optional Handy + speech model | uv -> project Python 3.13.x   |
  | optional Unity / Blender      | Node 24 + npm when needed     |
  | optional native mobile tools  | selected security binaries    |
  +-------------------------------+--------------------------------+
                                  |
  +-------------------------------+--------------------------------+
  | PROJECT LAYER: ~/projects/<project>/                           |
  | requirements + diagrams + ADRs + dependency records + tests    |
  | Python .venv / uv.lock: stdlib; pytest, Ruff, mypy              |
  |   conditional: FastAPI/Uvicorn, data driver, ONE model SDK     |
  | Web: HTML/CSS first; conditional React/TS/Vite/Biome            |
  |   node_modules / package-lock; Playwright Test if needed       |
  | Playwright CLI -> Chromium: reuse project CLI if supported;    |
  |   otherwise use a separate pinned tools environment            |
  | Local app/browser processes run while needed                  |
  +--------------------------+-------------------------------------+
                             |
        +--------------------+--------------------------+
        | PRIVATE LOCAL MEMORY                          |
        | phases 0-2: reviewed files; NO new MCP server |
        | phase 3: ONE Basic Memory pilot endpoint      |
        | Markdown + SQLite; lexical first; backups     |
        | loopback, trusted account, acceptance gates   |
        +--------------------+--------------------------+
                             |
  =================== EXPLICIT NETWORK / DATA BOUNDARY ===================
       |                         |                           |
       v                         v                           v
  REQUIRED WHEN USING       OPTIONAL DOWNLOADS /        OPTIONAL PRODUCT
  YOUR CLOUD AI CLIENT      UPDATE SOURCES              CLOUD SERVICES
  chosen model/account      OS/package registries       one host + database
  prompts + selected        browsers/model weights      domain/email delivery
  files/tool results        advisories/docs/remotes     hosted model API
  follow provider terms     source/release verification signing/build services

  OPTIONAL LOCAL INFERENCE: Ollama OR llama.cpp + selected weights
  can serve compatible app/evaluation use; benchmark capability first.
  OPTIONAL SPECIALIST MCP: editor/design endpoint only while needed;
  keep it separate from memory and review its actual permissions.

  SHARED LEARNING FEEDBACK LOOP, LOCAL RECORDS / CHOSEN MODEL:
  verified result + your correction -> redacted learning event
     -> candidate skill/profile change -> evaluations + regressions
     -> your review -> versioned release -> portable skill layer above
```

The shared layer is a versioned set of knowledge and procedures, not a new autonomous agent platform. Packages belong to their projects; memory has a separate private data directory; external services enter only through an explicit product or model requirement. Local memory can still reach a cloud provider when a client inserts retrieved text into a prompt. Judge the system by whether you can explain, test, recover and maintain a small application with it.
