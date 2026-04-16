import shutil
from pathlib import Path


def move_files(files: list, base_processed: str, quarantine_dir: str) -> list:

    processed_path = Path(base_processed)
    quarantine_path = Path(quarantine_dir)

    for file in files:
        source = file.full_path

        # Invalid → quarantine subfolders
        if not file.is_valid_file:

            if not file.is_valid_name and not file.is_valid_extension:
                subfolder = "invalid_both"
            elif not file.is_valid_name:
                subfolder = "invalid_filename"
            else:
                subfolder = "invalid_extension"

            destination = quarantine_path / subfolder / source.name

        # Valid → processed
        else:
            destination = processed_path / source.name

        shutil.move(str(source), str(destination))

        file.full_path = destination

    return files