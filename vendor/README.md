# Vendor complete snapshots with an explicit source revision

`pstack` is a plain copy of the tracked files in
[paperclipai/poteto-stack](https://github.com/paperclipai/poteto-stack), imported at
`37d2ddde97aaef8017ccef811e682948f421062d` on 2026-10-10. It is committed as ordinary
files: no nested repository, Git submodule, or subtree integration.

`pstack.lock.json` records every imported file's SHA-256 hash and executable bit.
Run `python3 scripts/verify_vendor.py` from the repository root to detect changed,
missing, or extra snapshot files. The snapshot currently has no local modifications.
The lock records the state of this import; it is not a cryptographic signature
of upstream authorship.

Keep `pstack/LICENSE`, `NOTICE.md`, `UPSTREAM.md`, and `metadata/` intact. The
Paperclip fork itself records its earlier import from Cursor and its portability
changes. This outer lock records the specific Paperclip revision we vendored.

To update, fetch the desired upstream revision into a temporary checkout, compare
it with this snapshot, then replace the tracked files and regenerate the outer
lock after reviewing the differences. Preserve executable bits and check for
removed files. Keep adaptations in our own packaging where possible; if a vendor
patch is necessary, document it explicitly instead of hiding it in a refreshed hash.

The upstream `scripts/validate.py` calls `git show 89b26b3:...` against its original
import history. That history deliberately is not included here, so use our outer
snapshot verifier for preservation. Run upstream history-dependent checks in an
upstream clone. The upstream installation documentation and scripts are otherwise
preserved unchanged.
