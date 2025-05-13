from pathlib import Path
from typing import Protocol


class FileNameTransformer(Protocol):
    def transform(self, file_name: str) -> str:
        ...


class Logger(Protocol):
    def log(self, entries: list[dict]) -> None:
        ...


class FileTransformer(Protocol):
    def transform(self, file_name: str) -> str:
        ...


class FileMover(Protocol):
    def move_and_rename(
        self,
        src_dir: Path,
        dst_dir: Path,
        file_names: list[str]
    ) -> None:
        ...


class MatchFileFilter(Protocol):
    def matches(self, file: Path) -> bool:
        ...


class TargetFileFilter(Protocol):
    def is_target(self, file: Path) -> bool:
        ...


# ==========================
# Protocols (Interfaces)
# ==========================


class StringCleaner(Protocol):
    def clean(self, string: str) -> str:
        ...


class Transliterator(Protocol):
    def transliterate(self, text: str) -> str:
        ...
