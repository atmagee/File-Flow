from src.fileflow.pipeline.stages import (
    scan_folder,
    validate_files,
    move_files
)


def run_pipeline():
    input_dir = "data/input"
    extensions_file = "config/extensions.txt"

    processed_dir = "data/processed"
    quarantine_dir = "data/quarantine"

    # 1. Scan
    files = scan_folder(input_dir)

    # 2. Validate
    files = validate_files(files, extensions_file)

    # 3. Move
    files = move_files(files, processed_dir, quarantine_dir)

    # Debug output
    for file in files:
        print(f"{file.full_path.name} → {file.full_path}")

    return files


if __name__ == "__main__":
    run_pipeline()