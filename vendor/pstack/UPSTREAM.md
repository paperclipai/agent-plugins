# Upstream provenance and preservation

- Repository: https://github.com/cursor/plugins
- Revision: `ccb5507cec1546dc88135c1139c811e6c59115ba`
- Imported pstack version: `0.15.15`
- Verbatim import commit: `89b26b3`
- Main source: `pstack/`, lifted to this repository's root.
- Vendored public dependencies: `cursor-team-kit/skills/{deslop,control-cli,control-ui,verify-this}`.
- Installed built-in dependencies: `skills-cursor/{create-skill,loop,automate}`, captured 2026-10-09; original files and SHA-256 hashes recorded at import.

The import commit contains the exact source files before portability edits. `metadata/upstream.json` maps every imported file to its source and original hash. `metadata/portability.json` records each changed source file, its final hash, the reason for the exception, and line-preservation statistics. `python3 scripts/validate.py` checks those records against Git history and the current files.

## Edit boundary

Preserve words, punctuation, formatting, ordering, and examples unless a host dependency must change. Do not restyle, summarize, reorganize, or improve upstream engineering guidance as part of this port. Preserve skill names except where frontmatter display names must become valid discovery identifiers.

Allowed changes are host tooling and discovery metadata, model identifiers/effort handling, installation paths, transcript discovery/schema, scheduler and webhook APIs, cloud/isolation assumptions, dependency resolution, relocated repository paths, and repository packaging/attribution. Pure principle files and the public control/review dependencies should remain byte-identical when they need no adaptation.

`create-skill` retains its general authoring text. `loop` and `automate` require larger replacements because their execution paths were defined by host-specific timers, editor handoffs, MCP catalogs, and automation schemas. Their portable parsing, intent, evidence, and approval behavior is retained where applicable. The original versions remain reviewable in the import commit.

## Dependency closure

| Referenced dependency | Resolution |
|---|---|
| deslop | Vendored unchanged from cursor-team-kit |
| control-cli | Vendored unchanged from cursor-team-kit |
| control-ui | Vendored unchanged from cursor-team-kit |
| verify-this, referenced by control-ui | Vendored unchanged from cursor-team-kit |
| create-skill | Vendored installed built-in; storage/tool instructions adapted |
| loop | Vendored installed built-in; host scheduler/active-session adapter |
| automate, used by Benny | Vendored installed built-in; host automation/Paperclip adapter |
| poteto-agent, Comment Sicko | Bundled agent definitions, portable discovery metadata |
| verify-<app>, mobile control skills | Intentionally project-specific; generated or supplied by the target repository |
| issue trackers, Slack, observability, browser tools | Optional integrations discovered from the host; absence is reported |

No external skill plugin is needed. Scheduling and connected services still require actual host support and user configuration.
