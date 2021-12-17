# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:34:04 2021

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
        return 0, 0
    version = int(bins[0:3], 2)
    typeId = int(bins[3:6], 2)
    if typeId == 4:
        return version, handle_literal(bins, literals)
    else:
        if int(bins[6]) == 0:
            count = 0
            length = int(bins[7:22], 2)
            while count < length:
                newv, newc = handle(bins[22 + count:], literals)
                version += newv
                count += newc
            return version, 22 + count
        else:
            count = 0
            length = int(bins[7:18], 2)
            for i in range(length):
                newv, newc = handle(bins[18 + count:], literals)
                version += newv
                count += newc
            return version, 18 + count
    
original = read_input("input 16.txt")
literals = []
version, length = handle(original, literals)