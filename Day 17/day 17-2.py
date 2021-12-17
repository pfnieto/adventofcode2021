# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:26:09 2021

@author: Pablo
"""

from math import sqrt, floor, ceil

def read_input(filename):
    with open(filename) as f:
        parts = f.readline().strip().split()
        x1, x2 = parts[2].replace(",", "").replace("x=", "").split("..")
        y1, y2 = parts[3].replace("y=", "").split("..")
        return {"x1": int(x1), "x2": int(x2), "y1": int(y1), "y2": int(y2)}
    
def contact_time_y(initial_speed, y):
    b = 1 - 2*initial_speed
    return (1/2) * (b + sqrt(b**2 + 8 * y))

def contact_time_x(initial_speed, x, entry=False):
    maximum_x = (1/2) * (initial_speed * (initial_speed + 1))
    if (maximum_x < x and entry):
        return None 
    b = 2 * initial_speed + 1
    delta = b ** 2 - 8 * x
    if delta < 0:
        return initial_speed
    return (1/2) * (b - sqrt(delta))
        
def find_y_times(position):
    times = {}
    for speed in range(position["y1"], abs(position["y1"]) + 1):
        entry_time = ceil(contact_time_y(speed, abs(position["y2"])))
        exit_time = floor(contact_time_y(speed, abs(position["y1"])))
        for time in range(entry_time, exit_time + 1):
            if time not in times:
                times[time] = []
            times[time].append(speed)
    return times

def find_x_times(position):
    times = {}
    repeating = []
    for speed in range(abs(position["x2"]) + 1):
        entry_time = contact_time_x(speed, abs(position["x1"]), entry=True)
        if entry_time is None:
            continue
        entry_time = ceil(entry_time)
        exit_time = floor(contact_time_x(speed, abs(position["x2"])))
        if speed == exit_time:
            repeating.append(speed)
        for time in range(entry_time, exit_time + 1):
            if time not in times:
                times[time] = []
            times[time].append(speed)
    return times, repeating

def add_repeated(x_times, y_times, x_repeating):
    for repeated in x_repeating:
        last = max(y_times.keys())
        for i in range(repeated + 1, last + 1):
            if i not in x_times:
                x_times[i] = []
            x_times[i].append(repeated)
            
def combine(x_times, y_times, position):
    output = set()
    for time, speeds in y_times.items():
        if time in x_times:
            for y_speed in speeds:
                for x_speed in x_times[time]:
                    output.add((x_speed,y_speed))
    return output
    
    
position = read_input("input 17.txt")
y_times = find_y_times(position)
x_times, x_repeating = find_x_times(position)
add_repeated(x_times, y_times, x_repeating)
output = len(combine(x_times, y_times, position))