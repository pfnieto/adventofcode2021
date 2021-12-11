# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:31:47 2021

@author: Pablo
"""

def read_input(filename):
    values = []
    with open(filename) as f:
        for line in f:
            values.append([int(x) for x in line.strip()])
    return values

def reset(values):
    count = 0
    for y in range(len(values)):
        for x in range(len(values)):
            if values[y][x] >= 10:
                count += 1
                values[y][x] = 0
    return count

def travel_path(x, y, values):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x + i < 0 or x + i >= len(values[0]) or y + j < 0 or y + j >= len(values)):
                continue
            values[y + j][x + i] += 1
            if values[y + j][x + i] == 10:
                travel_path(x + i, y + j, values)

def next_step(values):
    for y in range(len(values)):
        for x in range(len(values)):
            values[y][x] += 1
            if values[y][x] == 10:
                travel_path(x, y, values)

values = read_input("input 11.txt")
count = 0
for step in range(1000):
    next_step(values)
    flashes = reset(values)
    if flashes == (len(values) * len(values[0])):
        break
    count += flashes