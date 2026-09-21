---
name: browser-check
description: "Inspect a real web UI, forms, console/network behavior, responsive layout or screenshots, and turn important flows into repeatable browser tests."
---

# Browser Check

Use the client's available browser tools or the project's reviewed Playwright CLI. Inspect the installed version/help before choosing commands. If an isolated CLI is needed, explain and pin it; never auto-install global latest packages or grant broad npm/npx execution permission.

Use a named session and test identity. Inspect scoped page regions, interact through observed element references, check console/network failures, and capture relevant screenshots. Check keyboard/focus, narrow/wide viewports and error states. Prefer short results and selected artifacts over repeated whole-page dumps.

CLI sessions can persist; MCP is not required merely for state. Choose an MCP browser interface when client capabilities or measured workflow results justify it. Avoid multiple controllers manipulating the same profile.

Keep auth-state files, recordings and traces out of Git and public outputs. They may contain cookies, headers, bodies and private page content. Browser actions still need task authorization, especially submission, purchase, publication or production mutations.

Save durable flows in project Playwright Test when worthwhile. Control browser revision, fonts, viewport and test data for screenshot baselines. Review changed baselines deliberately. Distinguish exploration, regression tests and accessibility coverage. Report what ran and what was not checked.
