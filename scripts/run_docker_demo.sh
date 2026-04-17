#!/bin/bash

set -e  # stop script on any error

echo "========================================"
echo " Resetting demo data"
echo "========================================"

./scripts/reset_demo_data.sh

echo "========================================"
echo " Creating demo dataset"
echo "========================================"

./scripts/create_demo_data.sh

echo "========================================"
echo " Running FileFlow in Docker (DEMO MODE)"
echo "========================================"

docker run -it \
  -v "$(pwd -W)/demo_data:/app/demo_data" \
  -v "$(pwd -W)/data:/app/data" \
  fileflow --demo

echo "========================================"
echo " Demo complete"
echo "========================================"