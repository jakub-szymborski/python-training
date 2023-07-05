# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:54:14 2023

@author: Kuba
You will write four functions for this exercise. The functions area() and perimeter() have
length and width parameters and the functions volume() and surfaceArea() have length,
width, and height parameters. These functions return the area, perimeter, volume, and surface
area, respectively.
"""


def area(L,W):
   if L < 0 or W < 0:
       ar = 0
   else:
    ar = L * W
   return ar

def perimeter(L,W):
   if L < 0 or W < 0:
       per = 0
   else: 
    per = 2*L + 2*W
   return per
    
def volume(L,W,H):
   if L < 0 or W < 0 or H <0:
       vol = 0
   else:
    vol = L*W*H
    return vol

def surfaceArea(L,W,H):
    if L < 0 or W < 0 or H <0:
        sfA = 0
    else:
        sfA = 2*(L*W + L*H + W*H)
    return sfA

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340