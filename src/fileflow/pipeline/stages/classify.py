def build_extension_map(extensions_config: dict) -> dict:
    return {
        extension: category
        for category, extensions in extensions_config.items()
        for extension in extensions
        }


def classify_files(files: list, extension_map: dict) -> list:
    for file in files:
        if file.is_valid_extension:
            file.category = extension_map.get(file.extension, "invalid")
        else:
            file.category = "invalid"

    return files
