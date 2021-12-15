# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:52:52 2021

@author: Pablo
"""

def read_input(filename):
    with open(filename) as f:
        initial = list(f.readline().strip())
        codes = {}
        totals = {}
        letters = {}
        f.readline()
        for line in f.readlines():
            start, end = line.strip().split(" -> ")
            codes[start] =  end
            totals[start] = 0
            letters[start[0]] = 0
        for i in range(len(initial)):
            letters[initial[i]] += 1
            if (i + 1) == len(initial):
                continue
            totals[initial[i] + initial[i+1]] += 1            
        return codes, totals, letters
    
codes, totals, letters = read_input("input 14.txt")
steps = 10
for i in range(steps):
    copy = {**totals}
    for k, v in totals.items():
        letters[codes[k]] += v
        copy[k[0] + codes[k]] += v
        copy[codes[k] + k[1]] += v
        copy[k] -= v
    totals = copy
output = max(v for v in letters.values()) - min(v for v in letters.values())