from datetime import datetime

from fileflow.infrastructure import setup_logger, format_log_event, generate_report, archive_processed_files
from fileflow.pipeline.stages import scan_folder, validate_files, build_extension_map, classify_files, move_files


def run_pipeline(
        input_dir,
        processed_dir,
        quarantine_dir,
        log_dir,
        report_dir,
        filename_pattern,
        extensions_config,
        archive_config,
        ):

    # Create shared run_id
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    extension_map = build_extension_map(extensions_config)

    logger = setup_logger(log_dir, run_id)

    logger.info(
        format_log_event(
            {
                "action": "system",
                "message": f"Pipeline started | run_id={run_id}",
                },
            ),
        )

    print("\nTIME           ACTION         FILENAME              REASON                        ->RESULT")
    print("-----------------------------------------------------------------------------------------------------------")

    # 1. Scan
    try:
        files = scan_folder(input_dir)
    except Exception as e:
        logger.info(
            format_log_event(
                {
                    "action": "failed",
                    "filename": "SCAN_STAGE",
                    "error": str(e),
                    },
                ),
            )
        return []

    # 2. Validate
    try:
        files = validate_files(files, extensions_config, filename_pattern)
    except Exception as e:
        logger.info(
            format_log_event(
                {
                    "action": "failed",
                    "filename": "VALIDATE_STAGE",
                    "error": str(e),
                    },
                ),
            )
        return files

    # 3. Classify
    try:
        files = classify_files(files, extension_map)
    except Exception as e:
        logger.info(
            format_log_event(
                {
                    "action": "failed",
                    "filename": "CLASSIFY_STAGE",
                    "error": str(e),
                    },
                ),
            )
        return files

    # 4. Move
    try:
        files = move_files(files, processed_dir, quarantine_dir, logger)
    except Exception as e:
        logger.info(
            format_log_event(
                {
                    "action": "failed",
                    "filename": "MOVE_STAGE",
                    "error": str(e),
                    },
                ),
            )
        return files

    # 5. Archive
    try:
        if archive_config.get("enabled", False):
            archive_processed_files(
                processed_dir,
                archive_config.get("days_threshold", 30),
                archive_config.get("subfolder_name", "archive"),
                logger,
                )

        else:
            logger.info(
                format_log_event(
                    {
                        "action": "system",
                        "message": "Archive skipped (disabled)",
                        },
                    ),
                )

    except Exception as e:
        logger.info(
            format_log_event(
                {
                    "action": "failed",
                    "filename": "ARCHIVE_STAGE",
                    "error": str(e),
                    },
                ),
            )

    # 6. Report
    try:
        generate_report(files, report_dir, run_id)
        logger.info(
            format_log_event(
                {
                    "action": "system",
                    "message": "Report generated",
                    },
                ),
            )

    except Exception as e:
        logger.info(
            format_log_event(
                {
                    "action": "failed",
                    "filename": "REPORT_STAGE",
                    "error": str(e),
                    },
                ),
            )

        logger.info(
            format_log_event(
                {
                    "action": "system",
                    "message": f"Pipeline finished | run_id={run_id}",
                    },
                ),
            )

    return files
