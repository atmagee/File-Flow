import json
from datetime import datetime
from pathlib import Path


def generate_report(files: list, output_dir: str):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

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
        "timestamp": timestamp,
        "total_files": total,
        "valid_files": valid,
        "invalid_files": invalid,
        "invalid_name": invalid_name,
        "invalid_extension": invalid_ext,
        "invalid_both": invalid_both,
        "categories": category_counts
    }

    report_file = Path(output_dir) / f"report_{timestamp}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=4)

    print("\n=== FILEFLOW REPORT ===")
    print(f"Timestamp: {timestamp}")
    print(f"Total files: {total}")
    print(f"Valid files: {valid}")
    print(f"Invalid files: {invalid}")
    print(f"  - Invalid name: {invalid_name}")
    print(f"  - Invalid extension: {invalid_ext}")
    print(f"  - Invalid both: {invalid_both}")

    print("\nCategories:")
    for category, count in category_counts.items():
        print(f"  - {category}: {count}")

    print(f"\nSaved to: {report_file}")
    print("========================\n")
