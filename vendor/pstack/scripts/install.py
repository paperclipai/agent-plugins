#!/usr/bin/env python3
"""Install the canonical tree and host discovery links without overwriting user files."""
import argparse
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDES = {'.git', 'node_modules', '__pycache__', '.DS_Store'}


def files(root):
    return {p.relative_to(root): p for p in root.rglob('*')
            if p.is_file() and not (set(p.relative_to(root).parts) & EXCLUDES)}


def install(runtime, scope, project=None, copy=False, home=None):
    base = (Path(home or Path.home()) if scope == 'user' else Path(project)).resolve()
    discovery = base / ('.claude' if runtime == 'claude' else '.agents')
    bundle = base / '.agents' / 'poteto-stack' if copy else ROOT
    if copy and (bundle == ROOT or ROOT in bundle.parents):
        raise ValueError('Copy destination must be outside the source repository')
    source_files = files(ROOT) if copy else {}
    conflicts = []
    if copy:
        for rel, src in source_files.items():
            dest = bundle / rel
            if os.path.lexists(dest) and (dest.is_symlink() or not dest.is_file() or dest.read_bytes() != src.read_bytes()):
                conflicts.append(str(dest))
    links = [(discovery / 'skills' / p.name, bundle / 'skills' / p.name)
             for p in sorted((ROOT / 'skills').iterdir()) if (p / 'SKILL.md').is_file()]
    if runtime == 'claude':
        links += [(discovery / 'agents' / p.name, bundle / 'agents' / p.name)
                  for p in sorted((ROOT / 'agents').glob('*.md'))]
    for dest, target in links:
        if os.path.lexists(dest) and not (dest.is_symlink() and dest.resolve() == target.resolve()):
            conflicts.append(str(dest))
    if conflicts:
        raise ValueError('Conflicting files; review before installing:\n' + '\n'.join(conflicts))
    if copy:
        for rel, src in source_files.items():
            dest = bundle / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                shutil.copy2(src, dest)
    for dest, target in links:
        if not os.path.lexists(dest):
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.symlink_to(os.path.relpath(target, dest.parent), target_is_directory=target.is_dir())
    return links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime', required=True, choices=['codex', 'claude'])
    parser.add_argument('--scope', required=True, choices=['user', 'project'])
    parser.add_argument('--project', type=Path)
    parser.add_argument('--copy', action='store_true', help='Vendor files into .agents/poteto-stack; use for remote checkouts')
    args = parser.parse_args()
    if args.scope == 'project' and not args.project:
        parser.error('--scope project requires --project')
    try:
        links = install(args.runtime, args.scope, args.project, args.copy)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + '\n')
    print(f'Installed {len(links)} discovery links for {args.runtime}. Existing unrelated files preserved.')
    print('Start a new session and invoke poteto-mode. The installer does not change global instructions or schedule work.')


if __name__ == '__main__':
    main()
