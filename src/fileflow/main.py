from fileflow.config import load_config
from fileflow.infrastructure import ensure_directories
from fileflow.pipeline import run_pipeline


def main():
    config = load_config()

    paths = config["paths"]
    setup_config = config.get("setup", {})

    # Setup environment
    ensure_directories(config)

    # Run pipeline
    run_pipeline(
        paths["input"],
        paths["processed"],
        paths["quarantine"],
        paths["logs"],
        paths["reports"],
        config["validation"]["filename_pattern"],
        config["validation"]["extensions"],
        config.get("archive", {})
        )


if __name__ == "__main__":
    main()
