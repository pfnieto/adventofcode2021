# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:47:25 2021

@author: Pablo
"""

import heapq

def read_input(filename):
    with open(filename) as f:
        weights = {}
        distances = {}
        y = 0
        for line in f:
            cleaned = line.strip()
            for x in range(len(cleaned)):
                weights[(x, y)] = int(cleaned[x])
                distances[(x, y)] = float("inf")
            y += 1
        return weights, distances, x, y - 1
    
weights, distances, max_x, max_y = read_input("input 15.txt")

available = [(0, (0, 0))]
while len(available) > 0:
    distance, position = heapq.heappop(available)
    if distance > distances[position]:
        continue
    if position == (max_x, max_y):
        break
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x*y != 0):
                continue
            newp = (position[0] + x, position[1] + y)
            if newp not in distances:
                continue
            newd = distance + weights[newp]
            if newd < distances[newp]:
                distances[newp] = newd
                heapq.heappush(available, (newd, newp))
output = distances[(max_x, max_y)]