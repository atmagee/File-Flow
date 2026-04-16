import logging
from pathlib import Path


def setup_logger(log_dir: str) -> logging.Logger:

    logger = logging.getLogger("fileflow")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    log_file = Path(log_dir) / "fileflow.log"

    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger