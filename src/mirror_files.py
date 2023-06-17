import shutil
from pathlib import Path

from core.constants import PREFIXES
from core.funcs import (get_file_names_filter, get_file_names_set,
                        get_set_from_text_file)


def mirror_files(PATH_SRC, PATH_EXP, FILE_NAME_L, FILE_NAME_R):
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = get_set_from_text_file(FILE_NAME_L)
    file_names_r = get_set_from_text_file(FILE_NAME_R)

    file_names_l = get_file_names_filter(PREFIXES, PATH_SRC)
    file_names_r = get_file_names_filter(PREFIXES, PATH_EXP)

    for file_name in file_names_l - file_names_r:
        shutil.copy2(
            Path(PATH_SRC).joinpath(file_name),
            Path(PATH_EXP).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_SRC} to {PATH_EXP}')

    for file_name in file_names_r - file_names_l:
        shutil.copy2(
            Path(PATH_EXP).joinpath(file_name),
            Path(PATH_SRC).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_EXP} to {PATH_SRC}')


def mirror_files(PATH_SRC, PATH_EXP):
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = get_file_names_set(PATH_SRC)
    file_names_r = get_file_names_set(PATH_EXP)

    file_names_diff = set(
        filter(
            lambda _: not _.startswith(PREFIXES),
            file_names_l - file_names_r
        )
    )

    for file_name in file_names_diff:
        shutil.copy2(
            Path(PATH_SRC).joinpath(file_name),
            Path(PATH_EXP).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_SRC} to {PATH_EXP}')

    file_names_diff = set(
        filter(
            lambda _: not _.startswith(PREFIXES),
            file_names_r - file_names_l
        )
    )

    for file_name in file_names_diff:
        shutil.copy2(
            Path(PATH_EXP).joinpath(file_name),
            Path(PATH_SRC).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {PATH_EXP} to {PATH_SRC}')


def mirror_files(paths: tuple[str], file_names: tuple[str]) -> None:
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = get_set_from_text_file(file_names[0])
    file_names_r = get_set_from_text_file(file_names[1])

    for file_name in file_names_l - file_names_r:
        shutil.copy2(
            Path(paths[0]).joinpath(file_name),
            Path(paths[1]).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {paths[0]} to {paths[1]}')

    for file_name in file_names_r - file_names_l:
        shutil.copy2(
            Path(paths[1]).joinpath(file_name),
            Path(paths[0]).joinpath(file_name)
        )
        print(f'Copied <{file_name}> from {paths[1]} to {paths[0]}')
