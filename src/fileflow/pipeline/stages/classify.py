def get_extension_category(extension: str, extensions_config: dict) -> str:
    for category, ext_list in extensions_config.items():
        if extension in ext_list:
            return category
    return "other"


def classify_files(files: list, extensions_config: dict) -> list:
    for file in files:
        file.category = get_extension_category(file.extension, extensions_config)

    return files
