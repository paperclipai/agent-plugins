#!/usr/bin/env python3
"""Link dottastack skills from this checkout; use shared discovery for Codex and Cursor."""
import argparse
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {"codex": ".agents", "cursor": ".agents", "claude-code": ".claude"}


def matches(path, target):
    return path.is_symlink() and path.resolve() == target.resolve()


def install(agents, home, dry_run=False):
    skills = sorted((ROOT / "dottastack/skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No dottastack skills found")
    planned, obsolete, conflicts = [], [], []
    for directory in dict.fromkeys(DIRECTORIES[agent] for agent in agents):
        for skill in skills:
            target = skill.parent
            dest = home / directory / "skills" / target.name
            if os.path.lexists(dest):
                if not matches(dest, target):
                    conflicts.append(str(dest))
            else:
                for parent in dest.parents:
                    if os.path.lexists(parent) and not parent.is_dir():
                        conflicts.append(str(parent))
                        break
                planned.append((dest, target))
            if directory == ".agents":
                for legacy in [".codex", ".cursor"]:
                    path = home / legacy / "skills" / target.name
                    if os.path.lexists(path):
                        if matches(path, target):
                            obsolete.append((path, target))
                        else:
                            conflicts.append(str(path))
    if conflicts:
        raise ValueError("Conflicting entries; nothing changed:\n" + "\n".join(sorted(set(conflicts))))
    for dest, target in planned:
        print(f"{'Would link' if dry_run else 'Link'} {dest} -> {target}")
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.symlink_to(os.path.relpath(target, dest.parent), target_is_directory=True)
    for path, target in obsolete:
        print(f"{'Would remove' if dry_run else 'Remove'} redundant link {path}")
        if not dry_run:
            if not matches(path, target):
                raise ValueError(f"Link changed during installation; preserved {path}")
            path.unlink()
    print(f"{len(planned)} links {'planned' if dry_run else 'created'}; "
          f"{len(obsolete)} redundant links {'would be removed' if dry_run else 'removed'}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=DIRECTORIES, action="append", required=True)
    parser.add_argument("--home", type=Path, default=Path.home(), help="Target home; use a temporary path for checks")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        install(args.agent, args.home.expanduser().resolve(), args.dry_run)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
