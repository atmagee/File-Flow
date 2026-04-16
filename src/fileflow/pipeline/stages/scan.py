from pathlib import Path
from datetime import datetime
from dataclasses import dataclass


# Create a dataclass for files, that stores the data we need from each file for later manipulation
@dataclass
class FileMeta:
    full_path: Path     # for moving the file
    name: str       # for validating the naming scheme
    extension: str      # for making sure the extension is on the valid extension list
    last_modified: datetime     # for archiving old files
    is_valid_name: bool = None    # returns true for a valid file and false for an invalid file
    is_valid_extension: bool = None     # returns true for a valid extension and false for an invalid extension
    is_valid_file: bool = None       # returns true for a valid file and false for an invalid file


# Defines a function that scans the files and returns a list of dataclasses
def scan_folder(input_dir: str) -> list[FileMeta]:
    path = Path(input_dir)

    files = []

    for file in path.iterdir():
        if file.is_file():
            files.append(
                FileMeta(
                    full_path=file.resolve(),
                    name=file.stem,
                    extension=file.suffix.lstrip("."),
                    last_modified=datetime.fromtimestamp(file.stat().st_mtime)
                )
            )

    return files