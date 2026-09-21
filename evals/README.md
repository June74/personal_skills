# Behavioral evaluation: manual, no API spending or client launch

The 16 cases cover triggers, restraint, tests, evidence honesty, privacy, memory and teaching. They are supplied for your first actual client/model trials; they have not all been run. `tests/test_helpers.py` tests deterministic helper behavior, not AI quality.

For each selected case, copy the fixture into a disposable project. Give the client the prompt and the minimum required files; keep expected criteria away from the executing agent until grading. Run an unchanged baseline and candidate using the same model, permissions and starting files. Record outputs/artifacts and score each criterion pass/fail/uncertain with evidence. Repeat important variable cases. Keep held-out cases out of prompt tuning.

Use result-template.json for each trial. Review teaching for accuracy, useful explanation and learner independence. No aggregate percentage should hide a failed privacy, permission or truthfulness condition. Missing measurements are null, not invented zeros. A human should judge design and explanation; model grading may supplement, not replace it.

Propose small changes from repeated supported patterns and counterexamples, rerun regressions, review, then version. No automated observers or self-rewriting global rules are enabled.
