# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Webinar materials for a 1-hour live session: **"AI and the Software Development Lifecycle."**  
Presenter: Chris Penick (Ascendient Learning).

Contents: a Reveal.js slide deck and four hands-on demos — all designed to run live during the webinar.

---

## Running the slides

```bash
npm install
npm run slides        # serves at http://localhost:1948 with live reload
npm run build-slides  # static export to _site/
```

The deck lives in `slides/deck.md`. Slide separator is `---`. Speaker notes go in HTML comments: `<!-- .slide: data-notes="..." -->`.

---

## Demo overview

| Directory | What it shows | Runtime |
|---|---|---|
| `demos/01-claude-code/` | Live Claude Code session script | none (manual) |
| `demos/02-agentic-workflow/` | Tool-calling agent loop via Anthropic API | Python |
| `demos/03-before-after/` | Buggy code → AI-fixed code + tests | Python / pytest |
| `demos/04-cicd/` | GitHub Actions AI review workflow | YAML |

---

## Running Python demos

```bash
cp .env.example .env      # add your ANTHROPIC_API_KEY
python3.13 -m pip install -r requirements.txt

# Agentic workflow demo
python3.13 demos/02-agentic-workflow/sdlc_agent.py

# Run the fixed payment tests
python3.13 -m pytest demos/03-before-after/after/test_payment.py -v
```

---

## The central demo artifact

`demos/03-before-after/before/payment.py` contains a deliberate double-discount bug.  
`demos/03-before-after/after/payment.py` is the corrected version.  
`demos/03-before-after/after/test_payment.py` has tests that catch the bug (and a comment explaining which test catches which failure mode).

This file is the anchor for Demo 1 (Claude Code fixes it live) and Demo 3 (show before/after).  
**Do not silently fix the bug in `before/payment.py`** — it's intentional.

---

## Slide structure

The deck follows the webinar outline:
1. Opening / agenda
2. AI evolution: copilot → autonomous agent
3. AI across the SDLC
4. Agentic workflows
5. Quality, security, governance
6. Developer ownership
7. Practical steps / takeaways
8. Q&A

Target runtime per section is marked in the demo READMEs.

---

## Model choices in demo code

- `sdlc_agent.py` uses `claude-opus-5` — most capable, appropriate for a complex multi-step task shown as a demo.
- `ai-review.yml` uses `claude-haiku-4-5-20251001` — fast and cheap, appropriate for high-volume CI.

When updating models, keep these choices consistent with the talking points in the slides (the slide deck explains *why* you pick different models for different tasks).
