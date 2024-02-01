# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:17:05 2024

@author: Kuba
"""

     
def read_high_score():
    # open high score file, if not present, create one 
    filename ='high_scores.txt'
    try:
        with open (filename) as file_object:
            scoreboard = file_object.read()
            print(scoreboard)
            
    except FileNotFoundError:
        high_score_file = open(filename, "w")
        high_score_file.write('0 \n')
         
read_high_score()
