import re
import shutil
from pathlib import Path

from fileflow.infrastructure.logger import format_log_event


def get_unique_destination(destination: Path) -> Path:

    if not destination.exists():
        return destination

    parent = destination.parent
    suffix = destination.suffix
    stem = destination.stem

    match = re.match(r"^(.*?)(?:_(\d+))?$", stem)

    base_name = match.group(1)
    number = int(match.group(2)) if match.group(2) else 0

    counter = number + 1

    while True:
        new_name = f"{base_name}_{counter}{suffix}"
        new_path = parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def move_files(files: list, base_processed: str, quarantine_dir: str, logger) -> list:
    processed_path = Path(base_processed)
    quarantine_path = Path(quarantine_dir)

    for file in files:
        source = file.full_path

        # Invalid -> quarantine subfolders
        if not file.is_valid_file:

            if not file.is_valid_name and not file.is_valid_extension:
                subfolder = "invalid_both"
                reason = "invalid name and extension"

            elif not file.is_valid_name:
                subfolder = "invalid_filename"
                reason = "invalid naming format"

            else:
                subfolder = "invalid_extension"
                reason = "extension not allowed"

            destination = quarantine_path / subfolder / source.name
            action_type = "quarantined"
            file.was_quarantined = True

        # Valid -> processed
        else:
            destination = processed_path / file.category / source.name
            action_type = "processed"
            reason = "valid file"
            file.was_processed = True

        # Duplicate handling
        original_destination = destination
        destination = get_unique_destination(destination)

        file.is_duplicate = destination != original_destination

        if file.is_duplicate:
            match = re.search(r'_(\d+)$', destination.stem)
            file.duplicate_index = int(match.group(1)) if match else 1

        else:
            file.duplicate_index = 0

        # Move + Logging
        try:
            destination.parent.mkdir(parents = True, exist_ok = True)
            shutil.move(str(source), str(destination))
            file.full_path = destination

            # log duplicate
            if file.is_duplicate:
                logger.info(
                    format_log_event(
                        {
                            "action": "renamed",
                            "filename": source.name,
                            "destination_path": str(destination),
                            "reason": "duplicate filename",
                            },
                        ),
                    )

            # log final action
            logger.info(
                format_log_event(
                    {
                        "action": action_type,
                        "filename": source.name,
                        "destination_path": str(destination),
                        "reason": reason,
                        },
                    ),
                )

        except Exception as e:
            logger.info(
                format_log_event(
                    {
                        "action": "failed",
                        "filename": source.name,
                        "error": str(e),
                        },
                    ),
                )
            continue

    return files
