# Runtime support

The canonical skills live in `skills/`. Install discovery links for the worker runtime, then invoke `poteto-mode` using that runtime's skill selector (for example `$poteto-mode` in Codex or `/poteto-mode` in Claude Code). Slash syntax in the preserved guide names skills; it does not guarantee an identically named built-in command. When a host reserves a name such as `loop`, explicitly request the bundled skill by its installed file path.

## Install

From this checkout:

```bash
python3 scripts/install.py --runtime codex --scope user
python3 scripts/install.py --runtime claude --scope user
```

These install links into `~/.agents/skills/` or `~/.claude/skills/`. Claude also receives agent definitions in `~/.claude/agents/`. Keep this checkout at its installed location. Existing conflicting skills cause a refusal before any planned files are written; unrelated skills are preserved. Installation is repeatable.

For a repository or a Paperclip worker workspace:

```bash
python3 scripts/install.py --runtime codex --scope project --project /path/to/repo --copy
# Use --runtime claude for a Claude Code worker.
```

Copy mode vendors the complete distribution under `.agents/poteto-stack/` and uses relative discovery links. Commit both the copied tree and discovery links so a remote checkout is self-contained. Updates that would overwrite changed files are refused; review and merge those changes explicitly. Benny remains a dormant automation pack, not a globally registered skill.

## Host contract

Read `skills/runtime/SKILL.md`. It maps the existing workflow concepts to available tools without inventing APIs. Models default to inheriting the parent; `/setup-pstack` writes `~/.config/poteto-stack/models.md`. Set different model families where the host supports them to obtain actual cross-model review. Multiple inherited reviewers are independent runs of the same model, not a diverse-model panel.

Codex explicit-only skills have `agents/openai.yaml` invocation policies. Claude keeps the original `disable-model-invocation` frontmatter. Custom mode UI metadata was removed; carry mode instructions in the host's persistent context or invoke them for each task. No installer silently edits AGENTS.md, CLAUDE.md, or the host's general configuration.

Paperclip owns durable assignments, scheduling, and worker adapters. Skills execute inside the selected worker runtime. This package does not configure a company, create agents, connect Slack, or enable routines merely by being installed. The bundled `automate` and `loop` workflows discover and use supported host capabilities; if an event trigger or persistent scheduler is unavailable they report the limitation instead of pretending a background shell is a wake service.

Transcript workflows use host-provided, workspace-scoped APIs or exports. Export files only from authorized chats. For a worktree audit, set `PSTACK_TRANSCRIPTS_DIR` to that scoped directory. With no transcript directory, the audit does not label a worktree safe to delete.

## Tool dependencies

Python 3 installs the package. The validation command also requires PyYAML from `scripts/requirements-dev.txt`. Git and GitHub CLI are used by PR workflows. The upstream orchestration store and PR watcher require Bun; their checked-in package and lockfile install `commander`, TypeScript, and Bun types. Node runs the plan checker. Browser/PTY tools are selected by the bundled control skills from what the project already has. No Cursor installation, account, CLI, MCP, or cloud service is required.

```bash
python3 -m pip install -r scripts/requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
cd skills/poteto-mode/scripts
bun install --frozen-lockfile
bun test orch watch-pr
bun run typecheck
```

Optional recognition of Bugbot comments in the GitHub watcher remains unchanged. That is input compatibility, not a required service. The original guide illustrations and author introduction remain unchanged as source material.
