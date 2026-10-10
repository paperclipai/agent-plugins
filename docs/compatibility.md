# Keep the content portable and use richer host features when useful

This library should work across the agents Dotta uses without making one vendor's
format a permanent constraint. Cursor's plugin model is the preferred direction
for richer bundles; Agent Plugins provides a useful common foundation. Claude,
Codex, and Vercel's skills CLI are practical compatibility targets. These are
priorities, not a promise of identical behavior everywhere.

The initial package contains shared skills with small manifests. This document
separates the intended format support, installation choices, and known limits.
Source documentation was checked on 2026-10-10.

## Keep one source for skills and adapt the packaging

| Target | Approach in this repo | Boundary |
| --- | --- | --- |
| Cursor | `dstack/.cursor-plugin/plugin.json` and the root marketplace catalog | Preferred place to add useful agents, rules, commands, hooks, or variables; adapt them for other hosts when worthwhile. |
| Agent Plugins | `dstack/plugin.json`, standard `skills/<name>/SKILL.md` layout | Portable skills and optional MCP configuration; not a universal agents/hooks runtime. |
| Claude Code / Cowork | `dstack/.claude-plugin/plugin.json` and the root Claude catalog | Shared content, with host-specific configuration when needed. Code and Cowork can differ too. |
| Codex | Individual discovery symlinks into `dstack/skills` | Use `~/.agents/skills` with symlink targets in this checkout; migrate matching legacy `.codex` links. |
| Vercel skills CLI | Give it `./dstack` as a local package | Skill discovery/installation only; do not assume it installs agents, hooks, or MCP configuration. |

The manifests describe the same dstack content. A root Agent Plugins manifest
and native manifests coexist as authoring artifacts; selection and loading can
vary by client version. A future host-specific export can omit other manifests
if needed. Keep identifiers and versions consistent across the three manifests.

Pstack is the existing Paperclip portability fork, preserved under `vendor/pstack`.
Use its installer for Codex/Claude; do not infer native Cursor plugin compatibility
from its upstream ancestry. Its original Cursor manifest was removed by that port.

## Support the parts the host can actually execute

Plain instructions, references, assets, and portable scripts should be shared.
Subagent prompts can often be shared too, but tool names, model selection,
permissions, delegation, scheduling, and transcript access depend on the host.
Keep those dependencies explicit and use available host capabilities.

MCP standardizes communication with tools, not the surrounding credential setup
or installation behavior. Cursor normally discovers `mcp.json`; Claude normally
discovers `.mcp.json`. Plugin-root variables and hook event payloads differ.
Add small adapters only when a real integration needs them.

Preserve useful host-specific features rather than deleting them to satisfy a
lowest-common-denominator format. Record the limitation for other hosts. Do not
add an empty `agents`, `hooks`, or `commands` directory just to resemble a template.

## Choose installation based on whether you are authoring or consuming

For active authoring, use `scripts/install.py`: its links point directly to this
checkout. It currently exposes only skills. Codex and Cursor share
`.agents/skills`; Claude Code uses `.claude/skills`. Selecting both Codex and
Cursor creates one shared link per skill. Matching old `.codex/skills` and
`.cursor/skills` links are removed after the shared links exist. Different
content or targets cause a failure before any planned changes. `--home` supports
temporary-home verification. Keep cross-skill references portable instead of
relying on an old absolute discovery path.

Vercel's CLI is useful for consuming skills from this package:

```sh
npx skills add ./dstack --list
# Optional install, after choosing this instead of direct authoring links:
npx skills add ./dstack -g -a codex claude-code cursor
```

Its symlink mode connects agent locations to a canonical installed copy. It is
not a guarantee of a live link to this development checkout. Do not combine
installers blindly or overwrite an installation with local edits. Supply the
`dstack` path to avoid accidentally discovering vendored skills too.

For native plugin development, Claude supports `claude --plugin-dir ./dstack`.
Cursor documents local plugins under `~/.cursor/plugins/local`; external-target
symlinks there are skipped. Do not generalize skill-symlink behavior to native
plugin installation. Use the host's supported local directory/import workflow.

Local symlinks do not provision another machine or cloud worker. Clone/install
there, or include a self-contained package in the worker's checkout.

## Treat validation and runtime evidence separately

The initial validation covers manifest structure, Claude's plugin validator,
Vercel's skill discovery, installer behavior in a temporary home, exact preservation
of moved skills, and a hash/mode comparison of the vendor snapshot. The migration
also checks that existing discovery paths resolve to their new canonical files.

This does not establish live workflow execution across Cursor, Claude, Codex, or
Cowork. Test the relevant host when adding an agent, hook, connector, or other
host-dependent behavior. Keep claims no broader than the evidence.

References: [Agent Plugins](https://agent-plugins.org/),
[Cursor plugin reference](https://cursor.com/docs/reference/plugins),
[Claude plugin reference](https://code.claude.com/docs/en/plugins-reference),
[Codex skill discovery](https://learn.chatgpt.com/docs/build-skills), and
[Vercel skills CLI](https://github.com/vercel-labs/skills).
