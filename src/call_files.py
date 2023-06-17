#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from pathlib import Path, PosixPath

import pandas as pd
from pandas import DataFrame

PATH_SRC = '/home/green-machine/source'

PATH_EXP = '/home/green-machine/Downloads'

FILE_NAME = 'files_check.txt'

FILEPATH = Path(PATH_EXP).joinpath(FILE_NAME)


def read(filepath: PosixPath) -> DataFrame:
    kwargs = {
        'filepath_or_buffer': filepath,
        'names': ['time_stamp', 'wb_name', 'status'],
        'sep': '\t'
    }
    return pd.read_csv(**kwargs)


def mark_df(df: DataFrame) -> DataFrame:
    df['backed_up'] = False
    df['file_size'] = 0
    return df


if __name__ == '__main__':
    df = read(FILEPATH).pipe(mark_df)
    for _ in range(df.shape[0]):
        try:
            filepath = Path(PATH_SRC).joinpath(df.iloc[_, 1])
            df.iloc[_, -2] = filepath.is_file()
            df.iloc[_, -1] = os.stat(filepath).st_size
        except:
            pass

    FILE_NAME = 'files_check_report.xlsx'

    kwargs = {
        'excel_writer': Path(PATH_EXP).joinpath(FILE_NAME),
        'index': False
    }
    df.to_excel(**kwargs)
