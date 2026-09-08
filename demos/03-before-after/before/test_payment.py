"""Tests written by a developer before AI tooling — incomplete coverage."""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from payment import calculate_total


def test_basic():
    result = calculate_total(100.00)
    # Developer only checked that something came back, not the actual values
    assert result is not None
    assert "total" in result


def test_with_discount():
    result = calculate_total(100.00, discount_pct=10)
    # Checked the wrong thing — only verified total is less than subtotal,
    # not that the math is correct. The bug passes this test.
    assert result["total"] < result["subtotal"]
