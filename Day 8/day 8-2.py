# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:36:03 2021

@author: Pablo
"""

def read_input(filename):
    with open(filename) as f:
        encodings = []
        displays = []
        for line in f.readlines():
            encoding, display = line.strip().split(" | ")
            encodings.append(sorted(encoding.split(), key=lambda x: len(x)))
            displays.append(display.split())
        return encodings, displays
    
encodings, displays = read_input("input 8.txt")
lights = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9"
        }
output = 0
for i in range(len(encodings)):
    current = encodings[i]
    keys = {}
    keys["a"] = (set(current[1]) - set(current[0])).pop()
    keys["d"] = (set(current[2]) & set(current[3]) & set(current[4]) & set(current[5])).pop()
    keys["g"] = ((set(current[3]) & set(current[4]) & set(current[5])) - set([keys["a"], keys["d"]])).pop()
    keys["b"] = (set(current[2]) - set(current[0]) - set(keys["d"])).pop()
    keys["e"] = (set(current[9]) - set(current[1]) - set([keys["b"], keys["d"], keys["g"]])).pop()
    keys["f"] = ((set(current[6]) & set(current[7]) & set(current[8])) - set([keys["a"], keys["b"], keys["g"]])).pop()
    keys["c"] = (set(current[0]) - set([keys["f"]])).pop()
    conversions = {v:k for k,v in keys.items()}
    number = "".join([lights["".join(sorted(map(lambda x: conversions[x], word)))] for word in displays[i]])
    output += int(number)       
    