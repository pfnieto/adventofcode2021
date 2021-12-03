# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:33:08 2021

@author: Pablo
"""

def read_input(filename):
    values = []
    with open(filename) as f:
        for line in f:
            values.append(line.strip())             
    return values

def reduce(values, position, option):
    if len(values) == 1:
        return values[0]
    count = sum(list(map(lambda x: int(x[position]), values)))
    if count >= len(values)/2:
        return reduce(list(filter(lambda x: int(x[position]) == option, values)), position + 1, option)
    return reduce(list(filter(lambda x: int(x[position]) != option, values)), position + 1, option)

values = read_input("input 3.txt")
oxygen = reduce(values, 0, 1)
c02 = reduce(values, 0, 0)
output = int(oxygen, 2) * int(c02, 2)