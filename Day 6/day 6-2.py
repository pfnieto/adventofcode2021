# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:56:48 2021

@author: Pablo
"""

def read_input(filename):
    with open(filename) as f:
        return [int(x) for x in f.readline().split(",")]

def get_children(midv, starting_days, remaining_days):
    if remaining_days < starting_days:
        return 0
    if starting_days == first_birth:
        n_children = (remaining_days // next_birth) - (1 if remaining_days % next_birth < (1 + first_birth - next_birth) else 0)
    else:
        n_children = (remaining_days // next_birth) + (1 if remaining_days % next_birth > starting_days else 0)
    output = n_children
    for i in range(n_children):
        next_child = remaining_days - starting_days - next_birth * i
        if next_child not in midv:
            midv[next_child] = get_children(midv, first_birth, next_child)
        output += midv[next_child]
    return output


values = read_input("input 6.txt")
next_birth = 7
first_birth = 9
steps = 256
output = len(values)
results = {}
midv = {}
for x in values:
    if x not in results:
        results[x] = get_children(midv, x, steps)
    output += results[x]