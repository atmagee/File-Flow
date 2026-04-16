import re


def load_extensions(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        return [
            line.strip().lower()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

def validate_files(files: list, extensions_file: str, filename_pattern: str) -> list:

    allowed_extensions = load_extensions(extensions_file)
    pattern = re.compile(filename_pattern)

    for file in files:
        filename = file.name
        extension = file.extension.lower()

        # Validate filename
        if pattern.fullmatch(filename):
            file.is_valid_name = True
        else:
            file.is_valid_name = False

        # Validate extension
        if extension in allowed_extensions:
            file.is_valid_extension = True
        else:
            file.is_valid_extension = False

        # Combined result
        file.is_valid_file = file.is_valid_name and file.is_valid_extension

    return files