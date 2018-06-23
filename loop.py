#!/usr/bin/python3

numbers = list(range(1,11))

print("All informations numbers: {}, print(type(numbers)): {} ".format(numbers, type(numbers)))

print("")

print("The list numbers has: ")
print("") 

for number in numbers:
    print(number)

names = ['paloma','kenji','julia','aline bergamo','aline firmino','andreia']

print("All informations names: {}, print(type(names)): {} ".format(names, type(names)))

print("The length of list names is: {} ".format(len(names)))
print("") 

print("The list names has: ")
print("") 

for name in names:
    print(name.title())    

print("")     

limitNumber = input("Input the value maximum of the list: ")

limitNumber = int(limitNumber)

for number in range(limitNumber):
    print(number)    

print("")     