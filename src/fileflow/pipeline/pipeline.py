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

    extension_map = build_extension_map(extensions_config)

    # 1. Scan
    try:
        files = scan_folder(input_dir)
        logger.info(f"Scanned {len(files)} files")
    except Exception as e:
        logger.error(f"Scan failed: {e}")
        return []

    # 2. Validate
    try:
        files = validate_files(files, extensions_config, filename_pattern)
        logger.info("Validation complete")
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        return files

    # 3. Classify
    try:
        files = classify_files(files, extension_map)
        logger.info("Classification complete")
    except Exception as e:
        logger.error(f"Classification failed: {e}")
        return files

    # 4. Move
    try:
        files = move_files(files, processed_dir, quarantine_dir)
        logger.info("Move complete")
    except Exception as e:
        logger.error(f"Move failed: {e}")
        return files

    # 5. Log
    for file in files:
        try:
            logger.info(
                f"{file.full_path.name} | valid={file.is_valid_file} | "
                f"name_valid={file.is_valid_name} | ext_valid={file.is_valid_extension} | "
                f"category={file.category} | "
                f"duplicate={file.is_duplicate} | dup_index={file.duplicate_index}"
                )
        except Exception as e:
            logger.error(f"Logging failed for file {file.full_path}: {e}")

    # 6. Report
    try:
        generate_report(files, report_dir, run_id)
        logger.info("Report generated")
    except Exception as e:
        logger.error(f"Report generation failed: {e}")

    logger.info(f"Pipeline finished | run_id={run_id}")

    return files
