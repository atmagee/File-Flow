import re


FILENAME_PATTERN = re.compile(r'^[a-z]+(_[a-z]+)*([0-9]+)?$')


def load_extensions(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        return [
            line.strip().lower()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

def validate_files(files: list, extensions_file: str) -> list:

    allowed_extensions = load_extensions(extensions_file)

    for file in files:
        filename = file.full_path.stem
        extension = file.extension.lower()

        # Validate filename
        if FILENAME_PATTERN.fullmatch(filename):
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