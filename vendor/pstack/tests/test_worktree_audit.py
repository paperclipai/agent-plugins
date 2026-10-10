import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

AUDIT = Path(__file__).resolve().parents[1] / 'skills/poteto-mode/scripts/worktree-audit.sh'


@unittest.skipUnless(shutil.which('git'), 'git required')
class AuditTests(unittest.TestCase):
    def test_missing_transcripts_does_not_clear_a_merged_worktree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            repo = root / 'repo'; repo.mkdir()
            def git(*args):
                return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.DEVNULL, text=True)
            git('init', '-b', 'main')
            git('-c', 'user.name=Audit Test', '-c', 'user.email=audit@example.invalid', 'commit', '--allow-empty', '-m', 'baseline')
            remote = root / 'remote.git'
            git('clone', '--bare', str(repo), str(remote))
            git('remote', 'add', 'origin', str(remote))
            git('worktree', 'add', '-b', 'finished', str(root / 'worker'))
            # No external forge or account access in this integration check.
            bin_dir = root / 'bin'; bin_dir.mkdir()
            gh = bin_dir / 'gh'; gh.write_text('#!/bin/sh\nprintf \'[]\\n\'\n'); gh.chmod(0o755)
            env = dict(os.environ, PATH=str(bin_dir) + os.pathsep + os.environ['PATH'], PSTACK_TRANSCRIPTS_DIR='')
            result = subprocess.run(['bash', str(AUDIT), str(repo)], env=env, capture_output=True, text=True, check=True)
            self.assertIn('review-missing-transcripts', result.stdout)
            self.assertNotIn('\tsafe\t', result.stdout)
            self.assertTrue((root / 'worker').is_dir())


if __name__ == '__main__':
    unittest.main()
