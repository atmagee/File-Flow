import json
from pathlib import Path


def load_config():

    base_dir = Path(__file__).resolve().parents[3]
    config_path = base_dir / "config" / "config.json"

    with open(config_path) as f:
        return json.load(f)