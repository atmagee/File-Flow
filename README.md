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

## 🔄 Pipeline Flow

The pipeline follows a staged processing model:

```text
Input Folder
     ↓
  [Scan]
     ↓
[Validate] → Invalid → Quarantine
     ↓
[Classify]
     ↓
  [Move] → Processed
     ↓
 [Archive]
     ↓
[Report + Logs]
```

Each stage is modular, testable, and responsible for a single concern.

---

## 📂 Project Structure

```text
File-Flow/
├── config/
│   └── config.json
│
├── data/
│   └── default_input/
│
├── demo_data/
│   └── demo_input/
│
├── src/
│   └── fileflow/
│       ├── config/
│       │   └── settings.py
│       │
│       ├── infrastructure/
│       │   ├── archiver.py
│       │   ├── logger.py
│       │   └── reporter.py
│       │
│       ├── pipeline/
│       │   ├── pipeline.py
│       │   └── stages/
│       │       ├── scan.py
│       │       ├── validate.py
│       │       ├── classify.py
│       │       └── move.py
│       │
│       └── main.py
│
├── scripts/
│   ├── run.sh
│   ├── create_demo_data.sh
│   ├── reset_demo_data.sh
│   └── run_docker_demo.sh
│
├── Dockerfile
└── README.md
```

---

## 📁 Dynamic Folder Structure

All output folders are created **relative to the chosen input directory at runtime**.

Example (demo mode):

```text
demo_data/
├── demo_input/
├── processed/
├── quarantine/
└── output/
    ├── logs/
    └── reports/
```

Example (default mode):

```text
data/
├── default_input/
├── processed/
├── quarantine/
└── output/
```

This allows the tool to work with **any input location**.

---

## ⚙️ Configuration

Core behaviour is controlled via `config/config.json`.

### Example:

```json
{
  "validation": {
    "filename_pattern": "^[a-z]+(_[a-z]+)*(_[0-9]+)?$",
    "extensions": {
      "text": ["txt", "md"],
      "images": ["jpg", "png"],
      "documents": ["pdf"]
    }
  },
  "archive": {
    "enabled": true,
    "days_threshold": 30,
    "subfolder_name": "archive"
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

* Reads files from input folder
* Builds `FileMeta` objects

---

### 2. Validate

* Regex-based filename validation
* Extension validation from config
* Produces:

  * `is_valid_name`
  * `is_valid_extension`
  * `is_valid_file`

---

### 3. Classify

* Maps extensions → categories
* Invalid files marked explicitly

---

### 4. Move

* Valid → `processed/<category>/`
* Invalid → `quarantine/<reason>/`
* Duplicate-safe renaming

---

### 5. Archive

* Moves old processed files into:

```text
processed/<category>/archive/
```

* Based on configurable age threshold
* Tracks archived files per run

---

### 6. Logging

* Cross-cutting concern across all stages
* Structured log output (console + file)
* Full file paths included
* Per-run `run_id`

---

### 7. Reporting

* CSV report generated per run
* Includes:

  * processed
  * quarantined
  * duplicates
  * archived files
  * category breakdown

---

## 🖥️ CLI Usage

Run with:

```bash
./scripts/run.sh
```

### Options:

```bash
--demo        Use demo dataset
--input PATH  Use custom input folder
```

If no option is provided, the user is prompted to choose:

* default input
* demo input
* custom path

---

## 🐳 Docker Support

### Build image

```bash
docker build -t fileflow .
```

---

### Run container

```bash
docker run -it \
  -v "$(pwd -W)/demo_data:/app/demo_data" \
  -v "$(pwd -W)/data:/app/data" \
  fileflow --demo
```

---

### Demo script (recommended)

```bash
./scripts/run_docker_demo.sh
```

This will:

1. Reset demo data
2. Generate dataset
3. Run container
4. Persist outputs via mounted volumes

---

## 📊 Example Output

### Processed

```text
demo_data/processed/text/report_1.txt
```

### Quarantine

```text
demo_data/quarantine/invalid_filename/bad-name.txt
```

### Archive

```text
demo_data/processed/text/archive/old_file.txt
```

### Report

```text
demo_data/output/reports/report_<run_id>.csv
```

---

## 🧩 Design Principles

* **Config-driven validation** – flexible rules without changing code
* **Dynamic path resolution** – adapts to any input location at runtime
* **Modular pipeline stages** – independently testable and extendable components
* **Safe file operations** – avoids data loss through controlled movement and duplicate handling
* **Reproducible Docker execution** – identical behaviour across environments
* **Separation of concerns** – each stage handles a single responsibility

---

## ⚠️ Limitations

* No content-based duplicate detection
* No automated tests

---

## 🛣️ Future Improvements

* Add unit tests
* Improve commenting and hints
* Add --help functionality
* Improve CLI UX
* Add scheduling support
* Extend reporting (charts / summaries)

---

## 📌 Summary

FileFlow is a **containerised, configurable file processing pipeline** that:

* validates and organises files
* handles invalid inputs safely
* archives historical data
* logs and reports every run
* runs consistently via Docker

It demonstrates core engineering concepts:

* pipeline architecture
* configuration-driven design
* containerisation
* reproducibility
* observability

---
