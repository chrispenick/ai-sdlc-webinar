"""Payment processor — contains a deliberate bug for demo purposes."""

TAX_RATE = 0.08


def calculate_total(subtotal: float, discount_pct: float = 0.0) -> dict:
    """Return a breakdown of subtotal, discount, tax, and total."""
    # BUG: discount is applied before tax is calculated,
    # then the discounted amount is also shown as if it reduces the post-tax total.
    # Tax should be computed on the discounted subtotal, but the final total
    # should be: discounted_subtotal + tax — not subtracting discount again.
    discounted = subtotal * (1 - discount_pct / 100)
    tax = discounted * TAX_RATE
    total = subtotal - (subtotal * discount_pct / 100) - (subtotal * discount_pct / 100) + tax
    return {
        "subtotal": subtotal,
        "discount": subtotal * discount_pct / 100,
        "tax": round(tax, 2),
        "total": round(total, 2),
    }
