from pathlib import Path
from typing import Iterable, Optional

from ..interfaces.protocols import FileNameTransformer, Logger
from .loggers import NullLogger


class FileMoverRenamer:
    def __init__(
        self,
        transformer: FileNameTransformer,
        logger: Optional[Logger] = None
    ):
        self.transformer = transformer
        self.logger = logger or NullLogger()  # Fallback to NullLogger

    def move_and_rename(
        self,
        src_dir: Path,
        dst_dir: Path,
        file_names: Iterable[str]
    ) -> None:
        logs = []

        for file_name in file_names:
            src_path = src_dir / file_name
            if not src_path.exists():
                continue

            new_name = self.transformer.transform(file_name)

            if file_name == new_name:
                continue

            dst_path = dst_dir / new_name
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            src_path.rename(dst_path)

            logs.append({'src': file_name, 'dst': new_name})

        if logs:
            self.logger.log(logs)
        else:
            print('No Files Were Renamed')
