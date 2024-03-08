# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:54:35 2024

@author: Kuba
"""
from random import randint

class Dice():
    # a class for a single dice
    
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        # return result of a roll
        return randint(1,self.num_sides)