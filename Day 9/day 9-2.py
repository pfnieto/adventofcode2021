# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:27:24 2021

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
                    mins.append({"x": x, "y": y})
    return mins

def basin_size(values, coords, visited, movements):
    if values[coords["y"]][coords["x"]] in (9, 10):
        return 0
    if (coords["x"], coords["y"]) in visited:
        return 0
    visited[(coords["x"], coords["y"])] = 1
    count = 1
    for adj in movements:
        nextm = {"x": coords["x"] + adj["x"], "y": coords["y"] + adj["y"]}
        if values[nextm["y"]][nextm["x"]] - values[coords["y"]][coords["x"]] > 0:
            count += basin_size(values, nextm, visited, movements)
    return count
            

values = read_input("input 9.txt")
minimums = find_minimums(values)
movements = [{"x": 1, "y": 0}, {"x": 0, "y": 1}, {"x": -1, "y": 0}, {"x": 0, "y": -1}]
visited = {}
sizes = []
for coords in minimums:
    sizes.append(basin_size(values, coords, visited, movements))
ordered = sorted(sizes, reverse=True)
output = ordered[0]*ordered[1]*ordered[2]