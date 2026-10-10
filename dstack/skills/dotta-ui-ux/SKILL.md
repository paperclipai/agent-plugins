---
name: dotta-ui-ux
description: Design, refine, implement, or review application UI and user journeys with minimal controls, clear actions, shared components, realistic prototypes, and polished behavior. Use for product screens, forms, onboarding, navigation, settings, and chat/task interfaces; not backend-only work or general graphic design.
---

# Dotta UI / UX

Build interfaces that let the person accomplish their goal with little reading,
few unnecessary decisions, and a clear sense of what happened. Put care into
alignment, identity, transitions, and the complete journey.

Use these principles to guide judgment. The user's current instructions and the
product's design system take precedence. Adapt each recommendation to the task:
a useful explanation, distinct navigation tab, or multi-step flow earns its place
when it helps someone understand a choice or complete an action. Do not turn a
preference for less UI into a universal ban on a particular control.

## Start inside the existing product

Identify the user's natural entry point, intended outcome, and the existing
screen and components that own the behavior. Inspect the current implementation
before proposing a new surface; old prototypes and component previews can be
obsolete.

- Reuse the actual composer, picker, file tree, connection flow, task list, and
  navigation components. Similar CSS on a second implementation is insufficient.
- Put a new capability where users already manage that kind of thing. A new
  account connection belongs with other integrations; notification preferences
  belong with existing notification settings. Follow the product's established
  navigation rather than creating a destination for every backend object.
- Apply a correction to the shared component and affected variants within the
  assignment. A supplied URL often identifies an example, not the only instance
  of the problem. Avoid unrelated redesigns.

Follow the project's design guidance, shared components, and tokens for spacing,
typography, color, and motion. Inspect the production UI when documentation or
previews disagree with the current product.

## Make each control and sentence earn its place

Before adding a field, setting, heading, badge, paragraph, or step, identify the
decision or action it enables now. Remove it if the current context already
supplies the answer or the element merely narrates normal behavior.

- Omit redundant headings, repeated selections, optional naming fields without
  a real need, routine Active/Idle badges, unsupported capability controls, and
  generic explanation beneath an obvious label. Prefer a useful default to a
  chooser with one possible answer.
- Use familiar action language: “Connect account,” “Add project,” “Save changes.”
  Avoid exposing internal concepts such as reconciliation or capability negotiation
  as everyday product choices.
- Reveal advanced configuration and alternate input methods through a small
  link, disclosure, or contextual menu. Put infrequent management actions there
  too. Let a linked title navigate to its object instead of adding an equivalent
  “Open…” button alongside it.
- Keep instructions that remove real uncertainty. Put prerequisites near the
  top, credential directions beside their fields, and useful help icons where
  they can be found. Use the actual known person, app, or account name. Explain
  consequential choices where they are made.

Do not confuse concise with cryptic. A short “How it works” explanation, a clear
warning, or a larger connection action can be appropriate when it makes the next
step understandable. Do not remove required consent or materially important
permission information to make a screen smaller.

## Reduce ceremony and preserve context

- Reuse compatible accounts and values the person can access. First-time setup
  and adding another item later may need different states: do not ask someone
  to reselect the connection they just created. Keep a way to change it when
  there is a real choice. Do not broaden access permissions as a UI shortcut.
- Group steps around distinct human actions. Complex external setup may need
  several stable steps; a simple credential connection should stay short. Do
  not copy one provider's wizard onto a flow with different requirements.
- Keep inline repair, approvals, previews, and task-related work in context.
  Breadcrumbs should return to the current object. An image gallery or plan
  should open without discarding or reloading the conversation unnecessarily.
- Make the obvious action work directly: Enter submits appropriate forms,
  clicking a copy action copies and confirms it, single-selection questions can
  advance after brief visible feedback, and selectors dismiss on outside click.
  Preserve draft input and useful navigation state.
- Avoid unnecessary confirmations and reason fields for reversible operations.
  Retain concise confirmation for destructive actions. Simplifying the UI must
  preserve the operation's actual semantics and authorization.

## Keep everyday operation calm and blockers actionable

Do not surface a backend state machine as the main experience. Routine recovery,
lease renewal, ordinary working states, and bookkeeping should usually happen
without new cards, warnings, or decisions for the user.

- Avoid a toast that repeats feedback already visible on the current screen.
  A deliberate pause or cancellation should look neutral, not like a dramatic
  unexpected failure. A tool retry is not automatically a task-level failure.
- Show real blockers clearly and locally, with a useful action. For example,
  “Automatic recovery of this task stopped. [Retry]” communicates more usefully
  than an internal recovery explanation. Verify that Retry actually works.
- Make waiting understandable: connection testing, importing, and long work need
  timely progress. A disabled Continue button with no reason is broken UX.
  Detect completed setup automatically when the system can observe it.
- Present useful results richly; keep raw JSON, manifests, and diagnostics
  available on demand. Do not claim success before it is observed or conceal a
  failure the person must address.

## Polish the composition and the transitions

- Favor compact, aligned rows and a clear hierarchy. Use consistent row heights,
  control sizes, carets, baseline alignment, and tree indentation. Add breathing
  room between fields and the footer. Avoid gratuitous borders and separators.
- Put the primary action on the right. In setup footers, keep Save & exit or
  Back/Cancel on the left in the same aligned row; related secondary actions sit
  beside the primary. Each step owns its whole footer, including conditional
  loading, error, and success states.
- Use recognizable service icons and relevant avatars in lists, selections, and
  previews. Keep them crisp and visible after selection and at smaller sizes. Familiar
  secondary actions can be icons or appear on hover/focus; essential help and
  actions must remain discoverable with keyboard and touch.
- Use restrained, purposeful motion: selected-row feedback, copy confirmation,
  progress, smooth disclosure, and continuous movement between related states.
  Preserve an element's position through an animation. Follow product motion
  tokens and reduced-motion behavior.
- Treat flashes, snapping, layout jumps, unstable sorting, and unnecessary
  reloads as defects. Keep the shell and reading position stable through
  loading, streaming, opening panels, and changing selections. Watch transitions
  in the running UI; a settled screenshot cannot prove they are good.
- Design mobile in its real shell, including the bottom bar and keyboard. Check
  intermediate widths too. Prevent squeezed send buttons, clipped choices,
  jumping popovers, awkward wrapping, and crowded chips. Use a mobile modal or
  sheet for selectors when the desktop popover does not fit. Preserve identity
  cues and test real touch interaction, not only a narrow viewport.

## Make the preview and shipped feature agree

For a substantial new UI or redesign, prefer a short interactive preview before
deep implementation, using Storybook or the project's existing preview tools.
Follow an explicit request to review designs first; do not invent a new approval
gate when implementation is already authorized. Scale this workflow down for a
small edit; adding a preview framework is not a prerequisite for every UI change.

Keep each feature's component examples and user journeys together in a discoverable
feature group, following the project's directory and navigation conventions.
Make both kinds of review easy to find:

1. **Individual components:** cover every added or changed user-facing component
   and its relevant variants and states, using the shared production components.
2. **User journeys:** show realistic full pages in the actual app shell, with
   interactive or sequential stories that follow a person from the natural entry
   point to a useful result. Keep example data consistent across journey steps.

Use clear section names or numbered groups to make the feature easy to browse.
For features spanning many components or pages, add a short review guide linking
component coverage and the main journeys. Keep preview source, fixtures, helpers,
and required configuration with the feature so another person can reproduce it.

Show the actual component and a realistic full-page or sequential journey view
using the existing app shell. Include relevant first-use, returning, populated,
long-content, loading, error, and mobile states. Make example data editable when
the preview tool supports it. Keep demo scaffolding and developer explanations
outside the product canvas; describe the intended route in the preview's notes.

Implement the approved design in the shared production components. Do not keep
a beautiful “design” story and a divergent “implemented” version, or overwrite
the approved design to match an inferior implementation. Remove or update obsolete
stories that create confusion.

After implementation, start at the real entry point and walk through to a useful
result. Inspect every visible sentence and watch each transition. Exercise the
relevant alternate states and verify the result persists or can be used next.
Check keyboard and touch interaction where relevant, recovery from errors, and
whether the next useful action is clear. Separate functional success from
experience quality: a saved result can still come from a confusing flow. Browser
observation and automated tests provide different evidence. Report what was
actually tested and any limits of that evidence; if the real interface was not
exercised, say so. A working isolated screen does not establish a working journey.

Before handing off, ask: **What can I remove, reuse, align, move into context, or
actually try to make this easier for the person using it?** Fix those concrete
issues within scope. Keep the handoff focused on the user-visible change and
observed result.
