import filecmp
from hashlib import md5

from ..core.config import PATH, PATH_CTR, PATH_TST


def compare_file_digests_in_directory():
    # Function to calculate and compare digests of two files
    file_digests = []
    for archive_filename in ['project_2022-08-26.tar.gz', 'project_tar.gz']:
        archive_path = PATH.joinpath(archive_filename)
        with open(archive_path, 'rb') as archive_file:
            file_digest = md5(archive_file.read()).hexdigest()
            file_digests.append(file_digest)

    print(file_digests[0] == file_digests[1])


def compare_directories_and_report():
    # Function to compare directories and print the full closure report
    directory_comparison = filecmp.dircmp(PATH_CTR, PATH_TST)
    directory_comparison.report_full_closure()
