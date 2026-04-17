import shutil
from datetime import datetime, timedelta
from pathlib import Path

from fileflow.infrastructure import format_log_event


def archive_processed_files(processed_dir: str, days_threshold: int, archive_subfolder, logger) -> int:
    processed_path = Path(processed_dir)
    cutoff = datetime.now() - timedelta(days = days_threshold)

    archived_count = 0

    # Recursively scan all files
    for category_dir in processed_path.iterdir():
        if not category_dir.is_dir():
            continue

        for file in category_dir.iterdir():

            # Skip non-files
            if not file.is_file():
                continue

            # Skip archive folders
            if archive_subfolder in file.parts:
                continue

            try:
                last_modified = datetime.fromtimestamp(file.stat().st_mtime)

                if last_modified < cutoff:

                    archive_dir = category_dir / archive_subfolder
                    destination = archive_dir / file.name

                    archive_dir.mkdir(parents = True, exist_ok = True)

                    shutil.move(str(file), str(destination))
                    archived_count += 1

                    logger.info(
                        format_log_event(
                            {
                                "action": "archived",
                                "filename": file.name,
                                "destination_path": str(destination),
                                "archive_folder": archive_subfolder,
                                "reason": f"older than {days_threshold} days",
                                },
                            ),
                        )

            except Exception as e:
                logger.info(
                    format_log_event(
                        {
                            "action": "failed",
                            "filename": file.name,
                            "error": str(e),
                            },
                        ),
                    )

    return archived_count
