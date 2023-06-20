import re
from pathlib import Path

from fileworks.tools.name_utils import transliterate_to_latin


def clean_string(string: str, fill: str = ' ') -> str:
    split_string = re.split(r'\W', string)
    return fill.join(part for part in split_string if part)


def generate_trimmed_file_name(file_path: Path) -> str:
    file_stem = file_path.stem
    trimmed_name = clean_string(file_stem, '_')
    file_suffix = file_path.suffix
    return f'{transliterate_to_latin(trimmed_name)}{file_suffix}'


class TrimFileNameTransformer:
    def transform(self, file_name: str) -> str:
        return generate_trimmed_file_name(Path(file_name))
