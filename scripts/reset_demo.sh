#!/bin/bash
# ========================================
# Reset demo environment
# ========================================

DEMO_ROOT="demo_data"

echo "Resetting demo environment..."

# Remove demo folder if it exists
if [ -d "$DEMO_ROOT" ]; then
  rm -rf "$DEMO_ROOT"
fi

# Recreate demo input folder
mkdir -p "$DEMO_ROOT/demo_input"

echo "Demo environment reset."