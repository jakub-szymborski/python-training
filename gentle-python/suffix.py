# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:29:49 2023

@author: Kuba

In English, ordinal numerals have suffixes such as the ―th‖ in ―30th‖ or ―nd‖ in ―2nd‖. Write an
ordinalSuffix() function with an integer parameter named number and returns a string of the
number with its ordinal suffix. For example, ordinalSuffix(42) should return the string
'42nd'.
You may use Python’s str() function to convert the integer argument to a string. Python’s
endswith() string method could be useful for this exercise, but to maintain the challenge in this
exercise, don’t use it as part of your solution.
1st
2nd
3rd
4th
...
21st
22nd
23rd etc
"""

def ordinalSuffix(number):
    suffix = ''
    last_digit = str(number)[-1]
  
    if len(str(number)) >=2 and str(number)[-2] == '1':
        suffix = 'th'  
    elif last_digit == '1':
        suffix = 'st'
    elif last_digit == '2':
        suffix = 'nd'
    elif last_digit == '3':
        suffix = 'rd'
    else:
        suffix = 'th'
        
    return str(number) + suffix

ordinalSuffix(1101)

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'