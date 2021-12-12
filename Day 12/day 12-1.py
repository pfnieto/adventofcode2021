# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:13:53 2021

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

def travel(paths, current, visited, output):
    for path in paths[current[-1]]:
        if path not in visited:
            if path == "end":
                output.append(current + [path])
                continue
            n_visited = {**visited}
            if path.islower():
                n_visited[path] = 1
            travel(paths, current + [path], n_visited, output)           
    return output

paths = read_input("input 12.txt")
travels = travel(paths, ["start"], {"start": 1}, [])
output = len(travels)