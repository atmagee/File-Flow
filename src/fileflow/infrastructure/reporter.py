import json
from pathlib import Path


def generate_report(files: list, output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    total = len(files)
    valid = sum(1 for f in files if f.is_valid_file)
    invalid = total - valid

    invalid_name = sum(1 for f in files if not f.is_valid_name and f.is_valid_extension)
    invalid_ext = sum(1 for f in files if f.is_valid_name and not f.is_valid_extension)
    invalid_both = sum(1 for f in files if not f.is_valid_name and not f.is_valid_extension)

    # Category breakdown
    category_counts = {}
    for f in files:
        category = f.category or "unknown"
        category_counts[category] = category_counts.get(category, 0) + 1

    report = {
        "total_files": total,
        "valid_files": valid,
        "invalid_files": invalid,
        "invalid_name": invalid_name,
        "invalid_extension": invalid_ext,
        "invalid_both": invalid_both,
        "categories": category_counts
    }

    with open(Path(output_dir) / "report.json", "w") as f:
        json.dump(report, f, indent=4)