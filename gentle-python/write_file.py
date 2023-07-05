# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:47:51 2023

@author: Kuba
write a writeToFile() function with
two parameters for the filename of the file and the text to write into the file. Second, write an
appendToFile() function, which is identical to writeToFile() except that the file opens in
append mode instead of write mode. Finally, write a readFromFile() function with one parameter
for the filename to open. This function returns the full text contents of the file as a string.
"""
def writeToFile(fileName,text):
    plik = open(fileName, 'w')
    plik.write(text)
    
def appendToFile(fileName,text):
    plik = open(fileName, 'a')
    plik.write(text)
    
def readFromFile(fileName):
  #  with open(fileName) as fileObj:
  #      return fileObj.read()
    plik = open(fileName)
    return plik.read()
    

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'

print(readFromFile('greet.txt'))
