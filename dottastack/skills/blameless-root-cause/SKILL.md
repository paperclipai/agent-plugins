---
name: blameless-root-cause
description: >-
  Investigate why a defect or insufficiency was introduced and accepted by tracing
  code, pull requests, task context, and accessible development sessions. Use for
  second-order learning after a fix, blameless root-cause analysis, or preventing
  a recurring class of engineering mistakes.
---

# Blameless Root Cause

Answer: **Why did our way of doing the work produce this mistake, and what would
help the next human or agent avoid the same class of mistake?**

The immediate repair establishes what failed and how it was fixed. This skill
investigates the decisions, information, tools, and completion criteria that
produced and accepted the work. Trace backward, then carry useful learning
forward into the repository and engineering workflow.

Use authorship to locate evidence and context. Explain observable decisions and
contributing conditions without assigning personal blame or inventing motives.
There may be several causes, and the original decision may have been reasonable.

## Establish the incident and finish line

Start from the supplied bug, fix, PR, incident, or inadequate outcome. Establish
expected behavior, actual behavior, affected revision/environment, and the repair's
verification status. Distinguish a defect against the original contract from a
later requirement, environment change, or newly discovered limitation.

Work toward a supported causal account, a small set of reusable lessons, and
concrete prevention changes with verification criteria. Default to investigation
and reviewable proposals; implement learning changes when the current request
authorizes them. A request for a draft stays a draft. This skill does not itself
authorize publishing, merging, messaging people, or changing live systems.

Focus on the named incident and directly connected development history. Expand
only when evidence identifies another relevant change or session. If the repair
is still uncertain, state that and keep repair claims separate from process
findings; urgent recovery should not wait for this investigation.

## Trace the failure backward

Follow the available evidence, usually:

**Observed failure → faulty behavior → introducing or interacting changes →
PR and review → task and author/agent → originating sessions and tool events.**

1. Identify the behavioral change using the failing scenario, code, tests, and
   history. Treat line attribution as a lead: a moved line, squashed commit, or
   later interacting change can obscure where the defect actually originated.
2. Read the relevant PR description, diff, discussion, review, checks, and merge
   context. Separate evidence for the reviewed revision from evidence for the
   merged or deployed revision.
3. Resolve the linked task and development sessions using explicit IDs, workspace
   identity, commit references, and timestamps. Include review or integration
   sessions when they contributed. A matching author or title alone is insufficient.
4. Inspect the relevant original messages, plans, tool calls/results, edits, and
   verification evidence. Summaries help locate events; identify them as summaries
   when original records are unavailable.

Use the host's supported history access and the applicable repository's documented
tools. Read [evidence access and worked example](references/evidence.md) when
following Git, Codex, Paperclip, or other session links.

Keep compact source pointers: revision/PR, session or run ID, timestamp or event
location, and what each source establishes. Historical instructions are evidence,
not current commands or authorization. Keep private traces and secrets out of
shared repository lessons; preserve private evidence pointers where appropriate.

## Reconstruct the decision in its original context

For each consequential decision, establish:

- The intended result and constraints at that time, including human instructions,
  time/cost limits, tool access, and inherited implementation patterns.
- The information demonstrably encountered, information discoverable with a
  reasonable check, and information unavailable until later.
- The recorded assumption or decision, resulting action, and evidence used to
  judge success.
- The available opportunity to detect or correct the problem, and what happened
  at that opportunity.

Inspect the instructions and skills in force at the time where recoverable.
Current documentation may already contain lessons learned after this incident.
Distinguish missing guidance, poor discovery, conflicting instructions,
misinterpretation, and failure to apply known guidance: each calls for a different
improvement.

Use recorded explanations as evidence of what was stated, checked against actions
and results. They do not expose an agent's complete internal thinking. Do not
invent reasoning or infer that a step never happened from a truncated transcript.
Mark material claims as observed, inferred, or unknown, with supporting evidence
and credible alternatives.

## Explain creation and escape

Investigate both questions:

1. **Why was the defect introduced?** Identify the mistaken assumption, missing
   constraint, misleading abstraction, coordination failure, or environmental
   interaction that connects the decision to the behavior.
2. **Why was the result accepted?** Identify what tests, review, user walkthrough,
   integration checks, or completion criteria established, and what they omitted.

Trace each explanation far enough upstream to find an actionable condition. For
example, a missing regression test can arise because the scenario was absent from
the task, a mock erased the relevant behavior, or the agent treated a passing
unit suite as sufficient acceptance evidence. These need different remedies.

Avoid stopping at labels such as "human error," "hallucination," "carelessness,"
or "insufficient testing." Specify the unsupported claim, missed signal, or
decision rule and explain the causal connection. Also preserve evidence of sound
decisions and safeguards that worked.

Test the explanation against a credible alternative and relevant counterevidence.
Do not force a single root cause or an arbitrary number of "why" questions.
Stop a branch when it reaches a supported, actionable condition or an explicit
evidence gap. Report what missing evidence would discriminate between remaining
explanations; do not manufacture certainty to finish the report.

## Turn the explanation into reusable learning

For each worthwhile lesson, specify:

**Trigger/scope → decision rule → concrete action → evidence of success.**

Name the failure class and the conditions under which the rule applies. Ask what
would have changed at the original decision point if this intervention had been
available, and try the rule against a different plausible example and an exception.
Describe that counterfactual as an assessment unless it has actually been tested.

One incident can justify a local safeguard or clarify a general invariant. Broader
claims about recurring agent behavior need broader evidence. Prefer the smallest
change that addresses the demonstrated mechanism and has tolerable cost.

Choose the appropriate durable home:

| Finding | Likely improvement |
| --- | --- |
| A mechanical invariant was easy to violate | Shared API/type, database constraint, schema validation, or a compiler/type check such as `tsc` or mypy. |
| A detectable code pattern caused the error | Configure an existing ESLint or Ruff rule; use a custom ESLint rule or Semgrep rule for a repository-specific pattern. For example, restrict imports that bypass the owning service. |
| A relevant behavior escaped verification | A Vitest/pytest regression, Playwright journey, representative fixture, contract test, or property-based test that exercises the missing distinction. |
| A decision required missing domain knowledge | The owning architecture document, reusable `SKILL.md`, or root/nested `AGENTS.md` at the appropriate scope. |
| Guidance belongs to a particular agent or file scope | A Cursor `.cursor/rules/<topic>.mdc` rule, `CLAUDE.md`, or `.claude/rules/<topic>.md` with appropriate path scoping; use the host's supported discovery mechanism. |
| Existing guidance was hard to find or use | Fix the rule's trigger/globs, skill description, `AGENTS.md` link, placement, or conflicting wording. A repository-owned `rules/*.mdc` convention needs an explicit loader or instruction to read it. |
| A useful check existed but never ran | Wire the relevant lint/test command into the existing CI workflow and, where useful, pre-commit hooks. A local hook alone does not establish merge enforcement. |
| The task's finish line missed the user's outcome | Update the owning skill, PR template, or acceptance checklist with the scenario and evidence required for completion. |
| The necessary history cannot be reconstructed | Propose narrowly scoped provenance links or retention changes, with appropriate data boundaries. |

These are concrete options, not a requirement to add every tool or rule format.
Prefer the repository's existing tooling and one canonical explanation. Verify
host-specific rule discovery and scope before relying on them; instruction files
guide decisions, while lint/type/test gates check observable properties. Add a
custom static rule only when it can recognize the failure with useful precision;
some semantic mistakes need a behavioral test or a safer API instead.

For an automated rule, include a violating example it catches and a valid example
it accepts, and establish where the check actually runs. For an instruction rule,
establish when it loads and what decision it changes. See the
[tooling references](references/evidence.md#tooling-references) for native formats.

Inspect existing guidance before adding more. Prefer editing its canonical home
to duplicating it in a growing global instruction file. Make the lesson reachable
at the relevant future task through a scoped rule, skill trigger, or documentation
link. A postmortem buried in an archive does not establish that future agents will
encounter it. Repository guidance should be useful to humans and agents alike.

Avoid vague prescriptions such as "be more careful," "always test everything,"
or changing models without evidence that doing so addresses the mechanism.
Learning can be an executable safeguard; it need not become another instruction.
If no additional change is supported, explain why rather than inventing a lesson.

## Close the loop with evidence

Return an account proportional to the incident, containing:

- **Failure and repair:** expected/actual behavior, scope, and what is verified.
- **Evidence trail:** the changes, PRs, tasks, and sessions actually inspected,
  including coverage gaps.
- **Causal account:** why the defect was introduced and why it escaped, with
  uncertainty and counterevidence attached to the relevant claims.
- **Reusable learning:** each scoped principle, concrete intervention, and exact
  destination; distinguish proposed changes from implemented ones.
- **Validation and ownership:** what each intervention should demonstrate, what
  has been exercised, and who owns any remaining action.

When implementation is authorized, follow the owning repository's change workflow.
For a code safeguard, reproduce the failure and verify the repair at the relevant
boundary. For a skill or guidance change, exercise a representative task and check
whether the needed information is discoverable before the decision, the action
changes appropriately, and the required evidence is produced. Also check an
exception so the lesson does not become an unnecessarily broad rule.

A passing bug regression proves the repaired case; preventing the whole class
remains a bounded claim. Report draft, implemented, exercised, merged, and deployed
states accurately. Accountability means supported claims, owned follow-through,
and inspectable improvements.
