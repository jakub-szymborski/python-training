# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:03:10 2023

@author: Kuba
Write a convertIntToStr() function with an integerNum parameter. This function
operates similarly to the str() function in that it returns a string form of the parameter. For
example, convertIntToStr(42) should return the string '42'. The function doesn’t have to
work for floating-point numbers with a decimal point, but it should work for negative integer values.
Avoid using Python’s str() function in your code, as that would do the conversion for you and
defeat the purpose of this exercise.
"""


def convertIntToStr(integer):
    pass






for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)