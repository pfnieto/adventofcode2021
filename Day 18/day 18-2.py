# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:51:35 2021

@author: Pablo
"""

from ast import literal_eval
from math import floor, ceil

class Node:
    def __init__(self, values, side=0, parent=None, depth=0):
        self.parent = parent
        self.depth = depth
        self.side = side
        self.leftChild = Node(values[0], side=1, parent=self, depth=depth+1) if isinstance(values, list) else None
        self.rightChild = Node(values[1], side=-1, parent=self, depth=depth+1) if isinstance(values, list) else None
        self.value = None if isinstance(values, list) else values
        
    def magnitude(self):
        if self.value is not None:
            return self.value
        return 3*self.leftChild.magnitude() + 2*self.rightChild.magnitude()
    
    def get(self):
        if self.value is not None:
            return self.value
        inner = [self.leftChild.get() if self.leftChild else None, 
                 self.rightChild.get() if self.rightChild else None]
        return list(filter(lambda x: x is not None, inner))
    
    def add_left(self):
        previous = self.parent
        current = self.parent.parent
        while current is not None:
            if current.leftChild and current.leftChild != previous:
                current = current.leftChild
                break
            else:
                previous = current
                current = current.parent
        if current is None:
            return
        while current.value is None:
            if current.rightChild:
                current = current.rightChild
            else:
                current = current.leftChild
        current.value += self.value
        
    def add_right(self):
        previous = self.parent
        current = self.parent.parent
        while current is not None:
            if current.rightChild and current.rightChild != previous:
                current = current.rightChild
                break
            else:
                previous = current
                current = current.parent
        if current is None:
            return
        while current.value is None:
            if current.leftChild:
                current = current.leftChild
            else:
                current = current.rightChild
        current.value += self.value
    
    def has_exploded(self):
        if self.depth > 4:
            if self.side == 1:
                self.add_left()
                self.parent.rightChild.add_right()
            else:
                self.add_right()
                self.parent.leftChild.add_left()
            self.parent.leftChild = None
            self.parent.rightChild = None
            self.parent.value = 0
            return True
        else:
            return False
    
    def has_split(self):
        if self.value is not None and self.value > 9:
            self.leftChild = Node(floor(self.value / 2), side=1, parent=self, depth=self.depth+1)
            self.rightChild = Node(ceil(self.value / 2), side=-1, parent=self, depth=self.depth+1)
            self.value = None
            return True
        else:
            return False
    
    def find_explosion(self):
        explosion = self.has_exploded()
        if explosion:
            return True
        left_explosion = self.leftChild.find_explosion() if self.leftChild else False
        if left_explosion:
            return True
        right_explosion = self.rightChild.find_explosion() if self.rightChild else False
        return right_explosion
    
    def find_split(self):
        split = self.has_split()
        if split:
            return True
        left_split = self.leftChild.find_split() if self.leftChild else False
        if left_split:
            return True
        right_split = self.rightChild.find_split() if self.rightChild else False
        return right_split
    
    def find_error(self):
        if self.find_explosion():
            return True
        return self.find_split()       
            

def read_input(filename):
    with open(filename) as f:
        return [literal_eval(line.strip()) for line in f]
    
    
values = read_input("input 18.txt")
magnitudes = {}
for i in range(len(values)):
    for j in range(len(values)):
        if i == j:
            continue
        tree = Node([values[i], values[j]])
        while tree.find_error():
            continue
        magnitudes[(i, j)] = tree.magnitude()
max_m = magnitudes[max(magnitudes, key=magnitudes.get)]