#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# =============================================================================
# TODO: Edit This
# =============================================================================
import os

import pandas as pd
from core.constants import FILE_NAME_L, FILE_NAME_R, PATH_EXP, PATH_SRC
from core.funcs import trim_file_name
from pandas import DataFrame

from file_system.src.core.funcs import get_string_from_file

FILE_NAME = 'file_names.xlsx'
file_names_d = get_string_from_file(FILE_NAME_L)

file_names_e = get_string_from_file(FILE_NAME_R)

pd.concat(
    [
        DataFrame(data={'file_names_d': file_names_d}),
        DataFrame(data={'file_names_e': file_names_e})
    ],
    axis=0
).to_excel(FILE_NAME)

# =============================================================================
# Iteration
# =============================================================================
for file_name in tuple(os.listdir()):
    os.rename(
        file_name,
        trim_file_name(file_name)
    )

df = pd.read_excel(FILE_NAME)
df.columns = ('file_names_d', 'file_names_e', 'status')
df.fillna('None', inplace=True)
df.to_excel(FILE_NAME)

# =============================================================================
# Iteration
# =============================================================================
df = pd.read_excel(FILE_NAME)
df = df[df.iloc[:, 2] == 'None'][df.columns[[1, 0]]]
MAP_RENAMING = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))

# =============================================================================
# Iteration
# =============================================================================

for file_name in MAP_RENAMING.keys():
    try:
        os.rename(
            file_name,
            trim_file_name(file_name)
        )
    except:
        pass

for _ in range(df.shape[0]):
    if df.iloc[_, 0] == f'{PATH_EXP} TO {PATH_SRC}':
        print(f'{df.iloc[_, 1][3:]} {df.iloc[_, 2][3:]}')
        try:
            os.rename(df.iloc[_, 1][3:], df.iloc[_, 2][3:])
        except:
            pass
    elif df.iloc[_, 0] == f'{PATH_SRC} TO {PATH_EXP}':
        print(f'{df.iloc[_, 2]} {df.iloc[_, 1]}')
