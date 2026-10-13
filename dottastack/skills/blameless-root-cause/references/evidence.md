# Evidence access and worked example

Use only the sections relevant to the incident. These are discovery strategies;
the host's actual tool schemas, repository documentation, and access boundaries
determine available operations.

## Git and pull requests

Start with the implicated behavior and relevant history. For example, scoped
`git log -p -- path/to/file`, `git log -S 'relevant expression' -- path/to/file`,
and `git show <revision>:path/to/file` can establish when an assumption appeared
and what surrounded it. Inspect parent revisions and callers when necessary.
Use blame as a discovery aid, then validate behavior against the actual diff.

Resolve the hosting remote before finding the PR. Use the host's supported API
or CLI for the diff, discussion, reviews, checks, merge revision, and linked task.
Preserve revision identity: successful checks before a later edit do not verify
that edit. Inspect interactions between changes when no single change explains
the failure. Do not attribute a later requirement retroactively to an earlier PR.

## Codex sessions

Prefer a session ID or chat link from the task or PR. Discover the available chat
listing and reading tools; use their actual schemas and returned IDs. Search
within the relevant project and time window when no direct link exists. Titles
and summaries help locate candidates, but matching code, commit, workspace, and
events establish the connection.

Read the original request, consequential decisions, edits, and verification
outcomes. Request tool outputs only where needed. Follow supported pagination to
cover the relevant period and preceding context. Record truncation, omitted
outputs, forks, resumptions, and gaps after compaction.

Use a local transcript only when its documented or indexed location and ownership
are established. Inspect the actual record format and limit reading to connected
sessions. Do not crawl unrelated personal history because an incident lacks a
session link. Distinguish recorded statements, tool evidence, and later summaries;
do not attempt to reconstruct hidden internal reasoning.

## Paperclip runs

Resolve the correct instance, company, issue, agent, and run through an authorized
connector or the instance's documented API. Use the applicable Paperclip skill and
checkout documentation for access; do not guess endpoints.

Follow issue/PR references and run/session identifiers. Inspect effective task
input, run configuration, agent-visible instructions, tool events, output logs,
workspace revision, and completion evidence where retained. Follow connected
runs across resumptions or handoffs when they affected the change.

An assigned agent, commit author, or issue status is only a lead. Establish which
run produced which change. Distinguish the underlying agent's completion from
controller finalization, merge, and deployment. Configuration saved today does
not establish what the run received then.

## Other hosts and unavailable evidence

Use the host's documented conversation or execution records. Preserve source IDs,
timestamps, and record completeness. Do not infer thinking from an author name.
If the session cannot be found, retain what the code, PR, and checks establish
and mark upstream explanations provisional. Say which missing record would help.
An unavailable transcript can still leave enough evidence for a concrete test or
code safeguard; it does not justify a claim about an individual's reasoning.

## Worked example: a project selector shows stale results

This example is fictional and illustrates the reasoning process.

**Failure and repair.** Switching from project A to project B leaves A's issue
list visible. The request depends on the selected project, but the cache key
does not. Adding project identity to the key repairs the reproduced transition.

**Development evidence.** The task asked for a project selector. The original
plan stated that selection would be local UI state. The implementation reused
a cache key designed for a single project. The test rendered only project A,
and its fixture returned the same response regardless of the requested project.
The PR's acceptance evidence was a screenshot with the selector visible.

**Creation.** A single-project assumption survived the introduction of a second
project. The recorded plan supports a narrow interpretation of the change; the
code confirms that request identity did not track the selected project. This is
evidence about this decision, not a general judgment of the agent's capability.

**Escape.** The fixture erased the distinction the feature needed to preserve,
and acceptance evidence verified appearance without exercising the transition.
Adding more tests using that same fixture could still miss the problem.

**Reusable principle.** When introducing selectable context that changes fetched
data, trace that context through request construction and cache identity. Verify
a transition between two contexts with deliberately different data, including a
return transition where caching matters. Apply the rule only when context affects
the result; a purely cosmetic display option need not trigger a refetch.

**Durable changes.** Add the regression with distinct project fixtures. If shared
query builders own cache identity, strengthen that boundary. Update the existing
data-fetching guidance with the scoped decision rule and connect it to the
workflow that introduces selectors through an applicable `AGENTS.md` link, a
Cursor `.mdc` rule, or a Claude rule. Use a lint rule only if the repository's
query API makes a missing identity argument mechanically detectable; a behavioral
regression still covers the actual transition. Keep the incident's private
session excerpts in their original evidence store.

**Verification.** The regression should fail on the introducing revision and pass
after the repair. A future guidance exercise could add a workspace selector to a
different list, then inspect whether the agent traces request/cache identity and
tests the transition. That exercise would add evidence of transfer; merely
writing the guidance does not prove it.

## Counterexamples for reviewing this skill

- **The session is missing:** establish the cache defect and verification gap
  from available artifacts; do not claim the author ignored instructions.
- **The current guide already states the rule:** inspect the historical version
  and discoverability before adding duplicate guidance.
- **Two correct changes interact:** examine integration assumptions and checks;
  avoid forcing responsibility onto the last line's author.
- **The behavior was correct under the original requirement:** explain the changed
  contract and consider whether compatibility checks are now warranted. Do not
  manufacture an earlier mistake.
- **A lesson expands into "test every state":** narrow it to the demonstrated
  transition and failure class, and consider maintenance cost and exceptions.

## Tooling references

Consult the installed version and existing repository conventions before editing
configuration. These public references describe candidate mechanisms:

- [Cursor project rules](https://cursor.com/docs/rules): `.cursor/rules/*.mdc`
  and rule selection/scoping.
- [Claude Code project memory and rules](https://code.claude.com/docs/en/memory):
  `CLAUDE.md` and `.claude/rules/*.md`, including path-scoped rules.
- [ESLint custom rules](https://eslint.org/docs/latest/extend/custom-rules):
  repository-specific JavaScript/TypeScript checks when existing rules do not fit.
- [Semgrep rules](https://docs.semgrep.dev/writing-rules/overview): declarative
  code-pattern checks.

Keep host-specific wrappers small and point them at a shared explanation when
several agents need the same lesson. Verify each discovery path separately.
