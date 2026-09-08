# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.40.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
SDLC Agent demo — shows an agentic tool-call loop using the Anthropic API.

This agent accepts a GitHub issue description and:
  1. Analyzes the issue
  2. Proposes a fix (as a code diff)
  3. Generates tests for the fix
  4. Produces a PR description

Run:
    cp .env.example .env   # add ANTHROPIC_API_KEY
    uv run sdlc_agent.py
"""

import os
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
MODEL = "claude-opus-5"

# ---------------------------------------------------------------------------
# Tool definitions — what the agent can "do"
# ---------------------------------------------------------------------------

tools = [
    {
        "name": "read_file",
        "description": "Read the contents of a source file in the repository.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Repo-relative file path"}
            },
            "required": ["path"],
        },
    },
    {
        "name": "propose_fix",
        "description": "Propose a code change as a unified diff.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "diff": {"type": "string", "description": "Unified diff string"},
                "explanation": {"type": "string"},
            },
            "required": ["path", "diff", "explanation"],
        },
    },
    {
        "name": "generate_tests",
        "description": "Generate pytest tests for the proposed fix.",
        "input_schema": {
            "type": "object",
            "properties": {
                "test_code": {"type": "string"},
                "target_file": {"type": "string"},
            },
            "required": ["test_code", "target_file"],
        },
    },
    {
        "name": "write_pr_description",
        "description": "Write a pull request title and body.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "body": {"type": "string"},
            },
            "required": ["title", "body"],
        },
    },
]

# ---------------------------------------------------------------------------
# Simulated tool execution (in a real scenario, these would hit actual files/git)
# ---------------------------------------------------------------------------

DEMO_FILES = {
    "payment.py": open(
        os.path.join(os.path.dirname(__file__), "payment.py")
    ).read()
}


def execute_tool(name: str, inputs: dict) -> str:
    if name == "read_file":
        path = inputs["path"]
        content = DEMO_FILES.get(os.path.basename(path), f"[file not found: {path}]")
        return f"```python\n{content}\n```"

    if name == "propose_fix":
        print(f"\n[TOOL] propose_fix → {inputs['path']}")
        print(f"  Explanation: {inputs['explanation']}")
        print(f"  Diff:\n{inputs['diff']}\n")
        return "Fix recorded."

    if name == "generate_tests":
        print(f"\n[TOOL] generate_tests → {inputs['target_file']}")
        print(inputs["test_code"])
        return "Tests recorded."

    if name == "write_pr_description":
        print(f"\n[TOOL] write_pr_description")
        print(f"  Title: {inputs['title']}")
        print(f"  Body:\n{inputs['body']}\n")
        return "PR description recorded."

    return f"[unknown tool: {name}]"


# ---------------------------------------------------------------------------
# Agentic loop
# ---------------------------------------------------------------------------

ISSUE = """
GitHub Issue #42: Incorrect total when discount is applied

Steps to reproduce:
  result = calculate_total(100.0, discount_pct=10)
  # Expected total: 97.20  (90 subtotal + 7.20 tax)
  # Actual total:   79.20  (discount applied twice)

File: payment.py
"""


def run_agent():
    print("=" * 60)
    print("SDLC Agent — demo mode")
    print("Issue:", ISSUE.strip())
    print("=" * 60)

    messages = [
        {
            "role": "user",
            "content": (
                "You are an SDLC agent. Given the following GitHub issue, "
                "read the relevant file, propose a fix, generate tests, "
                "and write a PR description.\n\n"
                f"Issue:\n{ISSUE}"
            ),
        }
    ]

    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            tools=tools,
            messages=messages,
        )

        # Collect any text the model emits
        for block in response.content:
            if hasattr(block, "text") and block.text:
                print(f"\n[Agent]: {block.text}")

        if response.stop_reason == "end_turn":
            print("\n[Agent done]")
            break

        if response.stop_reason != "tool_use":
            print(f"[Unexpected stop reason: {response.stop_reason}]")
            break

        # Execute tool calls and feed results back
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"\n→ Calling tool: {block.name}")
                result = execute_tool(block.name, block.input)
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})


if __name__ == "__main__":
    run_agent()
