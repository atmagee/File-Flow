import csv
from pathlib import Path


def generate_report(files: list, report_dir: str, run_id: str) -> None:
    scanned = len(files)

    # Core metrics
    valid = sum(1 for f in files if f.is_valid_file)
    invalid = sum(1 for f in files if not f.is_valid_file)

    processed = sum(1 for f in files if f.was_processed)
    quarantined = sum(1 for f in files if f.was_quarantined)

    duplicates = sum(1 for f in files if f.is_duplicate)
    archived = sum(1 for f in files if f.was_archived)

    invalid_name = sum(1 for f in files if not f.is_valid_name and f.is_valid_extension)
    invalid_ext = sum(1 for f in files if f.is_valid_name and not f.is_valid_extension)
    invalid_both = sum(1 for f in files if not f.is_valid_name and not f.is_valid_extension)

    # Category breakdown
    category_counts = {}
    for f in files:
        category = f.category
        category_counts[category] = category_counts.get(category, 0) + 1

    Path(report_dir).mkdir(parents = True, exist_ok = True)
    report_file = Path(report_dir) / f"report_{run_id}.csv"

    with open(report_file, "w", newline = "") as f:
        writer = csv.writer(f)

        # Run ID
        writer.writerow(["run_id", run_id])
        writer.writerow([])

        # Metrics
        writer.writerow(["metric", "value"])
        writer.writerow(["scanned_files", scanned])

        writer.writerow(["valid_files", valid])
        writer.writerow(["processed_files", processed])

        writer.writerow(["invalid_files", invalid])
        writer.writerow(["quarantined_files", quarantined])

        writer.writerow(["duplicate_files", duplicates])
        writer.writerow(["archived_files", archived])

        writer.writerow(["invalid_name", invalid_name])
        writer.writerow(["invalid_extension", invalid_ext])
        writer.writerow(["invalid_both", invalid_both])

        writer.writerow([])

        # Categories
        writer.writerow(["category", "count"])
        for category, count in category_counts.items():
            writer.writerow([category, count])

    # Console output
    print("\n=== FILEFLOW REPORT ===")
    print(f"\nRun ID: {run_id}")
    print(f"\nScanned files: {scanned}")

    print(f"\nValid files: {valid}")
    print(f"Processed files: {processed}")

    print(f"\nInvalid files: {invalid}")
    print(f"Quarantined files: {quarantined}")

    print(f"\nDuplicate files: {duplicates}")
    print(f"Archived files: {archived}")

    print(f"\nInvalid breakdown:")
    print(f"  - Invalid name: {invalid_name}")
    print(f"  - Invalid extension: {invalid_ext}")
    print(f"  - Invalid both: {invalid_both}")

    print("\nCategories:")
    for category, count in category_counts.items():
        print(f"  - {category}: {count}")

    print(f"\nSaved to: {report_file}")
    print("========================\n")
