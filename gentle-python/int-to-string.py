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


def convertIntToStr(integerNum):
    stringNum = ''  
    sign = ''
    numDict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}    # numbers dict to not use str()

    if integerNum == 0:
        return '0'
    
    if integerNum < 0:
        sign = '-'
        integerNum = integerNum*(-1)
    
    while int(integerNum/10) != 0:  # loop will break at last digit, do_while would be nice 
        digit = integerNum % 10              # - rest from division by 10 is the last digit  
        integerNum =  int(integerNum / 10)   # removing last digit      
        stringNum = numDict[digit] + stringNum        
    
    digit = integerNum % 10                 # one more time for last digit  
    stringNum = numDict[digit] + stringNum          

    return sign + stringNum


def convertIntToStr2(integerNum):
    stringNum = ''  
    sign = ''
    numDict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}    # numbers dict to not use str()

    if integerNum == 0:
        return '0'
    
    if integerNum < 0:
        sign = '-'
        integerNum = integerNum*(-1)
    
    while integerNum != 0:   
        digit = integerNum % 10              # - rest from division by 10 is the last digit  
        integerNum =  int(integerNum / 10)   # removing last digit      
        stringNum = numDict[digit] + stringNum        
    
    return sign + stringNum

for i in range(-10000, 10000):
    assert convertIntToStr2(i) == str(i)
    
    
    
    