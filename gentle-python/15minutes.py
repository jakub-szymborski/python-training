# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:30:33 2023

@author: Kuba
Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm.
Your solution should produce the following output:
    12:00 am
    12:15 am
    12:30 am
    12:45 am
    1:00 am
    1:15 am
    --cut--
    11:45 am
    12:00 pm
    --cut--
    11:30 pm
    11:45 pm
"""


def Intervals():
    hh = 12 
    mm = 00
    
    timeOfDay = 'am' 
    intervals = 24*60/15 - 1     
    i = 0 

    while i <= intervals:
        if mm == 0:
            mm = '00'
            print(str(hh) +':'+ mm +' ' + timeOfDay)
            mm = 0
        else:
            print(str(hh) +':'+ str(mm) +' ' + timeOfDay)
        
        if hh == 11 and mm == 45:
            timeOfDay = 'pm'
            hh = 12
            mm = 00
         
        elif hh == 12 and mm == 45:
            hh = 1
            mm = 00
        
        elif mm == 45:
            hh += 1
            mm = 00
        else:
            mm +=15
        i+=1 
  
Intervals()   

def intervalsLoops():
    for meridiem in ['am', 'pm']:
    # Loop over every hour:
        for hour in ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
    # Loop over every 15 minutes:
            for minutes in ['00', '15', '30', '45']:
    # Print the time:
                print(hour + ':' + minutes + ' ' + meridiem)


intervalsLoops()
