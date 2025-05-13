import re


def convert_strings_to_snake_case(strings: tuple[str]) -> dict[str, str]:
    return {
        string: re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
        for string in strings
    }
