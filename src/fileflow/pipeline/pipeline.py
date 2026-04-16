from fileflow.pipeline.stages import (scan_folder, validate_files, classify_files, move_files)
from fileflow.infrastructure import setup_logger, generate_report


def run_pipeline(input_dir, extensions_config, processed_dir, quarantine_dir, filename_pattern, log_dir, report_dir):
    logger = setup_logger(log_dir)
    logger.info("Pipeline started")

    # 1. Scan
    files = scan_folder(input_dir)
    logger.info(f"Scanned {len(files)} files")

    # 2. Validate
    files = validate_files(files, extensions_config, filename_pattern)
    logger.info("Validation complete")

    # 3. Classify
    files = classify_files(files, extensions_config)
    logger.info("Classification complete")

    # 4. Move
    for file in files:
        logger.info(
            f"{file.full_path.name} | valid={file.is_valid_file} | "
            f"name_valid={file.is_valid_name} | ext_valid={file.is_valid_extension} | "
            f"category={file.category}"
        )

    files = move_files(files, processed_dir, quarantine_dir)
    logger.info("Move complete")

    # 5. Report
    generate_report(files, report_dir)
    logger.info("Report generated")

    logger.info("Pipeline finished")

    return files
