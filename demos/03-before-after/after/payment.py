"""Payment processor — fixed version."""

TAX_RATE = 0.08


def calculate_total(subtotal: float, discount_pct: float = 0.0) -> dict:
    """Return a breakdown of subtotal, discount, tax, and total."""
    discount = subtotal * discount_pct / 100
    discounted_subtotal = subtotal - discount
    tax = round(discounted_subtotal * TAX_RATE, 2)
    total = round(discounted_subtotal + tax, 2)
    return {
        "subtotal": subtotal,
        "discount": round(discount, 2),
        "tax": tax,
        "total": total,
    }
