#!/bin/bash

DEMO_ROOT="demo_data"

echo "Resetting demo environment..."

if [ -d "$DEMO_ROOT" ]; then
  rm -rf "$DEMO_ROOT"
fi

# Recreate empty demo root + input
mkdir -p "$DEMO_ROOT/demo_input"

echo "Demo environment reset."