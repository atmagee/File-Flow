from datetime import datetime
from pathlib import Path
import shutil


def archive_processed_files(processed_dir: str, days_threshold: int) -> int:
    processed_path = Path(processed_dir)
    now = datetime.now()

    archived_count = 0

    # recursively scan all files
    for file in processed_path.rglob("*"):

        # skip directories
        if file.is_dir():
            continue

        # skip files already in archive
        if "archive" in file.parts:
            continue

        last_modified = datetime.fromtimestamp(file.stat().st_mtime)
        age = now - last_modified

        if age.total_seconds() >= days_threshold * 86400:

            # archive folder inside the file's current directory
            archive_dir = file.parent / "archive"
            archive_dir.mkdir(exist_ok=True)

            destination = archive_dir / file.name

            try:
                shutil.move(str(file), str(destination))
                archived_count += 1
            except Exception:
                pass

    return archived_count