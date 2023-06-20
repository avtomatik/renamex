import re

from core.constants import MAP_CYRILLIC_TO_LATIN


def transliterate_to_latin(word: str, mapping: dict[str, str] = MAP_CYRILLIC_TO_LATIN) -> str:
    return ''.join(mapping.get(char, char) for char in word.lower())


def convert_strings_to_snake_case(strings: tuple[str]) -> dict[str, str]:
    return {
        string: re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
        for string in strings
    }
