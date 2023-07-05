# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:32:40 2023

@author: Kuba

Write a function named printHandshakes() with a list parameter named people which will
be a list of strings of people’s names. The function prints out 'X shakes hands with Y', where
X and Y are every possible pair of handshakes between the people in the list. No duplicates are
permitted: if ―Alice shakes hands with Bob‖ appears in the output, then ―Bob shakes hands with
Alice‖ should not appear
The printHandshakes() function must also return an integer of the number of handshakes.
"""

ppl = ['Tomek', 'Romek', 'Atomek'] 

def printHandshakes(people):
    numOfShakes = 0
    # 1a osoba wita sie ze wszystkimi kolejnymi 
        # 2ga wita sie ze wszystkimi kolejnymi, bez pierwszej 
    
    for i in range(0, len(people)-1):
        for j in range(i+1, len(people)):
            print(people[i] + ' shakes hands with ' + people[j])
            numOfShakes += 1
    return numOfShakes
    
printHandshakes(ppl)   
    
#for i in range(0, len(people) - 1):
#    for j in range(i, len(people)):  
    
   
assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6