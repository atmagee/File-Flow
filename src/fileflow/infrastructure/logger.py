import logging
from pathlib import Path


def setup_logger(log_dir: str, run_id: str) -> logging.Logger:
    log_file = Path(log_dir) / f"fileflow_{run_id}.log"

    logger = logging.getLogger(f"fileflow_{run_id}")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        )

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
