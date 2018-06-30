#!/usr/bin/python3

print("Dictionary aboout me: ")

dictPersons = {"name":"paloma","years old":"30"}

for x, y in dictPersons.items():
    print(x,y)

print("My Andress: ")
dictPersons.get("andress")    

print("My name: ")
dictPersons.get("name")    

print("My Andress: ")
dictPersons.get("andress", "Not found")    