# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:48:43 2021

@author: Pablo
"""

def read_input(filename):
    opener = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closer = {")": 1, "]": 2, "}": 3, ">": 4}
    inv_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    output = []
    with open(filename) as f:
        for line in f:
            skip = False
            current = 0
            stack = []
            for char in line:
                if char in opener:
                    stack.append(char)
                    continue
                if char in closer:
                    if inv_pairs[char] == stack[-1]:
                        stack.pop()
                        continue
                    else:
                        skip = True
                        break
            if skip:
                continue
            for op in reversed(stack):
                current = 5 * current + closer[opener[op]]
            output.append(current)           
    return output

scores = read_input("input 10.txt")
output = sorted(scores)[len(scores)//2]