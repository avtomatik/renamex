#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:56:25 2020

@author: Alexander Mikhailov
"""

from core.config import PATH_DST, PATH_SRC

# =============================================================================
# Script to Back-Up Empty Files from One Drive to Another
# =============================================================================

RESERVED = {'FOUND.000', 'System Volume Information'}
empty_file_names = [
    f.name
    for f in PATH_DST.iterdir()
    if f.is_file() and f.stat().st_size == 0 and f.name not in RESERVED
]

for filename in empty_file_names:
    file_name_src = PATH_SRC / filename
    file_name_dst = PATH_DST / filename

    if file_name_src.exists() and file_name_src.is_file():
        file_name_dst.write_bytes(file_name_src.read_bytes())
        print(f'Copied <{filename}> from {PATH_SRC} to {PATH_DST}')
