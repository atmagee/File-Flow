import json
from pathlib import Path


def generate_report(files: list, output_dir: str, run_id: str) -> None:
    total = len(files)
    valid = sum(1 for f in files if f.is_valid_file)
    invalid = total - valid

    processed = sum(1 for f in files if f.is_valid_file)
    duplicates = sum(1 for f in files if f.is_duplicate)
    quarantined = total - processed
    invalid_name = sum(1 for f in files if not f.is_valid_name and f.is_valid_extension)
    invalid_ext = sum(1 for f in files if f.is_valid_name and not f.is_valid_extension)
    invalid_both = sum(1 for f in files if not f.is_valid_name and not f.is_valid_extension)

    # Category breakdown
    category_counts = {}
    for f in files:
        category = f.category
        category_counts[category] = category_counts.get(category, 0) + 1

    report = {
        "run_id": run_id,
        "total_files": total,
        "processed_files": processed,
        "duplicate_files": duplicates,
        "quarantined_files": quarantined,
        "invalid_name": invalid_name,
        "invalid_extension": invalid_ext,
        "invalid_both": invalid_both,
        "categories": category_counts,
        }

    report_file = Path(output_dir) / f"report_{run_id}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent = 4)

    print("\n=== FILEFLOW REPORT ===")
    print(f"\nRun ID: {run_id}")
    print(f"\nTotal files: {total}")
    print(f"Processed files: {processed}")
    print(f"Duplicate files: {duplicates}")
    print(f"Quarantined files: {quarantined}")
    print(f"  - Invalid name: {invalid_name}")
    print(f"  - Invalid extension: {invalid_ext}")
    print(f"  - Invalid both: {invalid_both}")

    print("\nCategories:")
    for category, count in category_counts.items():
        print(f"  - {category}: {count}")

    print(f"\nSaved to: {report_file}")
    print("========================\n")
