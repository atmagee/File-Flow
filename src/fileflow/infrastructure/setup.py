from pathlib import Path


def ensure_directories(config: dict):
    paths = config["paths"]
    structure = config.get("structure", {})
    extensions = config["validation"]["extensions"]

    # Base directories
    for path in paths.values():
        Path(path).mkdir(parents = True, exist_ok = True)

    # Quarantine subfolders
    for sub in structure.get("quarantine_subfolders", []):
        (Path(paths["quarantine"]) / sub).mkdir(parents = True, exist_ok = True)

    # Processed category subfolders
    if structure.get("use_category_subfolders", True):
        for category in extensions.keys():
            (Path(paths["processed"]) / category).mkdir(parents = True, exist_ok = True)
