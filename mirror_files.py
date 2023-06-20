
from core.constants import PREFIXES
from fileworks.tools.filters import get_file_names, get_filtered_file_names
from fileworks.tools.io_utils import (copy_files_to_destination,
                                      extract_file_names_from_text_file)


def mirror_files(path_from, path_to, FILE_NAME_L, FILE_NAME_R):
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = extract_file_names_from_text_file(FILE_NAME_L)
    file_names_r = extract_file_names_from_text_file(FILE_NAME_R)

    file_names_l = get_filtered_file_names(PREFIXES, path_from)
    file_names_r = get_filtered_file_names(PREFIXES, path_to)

    copy_files_to_destination(
        tuple(file_names_l - file_names_r), path_from, path_to)

    copy_files_to_destination(
        tuple(file_names_r - file_names_l), path_to, path_from)


def mirror_files(paths: tuple[str], file_names: tuple[str]) -> None:
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = extract_file_names_from_text_file(file_names[0])
    file_names_r = extract_file_names_from_text_file(file_names[1])

    copy_files_to_destination(tuple(file_names_l - file_names_r), *paths)

    copy_files_to_destination(tuple(file_names_r - file_names_l), *paths[::-1])


def mirror_files(path_from, path_to):
    # =========================================================================
    # TODO: Review the Logic
    # =========================================================================
    file_names_l = get_file_names(path_from)
    file_names_r = get_file_names(path_to)

    file_names_diff = set(
        filter(
            lambda _: not _.startswith(PREFIXES),
            file_names_l - file_names_r
        )
    )

    copy_files_to_destination(tuple(file_names_diff), path_from, path_to)

    file_names_diff = set(
        filter(
            lambda _: not _.startswith(PREFIXES),
            file_names_r - file_names_l
        )
    )

    copy_files_to_destination(tuple(file_names_diff), path_to, path_from)
