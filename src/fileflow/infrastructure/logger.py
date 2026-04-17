import logging
from datetime import datetime
from pathlib import Path


def setup_logger(log_dir: str, run_id: str) -> logging.Logger:

    Path(log_dir).mkdir(parents = True, exist_ok = True)
    log_file = Path(log_dir) / f"fileflow_{run_id}.log"

    logger = logging.getLogger(f"fileflow_{run_id}")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter("%(message)s")

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def format_log_event(event: dict) -> str:
    time_str = datetime.now().strftime("%H:%M:%S.%f")[:-3]

    action_key = event["action"]
    action = action_key.upper().ljust(12)
    filename = event.get("filename", "").ljust(20)

    reason = event.get("reason", "")
    reason_str = f" ({reason})" if reason else ""

    # SYSTEM EVENTS
    if action_key == "system":
        message = event.get("message", "")
        return f"[{time_str}] [SYSTEM     ] {message}"

    # FAILURE EVENTS
    if action_key == "failed":
        return f"[{time_str}] [ERROR      ] {filename} -> move failed                   ({event['error']})"

    # RESULT LOGIC
    if action_key == "renamed":
        result = event["destination_path"]
    elif action_key == "processed":
        result = event["destination_path"]
    elif action_key == "quarantined":
        result = event["destination_path"]
    elif action_key == "archived":
        result = event["destination_path"]
    else:
        result = ""

    return f"[{time_str}] [{action}] {filename} {reason_str.ljust(30)} -> {result}"
