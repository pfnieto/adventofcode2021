# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:35:39 2021

@author: Pablo
"""

def read_input(filename):
    names = {
            "forward": {"x": 1, "aim": 0},
            "down": {"x": 0, "aim": 1},
            "up": {"x": 0, "aim": -1}
            }
    values = []
    with open(filename) as f:
        for line in f:
            direction, value = line.strip().split()
            values.append({
                    "direction": names[direction],
                    "value": int(value)
                    })
    return values
        
        
values = read_input("input 2-1.txt")
x = 0
y = 0
aim = 0
for item in values:
    x += item["direction"]["x"] * item["value"]
    y += item["direction"]["x"] * item["value"] * aim
    aim += item["direction"]["aim"] * item["value"]
mult = x * y