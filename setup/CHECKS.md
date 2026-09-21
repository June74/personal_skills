# Deterministic project checks

`scripts/run_checks.py` runs explicit argument lists from a reviewed JSON config, with no shell interpolation. **The commands themselves are executable code**; review an untrusted config before running. It does not install tools, fetch packages, auto-fix code or discover arbitrary npm scripts.

Copy `templates/checks.python.json` or `templates/checks.web.json`, adjust real source paths/scripts, and put it in your project. Preview:

```text
python /path/to/kit/scripts/run_checks.py --project /path/to/project --config /path/to/project/checks.json
```

Add `--run` to execute. Python example uses `uv run --no-sync` so missing tools fail rather than trigger dependency installation. Web example calls existing local tool entrypoints; it does not use an npx command that could download a missing package. On failure the runner preserves the nonzero outcome and stops; run more checks only when useful.

Use a narrow check while developing and the relevant suite before completion. A formatter check does not prove behavior. Review failures manually; do not suppress them. Outputs are shown to your terminal and can contain application logs, so use synthetic data and redact secrets at their source.

Before publishing, run a reviewed Gitleaks version with redaction. Use a reviewed OSV-Scanner against your lockfiles and record advisory-data freshness. Follow the selected version's help for flags; avoid hardcoding unstable scanner commands into an always-on hook. Add CI after local commands are understood. No hooks or scheduled updates are installed here.
