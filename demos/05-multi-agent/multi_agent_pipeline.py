# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.40.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
Multi-agent pipeline demo — three specialized agents, each a separate API call.

Pipeline: Planner (Haiku) → Coder (Opus) → Reviewer (Haiku)

Contrasts with Demo 02: instead of one agent with tools, this uses three
agents with scoped context and different models matched to each role.

Run:
    cd demos/05-multi-agent
    cp .env.example .env   # add ANTHROPIC_API_KEY
    uv run multi_agent_pipeline.py
"""

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

HAIKU = "claude-haiku-4-5-20251001"
OPUS  = "claude-opus-5"

ISSUE = """GitHub Issue #42: calculate_total(100.0, discount_pct=10) returns 87.20 instead of 97.20.
The discount appears to be applied twice in the total calculation.
File: payment.py"""

BUGGY_CODE = open(os.path.join(os.path.dirname(__file__), "payment.py")).read()

DIVIDER = "=" * 60


def call(model: str, system: str, user: str) -> str:
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return response.content[0].text


def planner(issue: str, code: str) -> str:
    print(f"\n{DIVIDER}")
    print("AGENT 1: PLANNER  (claude-haiku — fast, cheap)")
    print(DIVIDER)
    plan = call(
        model=HAIKU,
        system=(
            "You are a senior engineer planning a bug fix. "
            "Given a bug report and the relevant source code, produce a concise numbered list "
            "of implementation steps needed to fix the bug. Be specific about which lines to change "
            "and why. Do not write code — write a plan."
        ),
        user=f"Bug report:\n{issue}\n\nSource code:\n```python\n{code}\n```",
    )
    print(plan)
    return plan


def coder(plan: str, code: str) -> str:
    print(f"\n{DIVIDER}")
    print("AGENT 2: CODER  (claude-opus-5 — most capable, used only where it matters)")
    print(DIVIDER)
    fixed = call(
        model=OPUS,
        system=(
            "You are an expert Python developer. "
            "Given an implementation plan and the original buggy source code, "
            "produce the corrected Python file. "
            "Output only the corrected code — no explanation, no markdown fences."
        ),
        user=f"Implementation plan:\n{plan}\n\nOriginal code:\n```python\n{code}\n```",
    )
    print(fixed)
    return fixed


def reviewer(fixed_code: str) -> str:
    print(f"\n{DIVIDER}")
    print("AGENT 3: REVIEWER  (claude-haiku — fast, cheap)")
    print(DIVIDER)
    # Note: Reviewer only sees the corrected code, not the original issue.
    # Its context is intentionally scoped.
    review = call(
        model=HAIKU,
        system=(
            "You are a code reviewer. "
            "Review the following Python code for correctness, edge cases, and potential concerns. "
            "Be concise. Format as a short markdown list with a final verdict: APPROVED or NEEDS CHANGES."
        ),
        user=f"```python\n{fixed_code}\n```",
    )
    print(review)
    return review


def main():
    print(DIVIDER)
    print("MULTI-AGENT PIPELINE DEMO")
    print(f"Issue: {ISSUE.splitlines()[0]}")
    print(DIVIDER)

    plan        = planner(ISSUE, BUGGY_CODE)
    fixed_code  = coder(plan, BUGGY_CODE)
    _review     = reviewer(fixed_code)

    print(f"\n{DIVIDER}")
    print("Pipeline complete: Planner → Coder → Reviewer")
    print(DIVIDER)


if __name__ == "__main__":
    main()
