import argparse

from fileflow.config import load_config, resolve_paths
from fileflow.pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser(
        description = "FileFlow CLI (defaults to data/default_input if no option provided)",
        )

    # Mutually exclusive input options
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--input",
        type = str,
        help = "Custom input folder",
        )

    group.add_argument(
        "--demo",
        action = "store_true",
        help = "Use demo input folder",
        )

    # Demo-only operations
    parser.add_argument(
        "--reset-demo",
        action = "store_true",
        help = "Reset demo dataset (only valid with --demo)",
        )

    args = parser.parse_args()

    config = load_config()
    paths = resolve_paths(config, args)

    if args.demo:
        print("Using demo input folder")
    elif args.input:
        print(f"Using custom input folder: {paths['input']}")
    else:
        print("Using default input folder")

    run_pipeline(
        str(paths["input"]),
        str(paths["processed"]),
        str(paths["quarantine"]),
        str(paths["logs"]),
        str(paths["reports"]),
        config["validation"]["filename_pattern"],
        config["validation"]["extensions"],
        config.get("archive", {}),
        )


if __name__ == "__main__":
    main()
