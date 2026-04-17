#!/bin/bash

DEMO_DIR="demo_data/demo_input"

mkdir -p "$DEMO_DIR"
rm -f "$DEMO_DIR"/*

echo "Generating large test dataset in $DEMO_DIR..."

# ---------- CONFIG ----------
VALID_NAMES=("report" "run_john" "daily_log" "summary_file" "notes")
INVALID_NAMES=("InvalidName" "john123" "bad-name" "FILE" "test__file")
VALID_EXTENSIONS=("txt" "md" "pdf" "jpg")
INVALID_EXTENSIONS=("py" "exe" "xml" "MP3")

# ---------- FUNCTION: set timestamp ----------
set_age() {
  local file=$1
  local days=$2
  touch -d "$days days ago" "$file"
}

# ---------- CREATE VALID FILES ----------
for i in {1..20}; do
  name=${VALID_NAMES[$RANDOM % ${#VALID_NAMES[@]}]}
  ext=${VALID_EXTENSIONS[$RANDOM % ${#VALID_EXTENSIONS[@]}]}
  file="$DEMO_DIR/${name}_${i}.${ext}"

  touch "$file"
  set_age "$file" $((RANDOM % 60))
done

# ---------- INVALID NAME ----------
for i in {1..10}; do
  name=${INVALID_NAMES[$RANDOM % ${#INVALID_NAMES[@]}]}
  ext=${VALID_EXTENSIONS[$RANDOM % ${#VALID_EXTENSIONS[@]}]}
  file="$DEMO_DIR/${name}_${i}.${ext}"

  touch "$file"
  set_age "$file" $((RANDOM % 60))
done

# ---------- INVALID EXT ----------
for i in {1..10}; do
  name=${VALID_NAMES[$RANDOM % ${#VALID_NAMES[@]}]}
  ext=${INVALID_EXTENSIONS[$RANDOM % ${#INVALID_EXTENSIONS[@]}]}
  file="$DEMO_DIR/${name}_${i}.${ext}"

  touch "$file"
  set_age "$file" $((RANDOM % 60))
done

# ---------- INVALID BOTH ----------
for i in {1..10}; do
  name=${INVALID_NAMES[$RANDOM % ${#INVALID_NAMES[@]}]}
  ext=${INVALID_EXTENSIONS[$RANDOM % ${#INVALID_EXTENSIONS[@]}]}
  file="$DEMO_DIR/${name}_${i}.${ext}"

  touch "$file"
  set_age "$file" $((RANDOM % 60))
done

# ---------- DUPLICATES ----------
for i in {1..5}; do
  cp /dev/null "$DEMO_DIR/report_$i.txt"
done

# ---------- EDGE CASES ----------
touch "$DEMO_DIR/edge_30_days.txt"
set_age "$DEMO_DIR/edge_30_days.txt" 30

touch "$DEMO_DIR/very_old_file.txt"
set_age "$DEMO_DIR/very_old_file.txt" 120

touch "$DEMO_DIR/new_file.txt"
set_age "$DEMO_DIR/new_file.txt" 0

echo "Dataset created successfully."
echo "Total files: $(ls "$DEMO_DIR" | wc -l)"