# =============================================================================
# Separate Procedure
# =============================================================================

import shutil
from pathlib import Path


def incoherent_undefined():
    PATH_SRC = '/home/green-machine/source'

    PATH_EXP = '/media/green-machine/KINGSTON'

    FILE_NAME = 'pricesInverse.xlsm'

    shutil.copy2(
        Path(PATH_SRC).joinpath(FILE_NAME),
        Path(PATH_EXP).joinpath(FILE_NAME)
    )

    shutil.move(
        Path(PATH_SRC).joinpath(FILE_NAME),
        Path(PATH_EXP).joinpath(FILE_NAME)
    )
