from dataclasses import dataclass
from pathlib import Path


# Create a dataclass for files, that stores the data we need from each file for later manipulation
@dataclass
class FileMeta:
    full_path: Path  # for moving the file
    name: str  # for validating the naming scheme
    extension: str  # for making sure the extension is on the valid extension list
    category: str = None  # for classifying files before move
    is_valid_name: bool = None  # filename validation to be used in move
    is_valid_extension: bool = None  # extension validation to be used in move
    is_valid_file: bool = None  # combination of filename and extension validation to be used in move
    is_duplicate: bool = False
    duplicate_index: int = 0
    was_processed: bool = False
    was_archived: bool = False


# Defines a function that scans the files and returns a list of dataclasses
def scan_folder(input_dir: str, recursive: bool = False) -> list[FileMeta]:
    path = Path(input_dir)
    files = []

    iterator = path.rglob("*") if recursive else path.iterdir()

    for file in iterator:
        if file.is_file():
            files.append(
                FileMeta(
                    full_path = file.resolve(),
                    name = file.stem,
                    extension = file.suffix.lstrip("."),
                    ),
                )

    return files
