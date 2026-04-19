import shutil
from datetime import datetime, timedelta
from pathlib import Path

from fileflow.infrastructure.logger import format_log_event


def archive_processed_files(files, processed_dir: str, days_threshold: int, archive_subfolder, logger) -> None:
    cutoff = datetime.now() - timedelta(days = days_threshold)

    for file_meta in files:
        file = Path(file_meta.full_path)

        # Skip if file no longer exists
        if not file.exists():
            continue

        # Only archive processed files (not quarantined)
        if Path(processed_dir) not in file.parents:
            continue

        # Skip archive folders
        if archive_subfolder in file.parts:
            continue

        try:
            last_modified = datetime.fromtimestamp(file.stat().st_mtime)

            if last_modified < cutoff:

                archive_dir = file.parent / archive_subfolder
                destination = archive_dir / file.name

                archive_dir.mkdir(parents = True, exist_ok = True)

                shutil.move(str(file), str(destination))

                # Update metadata
                file_meta.was_archived = True
                file_meta.full_path = destination

                logger.info(
                    format_log_event(
                        {
                            "action": "archived",
                            "filename": file.name,
                            "destination_path": str(destination),
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
