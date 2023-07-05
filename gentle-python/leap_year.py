# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:17:52 2023

@author: Kuba
A leap year occurs on all years divisible by four (e.g., 2016, 2020, 2024, and so on).
However, the exception to this rule is that years divisible by one hundred (e.g., 2100, 2200, 2300, and
so on) aren’t leap years. And the exception to this exception is that years divisible by four hundred
(e.g., 2000, 2400, and so on) are leap years

Write a isLeapYear() function with an integer year parameter. If year is a leap year, the
function returns True. Otherwise, the function returns False.
"""

def isLeapYear(year):
    if year % 400 == 0:
        return True 
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
            
assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True