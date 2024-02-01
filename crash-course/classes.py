# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:42:35 2023

@author: Kuba

Class names should be in CamelCaps 
Instances and module names should be lowercase with _between_words
"""

class Dog():
    # pySzczek class 

    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def sit(self):
        # tell dog to sit 
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        # tell dog to roll over 
        print(self.name.title() + " rolled over!")
    
hauka = Dog('Chałka', 2)

hauka.sit()
hauka.roll_over()
hauka.name

brawurka = Dog('brawurka', 3)
brawurka.roll_over()

dogs = (hauka, brawurka)

for pies in dogs: 
    print(pies.name)
    
class User():
    def __init__(self, first_name, last_name, age, has_pies):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.has_pies = has_pies 
        
        
    def summary(self):
      """  print(self.first_name + ' '+ self.last_name + ' is ' + str(self.age).lower() \
              + " years old and it's " + str(self.has_pies) 
              + " that he/she has a dog")
      """      
      print(f"{self.first_name} {self.last_name} is {str(self.age)} years old and it's {str(self.has_pies).lower()} that he/she has a dog")
            
            
pszemo = User('Pszemek', 'Unc', 29, True)
elmo = User('Elmo', 'Bonk', 31, False)

for typ in (pszemo, elmo): 
    typ.summary()
    
    
    
# car class  --------------------------

class Car():
    # car class
    
    def __init__(self, maker, model, year):
        # init car attributes 
        self.maker = maker
        self.model = model
        self.year = year 
        self.mileage = 0
        
    def descriptiveName(self):
        # print description
        longName = str(self.year) + ' ' + self.maker +' ' + self.model
        return longName.title()

    def readMileage(self):
        # print car mileage 
        print("This bad boy has " + str(self.mileage) + " km on it.")
    
    def updateMileage(self, mileage):
        # set mileage to given value 
        if mileage >= self.mileage:
           self.mileage = mileage

        else:
            print("Dzwonie na policje")
            
    def addMileage(self, miles):
        # increase mileage by value
        if miles >= 0:
            self.mileage += miles
        else:
            print("Dzwonie na policje")
         
    def gasTank(self, volume = 50):
        # setup gas tank
        self.volume = volume
        
    def describeGasTank(self):
        print('Your car has ' + str(self.volume) + 'litre tank')
            

czarnaStrzala = Car('Polonez', 'Caro', 1996)
print(czarnaStrzala.descriptiveName())
czarnaStrzala.readMileage()

czarnaStrzala.mileage = 69
czarnaStrzala.readMileage()


czarnaStrzala.updateMileage(0)

czarnaStrzala.addMileage(10)
czarnaStrzala.readMileage()

# inheritance 

class ElectricCar(Car):
    # electric car child class
    def __init__(self, maker, model, year):
        # super() - odniesienie do superclass, klasy-matki
        # subclass - klasa dziecko / dziedziczaca
        super().__init__(maker, model, year) 
        self.battery = Battery()
           
    def describeGasTank(self):
        # method to override parent class method
        print("Electric cars don't have gas tank")
        self.battery.describeBattery()
        
elektrowoz = ElectricCar('Polonez', 'Elektra', 2137)        

elektrowoz.descriptiveName()    

elektrowoz.describeGasTank()
    

class Battery():
    # battery class 
    def __init__(self, batterySize=10):
        self.batterySize = batterySize 
    
    def describeBattery(self):
        print("This bad boy has " + str(self.batterySize) + "kWh battery.")
        
    def getRange(self):
        # describe range of a car with given battery 
        range = self.batterySize/0.2
        print(f"This bad boy has range of {range} miles")
     
elektrowoz.battery.getRange()

