from datetime import datetime

from fileflow.infrastructure import setup_logger, generate_report
from fileflow.pipeline.stages import scan_folder, validate_files,build_extension_map, classify_files, move_files


def run_pipeline(
        input_dir,
        processed_dir,
        quarantine_dir,
        log_dir,
        report_dir,
        filename_pattern,
        extensions_config,
        ):

    # Create shared run_id
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    logger = setup_logger(log_dir, run_id)
    logger.info(f"Pipeline started | run_id={run_id}")

    extensions_map = build_extension_map(extensions_config)

    # 1. Scan
    files = scan_folder(input_dir)
    logger.info(f"Scanned {len(files)} files")

    # 2. Validate
    files = validate_files(files, extensions_config, filename_pattern)
    logger.info("Validation complete")

    # 3. Classify
    files = classify_files(files, extensions_map)
    logger.info("Classification complete")

    # 4. Move
    files = move_files(files, processed_dir, quarantine_dir)
    logger.info("Move complete")

    # 5. Log
    for file in files:
        logger.info(
            f"{file.full_path.name} | valid={file.is_valid_file} | "
            f"name_valid={file.is_valid_name} | ext_valid={file.is_valid_extension} | "
            f"category={file.category}",
            )

    # 6. Report
    generate_report(files, report_dir, run_id)
    logger.info("Report generated")

    logger.info(f"Pipeline finished | run_id={run_id}")

    return files
