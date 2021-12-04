# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:23:45 2021

@author: Pablo
"""

def read_data(filename):
    bingo = []
    original = []
    selected = []
    positions = {}
    with open(filename) as f:
        bingo = [int(x) for x in f.readline().strip().split(",")]
        f.readline()
        current_matrix = []
        selected_matrix = []
        row = 0
        board = 0
        for line in f:
            current = line.strip().split()
            if len(current) == 0 :
                original.append(current_matrix)
                selected.append(selected_matrix)
                current_matrix = []
                selected_matrix = []
                row = 0
                board += 1
                continue
            for i in range(len(current)):
                if int(current[i]) not in positions:
                    positions[int(current[i])] = []
                positions[int(current[i])].append({"x": i, "y": row, "board": board})      
            current_matrix.append([int(x) for x in current])
            selected_matrix.append([0]*len(current))
            row += 1
        original.append(current_matrix)
        selected.append(selected_matrix)
    return bingo, original, selected, positions

def check_bingo(selected, positions, key):
    for position in positions[key]:
        selected[position["board"]][position["y"]][position["x"]] = 1
        bingo_row = sum(selected[position["board"]][position["y"]])
        bingo_column = sum([x[position["x"]] for x in selected[position["board"]]])
        if len(selected[position["board"]][position["y"]]) in (bingo_row, bingo_column):
            return position
    return None

bingo, original, selected, positions = read_data("input 4.txt")
winner = None
last_number = None
for key in bingo:
    winner = check_bingo(selected, positions, key)
    if winner:
        last_number = key
        break
not_selected = 0
for y in range(len(selected[winner["board"]])):
    for x in range(len(selected[winner["board"]][y])):
        if selected[winner["board"]][y][x] == 0:
            not_selected += original[winner["board"]][y][x]
output = last_number * not_selected