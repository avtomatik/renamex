from pathlib import Path


def count_files_in_directory(directory_path: Path):
    # Function to count the number of files in a specific directory
    return sum(file.is_file() for file in directory_path.rglob('*'))
