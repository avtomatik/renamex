from core.config import PATH_DST, PATH_SRC
from core.constants import PREFIXES

SUFFIX = '.py'

for path in PATH_SRC.rglob('*'):
    if path.is_file():
        file_name = path.name

        if file_name.endswith(SUFFIX) and not file_name.startswith(tuple(PREFIXES)):
            file_name_dst = PATH_SRC / file_name
            file_name_dst.write_bytes(path.read_bytes())

        file_name_dst = PATH_DST / file_name
        if not file_name_dst.exists():
            file_name_dst.write_bytes(path.read_bytes())
            path.unlink()
