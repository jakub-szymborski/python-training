# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:25:20 2023

@author: Kuba

Write a convertStrToInt() function with a stringNum parameter. This function returns an
integer form of the parameter just like the int() function. For example,
convertStrToInt('42') should return the integer 42. The function doesn’t have to work for
floating-point numbers with a decimal point, but it should work for negative number values.
Avoid using int() in your code, as that would do the conversion for you and defeat the purpose
of this exercise. However, we do use int() with assert statements to check that your
convertStrToInt() function works the same as int() for all integers from -10000 to 9999:
"""

def convertStrToInt(stringNum):
    strDict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}    # numbers dict to not use str()
    sign = 1 # sign, by default it's positive
    digit = 0
    integerNum = 0
    
    if stringNum == '0':
        return 0
    
    if stringNum[0] == '-':
        sign = -1
        stringNum = stringNum[1:]
    
    while len(stringNum) != 0:
        digit = stringNum[0]
        stringNum = stringNum[1:]
        integerNum = integerNum*10 + strDict[digit]
    return integerNum*sign
    


for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
    