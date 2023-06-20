from pathlib import Path

from core.config import PATH
from fileworks.mover.mover import FileMoverRenamer
from fileworks.tools.transformers import TrimFileNameTransformer

MATCHERS = ('.csv',)
MATCHERS = ('',)


def is_target(f: Path, matchers: tuple[str], flag: str = '') -> bool:
    return flag in f.name and f.suffix in matchers


if __name__ == '__main__':
    file_names = tuple(
        f.name for f in PATH.iterdir() if is_target(f, MATCHERS)
    )

    file_names = tuple(f.name for f in PATH.iterdir())

    file_transformer = TrimFileNameTransformer()
    mover = FileMoverRenamer(file_transformer)  # No logger passed
    mover.move_and_rename(PATH, PATH, file_names)
