# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:26:32 2023

@author: Kuba
Write two functions named calculateSum() and calculateProduct(). They both have a
parameter named numbers, which will be a list of integer or floating-point values. The
calculateSum() function adds these numbers and returns the sum while the
calculateProduct() function multiplies these numbers and returns the product. If the list passed
to calculateSum() is empty, the function returns 0. If the list passed to calculateProduct()
is empty, the function returns 1. Since this function replicates Python’s sum() function, your solution
shouldn’t call.
"""



def calculateSum(numbers):
    suma = 0
    for i in numbers: 
        suma = suma + i
    
    return suma 


def calculateProduct(numbers):
    product = 1
    for i in numbers: 
        product = product * i
    return product


assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840