from pathlib import Path

from fileworks.interfaces.protocols import MatchFileFilter


class NameExclusionFilter:
    """
    Filter files by excluding specific names.
    Usage:
        >>> service = FileService(Path(folder_str or '.'))
        >>> files = service.list_files(
                filters=[NameExclusionFilter(name_excluded)]
            )
    """

    def __init__(self, names_to_exclude: str | tuple[str, ...]):
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


class NullFileFilter:
    """Accepts all regular files (ignores directories)."""

    def is_target(self, file: Path) -> bool:
        return file.is_file()


class FileExtensionFilter:
    """Filter files by allowed extensions."""

    def __init__(self, extensions: tuple[str, ...]):
        self.extensions = tuple(
            ext if ext.startswith(".") else f".{ext}" for ext in extensions
        )

    def is_target(self, file: Path) -> bool:
        return file.is_file() and file.suffix in self.extensions


class FileService:
    """
    A service class for managing and filtering files in a directory.

    This class provides functionality to list, filter, and walk through files
    in a specified directory, with various filtering options. It supports
    filters based on file names, patterns, file size, and more.

    Attributes:
        folder (Path): The directory path where files will be listed and
        filtered.

    Methods:
        list_files(
            filters: list[MatchFileFilter] | None = None,
            lowercase: bool = False,
        ) -> list[str]:
            Lists all files in the directory, applying any specified filters.

        list_all_file_names() -> list[str]:
            Lists all file names in the directory, without any filtering.

        list_empty_files(reserved: set[str]) -> list[str]:
            Lists all empty files in the directory, excluding reserved file
            names.

        walk_directory() -> list[tuple[list[str], list[str]]]:
            Recursively walks through the directory and lists files and
            subdirectories.
    """

    def __init__(self, folder: Path = Path(".")):
        """
        Initializes the FileService with the given folder path.

        Args:
            folder (Path): The directory path to search for files
            (default is current directory).
        """
        self.folder = folder

    def list_files(
        self,
        filters: list[MatchFileFilter] | None = None,
        lowercase: bool = False,
    ) -> list[str]:
        """
        Lists files in the directory, optionally applying filters and
        transforming file names.

        Args:
            filters (list[MatchFileFilter] | None): A list of filters to apply
            to the files.
                If None, no filters are applied.
            lowercase (bool): If True, all file names are converted to
            lowercase.

        Returns:
            list[str]: A list of file names that pass the applied filters.

        Usage:
            >>> service = FileService(Path("/path/to/dir"))
            >>> files = service.list_files(
                    filters=[NameExclusionFilter(names_to_exclude)],
                    lowercase=True,
                )
        """
        filters = filters or []
        result: list[str] = []
        for file in self.folder.iterdir():
            if file.is_file() and all(f.matches(file) for f in filters):
                result.append(file.name.lower() if lowercase else file.name)
        return result

    def list_all_file_names(self) -> list[str]:
        """
        Lists all file names in the directory without applying any filters.

        Returns:
            list[str]: A list of all file names in the directory.

        Usage:
            >>> service = FileService(Path("/path/to/dir"))
            >>> all_file_names = service.list_all_file_names()
        """
        return [file.name for file in self.folder.iterdir() if file.is_file()]

    def list_empty_files(self, reserved: set[str]) -> list[str]:
        """
        Lists all empty files in the directory, excluding those that are
        reserved.

        Args:
            reserved (set[str]): A set of reserved file names to exclude from
            the result.

        Returns:
            list[str]: A list of empty file names that are not reserved.

        Usage:
            >>> service = FileService(Path("/path/to/dir"))
            >>> empty_files = service.list_empty_files(reserved={"README.md"})
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
        """
        Recursively walks through the directory and lists subdirectories and
        files.

        This method returns a list of tuples where each tuple contains:
            - A list of subdirectories in the current directory.
            - A list of files in the current directory.


        Returns:
            list[tuple[list[str], list[str]]]: A list of tuples representing
                                                subdirectories and files found
                                                while walking through the
                                                directory.

        Usage:
            >>> service = FileService(Path("/path/to/dir"))
            >>> directory_structure = service.walk_directory()
        """
        result: list[tuple[list[str], list[str]]] = []
        for path in self.folder.rglob("*"):
            if path.is_dir():
                dirnames = [p.name for p in path.iterdir() if p.is_dir()]
                filenames = [p.name for p in path.iterdir() if p.is_file()]
                result.append((dirnames, filenames))
        return result
