import argparse
from pathlib import Path

from fileworks.interfaces.adapters import FileMoverAdapter
from fileworks.tools.cleaners import (
    CyrillicToLatinTransliterator,
    RegexStringCleaner,
)
from fileworks.tools.filters import FileExtensionFilter, NullFileFilter
from fileworks.tools.transformers import TrimFileNameTransformer


def main():
    parser = argparse.ArgumentParser(
        description="FileWorks CLI: Move and rename files in a directory."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the directory in process (default: current directory)",
    )
    parser.add_argument(
        "-e",
        "--extensions",
        nargs="+",
        help="Filter files by extensions (space separated, e.g. -e csv txt)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help=(
            "Enable verbose output, printing details of files being processed"
        ),
    )

    args = parser.parse_args()

    path = Path(args.path).resolve()

    if not path.is_dir():
        print(f"Error: {args.path} is not a valid directory.")
        exit(1)

    file_filter = (
        FileExtensionFilter(tuple(args.extensions))
        if args.extensions
        else NullFileFilter()
    )

    cleaner = RegexStringCleaner(fill="_")
    transliterator = CyrillicToLatinTransliterator()
    transformer = TrimFileNameTransformer(cleaner, transliterator)
    mover = FileMoverAdapter(transformer)

    file_names = [f.name for f in path.iterdir() if file_filter.is_target(f)]

    if file_names:
        mover.move_and_rename(path, path, file_names, verbose=args.verbose)
        print(f"Processed {len(file_names)} file(s).")
    else:
        print("No files matched the specified criteria.")
