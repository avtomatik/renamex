#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:23:12 2024

@author: alexandermikhailov
"""

import filecmp
import os
import shutil
from hashlib import md5
from pathlib import Path

from core.config import PATH, PATH_CTR, PATH_TST

for file_name in os.listdir(PATH):
    if filecmp.cmp(
        PATH_CTR.joinpath(file_name),
        PATH_TST.joinpath(file_name),
        shallow=False
    ):
        PATH_TST.joinpath(file_name).unlink()
        shutil.move(
            PATH_CTR.joinpath(file_name),
            PATH_TST.joinpath(file_name),
        )

digests = list()
os.chdir(PATH)
for filename in ['project_2022-08-26.tar.gz', 'project_tar.gz']:
    with open(filename, 'rb') as f:
        digest = md5(f.read()).hexdigest()
        digests.append(digest)
print(digests[0] == digests[1])

comparison = filecmp.dircmp(PATH_CTR, PATH_TST)
comparison.report_full_closure()

count = []

for root, _, file_names in os.walk(
    (
        PATH
        .joinpath('production')
        .joinpath('egida_ptv')
        .joinpath('lib')
    )
):
    for file_name in file_names:
        count.append(Path(root).joinpath(file_name).is_file())

print(sum(count))

for (rt, _, fnames), (_rt, _, _fnames) in zip(
    os.walk(PATH.joinpath('production').joinpath(
        'egida_ptv').joinpath('lib')),
    os.walk(PATH.joinpath('web').joinpath(
        'egida_ptv').joinpath('lib'))
):
    for f, _f in zip(sorted(fnames), sorted(_fnames)):
        if filecmp.cmp(Path(rt).joinpath(f), Path(_rt).joinpath(_f)):
            Path(rt).joinpath(f).unlink()

for rt, _, fnames in os.walk(PATH.joinpath('production')):
    if not any(Path(rt).iterdir()):
        Path(rt).rmdir()
