import importlib.util
import os
from pathlib import Path
import shutil
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', SOURCE / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_codex_discovery_is_repeatable_and_preserves_other_skills(self):
        other = self.root / '.agents/skills/mine/SKILL.md'
        other.parent.mkdir(parents=True)
        other.write_text('user-owned')
        first = installer.install('codex', 'user', home=self.root)
        self.assertEqual(first, installer.install('codex', 'user', home=self.root))
        self.assertEqual(other.read_text(), 'user-owned')
        for link, target in first:
            self.assertEqual(link.resolve(), target.resolve())
            self.assertTrue((link / 'SKILL.md').is_file())
        policy = self.root / '.agents/skills/poteto-mode/agents/openai.yaml'
        self.assertIn('allow_implicit_invocation: false', policy.read_text())

    def test_claude_discovers_agents_and_skills(self):
        links = installer.install('claude', 'user', home=self.root)
        for link, target in links:
            self.assertEqual(link.resolve(), target.resolve())
        agent = self.root / '.claude/agents/poteto-agent.md'
        self.assertTrue(agent.is_file())
        self.assertTrue((self.root / '.claude/skills/runtime/SKILL.md').is_file())

    def test_conflict_refuses_before_installing_anything(self):
        conflict = self.root / '.agents/skills/poteto-mode'
        conflict.mkdir(parents=True)
        (conflict / 'SKILL.md').write_text('custom')
        with self.assertRaises(ValueError):
            installer.install('codex', 'user', home=self.root)
        self.assertFalse((self.root / '.agents/skills/arena').exists())
        self.assertEqual((conflict / 'SKILL.md').read_text(), 'custom')

    def test_copied_install_survives_relocation_with_references(self):
        project = self.root / 'original'; project.mkdir()
        installer.install('claude', 'project', project=project, copy=True)
        moved = self.root / 'fresh-checkout'; project.rename(moved)
        entry = moved / '.claude/skills/poteto-mode/SKILL.md'
        self.assertTrue(entry.is_file())
        self.assertTrue((entry.resolve().parent / '../runtime/SKILL.md').resolve().is_file())
        self.assertTrue((entry.resolve().parent / '../../agents/poteto-agent.md').resolve().is_file())
        for p in (moved / '.claude').rglob('*'):
            if p.is_symlink():
                self.assertFalse(os.path.isabs(os.readlink(p)))
                self.assertTrue(p.resolve().is_relative_to(moved.resolve()))
        self.assertFalse((moved / '.agents/poteto-stack/.git').exists())
        self.assertFalse((moved / '.agents/poteto-stack/skills/poteto-mode/scripts/node_modules').exists())
        installer.install('claude', 'project', project=moved, copy=True)
        owned = moved / '.agents/poteto-stack/skills/how/SKILL.md'
        owned.write_text('local change')
        with self.assertRaises(ValueError):
            installer.install('claude', 'project', project=moved, copy=True)
        self.assertEqual(owned.read_text(), 'local change')


if __name__ == '__main__':
    unittest.main()
