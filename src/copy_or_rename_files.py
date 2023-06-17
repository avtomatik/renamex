#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:06:20 2022

@author: Alexander Mikhailov
"""

import os

from core.funcs import copy_rename_files

if __name__ == '__main__':
    paths = ()

    PATH_SRC = '/home/green-machine/Downloads'

    MATCHERS = ['.csv']

    FLAG = ''

    file_names = tuple(filter(lambda _: FLAG in _, os.listdir(PATH_SRC)))

    kwargs = {
        'path_from': PATH_SRC,
        'path_to': PATH_SRC,
        'file_names': file_names,
    }

    copy_rename_files(**kwargs)
