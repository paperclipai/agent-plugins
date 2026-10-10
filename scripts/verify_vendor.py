#!/usr/bin/env python3
"""Verify the vendored snapshot against the recorded file hashes and executable bits."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    lock = json.loads((ROOT / "vendor/pstack.lock.json").read_text())
    root = ROOT / lock["directory"]
    expected = lock["files"]
    paths = list(root.rglob("*"))
    actual = {str(p.relative_to(root)): p for p in paths if p.is_file()}
    errors = [f"Unexpected symlink: {p.relative_to(root)}" for p in paths if p.is_symlink()]
    errors += [f"Nested Git metadata: {p.relative_to(root)}" for p in paths if p.name == ".git"]
    errors += [f"Missing: {name}" for name in sorted(expected.keys() - actual.keys())]
    errors += [f"Extra: {name}" for name in sorted(actual.keys() - expected.keys())]
    for name in sorted(expected.keys() & actual.keys()):
        path = actual[name]
        record = expected[name]
        if hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
            errors.append(f"Changed bytes: {name}")
        if bool(path.stat().st_mode & 0o111) != record["executable"]:
            errors.append(f"Changed executable bit: {name}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Verified {len(expected)} files from {lock['source']} at {lock['revision']}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
