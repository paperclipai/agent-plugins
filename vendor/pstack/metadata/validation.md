# Validation of the initial portable release

Tested on 2026-10-09, against upstream `ccb5507cec1546dc88135c1139c811e6c59115ba`.

- All 62 skill frontmatters parse, have unique valid names and descriptions, and contain only supported standard fields plus the preserved explicit-invocation flag.
- The skill-creator validator accepts the standard frontmatter projection of all 62 skills; Claude's explicit-invocation field and equivalent Codex policies are checked separately.
- Every actual local Markdown link resolves. Illustrative links inside fenced examples and the upstream `(url)` citation placeholder are excluded.
- Operational Markdown contains no required installation paths, tool names, model identifiers, service URLs, or plugin dependencies tied to the source runtime.
- Every imported file is checked against its baseline commit and upstream SHA-256. All principle skills and the four public vendored dependencies are byte-identical. The exact per-file exceptions and preservation counts are in `portability.json`.
- Five Python integration tests pass: Codex discovery links and repeatability, Claude discovery links and agent definitions, non-overwriting conflict behavior, relocation of a copied install, and refusal to classify a merged worktree as safe without transcript access.
- Native Codex app-server `skills/list` discovers all 59 top-level installed skills with no missing skills or parse errors in a temporary project. No agent turn was started. The three Benny skills remain direct-read automation instructions.
- All 52 upstream Bun tests pass (206 assertions), covering the orchestration store/CLI and GitHub PR watcher parsing, readiness, queue policy, and CLI.
- The upstream TypeScript strict typecheck passes.

The installer was tested in temporary workspaces; no global skill installation, model configuration, or automation was enabled for the user. Native Claude execution, Paperclip company integration, live Slack/webhook delivery, autonomous scheduling, and cross-model behavior have not been exercised end to end. Those depend on the target host's actual tools and configured integrations. The workflows now resolve those capabilities explicitly and report absence rather than assuming them.
