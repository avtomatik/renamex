from datetime import datetime
from pathlib import Path


class LogFilenameFactory:
    """
    Generates timestamped log filenames.

    Example:
        factory = LogFilenameFactory(prefix="run", ext="txt")
        factory()  # run_2025-08-21_12-34-56.txt
    """

    def __init__(
        self,
        prefix: str = 'log',
        ext: str = 'json',
        fmt: str = '%Y-%m-%d_%H-%M-%S'
    ):
        self.prefix = prefix
        self.ext = ext
        self.fmt = fmt

    def __call__(self, timestamp: datetime | None = None) -> Path:
        timestamp = timestamp or datetime.now()
        filename = f'{self.prefix}_{timestamp:{self.fmt}}.{self.ext}'
        return Path(filename)
