# Agent plugins

Dotta's personal agent library, maintained in Git and used directly from the
checkout. `dstack` holds original skills and workflows; `vendor` holds imported
packages with their attribution and provenance intact. The public repository is
[paperclipai/agent-plugins](https://github.com/paperclipai/agent-plugins).

The aim is useful compatibility, with Cursor's richer plugin model as the preferred
direction, the Agent Plugins standard as a portable foundation, and Claude, Codex,
and Vercel's skills CLI supported where practical. No single format is a hard
constraint. See [compatibility](docs/compatibility.md) for the boundaries.

```text
agent-plugins/
├── dstack/
│   ├── plugin.json                 # Agent Plugins portable manifest
│   ├── .cursor-plugin/plugin.json  # Cursor packaging
│   ├── .claude-plugin/plugin.json  # Claude packaging
│   └── skills/
│       ├── dotta-ui-ux/
│       └── trees-maps-theorems/
├── vendor/
│   ├── pstack/                     # Complete upstream snapshot, ordinary files
│   └── pstack.lock.json            # Source revision and file hashes
├── docs/
└── scripts/
```

`dstack` can grow agents, hooks, commands, and MCP integrations when there is a
real use for them. It currently contains two skills, not placeholder agents.
The root Cursor and Claude catalogs expose `dstack`; the preserved pstack port
uses its own installer and is not advertised as a native plugin.

## Use the checkout every day

Edit the canonical files here, try the change in an agent, and commit the result.
Discovery links expose those same files; edits do not require copying a skill
again. Start a fresh session if the agent has cached an older skill.

From this repository:

```sh
# Preview, then expose dstack skills to a selected agent.
python3 scripts/install.py --agent codex --dry-run
python3 scripts/install.py --agent codex
# Optional: --agent claude-code or --agent cursor; repeat --agent for several.
```

The installer links individual skill folders, preserves unrelated entries, and
refuses conflicts. Its Codex path is `~/.codex/skills`, matching this machine's
existing installation; see the compatibility notes for `.agents/skills` support.
It installs skills only. Do not also install dstack as a native plugin in the
same agent unless you intend to have both registrations.

The initial migration preserves the two existing Codex discovery paths as
symlinks into `dstack/skills`. The existing `~/.agents/poteto-stack` path points
to `vendor/pstack`, preserving its existing skill links. Other skills and agent
installations are unchanged.

For a separate pstack installation, its existing installer supports:

```sh
python3 vendor/pstack/scripts/install.py --runtime codex --scope user
python3 vendor/pstack/scripts/install.py --runtime claude --scope user
```

That installer reports conflicts rather than replacing another installation.
See [pstack runtime support](vendor/pstack/RUNTIME.md) for its supported workflows.

## Maintain and verify the library

```sh
python3 scripts/verify_vendor.py
git diff --check
```

Read [vendor maintenance](vendor/README.md) before updating pstack. Its upstream
history-dependent validator needs the original repository history and cannot run
unchanged against this plain snapshot. Our verifier checks every snapshot file
against the recorded hashes and executable bits instead.

There is no blanket license for the personal content yet. Vendored content keeps
its upstream license and notices; see `vendor/pstack/LICENSE`, `NOTICE.md`, and
`UPSTREAM.md`. Public repository visibility does not change those license terms.
