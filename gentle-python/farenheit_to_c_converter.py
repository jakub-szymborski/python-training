# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:01:15 2023

@author: Kuba

Write a convertToFahrenheit() function with a degreesCelsius parameter. This
function returns the number of this temperature in degrees Fahrenheit. Then write a function named
convertToCelsius() with a degreesFahrenheit parameter and returns a number of this
temperature in degrees Celsius.

Fahrenheit = Celsius × (9 / 5) + 32
Celsius = (Fahrenheit - 32) × (5 / 9)

"""

def convertToFahrenheit(degC):
    
    degF = degC * (9./5.) + 32
    return degF

def convertToCelsius(degF):
    
    degC = (degF - 32) * (5./9.)    
    return degC

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

# double check
print(convertToCelsius(0))
print(convertToCelsius(180))
print(convertToFahrenheit(0))
print(convertToFahrenheit(100))
print(convertToCelsius(convertToFahrenheit(15)))
