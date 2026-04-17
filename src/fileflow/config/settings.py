import json
from pathlib import Path


def load_config() -> dict:
    base_dir = Path(__file__).resolve().parents[3]
    config_path = base_dir / "config" / "config.json"

    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    with open(config_path) as f:
        return json.load(f)


def resolve_paths(config: dict, args) -> dict:
    base_dir = Path(__file__).resolve().parents[3]

    # -------------------------
    # Input selection
    # -------------------------
    if args.demo:
        input_path = base_dir / "demo_data" / "demo_input"
    elif args.input:
        input_path = Path(args.input).resolve()
    else:
        input_path = base_dir / "data" / "default_input"

    input_path.mkdir(parents = True, exist_ok = True)

    # -------------------------
    # All other folders inside input root
    # -------------------------
    root = input_path.parent

    paths = {
        "input": input_path,
        "processed": root / "processed",
        "quarantine": root / "quarantine",
        "logs": root / "output" / "logs",
        "reports": root / "output" / "reports",
        }

    return paths
