---
name: runtime
description: Resolve this stack's host tools, model roles, skill paths, transcripts, isolation, and wake mechanisms for Codex, Claude Code, or Paperclip workers.
---

# Runtime

Read this before executing a workflow that delegates work, chooses models, reads transcripts, schedules a wake, or installs a skill. The host's tool schemas, permissions, and the user's scope remain authoritative. Names and fields in examples describe intent; never pass unsupported arguments to a tool.

## Skills and instructions

Resolve the physical skill path first when discovery uses a symlink. Resolve sibling skills from this installation's `skills/` directory. `/name` denotes the named skill, not a promise that the host registers that slash command. Use the host's invocation syntax or read its `SKILL.md` directly. Keep all sibling references and scripts with the skill. Resolve `scripts/` commands relative to the skill that owns them. For `git show` examples, use the repository, base ref, and path prefix that actually own the installed stack files; a vendored copy has a prefix such as `.agents/poteto-stack/`. Never assume the application repository has the stack at its root.

Use `.agents/skills/` for shared project skills and `~/.agents/skills/` for personal skills. Claude Code discovers `.claude/skills/` and `~/.claude/skills/`; link or copy the same skill folders there when needed. Do not modify runtime-managed built-ins. An explicitly invoked mode remains a working instruction until the user exits it; include its entrypoint in resumed-task briefs rather than assuming a UI mode keeps it loaded.

## Delegation and models

Use only the delegation tools actually exposed by the host. On Codex use its native subagent tools. On Claude Code use its native agent tool and supported agent definitions. On Paperclip use the configured worker runtime for within-run subagents; use Paperclip assignments and adapters for durable owners or cross-runtime work. Discover the Paperclip tools or installed coordination skill before making control-plane calls. No guessed endpoints or tool fields.

Read `~/.config/poteto-stack/models.md` when present. Each role has a model identifier or `inherit-parent`/`auto`; either alias omits a model override. Comma-separated panel entries each create one independent reviewer. Defaults inherit the parent model, including two separate reviewers for two alias entries. This preserves independent review but does not provide model diversity. For a cross-model requirement, use distinct available families through the host or configured Paperclip adapters; report when that requirement cannot be met. Do not represent same-model review as cross-model proof.

Read the `# budget` line when present and map its reasoning budget to supported host effort settings separately from model identifiers. Without a budget, inherit the parent effort. Never synthesize identifiers by appending effort suffixes. On a rejected model, inspect available models, use a supported equivalent when authorized, and disclose the fallback. Do not edit upstream merely because one host rejects a model.

To spawn `poteto-agent` or `Comment Sicko`, load the matching file from `agents/` at this installation's root. Pass those instructions to the worker if the host cannot register the named type. General-purpose workers receive the referenced task template. Use background execution when supported and wait using the host's completion tools. Respect concurrency and nesting limits; roll excess work through available slots. Missing delegation is a reported limitation, not permission to invent a worker or certify independent review yourself.

Read-only tasks stay read-only. Enable the specific read tools they need without assuming read-only mode removes MCP access. Do not grant write access merely to perform an investigation.

## Isolation and persistence

Use isolated remote workers when the host provides them; otherwise give each writer a dedicated git worktree and isolate ports, data, and build output. Set the requested base branch using the host's supported workspace controls or create that worktree from the named ref. A local worker is not a cloud VM and may stop when the host exits. Check actual run state after a restart before resuming or replacing work.

For repeated wakeups use the bundled `loop` skill. For a new scheduled or event-driven automation use `automate`. A background shell process does not wake an agent unless the host explicitly supplies that behavior.

## Transcripts

Use the host's scoped conversation API or documented transcript location for this workspace only. If the workflow needs files, export authorized in-scope tool events and messages into a task-local transcript directory. Preserve source IDs and timestamps. Inspect the actual format instead of assuming a JSONL schema. No accessible transcript means report the gap or use an explicitly labeled session digest; do not claim to have verified unseen tool calls.

For `worktree-audit.sh`, set `PSTACK_TRANSCRIPTS_DIR` to this workspace's exported transcript directory. Without transcript evidence the audit cannot clear a worktree for deletion.
