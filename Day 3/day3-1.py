# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:21:35 2021

@author: Pablo
"""

def read_input(filename):
    values = []
    size = 0
    with open(filename) as f:
        for line in f:
            size += 1
            data = line.strip()
            if len(values) == 0:
                values = [0] * len(data)
            for i in range(len(data)):
                values[i] += int(data[i])                
    return values, size

values, length = read_input("input 3.txt")
gamma = "".join(list(map(lambda x: "1" if x > length/2 else "0", values)))
epsilon = "".join(list(map(lambda x: "1" if x < length/2 else "0", values)))
output = int(gamma, 2) * int(epsilon, 2)