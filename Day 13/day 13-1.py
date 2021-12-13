# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:03:17 2021

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
output = len(fold(coords, folds[0:1]))