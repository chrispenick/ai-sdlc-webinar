#!/usr/bin/env bash
# Run before the demo to clear any cached bytecode.
# The agent writes no files — output is stdout only.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

rm -rf "$DIR/__pycache__"

echo "✓ Demo 02 reset — bytecode cache cleared."
