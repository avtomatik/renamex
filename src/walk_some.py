import os
import shutil
from pathlib import Path

from core.constants import PREFIXES

PATH_SRC = '/media/green-machine/Transcend'
PATH_EXP = '/home/green-machine/Downloads'
SUFFIX = ''
SUFFIX = '.py'


for root, _, file_names in os.walk(PATH_SRC):
    for file_name in file_names:

        _file_name = ''

        if file_name.endswith(SUFFIX) and not file_name.startswith(PREFIXES):
            print(Path(root).joinpath(file_name))
            shutil.copy2(
                Path(root).joinpath(file_name),
                Path(PATH_SRC).joinpath(file_name)
            )

        if not Path(PATH_EXP).joinpath(_file_name).exists():
            shutil.move(
                Path(root).joinpath(file_name),
                Path(PATH_EXP).joinpath(_file_name)
            )
