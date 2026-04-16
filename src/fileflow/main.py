from fileflow.config.settings import load_config
from fileflow.infrastructure.setup import ensure_directories
from fileflow.pipeline.pipeline import run_pipeline


def main():
    config = load_config()

    paths = config["paths"]
    setup_config = config.get("setup", {})

    # Setup environment
    ensure_directories(
        paths,
        setup_config.get("create_missing_directories", True)
    )

    # Run pipeline
    run_pipeline(
        paths["input"],
        paths["processed"],
        paths["quarantine"],
        paths["logs"],
        paths["reports"],
        config["validation"]["filename_pattern"],
        config["validation"]["extensions"]
    )


if __name__ == "__main__":
    main()
