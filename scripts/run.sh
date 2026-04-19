#!/bin/bash
# ========================================
# Run FileFlow
# ========================================

# Go to project root
cd "$(dirname "$0")/.."

# Set Python path
export PYTHONPATH=src

# Run app
python -m fileflow.main "$@"