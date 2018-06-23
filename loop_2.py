#!/usr/bin/python3

"""
numbers = list(range(1,11))

print("All informations numbers: {}, print(type(numbers)): {} ".format(numbers, type(numbers)))

print("")

print("The list numbers has: ")
print("") 

for number in numbers:
    print(number)
"""

names = []

while True:
    name = input("Input a name or exit: ")

    if name.lower().strip() == "exit":
        break
    names.append(name.lower().strip())

#print("All informations names: {}, print(type(names)): {} ".format(names, type(names)))

searchName = "kenji"

for varName in names:
    if varName.lower().strip() == searchName:
        print("There is Kenji in the list")
        break
else:
    print("There isn't Kenji in the list")

print("There is Kenji in the list? {}".format(searchName in names))
