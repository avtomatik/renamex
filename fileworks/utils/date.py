from datetime import datetime
from pathlib import Path


def get_creation_time(file_path: Path) -> datetime:
    """
    Returns the creation time of the file at the given path.

    :param file_path: Path to the file
    :return: Creation time of the file as a datetime object
    """
    return datetime.fromtimestamp(file_path.stat().st_ctime)


def generate_log_filename(
    prefix: str = 'log',
    timestamp: datetime = None
) -> str:
    """
    Generates a timestamped log filename.

    :param prefix: Prefix for the log filename
    :param timestamp: Optional datetime object; if None, uses current time
    :return: Formatted log filename string
    """
    if timestamp is None:
        timestamp = datetime.now()
    return f'{prefix}_{timestamp:%Y-%m-%d_%H-%M-%S}.json'
