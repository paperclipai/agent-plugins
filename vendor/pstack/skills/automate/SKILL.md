---
name: automate
description: Use this skill to create agent automations through the host's supported scheduler or Paperclip routines.
---
# Create Automation (Interactive)

Read [runtime](../runtime/SKILL.md) for host-specific tools and paths.

Use this skill when the user explicitly wants to make, build, set up, or create a new **agent automation**.

**Disambiguation.** "Automation" in a user workspace can mean many things (`.github/workflows`, CI pipelines, scheduled jobs, scripts, dbt, browser automation, shell scripts, workflow engines). Route to the named surface when the user mentions one, use normal repo/product exploration when the context points elsewhere, or ask a short clarifying question when the target surface is ambiguous.

## Execution spine (every run)

1. **Finish-path check.** Discover the host's documented scheduling tools or Paperclip routines. Check that the required trigger, workspace, and tools are supported. If no supported creation path exists, prepare a reviewable draft and report the missing capability; do not claim it is scheduled.
2. **Capture intent + proactive integration discovery.** After the finish-path check passes, if the prompt is missing 2+ of {what kicks it off, what should happen, what outcome}, send one short plain-chat message asking for a 1–2 sentence description and wait. Skip when the prompt already names trigger + action + outcome. Proactively run discovery for any integration the user named or implied — `gh repo view` on cwd; Slack MCP channels; PagerDuty MCP services; Linear/Sentry MCP teams/projects. Use the results to skip questions later.
3. **Completeness gates.** Resolve the trigger, timezone, repository and branch, connected integrations, tools, prompt, name, permissions, and stop condition. Inspect the live catalog and authentication state. Never invent server names, IDs, webhook formats, or supported events. Missing access or an unsupported trigger leaves the automation disabled.
4. **One consolidated question.** Ask for whatever integration discovery couldn't resolve — trigger details, repo / channel / service when ambiguous, tools when not obvious.
5. **Draft table → approval → creation.** Show a compact Markdown table (plain language, no YAML) recapping name / description, trigger, tools, instructions, resolved settings, and remaining gaps. Honor the user's existing authorization and the host's approval contract. Create through the host's supported tool, or hand off to its editor when required. Verify the saved fields and return its identifier and enabled/disabled state. Do not enable a run while required readiness checks remain incomplete.

## House rules

- **Plain language only.** Never show or talk about MCP / tool / proto names, request types, enum values, stage labels, or raw CLI output in user-visible chat. Exception: the user explicitly asks to see internals.
- **No YAML in finalization.** The draft table = compact Markdown only in plain language. Build and validate the host payload internally; surface the wire payload only when the user asks for it.
- **No automatic fallbacks.** Do not switch schedulers, create duplicate jobs, or bypass a host's approval flow. A prepared draft is not a scheduled automation.
- **Creation-only.** This skill prepares new automations only. Use the host's supported read-only listing to avoid duplicates, but route requested edits to the existing automation through the host's update flow.
- **Repo file references.** Only reference a file from the chat's current repo (path, excerpt, or `@file` mention) in any draft field — prompt, instructions, name, or description — when **both** are true: (1) the automation will run in that same repo (its configured repository is the chat's repo) **and** (2) the file is committed to that repo (tracked by `git` on the branch the automation will check out, not just present in the working tree). If either condition fails, paraphrase the intent instead, or ask the user to commit and push the file first — do not embed the path or content. Untracked / staged-only / dirty-only files, files outside the automation's repo, and files in a different repo from the chat's checkout never qualify.

## Integration discovery

Before asking the user for a picker-backed value (repo, Slack channel / DM, GitHub/GitLab PR / comment scope, PagerDuty service, Linear team, Sentry project, …), proactively check whether the associated integration MCP or CLI is available and authenticated, then fetch the relevant records. For MCP-backed integrations, the availability check must be the current user's actual MCP/tool catalog, not a remembered or guessed server name.

Do not run broad private repo inventory or unscoped account/org sweeps. Keep discovery scoped to the named repository, owner, channel, or project. Resolve the destination where messages will be sent separately from the source trigger. A trigger does not authorize unrelated messages.

Connect missing integrations through the host's supported authentication flow. Keep credentials in its secret store or environment. Never embed secrets in prompts or committed files.

## Paperclip

When Paperclip owns the run, create the routine or heartbeat through its available control-plane tools and configured agent adapter. Preserve the issue/agent/workspace context. Inspect actual trigger support; do not assume a Slack event or webhook is supported merely because a timer is available. If it is missing, report the integration requirement and keep the automation disabled.
