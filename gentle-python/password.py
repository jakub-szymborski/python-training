# tagi: random, dict, string

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:47:28 2023

@author: Kuba
Write a generatePassword() function that has a length parameter. The length
parameter is an integer of how many characters the generated password should have. For security
reasons, if length is less than 12, the function forcibly sets it to 12 characters anyway. 
The password string returned by the function must have at least one lowercase letter, one uppercase letter, one
number, and one special character. The special characters for this exercise are ~!@#$%^&*()_+.
Your solution should import Python’s random module to help randomly generate these passwords.

Prerequisite concepts: import statements, random module, strings, string concatenation,
len(), append(), randint(), shuffle(), join()
"""
import random 


LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS       = '1234567890'
SPECIAL       = '~!@#$%^&*()_+'

    # list.append()     # dodaje element na koncu listy 
    # shuffle - losowe mieszanie listy, w miejscu, zwraca None 
    
def generatePassword(length):
    
    if length < 12:
        length = 12
    haslo = []
    
    # losuje po jednym obowiazkowym elemencie i dodaje je do listy 
    randSpecial = SPECIAL[random.randint(0,len(SPECIAL)-1)]
    randLower   = LOWER_LETTERS[random.randint(0,len(LOWER_LETTERS)-1)]
    randUpper   = UPPER_LETTERS[random.randint(0,len(UPPER_LETTERS)-1)]
    randNum     = NUMBERS[random.randint(0,len(NUMBERS)-1)]
   
    element = {0: randSpecial, 1:randLower, 2:randUpper, 3:randNum   }
    
    for e in element.items():
        haslo.append(e[1])   
    
    # losuje elementy do dodania tak dlugo, az osiagne odp. dlugosc
        # 1. losuje czy znak / liczba / litera mala / duza
        # 2. z wybranej kategorii losuje konkretna wartosc 
    while len(haslo) < length:
        randSpecial = SPECIAL[random.randint(0,len(SPECIAL)-1)]
        randLower   = LOWER_LETTERS[random.randint(0,len(LOWER_LETTERS)-1)]
        randUpper   = UPPER_LETTERS[random.randint(0,len(UPPER_LETTERS)-1)]
        randNum     = NUMBERS[random.randint(0,len(NUMBERS)-1)]
       
        element = {0: randSpecial, 1:randLower, 2:randUpper, 3:randNum}
        randElement = element[random.randint(0,3)]
        randChar    = randElement[random.randint(0,len(randElement)-1)]
        haslo.append(randChar)
        
   
    random.shuffle(haslo)   # random.shuffle zwraca None, wiec nie mozna wyniku przypisac do nowej zmiennej
    haslo = ''.join(haslo)
    return haslo


dupa = generatePassword(8)


if True:
    assert len(generatePassword(8)) == 12
    pw = generatePassword(14)
    assert len(pw) == 14
    hasLowercase = False
    hasUppercase = False
    hasNumber = False
    hasSpecial = False
    for character in pw:
        if character in LOWER_LETTERS:
            hasLowercase = True
        if character in UPPER_LETTERS:
            hasUppercase = True
        if character in NUMBERS:
            hasNumber = True
        if character in SPECIAL:
            hasSpecial = True
    assert hasLowercase and hasUppercase and hasNumber and hasSpecial