# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:15:41 2021

@author: Pablo
"""

def read_input(filename):
    opener = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closer = {")": 3, "]": 57, "}": 1197, ">": 25137}
    inv_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    output = 0
    with open(filename) as f:
        for line in f:
            for char in line:
                if char in opener:
                    stack.append(char)
                    continue
                if char in closer:
                    if inv_pairs[char] == stack.pop():
                        continue
                    output += closer[char]
                    break
    return output

output = read_input("input 10.txt")
                
            
        