# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.40.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
Local simulation of the GitHub Actions AI review workflow.

Diffs the before/ and after/ payment files and sends the diff to Claude
for review — same logic as the CI workflow, runnable without GitHub.

Usage:
    cd demos/04-cicd
    cp .env.example .env   # add ANTHROPIC_API_KEY
    uv run review_locally.py
"""

import os
import subprocess
import anthropic
from dotenv import load_dotenv

load_dotenv()

_HERE = os.path.dirname(__file__)
BEFORE = os.path.join(_HERE, "before/payment.py")
AFTER = os.path.join(_HERE, "after/payment.py")


def get_diff() -> str:
    result = subprocess.run(
        ["diff", "-u", BEFORE, AFTER],
        capture_output=True,
        text=True,
    )
    return result.stdout


def run_review(diff: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=(
            "You are a code reviewer. Review the following Python diff for: "
            "correctness bugs, security issues (injection, secret exposure, unsafe eval), "
            "and obvious inefficiencies. Be concise. Format as a markdown list. "
            "If there are no issues, say so clearly."
        ),
        messages=[{"role": "user", "content": f"```diff\n{diff}\n```"}],
    )
    return response.content[0].text


def main():
    print(f"Diffing:\n  {BEFORE}\n  {AFTER}\n")
    diff = get_diff()
    if not diff.strip():
        print("No differences found.")
        return

    print("Diff:\n" + "-" * 40)
    print(diff)
    print("-" * 40)

    print("\nSending to Claude Haiku for review...\n")
    review = run_review(diff)

    print("## AI Code Review\n")
    print(review)
    print("\n_Reviewed by claude-haiku-4-5 — human review still required._")


if __name__ == "__main__":
    main()
