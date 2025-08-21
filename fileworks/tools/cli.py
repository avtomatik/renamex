import argparse
from pathlib import Path

from ..interfaces.adapters import FileMoverAdapter
from .cleaners import CyrillicToLatinTransliterator, RegexStringCleaner
from .filters import FileExtensionFilter, NullFileFilter
from .transformers import TrimFileNameTransformer


def main():
    parser = argparse.ArgumentParser(description='FileWorks CLI')
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to the directory to process (default: current directory)',
    )
    parser.add_argument(
        '-e',
        '--extensions',
        nargs='+',
        help='Filter files by extensions (space separated, e.g. -e csv txt)',
    )
    args = parser.parse_args()

    path = Path(args.path).resolve()

    file_filter = (
        FileExtensionFilter(tuple(args.extensions))
        if args.extensions
        else NullFileFilter()
    )

    cleaner = RegexStringCleaner(fill='_')
    transliterator = CyrillicToLatinTransliterator()
    transformer = TrimFileNameTransformer(cleaner, transliterator)
    mover = FileMoverAdapter(transformer)

    file_names = [f.name for f in path.iterdir() if file_filter.is_target(f)]

    mover.move_and_rename(path, path, file_names)
