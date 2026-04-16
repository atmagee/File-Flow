from fileflow.pipeline.stages import (scan_folder, validate_files, classify_files, move_files)


def run_pipeline(input_dir, extensions_config, processed_dir, quarantine_dir, filename_pattern):
    # 1. Scan
    files = scan_folder(input_dir)

    # 2. Validate
    files = validate_files(files, extensions_config, filename_pattern)

    # 3. Classify
    files = classify_files(files, extensions_config)

    # 4. Move
    files = move_files(files, processed_dir, quarantine_dir)

    return files
