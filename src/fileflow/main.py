import argparse

from fileflow.config import load_config, resolve_paths
from fileflow.pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser(
        description="FileFlow: validate, organise, and report on files in a directory",
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--input",
        type=str,
        help="Path to a custom input folder (overrides default)",
    )

    group.add_argument(
        "--demo",
        action="store_true",
        help="Use the demo input folder instead of the default input folder",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="FileFlow 1.0",
    )

    args = parser.parse_args()

    config = load_config()
    paths = resolve_paths(config, args)

    if args.demo:
        source_type = "demo"
    elif args.input:
        source_type = "custom"
    else:
        source_type = "default"

    print(f"Using {source_type} input folder: {paths['input']}")

    validation_config = config.get("validation", {})

    run_pipeline(
        paths["input"],
        paths["processed"],
        paths["quarantine"],
        paths["logs"],
        paths["reports"],
        validation_config.get("filename_pattern"),
        validation_config.get("extensions"),
        config.get("archive", {}),
    )


if __name__ == "__main__":
    main()
