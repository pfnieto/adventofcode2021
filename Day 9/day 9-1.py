# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:52:02 2021

@author: Pablo
"""

def read_input(filename):
    values = []
    with open(filename) as f:
        for line in f:
            values.append([10] + [int(x) for x in line.strip()] + [10])
        values.append([10] * len(values[0]))
        values.insert(0, [10] * len(values[0]))
        return values
    
def find_minimums(values):
    mins = []
    for y in range(1, len(values) - 1):
        for x in range(1, len(values[y]) - 1):
            current = values[y][x]
            if (values[y][x - 1] > current and values[y - 1][x] > current):
                if (values[y][x + 1] > current and values[y + 1][x] > current):
                    mins.append(current + 1)
    return mins
            

values = read_input("example.txt")
minimums = find_minimums(values)
output = sum(minimums)