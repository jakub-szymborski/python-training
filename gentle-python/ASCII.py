# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:01:22 2023

@author: Kuba
Write a printASCIITable() function that displays the ASCII number and its corresponding
text character, from 32 to 126
"""

def printASCIITable():
    for i in range(32,127,1):
        print (i, chr(i))
        
    
printASCIITable()