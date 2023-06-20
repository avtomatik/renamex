#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:15:02 2023

@author: alexandermikhailov
"""


import filecmp
from datetime import datetime
from itertools import product
from pathlib import Path

from core.config import PATH_CTR, PATH_DST, PATH_SRC, PATH_TST


def get_creation_time(file_path: Path) -> datetime:
    return datetime.fromtimestamp(file_path.stat().st_ctime)


def copy_file(src: Path, dst: Path):
    dst.write_bytes(src.read_bytes())
    dst.chmod(src.stat().st_mode)
    dst.utime((src.stat().st_atime, src.stat().st_mtime))


for file_name in sorted(set(PATH_CTR.glob('*')) ^ set(PATH_TST.glob('*'))):
    file_ctrl = PATH_CTR / file_name
    file_test = PATH_TST / file_name
    file_dst = PATH_DST / file_name

    if file_ctrl.is_file():
        if get_creation_time(file_ctrl) <= get_creation_time(file_test):
            copy_file(file_ctrl, file_dst)
        else:
            copy_file(file_test, file_dst)
        file_ctrl.unlink()
        file_test.unlink()


file_names_src = [file.name for file in PATH_SRC.iterdir() if file.is_file()]


file_names_dst = [file.name for file in PATH_DST.iterdir() if file.is_file()]


for file_src, file_dst in product(file_names_src, file_names_dst):
    src_file = PATH_SRC / file_src
    file_dst = PATH_DST / file_dst
    if filecmp.cmp(src_file, file_dst, shallow=False):
        src_file.unlink()
        print(f'Deleted {src_file} as it matches {file_dst}')
