#!/usr/bin/python3

#wow pa q le meto esto!
### mainprogam.py
### IMPORTS ANOTHER MODULE

#taken from http://www.sthurlow.com/python/lesson09/

#import all the module!
import ModuleTest

#import individual objects
from ModuleTest import printhello


print ('ss9 Empieza testeo modulos')

# a variable from module
print ModuleTest.ageofqueen

# a class from module,,,,, instance?

# al llamar la clase, se llama el init!
myPiano =  ModuleTest.Piano()
myPiano.printdetails()

#call the individual object from import!
printhello()