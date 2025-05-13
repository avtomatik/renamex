import re

from ..core.constants import CYRILLIC_TO_LATIN


class RegexStringCleaner:
    def __init__(self, fill: str = '_'):
        self.fill = fill
        self.pattern = rf'[\W{re.escape(fill)}]+'

    def clean(self, text: str) -> str:
        parts = [
            part for part in re.split(self.pattern, text.strip()) if part
        ]
        return self.fill.join(parts).strip(self.fill)


class CyrillicToLatinTransliterator:
    def __init__(self, mapping: dict[str, str] = CYRILLIC_TO_LATIN):
        self.mapping = mapping

    def transliterate(self, text: str) -> str:
        return ''.join(self.mapping.get(char, char) for char in text.lower())
