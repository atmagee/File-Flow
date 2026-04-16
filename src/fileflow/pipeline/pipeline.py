from fileflow.pipeline.stages import (scan_folder, validate_files, move_files)


def run_pipeline(input_dir, extensions_file, processed_dir, quarantine_dir, filename_pattern):

    # 1. Scan
    files = scan_folder(input_dir)

    # 2. Validate
    files = validate_files(files, extensions_file, filename_pattern)

    # 3. Move
    files = move_files(files, processed_dir, quarantine_dir)

    return files