#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:37:25 2022

@author: green-machine
"""


from core.funcs import get_names_walk

PATH_SRC = '/home/green-machine/production'
PATH_EXP = '/home/green-machine/web'


file_names_l = get_names_walk(PATH_SRC)
file_names_r = get_names_walk(PATH_EXP)
print(file_names_r)
