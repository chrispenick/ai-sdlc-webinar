# Demo 4: AI in CI/CD

**Duration:** ~3 minutes (show the YAML, walk the flow, show a sample output)  
**Goal:** Demonstrate AI as a policy-enforcing layer in the pull request pipeline.

## What the workflow does

On every PR touching Python files:
1. Extracts the diff
2. Sends it to Claude Haiku (fast, cheap model — appropriate for CI)
3. Posts the review as a PR comment
4. Human still merges — AI is advisory, not a gate

## Run it locally (no GitHub needed)

```bash
cd demos/04-cicd
cp .env.example .env        # add your ANTHROPIC_API_KEY
uv run review_locally.py
```

`uv` installs dependencies automatically from the inline script metadata.

## What to narrate

- Model choice matters: Haiku for high-volume CI tasks, Opus for complex one-off analysis
- The review is **non-blocking** — it informs, doesn't block merge
- You can make it blocking: add a required status check and parse the review for severity keywords
- Every PR has a record of what the AI saw and said — that's auditability

## Sample AI review output

```markdown
## AI Code Review

- **Bug (medium):** `calculate_total` applies the discount twice in the `total`
  computation (line 14). The discounted subtotal is computed, then the discount
  is subtracted again from `subtotal` rather than from `discounted`.
- **No security issues found.**
- **Style:** Function lacks a return-type annotation. Consider `-> dict`.

_Reviewed by claude-haiku-4-5 — human review still required._
```

## Deploy to GitHub Actions

1. Add `ANTHROPIC_API_KEY` to your GitHub repo secrets.
2. Copy `.github/workflows/ai-review.yml` to your repo.
3. Open a PR — the bot comments automatically.
