"""Payment processor — contains a deliberate bug for demo purposes."""

TAX_RATE = 0.08


def calculate_total(subtotal: float, discount_pct: float = 0.0) -> dict:
    """Return a breakdown of subtotal, discount, tax, and total."""
    discounted = subtotal * (1 - discount_pct / 100)
    tax = discounted * TAX_RATE
    total = discounted + tax
    return {
        "subtotal": subtotal,
        "discount": subtotal * discount_pct / 100,
        "tax": round(tax, 2),
        "total": round(total, 2),
    }
