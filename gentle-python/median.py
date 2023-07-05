# tagi: loop, sort, median

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:01:07 2023

@author: Kuba
Write a median() function that has a numbers parameter. This function returns the statistical
median of the numbers list. The median of an odd-length list is the number in the middlemost
number when the list is in sorted order. If the list has an even length, the median is the average of the
two middlemost numbers when the list is in sorted order. Feel free to use Python’s built-in sort()
method to sort the numbers list.
Passing an empty list to average() should cause it to return None.
"""

def median(numbers):
        # 1. posortowac liste
        # 2. sprawdzic czy dlugosc jest parzysta:
        #    2a. Parzysta - zwrocic srednia z dwoch srodkowych wartosci 
        #    2b. Nieparzysta - zwrocic srodkowa wartosc 
    if len(numbers) == 0:
        return None 
    else:
        numbers_sorted = sorted(numbers) 
        
        if len(numbers) % 2 == 0:
            mid = int(len(numbers)/2)
            result = (numbers_sorted[mid-1] + numbers_sorted[mid])/2 
        
        else: 
            mid = int(len(numbers)/2)
            result = numbers_sorted[mid]
            
    return result
    
numerki = [2, 1, 3, 0, 5, 4, 6]  
numerki2 = [3, 7, 10, 4, 1, 9, 6, 5, 2, 8]      
median(sorted(numerki))    
median(sorted(numerki2))   


assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6