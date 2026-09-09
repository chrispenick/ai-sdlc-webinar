#!/usr/bin/env bash
# Run before the demo to clear pytest artifacts from prior runs.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

rm -rf "$DIR/before/__pycache__" "$DIR/before/.pytest_cache"
rm -rf "$DIR/after/__pycache__"  "$DIR/after/.pytest_cache"
rm -rf "$DIR/.pytest_cache"

echo "✓ Demo 03 reset — pytest artifacts cleared."
