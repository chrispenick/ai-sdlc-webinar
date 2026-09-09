#!/usr/bin/env bash
# Run before every practice run and the live demo.
# Removes anything Claude Code generated and restores payment.py to its buggy state.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

rm -f  "$DIR/test_payment.py"
rm -rf "$DIR/__pycache__" "$DIR/.pytest_cache"
cp     "$DIR/.original/payment.py" "$DIR/payment.py"

echo "✓ Demo 01 reset — payment.py restored, generated files removed."
