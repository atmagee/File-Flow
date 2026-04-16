from fileflow.config.settings import load_config
from fileflow.pipeline.pipeline import run_pipeline


def main():
    config = load_config()

    paths = config["paths"]
    validation = config["validation"]

    run_pipeline(
        paths["input"],
        validation["extensions_file"],
        paths["processed"],
        paths["quarantine"],
        validation["filename_pattern"]
    )

if __name__ == "__main__":
    main()