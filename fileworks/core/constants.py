CYRILLIC_TO_LATIN_LIST = [
    'a',
    'b',
    'v',
    'g',
    'd',
    'e',
    'zh',
    'z',
    'i',
    'y',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'r',
    's',
    't',
    'u',
    'f',
    'kh',
    'ts',
    'ch',
    'sh',
    'shch',
    '',
    'y',
    '',
    'e',
    'yu',
    'ya',
    'yo'
]

CYRILLIC_TO_LATIN = {
    chr(1072 + i): latin for i, latin in enumerate(CYRILLIC_TO_LATIN_LIST)
}

# Explicitly map 'ё' (Unicode 1105) if needed
CYRILLIC_TO_LATIN['ё'] = 'yo'


PREFIXES = {'.', '_', '~'}

RESERVED = {'FOUND.000', 'System Volume Information'}
