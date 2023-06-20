from typing import Protocol


class FileNameTransformer(Protocol):
    def transform(self, file_name: str) -> str:
        ...


class Logger(Protocol):
    def log(self, entries: list[dict]) -> None:
        ...
