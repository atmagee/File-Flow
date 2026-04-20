# 📁 FileFlow

A configurable, pipeline-based tool for validating, classifying, and organising files within a directory.

---

## 💡 Problem

Teams often share directories where files are inconsistently named, unorganised, and difficult to track. Over time, this
leads to confusion, duplication, and a lack of visibility over what has been processed.

## 🎯 Solution

FileFlow is a command-line tool that validates, organises, logs, and reports on files placed in a shared directory,
ensuring the workspace remains structured and usable.

## 👤 User Story

As a user, I want to drop files into a shared directory and run a simple tool that validates, organises, logs, and
reports on those files so that the shared area stays tidy and usable.

---

## 🚀 Overview

**FileFlow** processes files through a structured pipeline:

- scans an input directory
- validates filenames and extensions
- classifies files by type
- moves files into organised directories
- quarantines invalid files with clear reasons
- archives older processed files
- generates logs and reports for each run

The system is **configuration-driven**, so behaviour can be changed without modifying the core code.

---

## ▶️ Running FileFlow Locally

FileFlow can be run locally from a bash terminal, including the terminal inside PyCharm.

### Default mode

```bash
./scripts/run.sh
```

### Demo mode

```bash
./scripts/run.sh --demo
```

### Custom input directory

```bash
./scripts/run.sh --input /path/to/directory
```

Use a valid path for your system:

- Linux: `/home/user/files`
- Windows (Git Bash): `/c/Users/yourname/files`

⚠️ On Windows, when using Git Bash, you must use Unix-style paths (/c/...) rather than Windows-style paths (C:\...).

---

## 🧪 Demo Mode

Run FileFlow against the demo dataset.

### Create demo data

```bash
./scripts/create_demo_data.sh
```

### Run demo mode

```bash
./scripts/run.sh --demo
```

#### Repeat or reset

Repeat from step 1 to generate new files and observe duplicate handling behaviour, or reset the demo dataset:

```bash
./scripts/reset_demo.sh
```

These helper scripts are intended for bash environments.

---

## 🐳 Docker Execution

### Build the image

```bash
docker build -t fileflow .
```

### Run with a custom input directory

#### Linux

```bash
docker run -it \
  -v /path/to/parent_directory:/app/host \
  fileflow --input /app/host/input_directory
```

#### Windows Git Bash

```bash
MSYS_NO_PATHCONV=1 docker run -it \
  -v /c/Users/yourname/path/to/parent_directory:/app/host \
  fileflow --input /app/host/input_directory
```

⚠️ On Windows (Git Bash), prefix the command with `MSYS_NO_PATHCONV=1` to prevent path conversion issues.

---

## 🧪 Demo Mode (Docker)

Run FileFlow in Docker using the demo dataset.

```bash
./scripts/run_docker_demo.sh
```

This script:

- resets the demo data
- generates sample files
- runs the container
- mounts local directories so output persists

Use this to quickly demonstrate the full pipeline without setting up input manually

---

## ⚠️ Notes for Windows (Git Bash)

Git Bash rewrites Unix-style paths by default, which can break Docker commands.

To prevent this, prefix Docker commands with:

```bash
MSYS_NO_PATHCONV=1
```

Use `/c/...` style paths in Git Bash, for example:

```bash
/c/Users/yourname/Desktop
```

---

## 🧾 Script Overview

| Script                | Purpose                           |
|-----------------------|-----------------------------------|
| `run.sh`              | run FileFlow                      |
| `create_demo_data.sh` | generate sample files for testing |
| `reset_demo.sh`       | clear and reset demo directories  |
| `run_docker_demo.sh`  | run the demo workflow in Docker   |

---

## 🔄 Pipeline Flow

```text
             Input
               ↓
             Scan ----------------
               ↓                 |
            Validate             |
               ↓                 |
            Classify             |   
               ↓              Logging
             Move        (entire pipeline)
            ↙     ↘              |
     Processed   Quarantine      |
         ↓           ↓           |                
      Archive        ↓           |
            ↘      ↙             |
             Report --------------
```

Each stage has a single responsibility and operates independently.

---

## 📌 Key Behaviour

- the input directory is treated as a staging area
- files are moved out, not copied
- valid files are organised into categories
- invalid files are quarantined with reasons
- duplicate filenames are safely renamed (`_1`, `_2`, …)
- older processed files are archived
- logs and reports reflect actual execution results

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
│   ├── reset_demo.sh
│   └── run_docker_demo.sh
│
├── Dockerfile
└── README.md
```

---

## 📂 Output Structure

### Default Mode

```text
data/
├── default_input/
├── processed/
├── quarantine/
└── output/
    ├── logs/
    └── reports/
```

### Demo Mode

```text
demo_data/
├── demo_input/
├── processed/
├── quarantine/
└── output/
    ├── logs/
    └── reports/
```

### Custom Input

When a custom input directory is provided, FileFlow creates a separate output directory alongside the input:

```text
<parent_directory>/
├── <input_directory>/
└── sorted_<input_directory>/
    ├── processed/
    ├── quarantine/
    └── output/
        ├── logs/
        └── reports/
```

Example:

```text
C:\Users\name\Documents\
├── messy_folder/
└── sorted_messy_folder/
    ├── processed/
    ├── quarantine/
    └── output/
        ├── logs/
        └── reports/
```

The input directory is used as a staging area. Files are moved out during processing and organised into the new output
structure.

---

## ⚙️ Configuration

Behaviour is controlled through `config/config.json`.

### Example

```json
{
  "validation": {
    "filename_pattern": "^[a-z]+(_[a-z]+)*(_[0-9]+)?$",
    "extensions": {
      "text": [
        "txt",
        "md"
      ],
      "audio": [
        "mp3",
        "midi"
      ],
      "video": [
        "mp4",
        "webm"
      ],
      "images": [
        "jpg",
        "png"
      ],
      "documents": [
        "pdf",
        "docx"
      ]
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

### Filename

* lowercase only
* words separated by underscores
* optional numeric suffix (`_1`, `_2`, etc.)

### Extension

* must match a configured extension
* treated as case-sensitive

---

## 📊 Example Output

### Processed

```text
processed/text/report_1.txt
```

### Quarantine

```text
quarantine/invalid_filename/bad-name.txt
```

### Archive

```text
processed/text/archive/old_file.txt
```

### Logs

```text
output/logs/fileflow_<run_id>.log
```

### Report

```text
output/reports/report_<run_id>.csv
```

---

## 🧩 Design Principles

- **Configuration-driven** - no hardcoded rules
- **Modular pipeline stages** – easy to extend or modify
- **Deterministic behaviour** – consistent results per run
- **Separation of concerns** – each stage handles one responsibility
- **Safe file handling** – avoids overwriting through duplicate resolution

---

## ⚠️ Limitations

- no content-based duplicate detection
- limited automated test coverage
- helper scripts are bash-oriented

---

## 🛣️ Future Improvements

- add unit tests
- improve CLI usability (`--help`)
- extend reporting
- improve logging readability
- support scheduling
- detect changes in archived files

---

## 📌 Summary

FileFlow is a configurable pipeline that:

- validates and organises files
- separates valid and invalid inputs
- safely moves and structures data
- produces logs and reports for each run
- supports local execution and Docker-based execution on Windows and Linux

---