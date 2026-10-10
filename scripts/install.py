#!/usr/bin/env python3
"""Link dstack skills directly from this checkout into selected agent directories."""
import argparse
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {"codex": ".codex", "claude-code": ".claude", "cursor": ".cursor"}


def install(agents, home, dry_run=False):
    skills = sorted((ROOT / "dstack" / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No dstack skills found")
    planned = []
    conflicts = []
    for agent in dict.fromkeys(agents):
        for skill in skills:
            target = skill.parent
            dest = home / DIRECTORIES[agent] / "skills" / target.name
            if os.path.lexists(dest):
                if dest.is_symlink() and dest.resolve() == target.resolve():
                    continue
                conflicts.append(str(dest))
            else:
                planned.append((dest, target))
    if conflicts:
        raise ValueError("Conflicting entries; no links changed:\n" + "\n".join(conflicts))
    for dest, target in planned:
        print(f"{'Would link' if dry_run else 'Link'} {dest} -> {target}")
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.symlink_to(os.path.relpath(target, dest.parent), target_is_directory=True)
    print(f"{len(planned)} {'planned' if dry_run else 'created'} links; existing matching links preserved.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=DIRECTORIES, action="append", required=True)
    parser.add_argument("--home", type=Path, default=Path.home(), help="Target home (also useful for testing)")
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
