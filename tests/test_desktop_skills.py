"""Verify desktop skill deployment, including the workflow and invocation policy."""
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

KIT = Path(__file__).resolve().parents[1]
NAMES = (
    'desktop-boundary-probes', 'prototype-runtime-wiring',
    'async-side-effect-delivery', 'regression-test-credibility',
    'desktop-project-delivery',
)


class DesktopSkillTests(unittest.TestCase):
    def test_skills_remain_concise_and_model_invocable(self):
        total = 0
        for name in NAMES:
            folder = KIT / 'skills' / name
            text = (folder / 'SKILL.md').read_text()
            total += len(text.splitlines())
            frontmatter = text.split('---', 2)[1]
            self.assertNotRegex(frontmatter, r'disable-model-invocation:\s*true')
            metadata = (folder / 'agents/openai.yaml').read_text()
            self.assertRegex(metadata, r'(?m)^policy:\n  allow_implicit_invocation: true$')
        self.assertLessEqual(total, 200)

    def test_both_client_snapshots_include_complete_skills(self):
        with tempfile.TemporaryDirectory(prefix='desktop-skills-test-') as temp:
            for client, area in [('codex', '.agents'), ('claude', '.claude')]:
                with self.subTest(client=client):
                    project = Path(temp) / client
                    project.mkdir()
                    result = subprocess.run(
                        [sys.executable, '-B', str(KIT / 'scripts/prepare_client.py'),
                         '--client', client, '--project', str(project), '--apply'],
                        capture_output=True, text=True,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    for name in NAMES:
                        source = KIT / 'skills' / name
                        installed = project / area / 'skills' / name
                        for file in source.rglob('*'):
                            if file.is_file():
                                self.assertEqual(file.read_bytes(), (installed / file.relative_to(source)).read_bytes())
                        for link in re.findall(r'\]\((references/[^)]+)\)', (installed / 'SKILL.md').read_text()):
                            self.assertTrue((installed / link).is_file(), link)


if __name__ == '__main__':
    unittest.main()
