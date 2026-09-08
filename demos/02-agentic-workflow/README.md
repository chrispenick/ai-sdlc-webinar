# Demo 2: Agentic Workflow

**Duration:** ~5 minutes  
**Goal:** Show the anatomy of a tool-calling agentic loop — the model plans, acts, observes, and iterates.

## What it does

`sdlc_agent.py` is a minimal SDLC agent that:
1. Reads a buggy source file (`payment.py`)
2. Proposes a code fix (as a diff)
3. Generates pytest tests
4. Writes a PR description

All using the Anthropic Messages API with tool use. No frameworks — just the raw loop.

## Run it

```bash
cd demos/02-agentic-workflow
cp .env.example .env        # add your ANTHROPIC_API_KEY
uv run sdlc_agent.py
```

`uv` installs dependencies automatically from the inline script metadata — no separate install step needed.

## What to narrate during the demo

- Point out the `while True` loop — this is the **agentic loop**: model → tool call → result → model
- The model chose the *order* of operations (read first, then fix, then test, then PR) — you didn't specify that
- Each `→ Calling tool:` line in the output is a decision the model made on its own
- In production you'd swap the simulated tools for real file I/O, git commands, and GitHub API calls

## Key talking point

> "The developer didn't write a sequence of steps. They gave the agent a goal and the tools to achieve it. The model planned the steps."
