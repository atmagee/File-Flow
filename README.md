# 📁 FileFlow

A configurable Python pipeline for validating, classifying, and organising files based on naming conventions and file types.

---

## 🚀 Overview

**FileFlow** is a lightweight data engineering-style pipeline designed to:

* Scan an input directory for files
* Validate filenames against a defined pattern
* Validate file extensions against an allowed set
* Classify files by type
* Move valid files into structured folders
* Quarantine invalid files with clear categorisation
* Generate logs and structured reports per run

The system is fully driven by configuration, making it easy to adapt to different file management rules without modifying core logic.

---

## 🧱 Architecture

The pipeline follows a staged processing model:

```text
Scan → Validate → Classify → Move → Log → Report
```

Each stage is modular, testable, and responsible for a single concern.

---

## 📂 Project Structure

```text
File-Flow/
├── config/
│   └── config.json
├── data/
│   ├── input/
│   ├── processed/
│   ├── quarantine/
│   └── archive/
├── output/
│   ├── logs/
│   └── reports/
├── src/
│   └── fileflow/
│       ├── config/
│       ├── infrastructure/
│       ├── pipeline/
│       │   ├── stages/
│       │   │   ├── scan.py
│       │   │   ├── validate.py
│       │   │   ├── classify.py
│       │   │   └── move.py
│       │   └── pipeline.py
│       └── main.py
├── scripts/
│   └── run.sh
```

---

## ⚙️ Configuration

All behaviour is controlled via `config/config.json`.

### Example:

```json
{
  "paths": {
    "input": "data/input",
    "processed": "data/processed",
    "quarantine": "data/quarantine",
    "archive": "data/archive",
    "logs": "output/logs",
    "reports": "output/reports"
  },
  "structure": {
    "quarantine_subfolders": [
      "invalid_filename",
      "invalid_extension",
      "invalid_both"
    ],
    "use_category_subfolders": true
  },
  "validation": {
    "filename_pattern": "^[a-z]+(_[a-z]+)*(_[0-9]+)?$",
    "extensions": {
      "text": ["txt", "md"],
      "audio": ["mp3", "midi"],
      "video": ["mp4", "webm"],
      "images": ["jpg", "png"],
      "documents": ["pdf", "docx"]
    }
  }
}
```

---

## 🔍 Validation Rules

### Filename Rules

* Lowercase only
* Words separated by underscores
* Optional numeric suffix (`_1`, `_2`, etc.)

### Extension Rules

* Must match one of the configured extensions
* Case-sensitive (e.g. `.TXT` is treated as invalid)

---

## 🧠 Core Components

### 1. Scan

* Reads files from the input directory
* Extracts metadata into a structured `FileMeta` object

---

### 2. Validate

* Applies regex-based filename validation
* Checks extension against allowed list
* Produces:

  * `is_valid_name`
  * `is_valid_extension`
  * `is_valid_file`

---

### 3. Classify

* Maps valid extensions to categories
* Invalid extensions are explicitly marked

---

### 4. Move

* Valid files → `processed/<category>/`
* Invalid files → `quarantine/<reason>/`
* Handles duplicate filenames safely using incremental suffixes

---

### 5. Logging

* Per-run log file using a unique `run_id`
* Console + file logging
* Per-file audit entries

---

### 6. Reporting

* JSON report generated per run
* Includes:

  * total files
  * valid / invalid counts
  * breakdown of failure types
  * category distribution

---

## ▶️ Running the Pipeline

From project root:

```bash
./scripts/run.sh
```

This will:

1. Load configuration
2. Ensure required directories exist
3. Execute the pipeline
4. Output logs and reports

---

## 📊 Example Output

### Processed Files

```text
data/processed/text/example_file.txt
```

### Quarantined Files

```text
data/quarantine/invalid_filename/BadFile.txt
data/quarantine/invalid_extension/file.exe
```

### Report

```text
output/reports/report_2026-04-16_19-04-15.json
```

---

## 🧩 Design Principles

* **Config-driven** – no hardcoded paths or rules
* **Modular pipeline stages** – easy to extend or replace
* **Deterministic behaviour** – consistent outputs per run
* **Separation of concerns** – scanning, validation, and movement are isolated
* **Safe file handling** – avoids overwriting via duplicate resolution

---

## ⚠️ Current Limitations

* No archiving of older files yet
* No CLI interface (arguments/menu)
* Limited test coverage
* Duplicate handling is filename-based (not content-based)

---

## 🛣️ Next Steps

* Implement archive lifecycle logic
* Improve CLI usability
* Add Docker support
* Introduce automated tests
* Enhance reporting (CSV / summaries)

---

## 📌 Summary

This project demonstrates a clean, extensible approach to building a file processing pipeline using core data engineering principles:

* staged processing
* configuration-driven behaviour
* reproducible outputs
* clear logging and observability

It is designed to scale from a simple local utility into a more production-ready system with minimal structural changes.

---
