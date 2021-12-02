# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:01:38 2021

@author: Pablo
"""

values = []
with open("input 1-1.txt") as f:
    values = f.readlines()
values = list(map(lambda x: int(x.strip()), values))

inc = 0
dec = 0
prev = None
for item in values:
    if prev == None:
        prev = item
        continue
    if item > prev:
        inc += 1
    if item < prev:
        dec += 1
    prev = item