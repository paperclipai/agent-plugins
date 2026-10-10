#!/usr/bin/env python3
"""Validate discovery, references, host independence, and exact upstream preservation."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = '89b26b3'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def frontmatter(path):
    text = path.read_text()
    match = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        raise ValueError(f'{path}: missing frontmatter')
    return yaml.safe_load(match[1])


def source_report():
    manifest = json.loads((ROOT / 'metadata/upstream.json').read_text())
    rows = []
    for source in manifest['files']:
        rel = source['path']
        original = subprocess.check_output(['git', 'show', f'{BASE}:{rel}'], cwd=ROOT)
        if digest(original) != source['sha256']:
            raise ValueError(f'Import differs from recorded upstream bytes: {rel}')
        dest = ROOT / rel
        current = dest.read_bytes() if dest.exists() else None
        row = {'path': rel, 'source': source['source'], 'upstream_path': source['upstream_path'],
               'status': 'unchanged' if current == original else 'removed' if current is None else 'adapted',
               'upstream_sha256': digest(original), 'sha256': digest(current) if current is not None else None}
        try:
            lines = original.decode('utf-8').splitlines(keepends=True)
            after = current.decode('utf-8').splitlines(keepends=True) if current else []
            equal = sum(m.size for m in difflib.SequenceMatcher(None, lines, after, autojunk=False).get_matching_blocks())
            row.update(upstream_lines=len(lines), unchanged_lines=equal)
        except UnicodeDecodeError:
            pass
        if row['status'] != 'unchanged':
            if rel == '.cursor-plugin/plugin.json': reason = 'Replace host plugin packaging with runtime discovery installer'
            elif rel in ('skills/automate/SKILL.md', 'skills/loop/SKILL.md'): reason = 'Replace host-specific scheduling, editor, and automation APIs; retain portable workflow text'
            elif 'make-bot-ui' in rel: reason = 'Replace host-specific webhook API, UI, credentials, and event schema'
            elif rel.endswith('worktree-audit.sh'): reason = 'Accept scoped transcript exports; missing transcript access must not certify deletion safety'
            elif rel.endswith(('package.json', 'bun.lock')): reason = 'Rename package metadata namespace'
            elif rel == 'README.md': reason = 'Repository identity/attribution, portable installation, models, modes, and dependency documentation'
            else: reason = 'Translate host paths, tools, models, discovery metadata, isolation, scheduling, or relocated dependency references'
            row['reason'] = reason
        rows.append(row)
    totals = {key: sum(r.get(key, 0) for r in rows) for key in ['upstream_lines', 'unchanged_lines']}
    totals.update(imported_files=len(rows), byte_identical_files=sum(r['status'] == 'unchanged' for r in rows))
    pstack = [r for r in rows if r['upstream_path'].startswith('pstack/')]
    totals['pstack_upstream_lines'] = sum(r.get('upstream_lines', 0) for r in pstack)
    totals['pstack_unchanged_lines'] = sum(r.get('unchanged_lines', 0) for r in pstack)
    return {'baseline_commit': BASE, 'summary': totals, 'files': rows}


def check(write_report=False):
    errors = []
    skills = list((ROOT / 'skills').glob('*/SKILL.md')) + list((ROOT / 'automations').rglob('SKILL.md'))
    names = set()
    for path in skills:
        meta = frontmatter(path)
        unknown = set(meta) - {'name', 'description', 'license', 'allowed-tools', 'metadata', 'disable-model-invocation'}
        if unknown:
            errors.append(f'{path.relative_to(ROOT)}: unsupported frontmatter {sorted(unknown)}')
        name = meta.get('name', '')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            errors.append(f'{path.relative_to(ROOT)}: invalid discovery name {name!r}')
        if name in names:
            errors.append(f'Duplicate skill name: {name}')
        names.add(name)
        if not isinstance(meta.get('description'), str) or not meta['description'].strip():
            errors.append(f'{path.relative_to(ROOT)}: missing description')
        if meta.get('disable-model-invocation') is True and path.parent.parent == ROOT / 'skills':
            policy = path.parent / 'agents/openai.yaml'
            if not policy.exists() or yaml.safe_load(policy.read_text()).get('policy', {}).get('allow_implicit_invocation') is not False:
                errors.append(f'{path.relative_to(ROOT)}: missing Codex explicit invocation policy')
    # Match runtime dependencies, not ordinary words such as an editor cursor or GraphQL endCursor.
    prohibited = re.compile(r'\.cursor(?:/|\b)|cursor\.com|api2\.cursor|cursor-subscriptions|cursor-app-control|cursor-team-kit|/add-plugin|cloud_base_branch|run_in_background|\bTask tool\b|`Task`|\bAskQuestion\b|alwaysApply|grok-4\.7|claude-opus-5-5|notify_on_output|SendToUser')
    for root in ['skills', 'agents', 'automations', 'docs']:
        for path in (ROOT / root).rglob('*.md'):
            if 'node_modules' in path.parts:
                continue
            content = path.read_text()
            if prohibited.search(content):
                errors.append(f'{path.relative_to(ROOT)}: host-specific instruction {prohibited.search(content)[0]!r}')
            # Markdown examples may deliberately contain placeholder references. Validate actual prose links.
            fence = False
            for number, line in enumerate(content.splitlines(), 1):
                if line.startswith('```'):
                    fence = not fence
                    continue
                if fence:
                    continue
                for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)', re.sub(r'`[^`]*`', '', line)):
                    if ':' in target or target.startswith('#') or '<' in target or target == 'url':
                        continue
                    location = (path.parent / target.split('#')[0]).resolve()
                    if not location.exists():
                        errors.append(f'{path.relative_to(ROOT)}:{number}: missing link {target}')
    report = source_report()
    for row in report['files']:
        rel = row['path']
        if rel.startswith('skills/principle-') and row['status'] != 'unchanged':
            errors.append(f'Pure principle changed: {rel}')
        if any(rel.startswith(f'skills/{n}/') for n in ['deslop','control-cli','control-ui','verify-this']) and row['status'] != 'unchanged':
            errors.append(f'Portable dependency changed: {rel}')
    out = ROOT / 'metadata/portability.json'
    if write_report:
        out.write_text(json.dumps(report, indent=2) + '\n')
    elif not out.exists() or json.loads(out.read_text()) != report:
        errors.append('Portability report stale: run python3 scripts/validate.py --write-report after reviewing the diff')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(skills)} skills; discovery, local links, host independence, and upstream hashes verified')
    print(json.dumps(report['summary'], indent=2))
    return 0


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write-report', action='store_true')
    sys.exit(check(p.parse_args().write_report))
