---
name: loop
description: >-
  Run a prompt or skill in this session on a recurring or variable interval
  (e.g. /loop 5m /foo).
---
# Loop

Read [runtime](../runtime/SKILL.md) for host-specific tools and paths.

Run `/loop` on a recurring or variable interval. First decide which mechanism applies from the tools you have, then follow only that section below:

- If the host exposes a persistent scheduler or heartbeat, use **Host scheduler**.
- Otherwise use **Active session** and disclose that the loop cannot continue after the session ends.

## Parse

Accept `/loop [interval] <prompt>`.

- Leading interval: `5m /foo`, `30s check status`, `2h run report`.
- Trailing interval: `check deploy every 5m`, `run tests every 10 minutes`.
- No interval: dynamic mode; the agent chooses the delay and may change it tick to tick.
- Empty prompt: show `Usage: /loop [interval] <prompt>`.

Use intervals like `30s`, `5m`, `2h`, `1d`. Convert unit words to short units. If the user gives a cron-style phrase ("every weekday at 9am") use the host scheduler's supported schedule representation.

## Host scheduler

Use the host's documented scheduler, never guessed tool names or arguments. On Codex desktop use its automation capability when available. On Claude Code use its exposed scheduling tools when available. For Paperclip-managed work, use Paperclip heartbeats or routines; do not create a competing scheduler inside the worker.

1. Check existing schedules for an already-running matching loop.
2. Run the prompt once immediately.
3. Create or update one schedule with the requested prompt, interval, execution workspace, and finish condition. For an event-driven loop, use a supported event trigger with a long fallback heartbeat.
4. Confirm the persisted schedule identifier, actual interval, and execution scope returned by the host. Do not claim the loop survives session exit unless the host supports it.
5. On each wake, check the finish condition before doing more work. Read live state, perform the next iteration, and record the result. If both an event wake and a timer arrive, avoid duplicate work.
6. To change pace, update the existing schedule through the host's documented operation. Do not create duplicates.
7. On completion or a stop request, disable or delete only this loop's schedule and confirm the resulting state.

If several timers match the purpose and you cannot disambiguate, surface the candidates to the user and ask which one to stop.

## Active session

The user wants the agent to self-pace. Decide what makes the next iteration worth running — a passage of time, or an observable event.

1. **Run the prompt now.**
2. Use the host's supported wait or event tools, then re-check the predicate. Keep waits bounded so new user input can interrupt.
3. Repeat while the session is active and work remains authorized.
4. If the session must end before completion, write a checkpoint and say that no future wake has been scheduled. A background shell `sleep` or printed sentinel alone does not wake the agent.
5. **To stop**, stop the owned watcher and do not begin another iteration.

## Guidance

- Use a unique name per loop so unrelated timers do not collide.
- Avoid noisy commands inside the loop.
- Do not create duplicate fixed loops or dynamic sleepers.
- On stop, do not schedule another timer.
