# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:25:23 2021

@author: Pablo
"""

def read_input(filename):
    with open(filename) as f:
        count = 0
        for line in f.readlines():
            encoding, display = line.strip().split(" | ")
            for item in display.split():
                if len(item) in [2,3,4,7]:
                    count += 1
        return count
    
count = read_input("input 8.txt")
                