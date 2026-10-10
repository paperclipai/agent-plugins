---
name: trees-maps-theorems
description: >
  Structure any communication artifact — documents, reports, plans, issue
  comments, PR descriptions, emails, presentations, slides, charts, and
  dashboards — using Jean-luc Doumont's "Trees, Maps, and Theorems" method.
  Use whenever the goal is to get a message across to a busy audience, when
  asked to improve clarity or structure of writing or slides, or when a
  deliverable will be judged by whether readers act on it, not just read it.
---

# Trees, Maps, and Theorems

This skill distills Jean-luc Doumont's *Trees, Maps, and Theorems: Effective
Communication for Rational Minds* (Principiae, 2009) into a procedure for
producing communication that busy, selective readers can act on. The title is
the method: organize content as a **tree**, give the audience a **map** of
that tree, and state each point as a **theorem** — the assertion first, the
proof after.

Communication is not about what you want to say; it is about what you want
the audience to *do* as a result. Optimize for their reading, not your
writing.

## The three laws

Apply these to every artifact, at every level, before any other rule. When
two rules conflict, the laws win; when the laws conflict, audience wins.

1. **Adapt to your audience.** Decide who will consume this and what they
   need in order to decide or act. Write for their questions, vocabulary,
   and available time — not for your process. "What I did, in the order I
   did it" is almost never the right structure.
2. **Maximize the signal-to-noise ratio.** Noise is anything that does not
   carry your message: hedging, boilerplate, decoration, repeated context
   the reader already has, chartjunk, screenshots of things nobody must
   inspect. Removing noise beats amplifying signal.
3. **Use effective redundancy.** Important messages should survive skimming:
   state them in the title AND the summary AND the relevant section; in a
   talk, say it and show it. Redundancy is for the essentials only —
   redundant noise is the worst of both worlds.

## Messages, not information

Information is fact; a message is what the audience should conclude or do.

- Information: "The test suite takes 14 minutes."
- Message: "The test suite is too slow to gate every commit — run it
  nightly instead."

Apply the **"so what?" test** to every title, heading, paragraph, slide, and
figure caption. If a reader can answer "so what?" faster than you stated it,
you wrote information, not a message. State conclusions as complete
sentences; "Results" is a label, "Latency doubles above 100 concurrent
users" is a message.

## Trees: structure the content hierarchically

- Break content into **3–5 branches per level**. More than ~5 items at one
  level means a grouping is missing; one item means the level is fake.
- Make each branch meaningful on its own: a reader who opens only one
  section should get a complete, coherent unit.
- Order branches by what the audience needs first (usually: conclusion →
  support → detail), not by chronology of your work.
- Depth is fine; unmapped depth is not. Every level you add needs a map
  (below).

## Maps: reveal the structure before the detail

Readers navigate; they do not read linearly. At every branching point, tell
them where they are and what is coming.

**Open every substantial artifact with a foreword that answers four
questions, in order:**

| Element | Question it answers |
|---|---|
| **Context** | What situation is this about? What does the reader already know? |
| **Need** | Why must something be done — and why now? |
| **Task** | What was done (or will be done) about the need? |
| **Object** | What does *this document* cover, and how is it organized? |

Then preview the branches ("Section 2 shows X; Section 3 proposes Y").
Inside the body, open each section with a one-line map of its subsections.
A reader who reads only your forewords should still leave with every main
message.

## Theorems: state the message, then prove it

Lead every unit with its message as a full assertion; everything after is
proof.

- **Documents**: the summary states the main messages and conclusions —
  self-contained, because most readers read nothing else.
- **Sections**: the first paragraph states the section's message.
- **Paragraphs**: the first sentence is the point; the rest supports it.
  If you must skim a colleague's paragraph, you read its first sentence —
  write so that this works on yours.
- **Headings and slide titles**: prefer sentences ("Caching removes the
  p99 spike") over labels ("Performance").
- Never bury the conclusion at the end "to build up to it." Rational minds
  accept a stated theorem and then check the proof; they resent a mystery.

## Written documents

Structure any report, plan, RFC, or doc as four components:

1. **Header** — informative title + abstract. The abstract compresses the
   whole document: need, task, findings, conclusion. No suspense.
2. **Foreword** — context, need, task, object (see Maps).
3. **Summary** — the main messages and recommendations, self-supporting.
4. **Body** — the tree of sections, each theorem-first, ending with a
   conclusion that restates the messages (effective redundancy) and names
   the next action and its owner.

For short artifacts (comments, emails), collapse this: one status line that
IS the message, bullets as proof, explicit next action. The structure
scales down; it never disappears.

### Applied to everyday engineering artifacts

- **Issue comment / status update**: first line = the message ("Fix shipped
  and verified; nothing remains on this issue" / "Blocked: X must do Y").
  Bullets = evidence with links. Last line = who does what next.
- **PR description**: title is a message, not a location ("Stop retrying
  409s" not "Update checkout logic"). Body: why (need), what changed
  (task), how it is verified (proof), what reviewers should look at (map).
- **Plan**: recommendation first, then the map of phases, then per-phase
  messages with their proof. A plan whose summary cannot be approved
  without reading the body has failed the summary.
- **Incident report / RCA**: impact and root cause in the first two
  sentences; timeline is an appendix, not an opening.

## Oral presentations and slides

- **Plan the talk around one main message** the audience must retain, and
  at most 3–5 supporting messages. Time is the audience's, not yours.
- **Open** with: attention getter → need → task → preview (the map). Do not
  open with an outline slide of labels; open with why they should listen.
- **One message per slide**, stated as a full sentence, ideally as the
  slide title. Everything else on the slide is proof of that sentence.
- Slides support the speaker; they do not duplicate the script. If the
  slide can be read instead of listening to you, cut the slide or cut you.
- Maximize signal-to-noise ruthlessly on slides: no decorative images,
  logos on every page, or bullet pyramids. White space is not wasted space.
- **Close** by restating the main messages and the call to action
  (effective redundancy) — never end on "Questions?" as the final content.

## Graphical displays

- A graph answers a question; pick the graph type from the question, not
  from the tool's default. Trends → lines; comparison → bars; exact values
  → a table, not a graph.
- **The caption states the message**: "Throughput degrades sharply beyond
  8 workers," not "Throughput vs. worker count." A figure whose caption is
  a label forces every reader to re-derive your conclusion.
- Maximize data-ink: remove gridlines, frames, 3D effects, and colors that
  encode nothing. Label curves directly instead of using a legend when
  practical.
- Design each figure to be understood standalone — figures are harvested
  out of documents and pasted into other ones.

## Pre-publish checklist

Run this before posting/sending any nontrivial artifact:

- [ ] Named the audience and the action you want from them?
- [ ] First line/title/abstract states the main message (passes "so what?")?
- [ ] Foreword answers context, need, task, object?
- [ ] Structure is a mapped tree — 3–5 branches, previewed before detail?
- [ ] Every paragraph/slide/figure leads with its message?
- [ ] Noise removed — hedges, boilerplate, decoration, known context?
- [ ] Essentials redundantly encoded (title + summary + body)?
- [ ] Next action and its owner explicit at the end?

## Attribution

Method from Jean-luc Doumont, *Trees, Maps, and Theorems: Effective
Communication for Rational Minds*, Principiae, 2009
(https://www.principiae.be/). This skill is a distillation for agent use,
not a reproduction of the book.
