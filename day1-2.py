# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:01:38 2021

@author: Pablo
"""

class RollingList:
    def __init__(self, length):
        self.values = []
        self.length = length
    
    def append(self, item):
        self.values.append(item)
        if len(self.values) > self.length:
            self.values.pop(0)
    
    def rolling(self):
        if len(self.values) < self.length:
            return None
        return sum(self.values)

values = []
with open("input 1-1.txt") as f:
    values = f.readlines()
values = list(map(lambda x: int(x.strip()), values))

inc = 0
dec = 0
previous = None
sliding = RollingList(3)
for item in values:
    sliding.append(item)
    if sliding.rolling() is None:
        continue
    if previous is None:
        previous = sliding.rolling()
        continue
    if sliding.rolling() > previous:
        inc += 1
    if sliding.rolling() < previous:
        dec += 1
    previous = sliding.rolling()
    