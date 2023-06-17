

import os

from core.constants import PATH
from core.funcs import delete_files, move_files, rename_files

FILE_NAMES = ['test.py']
FILE_NAMES = [
    'incompleteDFT.py',
    'incompleteDataFusionUSACostIndex.py',
    'incompleteUSABLSV.py'
    'incompletedataFetchCAN.py',
]
FILE_NAMES = ['project.py', 'datafetch.py', 'tools.py', 'test.py']
FILE_NAMES = [
    'Reference EN Cobb C.W., Douglas P.H. A Theory of Production.pdf',
    'Reference EN Douglas P.H. The Theory of Wages.pdf',
    'Reference EN Kendrick J.W. Productivity Trends in the United States c2246.pdf',
    'Reference EN Kendrick J.W. Productivity Trends in the United States c2249.pdf',
    'Reference RU Brown M. 0597_088.pdf',
    'Reference RU Brown M. 0597_099.pdf',
    'Reference RU Kurenkov Yu.V. Proizvodstvennye moshchnost v promyshlennosti glavnykh kapitalisticheskikh stran.pdf'
]

delete_files(FILE_NAMES, PATH)


rename_files(FILE_NAMES, PATH)


move_files(FILE_NAMES)


if os.getcwd() == PATH:
    for file_name in FILE_NAMES:
        os.unlink(file_name)
