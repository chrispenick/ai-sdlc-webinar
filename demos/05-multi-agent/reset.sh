#!/usr/bin/env bash
# Run before the demo to clear any cached bytecode.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

rm -rf "$DIR/__pycache__"

echo "✓ Demo 05 reset — bytecode cache cleared."
