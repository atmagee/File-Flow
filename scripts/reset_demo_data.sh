#!/bin/bash

INPUT_DIR="data/input"
PROCESSED_DIR="data/processed"
QUARANTINE_DIR="data/quarantine"
OUTPUT_DIR="output"

echo "Resetting demo data..."

# -----------------------------
# 1. Clear input directory
# -----------------------------
echo "Clearing input directory..."

if [ -d "$INPUT_DIR" ]; then
  rm -rf "$INPUT_DIR"/*
fi

# -----------------------------
# 2. Remove generated directories
# -----------------------------
echo "Removing generated directories..."

rm -rf "$PROCESSED_DIR"
rm -rf "$QUARANTINE_DIR"
rm -rf "$OUTPUT_DIR"

echo "Reset complete."