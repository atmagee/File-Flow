from dataclasses import dataclass
from pathlib import Path


# Represents a single file as it moves through the pipeline
@dataclass
class FileMeta:

    # --- Core file metadata ---
    full_path: Path  # Absolute path (used for moving/renaming)
    name: str  # Filename without extension (used for validation)
    extension: str  # File extension (used for validation/classification)

    # --- Classification ---
    category: str = None  # Target category (e.g. text, images, documents)

    # --- Validation results ---
    is_valid_name: bool = None  # Matches filename pattern
    is_valid_extension: bool = None  # Extension is allowed
    is_valid_file: bool = None  # Combined validation result

    # --- Duplicate handling ---
    is_duplicate: bool = False  # True if renamed due to conflict
    duplicate_index: int = 0  # Suffix index (_1, _2, ...)

    # --- File state tracking ---
    was_processed: bool = False  # Moved to processed/
    was_quarantined: bool = False  # Moved to quarantine/
    was_archived: bool = False  # Moved to archive/


# Defines a function that scans the files and returns a list of dataclasses
def scan_folder(input_dir: str, recursive: bool = False) -> list[FileMeta]:
    path = Path(input_dir)
    files = []

    iterator = path.rglob("*") if recursive else path.iterdir()

    for file in iterator:
        if file.is_file():
            files.append(
                FileMeta(
                    full_path = file,
                    name = file.stem,
                    extension = file.suffix.lstrip("."),
                    ),
                )

    return files
