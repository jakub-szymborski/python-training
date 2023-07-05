# tagi: random

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:17:10 2023

@author: Kuba

Write a rollDice() function with a numberOfDice parameter that represents the number of
six-sided dice. The function returns the sum of all of the dice rolls. For this exercise you must import
Python’s random module to call its random.randint() function for this exercise.
"""
import random

# help(random.randint)
# randint(a, b) method of random.Random instance
 #   Return random integer in range [a, b], including both end points.

def rollDice(noDice):
    suma = 0
    
    for i in range(noDice):
        suma += random.randint(1,6)
    return suma

print(rollDice(0))

assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
    assert 1 <= rollDice(1) <= 6
    assert 2 <= rollDice(2) <= 12
    assert 3 <= rollDice(3) <= 18
    assert 100 <= rollDice(100) <= 600