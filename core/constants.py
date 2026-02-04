from typing import Final

# =============================================================================
# Cyrillic >> Latin transliteration
# =============================================================================

CYRILLIC_TO_LATIN_LIST: Final = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "zh",
    "z",
    "i",
    "y",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "kh",
    "ts",
    "ch",
    "sh",
    "shch",
    "",
    "y",
    "",
    "e",
    "yu",
    "ya",
    "yo",
)

CYRILLIC_TO_LATIN: Final = {
    chr(1072 + i): latin for i, latin in enumerate(CYRILLIC_TO_LATIN_LIST)
}

# Explicitly map 'ё' (Unicode 1105) if needed
CYRILLIC_TO_LATIN["ё"] = "yo"


# =============================================================================
# File / Path constants
# =============================================================================
PREFIXES: Final = frozenset({".", "_", "~"})

RESERVED: Final = frozenset({"FOUND.000", "System Volume Information"})
