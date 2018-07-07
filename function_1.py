#!/usr/bin/python3

def welcome(name, yearsOld):
    print("Welcome {0}. You are {1} years old.".format(name, str(yearsOld)))

"""
for x in range(3):
    welcome("Paloma",30)    
"""

names = ["paloma","bareli","ribeiro"]  

for name in names:
    print(welcome(name, 30))

welcome(name="Paloma", yearsOld = 30)           
welcome("Paloma", 30)           