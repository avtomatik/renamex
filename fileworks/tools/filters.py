from pathlib import Path

from core.constants import PREFIXES


def get_files_excluding(name_excluded: str, folder_str=None) -> tuple[str, ...]:
    path = Path(folder_str or '.')
    return tuple(
        file.name
        for file in path.iterdir()
        if file.is_file() and file.name != name_excluded
    )


def get_filtered_file_names(prefixes: set[str] = PREFIXES, folder_str=None) -> set[str]:
    # W0102
    path = Path(folder_str or '.')
    return {
        file.name.lower()
        for file in path.iterdir()
        if file.is_file() and not any(
            file.name.lower().startswith(prefix) for prefix in prefixes
        )
    }


def get_files_matching_all_patterns(matchers: tuple[str], folder_str=None) -> list[str]:
    path = Path(folder_str or '.')
    return [
        file.name
        for file in path.iterdir()
        if file.is_file() and all(matcher in file.name for matcher in matchers)
    ]


def get_files_matching_any_pattern(matchers: tuple[str], folder_str=None) -> list[str]:
    path = Path(folder_str or '.')
    return [
        file.name
        for file in path.iterdir()
        if file.is_file() and any(matcher in file.name for matcher in matchers)
    ]


def get_file_names(path: Path) -> set[str]:
    return [f.name.lower() for f in path.iterdir() if f.is_file()]


def walk_and_list_directory(path: Path):
    result = []
    for path in path.rglob('*'):
        if path.is_dir():
            dirnames = [p.name for p in path.iterdir() if p.is_dir()]
            filenames = [p.name for p in path.iterdir() if p.is_file()]
            result.append((dirnames, filenames))
    return result
