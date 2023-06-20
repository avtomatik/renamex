import json
from pathlib import Path


class JsonFileLogger:
    def __init__(self, log_path: Path):
        self.log_path = log_path

    def log(self, entries: list[dict]) -> None:
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open('w', encoding='utf-8') as f:
            json.dump(entries, f, ensure_ascii=False, indent=4)
        print(f'Renamed and Moved {len(entries)} Files')


class NullLogger:
    def log(self, entries: list[dict]) -> None:
        pass
