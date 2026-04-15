# File-Flow
Containerised Python file organiser and reporting tool

## 🔍 Regex Explanation

The following regex is used to validate filenames:

```regex
^[a-z]+(_[a-z]+)*([0-9]+)?\.(txt|pdf|xml)$
```

This pattern enforces all project naming rules. Below is a breakdown of each component and how it maps to the requirements.

---

### `^`

* Anchors the pattern to the **start of the filename**
* Ensures no invalid characters appear before the name begins

---

### `[a-z]+`

* Matches the **first word** of the filename
* Requirements enforced:

  * Must contain **only lowercase letters**
  * Must be at least one character long

✅ Examples:

* `file`
* `report`

❌ Invalid:

* `File` (uppercase not allowed)
* `123file` (must start with letters)

---

### `(_[a-z]+)*`

* Matches **zero or more additional word segments**, each preceded by an underscore `_`
* Requirements enforced:

  * Words must be separated by underscores
  * Each segment must contain only lowercase letters

✅ Examples:

* `_backup`
* `_final`
* `_version`

Allows:

* `file_backup`
* `report_final_version`

---

### `([0-9]+)?`

* Matches an **optional numeric suffix**
* Requirements enforced:

  * Numbers can only appear **at the end**
  * Numbers must follow a word (not an underscore)

✅ Examples:

* `file1`
* `report_final2`

❌ Invalid:

* `file_2` (number cannot directly follow underscore)
* `file2_backup` (numbers cannot appear in the middle)

---

### `\.`

* Matches a literal dot (`.`)
* Separates the filename from the extension

---

### `(txt|pdf|xml)`

* Matches **allowed file extensions**
* This should be dynamically generated from `extensions.txt` in production

---

### `$`

* Anchors the pattern to the **end of the filename**
* Ensures no extra characters appear after the extension

---

## ✅ Summary

This regex guarantees that:

* Filenames are strictly lowercase
* Names are composed of valid words separated by underscores
* Numeric suffixes are used correctly and only at the end
* Only approved file extensions are allowed

---

## 🧪 Example Matches

| Filename           | Valid | Reason                              |
| ------------------ | ----- |-------------------------------------|
| `file.txt`         | ✅     | Simple valid format                 |
| `report_final.pdf` | ✅     | Underscore-separated words          |
| `data_backup2.xml` | ✅     | Valid numeric suffix                |
| `file_2.txt`       | ❌     | Number follows underscore           |
| `File.txt`         | ❌     | File name includes uppercase letter |
| `file.txt.bak`     | ❌     | Extra extension                     |

---
