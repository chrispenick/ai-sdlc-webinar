# Demo 06 — Spec-Driven Development with OpenSpec

**Time:** ~4 minutes  
**Key point:** Instead of asking AI to fix a bug, give it a formal spec. The spec is the contract between you and the AI — agreement on *what* to build before any code is written.

---

## Setup (before the session)

```bash
cd demos/06-openspec
./reset.sh
```

Confirm you have `ANTHROPIC_API_KEY` set (or copy from `demos/02-agentic-workflow/.env`).

---

## What OpenSpec is

OpenSpec (github.com/Fission-AI/OpenSpec) is a lightweight spec-driven framework.
You write requirements and GIVEN/WHEN/THEN scenarios in Markdown.
AI coding tools read the spec before writing code — so humans and AI agree on *what* first.

Key ideas:
- Requirements use RFC 2119 language: SHALL, MUST, SHOULD
- Scenarios are testable acceptance criteria
- The workflow is: spec → propose → apply → archive

---

## Live walkthrough

### 1. Show the spec

Open `specs/payment.md` in the editor or print it:

```bash
cat specs/payment.md
```

**What to say:**
> "This is an OpenSpec document. It defines what `calculate_total` SHALL do — in plain language
> that both developers and AI can reason about. Notice the GIVEN/WHEN/THEN scenarios:
> these are acceptance criteria, not implementation hints."

Point out:
- The `SHALL apply a percentage discount once` requirement
- The scenario `total equals $97.20` — this is a specific, verifiable claim
- There is no code here — just behaviour

### 2. Show the buggy code

```bash
cat payment.py
```

**What to say:**
> "Here's the current implementation. It has a bug — the discount is subtracted twice.
> But instead of asking Claude 'find and fix the bug', we're going to hand it the spec
> and say: make this code satisfy these scenarios."

### 3. Run the demo

```bash
uv run spec_driven_fix.py
```

**What to say as it runs:**
> "Claude reads the spec, reads the code, and derives the fix from the WHEN/THEN clauses —
> not from pattern-matching 'what does a discount function usually look like'.
> The spec is the source of truth."

### 4. Review the output

The script prints:
- The spec (what we agreed on)
- The current buggy code
- Claude's spec-derived implementation
- Scenario verification results (5/5 pass)

**What to say:**
> "Five scenarios, all green. The spec drove the implementation.
> Tomorrow, when a new engineer joins the team, they read the spec — not the code —
> to understand what this function must do. The AI and the human are aligned."

---

## Key talking points

- **Spec-first prevents scope creep.** If it's not in the spec, AI won't build it.
- **Scenarios are tests in disguise.** A well-written scenario is a pytest waiting to be written.
- **The spec outlives the code.** Code gets refactored; the spec stays as the record of intent.
- **OpenSpec integrates with Claude Code and Cursor** via slash commands (`/opsx:propose`, `/opsx:apply`).

---

## Optional: show the OpenSpec CLI

If time allows, demonstrate the CLI workflow concept (requires `npm install -g @fission-ai/openspec@latest`):

```bash
openspec list --specs   # list specs with requirement counts
```

The full workflow:
```
/opsx:propose  →  review plan  →  /opsx:apply  →  review code  →  /opsx:archive
```
