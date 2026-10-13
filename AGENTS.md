# Maintain this library at its source

- Author Dotta's original skills and workflows under `dottastack`. Edit the canonical
  checkout, not an installed copy or plugin cache. Keep supporting resources with
  their skill and preserve its invocation policy.
- Compatibility is best effort. Prefer Cursor's useful capabilities, preserve a
  portable Agent Skills/Agent Plugins core where practical, and support Claude,
  Codex, and Vercel skills discovery without forcing all hosts to the same limits.
- Keep host-specific manifests and adapters small. Document unsupported behavior;
  do not invent agent APIs or equate a manifest passing validation with a workflow
  working in every client. See `docs/compatibility.md`.
- Treat `vendor/pstack` as a verbatim upstream snapshot. Keep local packaging and
  provenance outside it. For an intentional upstream update, replace the snapshot
  from the chosen revision, review the diff, and regenerate `vendor/pstack.lock.json`.
  Preserve licenses and authorship. Do not add a nested `.git`, submodule, or subtree.
- Keep installation repeatable and preserve unrelated user files. Do not replace
  an entire agent skills directory or silently overwrite a conflicting skill.
- Run `python3 scripts/verify_vendor.py` and `git diff --check` for repository
  changes. Exercise installer changes in a temporary home before changing live links.
