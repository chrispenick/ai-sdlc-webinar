---
title: AI and the Software Development Lifecycle
theme: solarized
highlightTheme: github
revealOptions:
  transition: slide
  controls: true
  progress: true
  slideNumber: true
---

# AI and the Software Development Lifecycle

### What It Means for Your Team, Right Now

**Chris Penick** | Ascendient Learning

---

## Today's Agenda

1. AI's evolution: copilot → autonomous agent
2. AI across the SDLC
3. Agentic workflows in practice
4. Quality, security, and governance
5. Keeping developers in control
6. What to put in place now

---

## About Chris

- Instructor at Ascendient Learning
- Developer and AI practitioner
- Working with engineering teams adopting AI tooling daily

<!-- .slide: data-notes="Personal intro, credibility note. Keep to ~60 seconds." -->

---

# Part 1

## From Copilot to Autonomous Agent

---

## The Copilot Era (2021-2023)

- GitHub Copilot, Tabnine, Codeium
- Autocomplete for developers
- Still human-driven: you write, AI suggests

**Key insight:** AI as a junior pair programmer

<!-- .slide: data-notes="Set the baseline. Most audience members know this era well." -->

---

## What Changed

- Models got dramatically more capable (GPT-4, Claude 3.x, Gemini)
- Context windows expanded from 4K → 200K+ tokens
- Tools let AI act, not just suggest

**AI can now read your codebase, run commands, and iterate**

---

## The Spectrum Today

| Mode | Who drives? | AI does |
|------|-------------|---------|
| Autocomplete | Human | Single-line suggestions |
| Chat assistant | Human | Explains, drafts, reviews |
| Inline agent | Human | Multi-file edits |
| Agentic loop | AI | Plans, executes, tests, iterates |

<!-- .slide: data-notes="This table is the conceptual anchor for the whole session." -->

---

## Demo: Claude Code in Action

> **Live demo:** see `/demos/01-claude-code/`

*Claude Code reads an existing codebase, identifies a bug, writes a fix, and runs tests. No hand-holding.*

<!-- .slide: data-notes="Switch to terminal. Follow the script in demos/01-claude-code/session.md" -->

---

# Part 2

## AI Across the Software Development Lifecycle

---

## Where AI Adds Value

<div style="display:flex;align-items:flex-start;justify-content:center;gap:6px;font-size:0.52em;margin-top:1em">
  <div style="text-align:center;background:#e8e8e8;border-radius:6px;padding:10px 8px;min-width:74px"><strong>Requirements</strong><br><span style="color:#586e75;font-size:0.9em">AI drafts</span></div>
  <div style="padding-top:14px;color:#999">→</div>
  <div style="text-align:center;background:#e8e8e8;border-radius:6px;padding:10px 8px;min-width:74px"><strong>Design</strong><br><span style="color:#586e75;font-size:0.9em">AI mocks</span></div>
  <div style="padding-top:14px;color:#999">→</div>
  <div style="text-align:center;background:#e8e8e8;border-radius:6px;padding:10px 8px;min-width:74px"><strong>Code</strong><br><span style="color:#586e75;font-size:0.9em">AI writes</span></div>
  <div style="padding-top:14px;color:#999">→</div>
  <div style="text-align:center;background:#e8e8e8;border-radius:6px;padding:10px 8px;min-width:74px"><strong>Test</strong><br><span style="color:#586e75;font-size:0.9em">AI writes</span></div>
  <div style="padding-top:14px;color:#999">→</div>
  <div style="text-align:center;background:#e8e8e8;border-radius:6px;padding:10px 8px;min-width:74px"><strong>Review</strong><br><span style="color:#586e75;font-size:0.9em">AI flags</span></div>
  <div style="padding-top:14px;color:#999">→</div>
  <div style="text-align:center;background:#e8e8e8;border-radius:6px;padding:10px 8px;min-width:74px"><strong>Deploy</strong><br><span style="color:#586e75;font-size:0.9em">AI gates</span></div>
  <div style="padding-top:14px;color:#999">→</div>
  <div style="text-align:center;background:#e8e8e8;border-radius:6px;padding:10px 8px;min-width:74px"><strong>Monitor</strong><br><span style="color:#586e75;font-size:0.9em">AI alerts</span></div>
</div>

---

## Requirements & Planning

- AI summarizes Jira/Linear tickets into acceptance criteria
- Identifies ambiguity and asks clarifying questions
- Drafts technical specs from user stories

**Risk:** Garbage in, garbage out. AI amplifies vague requirements.

---

## Code Generation

- Function-level: 70-90% of simple CRUD is AI-generated
- File-level: AI scaffolds entire modules from a spec
- Repo-level: agents build features end-to-end

**The question shifts from "can it write code?" to "can we trust it?"**

---

## Automated Testing

- AI generates unit tests from function signatures
- Mutation testing and edge-case discovery
- Test gap analysis against existing coverage

> Demo: see `/demos/03-before-after/` for AI-generated vs. hand-written test comparison

---

## Code Review

- PR summary generation (what changed, why it matters)
- Security and style linting at commit time
- AI reviewer catches logic errors, not just formatting

> Demo: see `/demos/04-cicd/` for a GitHub Actions AI review workflow

---

# Part 3

## Agentic Workflows in Practice

---

## What Is an Agentic Workflow?

An AI that:
1. Receives a high-level goal
2. Plans steps on its own
3. Calls tools (shell, API, browser)
4. Evaluates output and iterates
5. Delivers a result

**Not autocomplete. Closer to a junior developer you assign a ticket.**

---

## Building Blocks

- **LLM:** reasoning engine
- **Tools:** what it can do (bash, search, read/write files)
- **Memory:** context across steps
- **Guardrails:** what it can't do

<!-- .slide: data-notes="Keep this conceptual. The demo will make it concrete." -->

---

## Demo: SDLC Agent

> **Live demo:** see `/demos/02-agentic-workflow/`

*A Python agent that takes a GitHub issue, writes a fix, runs the test suite, and opens a draft PR.*

<!-- .slide: data-notes="Walk through sdlc_agent.py. Highlight the tool-call loop in the output." -->

---

## Multi-Agent Pipelines

One agent does everything. Multi-agent: each specialist does one job.

```
Planner → Coder → Reviewer
```

- Each agent gets a focused system prompt and scoped context
- Cheap fast models (Haiku) for planning and review; capable models (Opus) for generation
- Agents can run in parallel when tasks are independent
- A bad plan fails loudly before bad code is written

> **Live demo:** see `/demos/05-multi-agent/`

<!-- .slide: data-notes="Contrast with Demo 02 — same problem, different architecture. Point out the model choices: Haiku for Planner and Reviewer, Opus for Coder. Ask: why not just use Opus for everything?" -->

---

## Where Teams Are Deploying Agents Today

- **PR agents:** auto-review, auto-fix lint/type errors
- **Test agents:** fill coverage gaps on demand
- **Documentation agents:** keep docs in sync with code changes
- **On-call agents:** triage alerts, suggest runbooks

---

## What's Coming (Next 12-18 Months)

- Agents that own whole features from ticket to deploy
- Multi-agent pipelines that span the full delivery cycle
- AI as a participant in sprint planning

**The bottleneck shifts from writing code to reviewing it**

---

# Part 4

## Quality, Security, and Governance

---

## The Trust Problem

AI-generated code:
- Passes tests that weren't written to catch AI mistakes
- Looks plausible but may be subtly wrong
- Can introduce vulnerabilities the developer didn't intend

**Code review becomes more important, not less**

---

## Security Considerations

- AI trained on public code, including vulnerable code
- Prompt injection in AI coding tools
- Supply-chain risks when agents can run `pip install`
- Data exfiltration via AI tools with broad permissions

<!-- .slide: data-notes="Don't catastrophize. These are real but manageable with the right controls." -->

---

## A Governance Framework

<div style="display:flex;justify-content:center;gap:24px;font-size:0.6em;margin-top:1em">
  <div style="text-align:center;flex:1;max-width:200px">
    <div style="font-weight:bold;font-size:1.1em;border-bottom:2px solid #93a1a1;padding-bottom:6px;margin-bottom:10px">Visibility</div>
    <div style="color:#586e75;line-height:2">Audit logs<br>Cost tracking<br>Tool logging</div>
  </div>
  <div style="text-align:center;flex:1;max-width:200px">
    <div style="font-weight:bold;font-size:1.1em;border-bottom:2px solid #93a1a1;padding-bottom:6px;margin-bottom:10px">Control</div>
    <div style="color:#586e75;line-height:2">Human approval<br>Scope limits<br>Rollback policy</div>
  </div>
  <div style="text-align:center;flex:1;max-width:200px">
    <div style="font-weight:bold;font-size:1.1em;border-bottom:2px solid #93a1a1;padding-bottom:6px;margin-bottom:10px">Accountability</div>
    <div style="color:#586e75;line-height:2">Code ownership<br>Review gates<br>Incident playbooks</div>
  </div>
</div>

---

## Quality Gates in CI/CD

> Demo: see `/demos/04-cicd/.github/workflows/`

- AI generates code → human reviews PR
- AI reviewer flags issues → human approves merge
- AI coverage check → blocks merge if gaps detected

**Policy lives in the pipeline, not in individual discipline**

---

# Part 5

## Keeping Developers in Control

---

## The Ownership Risk

If a developer doesn't understand the code AI wrote:
- They can't debug it confidently
- They can't extend it safely
- They become dependent on AI to maintain AI-written code

**This is the "junior dev trap" at scale**

---

## Practical Ownership Strategies

- **Read before you merge:** no rubber-stamping AI output
- **Write the tests first:** you understand the spec better than the AI
- **Explain it back:** if you can't explain the change, you don't own it
- **Keep AI off the critical path** until it's earned trust

---

## What Healthy AI-Assisted Development Looks Like

1. Developer sets intent and acceptance criteria
2. AI drafts implementation
3. Developer reads, questions, modifies
4. AI fills gaps developer identifies
5. Developer reviews final output and merges

**AI accelerates; developer steers**

---

# Part 6

## What to Put in Place Now

---

## For Individual Developers

- Learn one AI coding tool deeply (Claude Code, Copilot, Cursor)
- Practice reading AI-generated code critically
- Develop a personal "AI review checklist"

---

## For Engineering Managers

- Define your team's AI policy (what's allowed, what isn't)
- Add AI output review to your PR process
- Track AI tool costs alongside other tooling

---

## For Architects and Leads

- Identify your stack's highest-risk areas for AI errors
- Define guardrails before deploying agents (scope, permissions, rollback)
- Pilot agentic workflows in low-risk areas first

---

## For Technology Leaders

- Treat AI tooling as infrastructure, with procurement, security, and audit requirements
- Invest in developer AI literacy, not just tool adoption
- Build governance before you need it

---

## The One Thing to Do This Week

> **Define what "good AI-assisted code" means on your team. Write it down.**

A checklist. A policy doc. A one-pager. Something.

If it isn't written, it isn't enforced.

---

## Key Takeaways

- AI is already autonomous enough to change how teams work
- Value is real, but so are the risks if governance lags
- Developer ownership and understanding are not optional
- Policy and process matter more than any single tool

---

## Resources

- [Claude Code](https://claude.ai/code): agentic coding assistant
- [GitHub Copilot](https://github.com/features/copilot): inline AI coding
- [Anthropic Claude API](https://www.anthropic.com/api): build your own agents
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/): AI security risk reference
- [MITRE ATLAS](https://atlas.mitre.org/): adversarial threat landscape for AI systems
- Demo code: `/demos/` in this repo

---

# Q&A

**Bring your questions.**

Chris Penick | [chris.penick@accenture.com](mailto:chris.penick@accenture.com)
