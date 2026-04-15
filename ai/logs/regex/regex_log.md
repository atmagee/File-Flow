# 🤖 AI Usage Log – Filename Validation Regex Task

## 📌 Project Context

Development of a Python-based tool to validate and **organise** filenames in a shared team folder. The validation logic is driven by a regex pattern aligned with rules defined by the project and a dynamic list of file extensions stored in `extensions.txt`.

---

## 🗓️ Date of Interaction

**April 15, 2026**

---

## 👤 Role of AI

The AI (ChatGPT) was used as a **Senior Data Engineering assistant** to:

* Design a regex for filename validation
* Explain the regex in a structured README format
* Compare multiple regex approaches
* Provide engineering-level evaluation and recommendations
* Generate documentation for project governance

---

## 🧩 Tasks Performed by AI

### 1. Regex Design

* Created an initial regex pattern to enforce:

  * Lowercase filenames
  * Word-based naming with optional underscore-separated segments
  * Optional numeric suffix at the end
  * Valid extensions sourced dynamically

**Output:**

```regex
^[a-z]+(_[a-z]+)*[0-9]*\.(txt|pdf|xml)$
```

---

### 2. Documentation (README)

* Produced a GitHub-ready README including:

  * Clear breakdown of regex components
  * Mapping of regex to requirements
  * Valid and invalid filename examples
  * Python implementation snippet

---

### 3. Regex Comparison & Evaluation

* Compared two regex patterns:

  * Original AI-generated regex
  * User-provided alternative regex

* Evaluation criteria included:

  * Correctness against requirements
  * Robustness and edge case handling
  * Readability and maintainability
  * Computational efficiency
  * Backtracking and performance considerations

---

### 4. Engineering Review & Recommendation

* Identified:

  * Weak validation in original regex (over-permissive numeric handling)
  * Logical flaws in alternative regex (incorrect acceptance/rejection cases)

* Proposed improved regex:

```regex
^[a-z]+(_[a-z]+)*([0-9]+)?\.(txt|pdf|xml)$
```

* Justified recommendation based on:

  * Simplicity
  * Performance
  * Alignment with requirements
  * Reduced ambiguity

---

## ⚖️ Human Oversight

* User provided:

  * Initial requirements and constraints
  * Alternative regex for comparison

* AI outputs were reviewed and iterated upon through follow-up questioning

---

## ⚠️ Limitations & Considerations

* Regex assumes:

  * Extensions are lowercase and **sanitised** from `extensions.txt`

* Edge cases may still require:

  * Unit testing beyond regex validation

* Regex does not enforce:

  * File system constraints (e.g. max filename length)
  * Reserved keywords or OS-specific restrictions

---

## 🔐 Compliance & Transparency Notes

* No sensitive or personal data was used in this interaction

* AI-generated outputs were used strictly for:

  * Development support
  * Documentation generation

* All outputs should be reviewed before production deployment

---

## 🚀 Outcome

* A validated and well-documented regex solution
* Clear comparison of alternative approaches
* Production-ready documentation **artefacts**
* Traceable record of AI-assisted development

---

## 📎 Recommendation

For governance and reproducibility:

* Store this log alongside the project repository
* Version control regex changes
* Add automated tests to validate filename compliance

---
