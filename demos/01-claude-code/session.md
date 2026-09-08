# Demo 1: Claude Code Live Session

**Duration:** ~5 minutes  
**Goal:** Show Claude Code reading a real codebase, identifying a bug, writing a fix, and verifying it — with no manual hand-holding.

---

## Before the webinar

```bash
# Reset to clean state (do this before every practice run too)
bash demos/01-claude-code/reset.sh

# Confirm Claude Code is installed
claude --version
```

---

## Demo Script

### Step 1 — Open Claude Code in the demo directory

```bash
cd demos/01-claude-code
claude
```

*Talking point:* Claude Code is a terminal-based agentic coding assistant. It reads your working directory — every file, not just the one you have open.

---

### Step 2 — Give it a high-level task

Type at the Claude Code prompt:

```
There's a bug in payment.py — the discount is applied twice in the total
calculation. Find it, fix it, and add a test that would have caught it.
```

*What to narrate while it runs:*
- Watch it read the file first (tool call: Read) — you didn't tell it which lines
- It identifies the bug from the logic, not from the description
- It writes a test without being told which framework to use — it detects pytest from the directory
- The whole thing runs in under 2 minutes

---

### Step 3 — Review the output together

- Walk through the diff it produced
- Read the new test aloud — point out it tests the *exact invariant*, not just "total is a number"
- Talking point: *The developer's job shifted. They didn't write this — they're reviewing it. That's the new skill.*

---

### Step 4 — Run the generated test

```bash
uv run --with pytest pytest test_payment.py -v
```

*Talking point:* The test passes. But a human still needs to verify the test is testing the right thing — AI can write tests that pass but miss the actual bug class.

---

## Fallback (if live demo fails)

Show `fallback-diff.txt` and walk through it manually. Same talking points apply.
