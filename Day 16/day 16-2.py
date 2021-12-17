# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:56:20 2021

@author: Pablo
"""

def read_input(filename):
    with open(filename) as f:
        bins = ""
        for k in f.readline().strip():
            bins += bin(int(k, 16))[2:].zfill(4)
        while len(bins) % 4 != 0:
            bins = "0" + bins
        return bins
    
def actions(typeId, values):
    if (typeId == 0):
        return sum(values)
    if (typeId == 1):
        output = 1
        for x in values:
            output *= x
        return output
    if (typeId == 2):
        return min(values)
    if (typeId == 3):
        return max(values)
    if (typeId == 5):
        return 1 if values[0] > values[1] else 0
    if (typeId == 6):
        return 1 if values[0] < values[1] else 0
    else:
        return 1 if values[0] == values[1] else 0
    
def handle_literal(bins, literals):
    literal = ""
    for i in range(len(bins[6:]) // 5):
        literal += bins[6 + 5*i + 1:6 + 5*(i+1)]
        if int(bins[6 + 5*i]) == 0:
            break
    literals.append(int(literal, 2))
    return 6 + 5 *(i+1)
    
def handle(bins, literals):
    if len(bins) == 0:
        return 0
    typeId = int(bins[3:6], 2)
    if typeId == 4:
        return handle_literal(bins, literals)
    else:
        inner = []
        count = 0
        start = 22
        if int(bins[6]) == 0:
            length = int(bins[7:22], 2)
            while count < length:
                newc = handle(bins[22 + count:], inner)
                count += newc
        else:
            start = 18
            length = int(bins[7:18], 2)
            for i in range(length):
                newc = handle(bins[18 + count:], inner)
                count += newc
        literals.append(actions(typeId, inner))
        return start + count
    
original = read_input("input 16.txt")
literals = []
length = handle(original, literals)