#!/usr/bin/python3
names = ['paloma','julia','aline bergamo','aline firmino','andreia']

print("All informations names: {}, print(type(names)): {} ".format(names, type(names)))
print("First: {}, print(type(names)): {} ".format(names[0], type(names[0])))
print("Last: {}, print(type(names)): {} ".format(names[-1], type(names[-1])))

print("")

namePaloma = ['paloma    ','bareli','ribeiro']

print("All informations of namePaloma: {}, print(type(namePaloma)): {} ".format(namePaloma, type(namePaloma)))
print("First: {}, print(type(namePaloma)): {} ".format(namePaloma[0], type(namePaloma[0])))
print("First: {}, print(type(namePaloma)) plus rstrip(): {} ".format(namePaloma[0].rstrip(), type(namePaloma[0].rstrip())))

print("")

person1 = input("Add one person in the finish of list: ")
names.append(person1)

print("All informations of names: {}, print(type(names)): {} ".format(names, type(names)))

print("")

person2 = input("Add one person in the start of list: ")
names.insert(0, person2)

print("All informations of names: {}, print(type(names)): {} ".format(names, type(names)))



