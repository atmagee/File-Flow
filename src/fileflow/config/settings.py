import json
from pathlib import Path


def load_config() -> dict:
    base_dir = Path(__file__).resolve().parents[3]
    config_path = base_dir / "config" / "config.json"

    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    with open(config_path) as f:
        return json.load(f)


def resolve_paths(input_path: str = None, demo: bool = False) -> dict:

    base_dir = Path(__file__).resolve().parents[3]

    # -------------------------
    # Input folder
    # -------------------------
    if demo:
        input_dir = base_dir / "demo_data" / "demo_input"
        root = base_dir / "demo_data"
        source_type = "demo"

    elif input_path:

        input_dir = Path(input_path).expanduser()

        if not input_dir.is_absolute():
            input_dir = (base_dir / input_dir).resolve()

        parent = input_dir.parent
        input_name = input_dir.name

        if input_name.startswith("sorted_"):
            root = parent / input_name
        else:
            root = parent / f"sorted_{input_name}"

        source_type = "custom"

    else:
        input_dir = base_dir / "data" / "default_input"
        root = base_dir / "data"
        source_type = "default"

    # Ensure input folder exists
    input_dir.mkdir(parents = True, exist_ok = True)

    # Ensure output root exists
    root.mkdir(parents = True, exist_ok = True)

    # -------------------------
    # Output structure
    # -------------------------
    paths = {
        "input": input_dir,
        "root": root,
        "processed": root / "processed",
        "quarantine": root / "quarantine",
        "logs": root / "output" / "logs",
        "reports": root / "output" / "reports",
        "source_type": source_type,
        }

    return paths
