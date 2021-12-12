# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 11:17:54 2021

@author: Pablo
"""

def read_input(filename):
    paths = {}
    with open(filename) as f:
        for line in f:
            start, end = line.strip().split("-")
            if (start not in paths):
                paths[start] = []
            if (end not in paths):
                paths[end] = []
            paths[start].append(end)
            paths[end].append(start)
    return paths

def travel(paths, current, visited, output, double):
    for path in paths[current[-1]]:
        n_double = double
        if path in visited: 
            if n_double is None:
                n_double = path
            else:
                continue
        if path == "start":
            continue
        if path == "end":
            output.append(current + [path])
            continue
        n_visited = {**visited}
        if path.islower():
            n_visited[path] = 1                
        travel(paths, current + [path], n_visited, output, n_double)           
    return output

paths = read_input("input 12.txt")
travels = travel(paths, ["start"], {"start": 1}, [], None)
output = len(travels)