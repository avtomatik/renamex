#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import csv
from pathlib import Path
from typing import Dict, List

from ..core.config import PATH


class FileReader:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read(self) -> List[Dict[str, str]]:
        with self.file_path.open(newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            return [row for row in reader]


class FileProcessor:
    def __init__(self, base_path: Path):
        self.base_path = base_path

    def process(self, rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        for row in rows:
            wb_name = row['wb_name']
            full_path = self.base_path / wb_name
            backed_up = full_path.exists() and full_path.is_file()
            file_size = full_path.stat().st_size if backed_up else 0
            row['backed_up'] = backed_up
            row['file_size'] = file_size
        return rows


class ReportWriter:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def write(self, rows: List[Dict[str, str]], fieldnames: List[str]):
        mode = 'a' if self.file_path.exists() else 'w'
        with self.file_path.open(mode, newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerows(rows)


def main():
    base_path = PATH
    input_file = base_path / 'files_check.txt'
    output_file = base_path / 'files_check_report.csv'
    fieldnames = ['time_stamp', 'wb_name', 'status', 'backed_up', 'file_size']

    reader = FileReader(input_file)
    rows = reader.read()

    processor = FileProcessor(base_path)
    processed_rows = processor.process(rows)

    writer = ReportWriter(output_file)
    writer.write(processed_rows, fieldnames)


if __name__ == '__main__':
    main()
