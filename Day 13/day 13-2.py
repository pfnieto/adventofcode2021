# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:27:50 2021

@author: Pablo
"""

def read_input(filename):
    coords = set()
    folds = []
    order = {"x": 0, "y": 1}
    with open(filename) as f:
        for line in f:
            if "," in line:
                x, y = line.strip().split(",")
                coords.add((int(x), int(y)))
                continue
            if line.startswith("fold"):
                instruction, position = line.strip().split("=")
                folds.append({"axis": order[instruction[-1]], "position": int(position)})
    return coords, folds

def fold(coords, folds):
    if len(folds) == 0:
        return coords
    current = folds.pop(0)
    folded = set()
    for coord in coords:
        if coord[current["axis"]] <= current["position"]:
            folded.add(coord)
        else:
            newc = [*coord]
            newc[current["axis"]] = newc[current["axis"]] - 2 * abs(newc[current["axis"]] - current["position"])
            folded.add(tuple(newc))
    return fold(folded, folds)
        
        
coords, folds = read_input("input 13.txt")
output = fold(coords, folds)
# display
x_size = max(output, key=lambda x: x[0])[0]
y_size = max(output, key=lambda x: x[1])[1]
matrix = [[0 for x in range(x_size + 1)] for y in range(y_size + 1)]
for coord in output:
    matrix[coord[1]][coord[0]] = 1
for row in matrix:
    print("".join(map(lambda x: "X" if x == 1 else " ", row)))