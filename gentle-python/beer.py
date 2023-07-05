# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:41:28 2023

@author: Kuba
Write a program that displays the lyrics to ―99 Bottles of Beer.‖ Each stanza of the song goes like
this:
X bottles of beer on the wall,
X bottles of beer,
Take one down,
Pass it around,
X – 1 bottles of beer on the wall,
The X in the song starts at 99 and decreases by one for each stanza. When X is one (and X – 1 is
zero), the last line is ―No more bottles of beer on the wall!‖ After each stanza, display a blank line to
separate it from the next stanza.
"""


def singBottlesOfBeer(number):
    for i in range(number,0,-1):
        print('{0} bottles of beer on the wall, \n'.format(i))
        print('{0} bottles of beer, \n'.format(i))
        print('Take one down, \n')
        print('Pass it around, \n')
        print('\n')
    print('No more bottles of beer on the wall!')       
