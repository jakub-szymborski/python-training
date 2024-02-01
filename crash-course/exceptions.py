# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 11:47:53 2023

@author: Kuba
"""

# prosty kalkulator 

def calc():
    print("Write two numbers to divide")
    print("Press q to quit")
    first_number = input("\n First number: ")
    if first_number == 'q':
        return None
    second_number = input("\n Second number: ")
    if second_number == 'q':
        return None
    
    try:
        first_number= float(first_number)
    except ValueError:    
        print('Please try again')
        calc()
    try:
        second_number= float(second_number)
    except ValueError:
        print('Please try again \n')
        calc()
    
    
    try:
        answer = division(first_number, second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return None 
    return answer
    
def division(first, second):
    div = first/second
    return div

division(5,0)
calc()
