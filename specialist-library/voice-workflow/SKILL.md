---
name: voice-workflow
description: "Specify, build or evaluate the user's own dictation workflow, preserving technical vocabulary, pauses, corrections and safe text insertion."
---

# Custom voice workflow

The user intends to build their own voice tool. Do not replace that choice with a packaged dictation app or assume a speech engine has been selected.

Define microphone capture, hold/toggle hotkeys, transcription, optional cleanup, review and text insertion as separate responsibilities. On Windows/WSL, evaluate host capture and ordinary text insertion before adding Linux audio plumbing. Implement one end-to-end slice before a larger architecture.

Compare local transcription engines and model sizes against real hardware, language, latency and technical vocabulary. Explain runtime/build/native/model dependencies, downloads and licenses before introducing them. Reuse an existing inference runtime only if appropriate; cloud cleanup changes the data boundary.

Test actual receiving clients with pauses, file paths, identifiers, negation, numbers and false starts. Preserve corrections and uncertainty. Never auto-submit a command because speech stops. Use templates/voice-trial.md from the kit when available. Let the user choose retention of raw audio/transcripts. This skill is development guidance, not an implemented application.
