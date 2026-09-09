#!/usr/bin/env bash
# Run before the demo to restore clean state.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Restore the original buggy payment.py from the canonical before/ copy
cp "$(dirname "$DIR")/03-before-after/before/payment.py" "$DIR/payment.py"

rm -rf "$DIR/__pycache__"

echo "✓ Demo 06 reset — buggy payment.py restored, cache cleared."
