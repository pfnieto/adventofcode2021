# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:01:07 2021

@author: Pablo
"""

def read_input(filename):
    with open(filename) as f:
        fuel = {}
        original = [int(x) for x in f.readline().split(",")]
        count = [0] * (max(original) + 1)
        total = 0
        for x in original:
            count[x] += 1
            total += x
        for i in range(len(count)):
            for j in range(len(count)):
                if i == j:
                    continue
                if i not in fuel:
                    fuel[i] = 0
                fuel[i] += abs(i - j) * count[j]
            if i > 1 and fuel[i] > fuel[i - 1]:
                break
        return fuel
    
fuel = read_input("input 7.txt")
out = min(fuel.values())
            