import filecmp
from itertools import product
from pathlib import Path

from ..core.config import PATH, PATH_CTR, PATH_DST, PATH_SRC, PATH_TST
from ..tools.filters import FileService
from .date import get_creation_time


def copy_files_to_destination(file_names: tuple[str], path_src: Path, path_dst: Path) -> None:
    for file_name in file_names:
        file_path_src = path_src / file_name
        file_path_dst = path_dst / file_name

        file_path_dst.parent.mkdir(parents=True, exist_ok=True)
        with file_path_src.open('rb') as fsrc, file_path_dst.open('wb') as fdst:
            fdst.write(fsrc.read())

        print(f'Copied <{file_name}> from {path_src} to {path_dst}')


def move_files_to_destination(file_names: tuple[str], path_src: Path, path_dst: Path) -> None:
    path_dst.mkdir(parents=True, exist_ok=True)

    for file_name in file_names:
        src = path_src / file_name
        dst = path_dst / file_name

        src.rename(dst)
        print(f'Moved <{file_name}> from {path_src} to {path_dst}')


def rename_files_based_on_mapping(mapping: dict[str, str], path: Path) -> None:
    for src, dst in mapping.items():
        src_path = path / src
        dst_path = path / dst
        src_path.rename(dst_path)

    print(f'{path}: Done')


def delete_files(file_names: tuple[str], path: Path) -> None:

    for file_name in file_names:
        path.joinpath(file_name).unlink()

    print(f'{path}: Done')


def move_and_replace_files_in_directories():
    # Function to move and replace files between directories
    for file in PATH.iterdir():
        source_file = PATH_CTR.joinpath(file.name)
        destination_file = PATH_TST.joinpath(file.name)

        if filecmp.cmp(source_file, destination_file, shallow=False):
            destination_file.unlink()  # Remove the existing file
            file.rename(destination_file)  # Rename (move) the file


def copy_empty_files(file_names: list, src_path: Path, dst_path: Path) -> None:
    """
    Copy empty files from source to destination if they exist.

    :param file_names: List of file names to copy.
    :param src_path: Path to the source directory.
    :param dst_path: Path to the destination directory.
    """
    for filename in file_names:
        src_file = src_path / filename
        dst_file = dst_path / filename

        if src_file.exists() and src_file.is_file():
            dst_file.write_bytes(src_file.read_bytes())
            print(f'Copied <{filename}> from {src_path} to {dst_path}')


def backup_files(PATH_SRC: Path, PATH_DST: Path, PREFIXES: set, SUFFIX: str) -> None:
    """
    Backup files from the source directory to the destination directory based on specific conditions.

    :param PATH_SRC: Path to the source directory.
    :param PATH_DST: Path to the destination directory.
    :param PREFIXES: Set of file name prefixes to exclude.
    :param SUFFIX: File suffix (e.g., '.py') to filter the files by.
    """
    for path in PATH_SRC.rglob('*'):
        if not path.is_file():
            continue

        file_name = path.name
        file_name_dst = PATH_SRC / file_name

        # Copy to PATH_SRC if valid (ends with SUFFIX and does not start with a prefix)
        if file_name.endswith(SUFFIX) and not file_name.startswith(tuple(PREFIXES)):
            file_name_dst.write_bytes(path.read_bytes())
        # Copy to PATH_DST if not already present
        file_name_dst = PATH_DST / file_name
        if not file_name_dst.exists():
            file_name_dst.write_bytes(path.read_bytes())
            path.unlink()


def delete_matching_files():
    """
    Deletes files from the source path if they have a matching file in the destination path.
    """
    service = FileService(PATH_SRC)
    source_file_names = service.list_all_file_names()
    service = FileService(PATH_DST)
    destination_file_names = service.list_all_file_names()

    for source_file, destination_file in product(source_file_names, destination_file_names):
        source_path = PATH_SRC / source_file
        destination_path = PATH_DST / destination_file

        if filecmp.cmp(source_path, destination_path, shallow=False):
            source_path.unlink()  # Delete matching file from source
            print(f'Deleted {source_path} as it matches {destination_path}')


def copy_file(src: Path, dst: Path):
    """
    Copies the file from the source path to the destination path, preserving file metadata.

    :param src: Source file path
    :param dst: Destination file path
    """
    # Read content from source and write to destination
    dst.write_bytes(src.read_bytes())

    # Copy file permissions
    dst.chmod(src.stat().st_mode)

    # Copy access and modification times
    dst.utime((src.stat().st_atime, src.stat().st_mtime))


def sync_files_from_control_to_destination():
    """
    Synchronize files between the control path and the test path by copying the latest file
    (based on creation time) to the destination and removing files from the source and test path.
    """
    for file_name in sorted(set(PATH_CTR.glob('*')) ^ set(PATH_TST.glob('*'))):
        control_file = PATH_CTR / file_name
        test_file = PATH_TST / file_name
        destination_file = PATH_DST / file_name
        if control_file.is_file():
            if get_creation_time(control_file) <= get_creation_time(test_file):
                copy_file(test_file, destination_file)
            else:
                copy_file(control_file, destination_file)

            control_file.unlink()  # Delete the original file from the control path
            test_file.unlink()  # Delete the original file from the test path


def remove_empty_directories_in_directory():
    # Function to remove empty directories
    for directory in (PATH / 'production').rglob('*'):
        if not any(directory.iterdir()):  # Check if the directory is empty
            directory.rmdir()  # Remove the empty directory


# =============================================================================
# def remove_matching_files_between_directories():
#     # Function to compare files between two directories and remove matching ones
#     for source_root, _, source_files in zip(
#         (PATH / 'production' / 'egida_ptv' / 'lib').rglob('*'),
#         (PATH / 'web' / 'egida_ptv' / 'lib').rglob('*')
#     ):
#         for source_file, destination_file in zip(sorted(source_files), sorted(file_names)):
#             if filecmp.cmp(source_root / source_file, root / destination_file):
#                 (source_root / source_file).unlink()  # Remove matching file
# =============================================================================
