#!/bin/bash

# Go to project root
cd "$(dirname "$0")/.."

echo "Resetting demo data..."

INPUT_DIR="data/input"
PROCESSED_DIR="data/processed"
QUARANTINE_DIR="data/quarantine"
OUTPUT_DIR="output"


# Ensure input exists
mkdir -p "$INPUT_DIR"

# 1. Move files BACK to input
echo "Restoring files to input..."

if [ -d "$PROCESSED_DIR" ]; then
  find "$PROCESSED_DIR" -type f -exec mv -t "$INPUT_DIR" {} +
fi

if [ -d "$QUARANTINE_DIR" ]; then
  find "$QUARANTINE_DIR" -type f -exec mv -t "$INPUT_DIR" {} +
fi

echo "Files restored to input"

# 2. Remove runtime directories completely
echo "Removing generated directories..."

rm -rf "$PROCESSED_DIR"
rm -rf "$QUARANTINE_DIR"
rm -rf "$OUTPUT_DIR"

echo "Removed processed, quarantine, and output directories"

# 3. Recreate clean base structure (optional but recommended)
mkdir -p "$INPUT_DIR"

echo "Reset complete"