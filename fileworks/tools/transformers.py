from pathlib import Path

from ..interfaces.protocols import StringCleaner, Transliterator


class TrimFileNameTransformer:
    def __init__(self, cleaner: StringCleaner, transliterator: Transliterator):
        self.cleaner = cleaner
        self.transliterator = transliterator

    def transform(self, file_name: str) -> str:
        path = Path(file_name)
        cleaned_name = self.cleaner.clean(path.stem)
        transliterated = self.transliterator.transliterate(cleaned_name)
        return f'{transliterated}{path.suffix}'
