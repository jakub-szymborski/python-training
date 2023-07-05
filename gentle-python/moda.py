# tagi: random, dict, loop, mode

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:43:18 2023

@author: Kuba
Write a mode() function that has a numbers parameter. This function returns the mode, or
most frequently appearing number, of the list of integer and floating-point numbers passed to the
function.
"""
numerki = [1, 2, 3, 4, 4]
biblio = {}

for num in numerki: 
    biblio[num] = 0
    
for num in numerki: 
    biblio[num] += 1


def mode(numbers):
   wystapienia = {}
   
   mostFreqNumber = None
   mostFreqNumberCount = 0
   
   if len(numbers) == 0:
       return None

   for num in numbers:
        if num not in wystapienia:
            wystapienia[num] = 1
            if wystapienia[num] > mostFreqNumberCount:
                mostFreqNumber = num 
                mostFreqNumberCount = wystapienia[num]
        else:
            wystapienia[num] += 1
            if wystapienia[num] > mostFreqNumberCount:
                mostFreqNumber = num 
                mostFreqNumberCount = wystapienia[num]
    
   return mostFreqNumber
 


ziemniaczki = ['ziemniaczek', 'cebulka','ziemniaczek', 'cebulka', 'kurczak', '4sery', 'cebulka'] 

print(mode(ziemniaczki))
print(mode(numerki))
  
assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4