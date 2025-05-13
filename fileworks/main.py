import argparse
from pathlib import Path

from .interfaces.adapters import FileMoverAdapter
from .tools.cleaners import CyrillicToLatinTransliterator, RegexStringCleaner
from .tools.filters import FileExtensionFilter, NullFileFilter
from .tools.transformers import TrimFileNameTransformer


def main():
    parser = argparse.ArgumentParser(description='FileWorks CLI')
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to the directory to process (default: current directory)'
    )
    parser.add_argument(
        '-e', '--extensions',
        nargs='+',
        help='Filter files by extensions (space separated, e.g. -e csv txt)'
    )
    args = parser.parse_args()

    PATH = Path(args.path).resolve()

    if args.extensions:
        file_filter = FileExtensionFilter(tuple(args.extensions))
    else:
        file_filter = NullFileFilter()

    cleaner = RegexStringCleaner(fill='_')
    transliterator = CyrillicToLatinTransliterator()
    transformer = TrimFileNameTransformer(cleaner, transliterator)
    mover = FileMoverAdapter(transformer)

    file_names = [
        f.name for f in PATH.iterdir()
        if file_filter.is_target(f)
    ]

    mover.move_and_rename(PATH, PATH, file_names)


if __name__ == '__main__':
    main()
