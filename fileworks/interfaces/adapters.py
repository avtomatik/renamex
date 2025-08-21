from pathlib import Path

from ..tools.movers import FileMoverRenamer
from ..tools.transformers import TrimFileNameTransformer
from .protocols import FileTransformer


class TrimFileNameTransformerAdapter:
    """Adapter to make TrimFileNameTransformer compatible with FileTransformer
    protocol."""

    def __init__(self, transformer: TrimFileNameTransformer):
        self.transformer = transformer

    def transform(self, file_name: str) -> str:
        return self.transformer.transform(file_name)


class FileMoverAdapter:
    """Adapter to wrap FileMoverRenamer with the required transformer."""

    def __init__(self, transformer: FileTransformer):
        self.transformer = transformer

    def move_and_rename(
        self,
        src_dir: Path,
        dst_dir: Path,
        file_names: list[str]
    ) -> None:
        mover = FileMoverRenamer(self.transformer)
        mover.move_and_rename(src_dir, dst_dir, file_names)
