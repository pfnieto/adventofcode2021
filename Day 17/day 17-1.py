# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:43:46 2021

@author: Pablo
"""

def read_input(filename):
    with open(filename) as f:
        parts = f.readline().strip().split()
        x1, x2 = parts[2].replace(",", "").replace("x=", "").split("..")
        y1, y2 = parts[3].replace("y=", "").split("..")
        return {"x1": int(x1), "x2": int(x2), "y1": int(y1), "y2": int(y2)}

def position_y(speed, time):
    return speed * time - (time * (time + 1) / 2)
        
def find_maximum_height(position):
    heights = [(0, 0)]
    speed = 1
    while True:
        print(speed)
        height = speed * (speed + 1) / 2
        if speed > abs(position["y1"]):
            break
        for time in range(2*speed - 1, 2*speed - 1 + abs(position["y1"])):
            pos = position_y(speed, time)
            print(speed, time, pos)
            if pos < position["y2"] and pos > position["y1"]:
                heights.append((speed, height))
                break
            if pos < position["y1"]:
                break
        if heights[-1][1] < heights[-2][1]:
            break
        speed += 1
    return heights    
    
position = read_input("input 17.txt")
heights = find_maximum_height(position)
max_height = int(max(heights, key=lambda x: x[1])[1])