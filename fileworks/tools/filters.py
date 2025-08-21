from pathlib import Path
from typing import Union

from ..interfaces.protocols import MatchFileFilter


class NameExclusionFilter:
    """
    Filter files by excluding specific names.
    Usage:
        >>> service = FileService(Path(folder_str or '.'))
        >>> files = service.list_files(
                filters=[NameExclusionFilter(name_excluded)]
            )
    """

    def __init__(self, names_to_exclude: Union[str, tuple[str, ...]]):
        if isinstance(names_to_exclude, str):
            self.names_to_exclude = {names_to_exclude}
        else:
            self.names_to_exclude = set(names_to_exclude)

    def matches(self, file: Path) -> bool:
        return file.name not in self.names_to_exclude


class PrefixExclusionFilter:
    """
    Filter files by excluding specific prefixes.
    Usage:
        >>> service = FileService(Path(folder_str or '.'))
        >>> files = service.list_files(
                filters=[PrefixExclusionFilter(prefixes)],
                lowercase=True
            )
    """

    def __init__(self, prefixes: set[str]):
        self.prefixes = prefixes

    def matches(self, file: Path) -> bool:
        name = file.name.lower()
        return not any(name.startswith(prefix) for prefix in self.prefixes)


class PatternAllMatchFilter:
    """
    Filter files that match all specified patterns.
    Usage:
        >>> service = FileService(Path(folder_str or '.'))
        >>> files = service.list_files(
                filters=[PatternAllMatchFilter(matchers)]
            )
    """

    def __init__(self, patterns: tuple[str, ...]):
        self.patterns = patterns

    def matches(self, file: Path) -> bool:
        return all(p in file.name for p in self.patterns)


class PatternAnyMatchFilter:
    """
    Filter files that match any of the specified patterns.
    Usage:
        >>> service = FileService(Path(folder_str or '.'))
        >>> files = service.list_files(
                filters=[PatternAnyMatchFilter(matchers)]
            )
    """

    def __init__(self, patterns: tuple[str, ...]):
        self.patterns = patterns

    def matches(self, file: Path) -> bool:
        return any(p in file.name for p in self.patterns)


class EmptyFileFilter:
    """Filter files that are empty and not reserved."""

    def __init__(self, reserved: set[str]):
        self.reserved = reserved

    def matches(self, file: Path) -> bool:
        return (
            file.is_file()
            and file.stat().st_size == 0
            and file.name not in self.reserved
        )


class FileService:
    """Service to list and filter files in a directory."""

    def __init__(self, folder: Path = Path('.')):
        self.folder = folder

    def list_files(
        self,
        filters: list[MatchFileFilter] | None = None,
        lowercase: bool = False
    ) -> list[str]:
        """_summary_

        Args:
            filters (List[FileFilter], optional): _description_.
                Defaults to None.
            lowercase (bool, optional): _description_. Defaults to False.

        Returns:
            List[str]: _description_

        Usage:
            >>> service = FileService(path)
            >>> files = service.list_files(lowercase=True)
        """
        filters = filters or []
        result: list[str] = []
        for file in self.folder.iterdir():
            if file.is_file() and all(f.matches(file) for f in filters):
                result.append(file.name.lower() if lowercase else file.name)
        return result

    def list_all_file_names(self) -> list[str]:
        """_summary_

        Returns:
            List[str]: _description_

        Usage:
            >>> service = FileService(path)
            >>> source_file_names = service.list_all_file_names()
        """
        return [file.name for file in self.folder.iterdir() if file.is_file()]

    def list_empty_files(self, reserved: set[str]) -> list[str]:
        """_summary_

        Args:
            reserved (Set[str]): _description_

        Returns:
            List[str]: _description_

        Usage:
            >>> service = FileService(path)
            >>> empty_files = service.list_empty_files(reserved)
        """
        return [
            file.name
            for file in self.folder.iterdir()
            if (
                file.is_file()
                and file.stat().st_size == 0
                and file.name not in reserved
            )
        ]

    def walk_directory(self) -> list[tuple[list[str], list[str]]]:
        """_summary_

        Returns:
            List[Tuple[List[str], List[str]]]: _description_

        Usage:
            >>> service = FileService(path)
            >>> structure = service.walk_directory()
        """
        result: list[tuple[list[str], list[str]]] = []
        for path in self.folder.rglob('*'):
            if path.is_dir():
                dirnames = [p.name for p in path.iterdir() if p.is_dir()]
                filenames = [p.name for p in path.iterdir() if p.is_file()]
                result.append((dirnames, filenames))
        return result


class NullFileFilter:
    """Accepts all regular files (ignores directories)."""

    def is_target(self, file: Path) -> bool:
        return file.is_file()


class FileExtensionFilter:
    """Filter files by allowed extensions."""

    def __init__(self, extensions: tuple[str, ...]):
        self.extensions = tuple(
            ext if ext.startswith('.') else f'.{ext}' for ext in extensions
        )

    def is_target(self, file: Path) -> bool:
        return file.is_file() and file.suffix in self.extensions
