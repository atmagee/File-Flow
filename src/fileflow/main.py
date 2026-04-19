import argparse

from fileflow import run_pipeline
from fileflow.config import resolve_paths, load_config


def main():
    parser = argparse.ArgumentParser(
        description = "FileFlow: validate, organise, and report on files in a folder",
        )

    parser.add_argument("--input", type = str, help = "Path to a custom input folder")
    parser.add_argument("--demo", action = "store_true", help = "Use demo input folder")
    parser.add_argument("--version", action = "version", version = "FileFlow 1.0")

    args = parser.parse_args()

    # Resolve paths (cross-platform, Windows or Linux)
    paths = resolve_paths(input_path = args.input, demo = args.demo)

    print(f"Using {paths['source_type']} input folder: {paths['input']}")

    # Load validation/config
    config = load_config()
    validation_config = config.get("validation", {})

    run_pipeline(
        input_dir = paths["input"],
        processed_dir = paths["processed"],
        quarantine_dir = paths["quarantine"],
        log_dir = paths["logs"],
        report_dir = paths["reports"],
        filename_pattern = validation_config.get("filename_pattern"),
        extensions_config = validation_config.get("extensions"),
        archive_config = config.get("archive", {}),
        )


if __name__ == "__main__":
    main()
