# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.40.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""Demo 06: Spec-driven development with OpenSpec + Claude.

Instead of asking Claude to 'fix a bug', we hand it a formal spec and say:
'Make this code satisfy the spec.' The spec is the source of truth.

Run:
    cp .env.example .env   # add ANTHROPIC_API_KEY
    uv run spec_driven_fix.py
"""

import os
import pathlib
import anthropic
from dotenv import load_dotenv

load_dotenv()

HERE = pathlib.Path(__file__).parent

SEPARATOR = "─" * 60


def read(path: pathlib.Path) -> str:
    return path.read_text()


def section(title: str) -> None:
    print(f"\n{SEPARATOR}")
    print(f"  {title}")
    print(SEPARATOR)


def main() -> None:
    spec = read(HERE / "specs" / "payment.md")
    code = read(HERE / "payment.py")

    section("SPEC  (specs/payment.md)")
    print(spec)

    section("CURRENT CODE  (payment.py — contains a bug)")
    print(code)

    section("ASKING CLAUDE TO IMPLEMENT AGAINST THE SPEC...")
    print()

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    system = (
        "You are a senior Python engineer. "
        "You receive an OpenSpec specification and a current implementation. "
        "Your job is to rewrite the implementation so every scenario in the spec passes. "
        "Do not guess — derive the correct logic directly from the spec's WHEN/THEN clauses. "
        "Reply with ONLY the corrected Python source file, no explanation."
    )

    prompt = f"""## Spec

{spec}

## Current implementation (may violate the spec)

```python
{code}
```

Rewrite `payment.py` so it satisfies every scenario in the spec.
Return only the Python source, no markdown fences."""

    message = client.messages.create(
        model="claude-opus-5",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )

    fixed_code = message.content[0].text.strip()

    section("CLAUDE'S IMPLEMENTATION (spec-derived)")
    print(fixed_code)

    section("VERIFYING AGAINST SPEC SCENARIOS")
    print()
    _verify(fixed_code)


def _verify(source: str) -> None:
    namespace: dict = {}
    exec(source, namespace)  # noqa: S102
    calc = namespace["calculate_total"]

    scenarios = [
        ("Discount deducted once",
         lambda: _check(calc(100.00, 10), discount=10.00, total=97.20)),
        ("Discount field accuracy — not double-subtracted",
         lambda: _check(calc(200.00, 25), discount=50.00, total=162.00)),
        ("Tax base is post-discount",
         lambda: _check(calc(100.00, 10), tax=7.20)),
        ("Correct total with discount and tax",
         lambda: _check(calc(100.00, 10), total=97.20)),
        ("No discount",
         lambda: _check(calc(100.00, 0), total=108.00)),
    ]

    passed = 0
    for name, check in scenarios:
        try:
            check()
            print(f"  PASS  {name}")
            passed += 1
        except AssertionError as exc:
            print(f"  FAIL  {name} — {exc}")

    print(f"\n  {passed}/{len(scenarios)} scenarios passed")
    if passed == len(scenarios):
        print("\n  Spec satisfied. Code is ready for review.")
    else:
        print("\n  Spec not fully satisfied — review Claude's output above.")


def _check(result: dict, **expected) -> None:
    for key, val in expected.items():
        actual = result.get(key)
        assert round(actual, 2) == round(val, 2), (
            f"{key}: expected {val}, got {actual}  |  full result: {result}"
        )


if __name__ == "__main__":
    main()
