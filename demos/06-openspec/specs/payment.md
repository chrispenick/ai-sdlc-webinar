# Payment Processing Specification

## Purpose
Accurate calculation of order totals including optional percentage discounts and sales tax.
This spec defines the correct behavior for `calculate_total` so that humans and AI
coding assistants agree on what the function must do before any code is written.

## Requirements

### Requirement: Single discount application
The system SHALL apply a percentage discount to the subtotal exactly once.

#### Scenario: Discount deducted once
- GIVEN a subtotal of $100.00 and a discount of 10%
- WHEN `calculate_total` is called
- THEN `discount` equals $10.00
- AND `discounted_subtotal` equals $90.00

#### Scenario: Discount field accuracy
- GIVEN a subtotal of $200.00 and a discount of 25%
- WHEN `calculate_total` is called
- THEN `discount` equals $50.00
- AND the discount is NOT subtracted from the total a second time

---

### Requirement: Tax on discounted amount
The system SHALL calculate tax on the discounted subtotal, not the original subtotal.

#### Scenario: Tax base is post-discount
- GIVEN a subtotal of $100.00, a discount of 10%, and a tax rate of 8%
- WHEN `calculate_total` is called
- THEN `tax` equals $7.20 (8% of $90.00, not 8% of $100.00)

---

### Requirement: Total composition
The system SHALL compute `total` as `discounted_subtotal + tax`.

#### Scenario: Correct total with discount and tax
- GIVEN a subtotal of $100.00 and a discount of 10%
- WHEN `calculate_total` is called
- THEN `total` equals $97.20
- AND `total` is greater than `discounted_subtotal`

#### Scenario: No discount
- GIVEN a subtotal of $100.00 and no discount (0%)
- WHEN `calculate_total` is called
- THEN `total` equals $108.00 (subtotal + 8% tax, no deduction)

#### Scenario: No discount, no tax edge case
- GIVEN any subtotal and 0% discount
- WHEN `calculate_total` is called
- THEN `total` equals `subtotal * 1.08` (rounded to 2 decimal places)
