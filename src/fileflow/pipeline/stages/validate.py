import re


def get_valid_extensions(config_extensions: dict) -> set:
    valid_extensions = set()

    for group in config_extensions.values():
        valid_extensions.update(ext.lower() for ext in group)

    return valid_extensions


def validate_files(files: list, extensions_config: dict, filename_pattern: str) -> list:
    pattern = re.compile(filename_pattern)
    valid_extensions = get_valid_extensions(extensions_config)

    for file in files:

        # Validate filename
        if pattern.fullmatch(file.name):
            file.is_valid_name = True
        else:
            file.is_valid_name = False

        # Validate extension
        if file.extension in valid_extensions:
            file.is_valid_extension = True
        else:
            file.is_valid_extension = False

        # Combined result
        file.is_valid_file = file.is_valid_name and file.is_valid_extension

    return files
