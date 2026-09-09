# Demo 5: Multi-Agent Pipeline

**Duration:** ~5 minutes  
**Goal:** Show how specialization across multiple agents differs from a single agent doing everything.

## What it demonstrates

Three agents, three API calls, one pipeline:

| Agent | Model | Role |
|-------|-------|------|
| Planner | claude-haiku-4-5 | Reads the bug report and code, produces a numbered fix plan |
| Coder | claude-opus-5 | Takes the plan and buggy code, returns corrected code |
| Reviewer | claude-haiku-4-5 | Reads only the corrected code, returns a verdict |

Each agent's context is intentionally scoped. The Reviewer never sees the original bug report — it evaluates the code on its own merits.

Contrast with Demo 02: that's one agent calling tools in a loop. This is three agents in a chain, each with a specialized system prompt and the right model for the job.

## Run it

```bash
cd demos/05-multi-agent
cp .env.example .env        # add your ANTHROPIC_API_KEY
uv run multi_agent_pipeline.py
```

## What to narrate

- **Model choice:** Planner and Reviewer use Haiku (fast, cheap); Coder uses Opus (most capable). You match the model to the task, not the other way around.
- **Scoped context:** The Reviewer only sees the fixed code. It can't rationalize a bad fix by knowing the original intent. That independence makes it a more honest check.
- **Parallelism:** In a real system, Planner and Reviewer could run in parallel. Here they're sequential to keep the demo readable.
- **Failure modes:** If the Planner produces a bad plan, the Coder follows a bad plan. The pipeline makes each agent's output visible so failures are caught early.

## Key talking point

> "You don't need one superintelligent agent. You need the right agent for each job."
