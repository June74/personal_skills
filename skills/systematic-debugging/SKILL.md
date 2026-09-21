---
name: systematic-debugging
description: "Investigate unexpected behavior, failing tests or builds through reproduction and evidence before changing code."
---

# Systematic Debugging

Capture expected versus observed behavior, exact conditions, versions and a minimal reproducible case. Do not print secrets or full environment variables. Record presence, redacted metadata and safe synthetic data instead.

Trace the failing path across boundaries. Reduce inputs, compare a working case, inspect relevant logs/network/state and recent changes. Form one falsifiable hypothesis; select the smallest observation or experiment that distinguishes it. Instrument narrowly, run the experiment, and revise the hypothesis when evidence contradicts it.

Identify the cause before choosing the fix. Avoid unrelated cleanup and multiple speculative changes. When blocked, report what was ruled out and what missing evidence would help; do not conceal repeated failure with a larger rewrite.

Fix at the responsible boundary, add an appropriate regression test, reproduce the original case and run affected checks. Remove temporary instrumentation or retain it only if useful and safe. Explain the causal chain and why the fix addresses it.

Use the project's runner, browser and debugger. Do not copy Bash/npm-specific binary-search helpers into Python/Windows projects blindly. Test helper assumptions about filenames, exit codes and suppressed output before trusting their verdict.
