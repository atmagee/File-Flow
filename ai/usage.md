
---

# 🤖 AI Usage Log

## 📌 Overview

AI was used throughout the development of FileFlow to support planning, design validation, debugging, and implementation refinement of a configurable file-processing pipeline.

AI outputs were treated as proposals, not final solutions. All outputs were reviewed, tested, and selectively implemented based on correctness, maintainability, and alignment with project requirements.

---

## 🧠 Prompting Strategy

AI was guided using structured prompts to enforce  reasoning and output quality.

### Example Prompt

```text
Persona:
You are a senior software engineer 

Context:
You are building File-Flow, a lightweight command-line file processing tool for a shared team folder. 
The user story for the project is: “As a user, I want to drop files into a shared folder and run a simple tool that 
validates, organises, logs, and reports on those files so that the shared area stays tidy and usable.” 

Objective:
The required features are:
* Scan a chosen input folder
* Detect files available for processing
* Validate filenames against a naming convention
* Classify files by type or naming rule
* Move valid files to the correct output folder
* Move invalid files to a quarantine folder
* Generate a text or CSV summary report
* Record actions to a log file
* Support repeated runs without crashing
* Save configuration in a file such as JSON

Tasks:
1) Validate that all the programs work together by following the logic from each program into the next.
2) Propose 2–3 solutions with trade-offs, failure modes, and operational impact.
3) Recommend one option with reasoning.
4) Identify simplification opportunities with trade-offs.
5) Provide rollout + rollback plan and open questions.
```

This ensured:

* responses included trade-offs and failure modes
* outputs were structured (tables, checklists)
* AI functioned as a design reviewer rather than a generator

---

## 🧩 Areas of AI Usage

### 1. Planning & Backlog Structuring

AI was used to:

* translate requirements into structured backlog items
* define milestones and development phases
* recommend execution order to reduce risk

Outputs were used as a planning reference, but were not followed rigidly.

---

### 2. Validation Logic & Regex Design

AI assisted in:

* designing filename validation rules
* generating and comparing regex patterns
* identifying edge cases and incorrect matches

Final regex was selected based on:

* correctness against requirements
* simplicity and maintainability
* comparisons to others created by both the AI and user

---

### 3. Pipeline Architecture Review

AI was used to:

* review interactions between pipeline stages (`scan → validate → classify → move`)
* identify duplicated or inconsistent logic
* suggest improvements to separation of concerns

Changes were applied selectively to avoid unnecessary abstraction.

---

### 4. Feature Design (Reporting & Archiving)

AI supported:

* evaluation of report formats
* design of report structure and metrics
* archive feature design

Final implementation decisions prioritised:

* simplicity
* usability
* alignment with project scope

---

### 5. Debugging & Issue Resolution

AI was used to assist in diagnosing issues, but required manual validation and reasoning.

#### Duplicate Filename Handling

* Issue:

  * incorrect renaming (`file_1.txt → file_1_1.txt`)
* Resolution:

  * implemented suffix-aware parsing and increment logic

---

#### Reporting Metric Mismatch

* Issue:

  * mismatch between valid and processed file counts
* Root cause:

  * validation state used as proxy for execution outcome
* Resolution:

  * introduced execution flags:

    * `was_processed`
    * `was_quarantined`
    * `was_archived`

---

#### Path & Environment Issues

* Issue:

  * incorrect paths and Docker volume inconsistencies
* Resolution:

  * aligned file operations with runtime environment
  * corrected volume mappings and execution flow

---

### 6. Logging & Observability

AI contributed to:

* structured logging format
* inclusion of full file paths
* separation of actions:

  * `RENAMED`
  * `PROCESSED`
  * `QUARANTINED`
  * `ARCHIVED`

Final implementation ensured logs reflect actual execution events.

---

### 7. Code Refinement

AI suggested improvements to:

* remove redundant logic
* simplify classification
* standardise validation outputs

Not all suggestions were implemented; decisions were based on:

* readability
* maintainability
* scope

---

## ⚖️ Validation & Control of AI Outputs

AI outputs were:

* validated through testing
* challenged via follow-up prompts
* compared against alternative approaches
* modified or rejected where necessary

Examples of control:

* replacing validation-based metrics with execution-based tracking
* simplifying reporting structure instead of implementing more complex AI suggestions
* refining duplicate handling logic beyond initial AI output

---

## ⚠️ Limitations

* AI outputs occasionally:

  * lacked awareness of runtime context
  * required adjustment for edge cases
* Some issues (e.g. duplicate handling, reporting mismatches) required:

  * manual debugging
  * iterative refinement beyond initial suggestions

---

## 📌 Summary

AI was used to support:

* planning and backlog creation
* validation logic design
* pipeline architecture review
* feature design (reporting, archiving)
* debugging and issue diagnosis
* logging and observability improvements

All outputs were reviewed, validated, and adapted, with final implementation decisions based on independent judgement.

---