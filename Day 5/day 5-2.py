# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 10:39:03 2021

@author: Pablo
"""
import re

def read_data(filename):
    values = []
    x = 0
    y = 0
    with open(filename) as f:
        for line in f.readlines():
            parts = [int(i) for i in re.split(",| -> ", line.strip())]
            coords = {"x1": parts[0], "y1": parts[1], "x2": parts[2], "y2": parts[3],}
            x = max(x, max(coords["x1"], coords["x2"]))
            y = max(y, max(coords["y1"], coords["y2"]))
            values.append(coords)
    return values, x, y

def build_board(values, size_x, size_y):
    board = [[0 for j in range(size_x + 1)] for i in range(size_y + 1)]
    common = {}
    for coords in values:
        m = (coords["y2"] - coords["y1"])/(coords["x2"] - coords["x1"]) if (coords["x2"] != coords["x1"]) else None
        n = coords["y1"] - m * coords["x1"] if m is not None else None
        for y in range(min(coords["y1"], coords["y2"]), max(coords["y1"], coords["y2"]) + 1):            
            for x in range(min(coords["x1"], coords["x2"]), max(coords["x1"], coords["x2"]) + 1):
                if (m is not None and n is not None and y != m * x + n):
                    continue
                board[y][x] += 1
                if board[y][x] > 1:
                    common[(x, y)] = 1
    return board, len(common.keys())

values, size_x, size_y = read_data("input 5.txt")
board, common = build_board(values, size_x, size_y)