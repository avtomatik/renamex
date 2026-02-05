from pathlib import Path
from typing import Iterable

from fileworks.interfaces.protocols import FileNameTransformer, Logger
from fileworks.tools.loggers import NullLogger


class FileMoverRenamer:
    """
    Moves and renames files in a directory using a transformer, with optional
    logging and verbose output.
    """

    def __init__(
        self, transformer: FileNameTransformer, logger: Logger | None = None
    ):
        self.transformer = transformer
        self.logger = logger or NullLogger()  # Fallback if no logger provided

    def move_and_rename(
        self,
        src_dir: Path,
        dst_dir: Path,
        file_names: Iterable[str],
        verbose: bool = False,
    ) -> None:
        logs: list[dict[str, str]] = []

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

            logs.append({"src": file_name, "dst": new_name})

            if verbose:
                print(f"Renaming '{file_name}' >> '{new_name}'")

        if logs:
            self.logger.log(logs)
        else:
            print("No Files Were Renamed")
