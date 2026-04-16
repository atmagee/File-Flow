import json
from pathlib import Path


def load_config():
    # Project root (File-Flow/)
    base_dir = Path(__file__).resolve().parents[3]

    config_path = base_dir / "config" / "config.json"

    with open(config_path) as f:
        config = json.load(f)

    # Resolve all paths to absolute
    if "paths" in config:
        for key, value in config["paths"].items():
            config["paths"][key] = str(base_dir / value)

    return config