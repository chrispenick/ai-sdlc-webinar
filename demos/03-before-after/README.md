# Demo 3: Before / After — AI-Assisted Bug Fix

**Duration:** ~4 minutes (walk through files; no live execution needed)  
**Goal:** Show concretely what AI-generated code review and testing look like vs. what developers typically produce under time pressure.

## The scenario

A payment processor has a double-discount bug. A developer wrote minimal tests that pass despite the bug. AI rewrites the tests with full intent coverage — and they catch it.

## File map

| File | What to show |
|------|-------------|
| `before/payment.py` | The buggy implementation — `total` subtracts discount twice |
| `before/test_payment.py` | Developer's original tests — only assert "total is less than subtotal"; bug passes |
| `after/payment.py` | AI-corrected implementation |
| `after/test_payment.py` | AI-generated tests — cover the exact failure mode, zero subtotal, full discount |

## Step 1 — Run the before tests (they pass despite the bug)

```bash
cd demos/03-before-after
uv run --with pytest pytest before/ -v
```

Expected: `2 passed` — the bug is invisible to these tests.

## Step 2 — Run the after tests (5 cases, covering the actual invariant)

```bash
uv run --with pytest pytest after/ -v
```

Expected: `5 passed`.

Show both outputs and walk through `test_discount_not_double_applied` — that's the test that names the exact bug.

## Talking points

- The developer's tests weren't bad — they were written quickly under normal pressure
- AI generates tests from *intent* (the docstring + types), not from "what's easy to assert"
- The key contrast: `assert result["total"] < result["subtotal"]` vs. `assert result["total"] == 97.2` — a human reaches for the nearest reasonable check; AI reaches for the precise invariant
- **This is where AI adds structural value**: not writing faster, but covering more cases
