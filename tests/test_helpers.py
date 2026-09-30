"""Deterministic tests only. Uses isolated temporary projects, no network."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

KIT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(KIT/'scripts'))
import prepare_client
from validate_memory import validate

class HelperTests(unittest.TestCase):
    def setUp(self):
        # All temporary files remain below the OS-designated temp directory.
        self.temp=tempfile.TemporaryDirectory(prefix='ai-dev-system-test-')
        self.root=Path(self.temp.name).resolve()
        self.assertTrue(self.root.is_relative_to(Path(tempfile.gettempdir()).resolve()))
        self.project=self.root/'project with spaces'; self.project.mkdir()
    def tearDown(self):
        # Validate the exact recursive-cleanup target before removing our temp tree.
        self.assertTrue(self.root.is_relative_to(Path(tempfile.gettempdir()).resolve()))
        self.assertTrue(self.root.name.startswith('ai-dev-system-test-'))
        self.temp.cleanup()
    def run_helper(self,name,*args):
        return subprocess.run([sys.executable,'-B',str(KIT/'scripts'/name),*map(str,args)],capture_output=True,text=True)
    def test_preview_writes_nothing(self):
        result=self.run_helper('prepare_client.py','--client','codex','--project',self.project)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(list(self.project.iterdir()),[])
    def test_apply_idempotent_and_core_only(self):
        for _ in range(2):
            result=self.run_helper('prepare_client.py','--client','codex','--project',self.project,'--apply')
            self.assertEqual(result.returncode,0,result.stderr)
        deployed=list((self.project/'.agents/skills').glob('*/SKILL.md'))
        self.assertEqual(len(deployed),17)
        self.assertFalse((self.project/'.agents/skills/mobile-release').exists())
    def test_conflict_preserves_file_and_no_partial_writes(self):
        sentinel=self.project/'AGENTS.md';sentinel.write_text('My existing rules')
        result=self.run_helper('prepare_client.py','--client','cursor','--project',self.project,'--apply')
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(sentinel.read_text(),'My existing rules')
        self.assertFalse((self.project/'.agents').exists())
    def test_specialist_is_opt_in(self):
        result=self.run_helper('prepare_client.py','--client','claude','--project',self.project,'--specialist','mobile-release','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(len(list((self.project/'.claude/skills').glob('*/SKILL.md'))),18)
        self.assertEqual((self.project/'CLAUDE.md').read_text(),'@AGENTS.md\n')
    def test_bad_specialist_path_rejected(self):
        result=self.run_helper('prepare_client.py','--client','codex','--project',self.project,'--specialist','../rules','--apply')
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(list(self.project.iterdir()),[])
    def test_duplicate_discovery_stops(self):
        first=self.run_helper('prepare_client.py','--client','codex','--project',self.project,'--apply')
        self.assertEqual(first.returncode,0,first.stderr)
        second=self.run_helper('prepare_client.py','--client','claude','--project',self.project,'--apply')
        self.assertNotEqual(second.returncode,0)
        self.assertFalse((self.project/'.claude').exists())
    def test_checked_target_rejects_escape(self):
        with self.assertRaises(ValueError): prepare_client.checked_target(self.project,Path('../outside'))
    def test_link_escape_rejected(self):
        outside=self.root/'outside';outside.mkdir()
        try: (self.project/'.agents').symlink_to(outside,target_is_directory=True)
        except (OSError,NotImplementedError): self.skipTest('Host cannot create directory symlinks')
        result=self.run_helper('prepare_client.py','--client','codex','--project',self.project,'--apply')
        self.assertNotEqual(result.returncode,0)
        self.assertFalse((self.project/'AGENTS.md').exists())
        self.assertEqual(list(outside.iterdir()),[])
    def config(self,argv):
        path=self.project/'checks.json'
        path.write_text(json.dumps({'checks':[{'name':'synthetic','argv':argv,'timeout_seconds':5}]}))
        return path
    def test_check_preview_does_not_execute(self):
        cfg=self.config([sys.executable,'-c',"from pathlib import Path; Path('ran').touch()"])
        result=self.run_helper('run_checks.py','--project',self.project,'--config',cfg)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertFalse((self.project/'ran').exists())
    def test_check_success_executes_and_failure_propagates(self):
        cfg=self.config([sys.executable,'-c',"from pathlib import Path; Path('ran').touch()"])
        result=self.run_helper('run_checks.py','--project',self.project,'--config',cfg,'--run')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue((self.project/'ran').exists())
        cfg=self.config([sys.executable,'-c','raise SystemExit(7)'])
        result=self.run_helper('run_checks.py','--project',self.project,'--config',cfg,'--run')
        self.assertEqual(result.returncode,1)
    def test_missing_check_tool_fails(self):
        cfg=self.config(['ai-dev-test-nonexistent-executable-71382'])
        result=self.run_helper('run_checks.py','--project',self.project,'--config',cfg,'--run')
        self.assertEqual(result.returncode,2)
    def test_shell_metacharacters_are_literal_arguments(self):
        payload='hello; echo BAD | something $(not-a-command)'
        cfg=self.config([sys.executable,'-c',"import sys; from pathlib import Path; Path('literal').write_text(sys.argv[1])",payload])
        result=self.run_helper('run_checks.py','--project',self.project,'--config',cfg,'--run')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual((self.project/'literal').read_text(),payload)
    def test_timeout_is_failure(self):
        cfg=self.config([sys.executable,'-c','import time; time.sleep(3)'])
        obj=json.loads(cfg.read_text());obj['checks'][0]['timeout_seconds']=1;cfg.write_text(json.dumps(obj))
        result=self.run_helper('run_checks.py','--project',self.project,'--config',cfg,'--run')
        self.assertEqual(result.returncode,1)
    def test_memory_valid_and_invalid(self):
        record=json.loads((KIT/'memory/examples/preference.json').read_text())
        self.assertEqual(validate(record),[])
        for key,value in [('confidence','certain'),('valid_to','2020-01-01'),('namespace','../../private'),('recorded_at','2026-09-20'),('supersedes',record['id'])]:
            candidate=copy.deepcopy(record);candidate[key]=value
            self.assertTrue(validate(candidate),(key,value))
    def test_memory_malformed_types_are_rejected(self):
        record=json.loads((KIT/'memory/examples/preference.json').read_text())
        for key,value in [('kind',[]),('links',[None]),('statement',None)]:
            candidate=copy.deepcopy(record);candidate[key]=value
            self.assertTrue(validate(candidate))
    def test_structural_validation(self):
        result=self.run_helper('validate_kit.py')
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)

if __name__=='__main__':
    unittest.main(verbosity=2)
