# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:13:12 2023

@author: Kuba
Write a getSmallest() function that has a numbers parameter. The numbers parameter will
be a list of integer and floating-point number values. The function returns the smallest value in the
list. If the list is empty, the function should return None. Since this function replicates Python’s
min() function, your solution shouldn’t use it.
"""


def getSmallest(numbers):
    if numbers == []:
        return None
    
    minn = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] < minn:
            minn = numbers[i]
            
    return minn
            
assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None