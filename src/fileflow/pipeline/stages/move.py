import re
import shutil
from pathlib import Path


def get_unique_destination(destination: Path, ) -> Path:

    if not destination.exists():
        return destination

    parent = destination.parent
    suffix = destination.suffix

    # Extract base + number suffix based on the pattern (_number)
    match = re.match(r'^(?P<base>.+?)(?:_(?P<num>\d+))?$', destination.stem)
    base = match.group("base")
    num = match.group("num")

    counter = int(num) + 1 if num else 1

    while True:
        new_name = f"{base}_{counter}{suffix}"
        new_path = parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


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
            destination = processed_path / file.category / source.name

        # Duplicate handling
        original_destination = destination
        destination = get_unique_destination(destination)

        if destination != original_destination:
            file.is_duplicate = True

            match = re.search(r'_(\d+)$', destination.stem)
            file.duplicate_index = int(match.group(1)) if match else 0
        else:
            file.is_duplicate = False
            file.duplicate_index = 0

        # Ensure destination directory exists
        destination.parent.mkdir(parents = True, exist_ok = True)

        shutil.move(str(source), str(destination))

        file.full_path = destination

    return files
