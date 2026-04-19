#!/bin/bash
# ========================================
# Run the demo in Docker
# ========================================

set -e  # stop script on any error

echo "========================================"
echo " Resetting demo"
echo "========================================"

./scripts/reset_demo.sh

echo "========================================"
echo " Creating demo dataset"
echo "========================================"

./scripts/create_demo_data.sh

echo "========================================"
echo " Running FileFlow in Docker (DEMO MODE)"
echo "========================================"

docker run -it \
  -v "$(pwd -W)/demo_data:/app/demo_data" \
  fileflow --demo

echo "========================================"
echo " Demo complete"
echo "========================================"