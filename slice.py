#!/usr/bin/python3

names = ['paloma','julia','aline bergamo','aline firmino','andreia']
numbers = list(range(10))

print("All informations names: {}, print(type(names)): {} ".format(names, type(names)))

copy = names
print("All informations copy: {}, print(type(copy)): {} ".format(copy, type(copy)))

names[0] = "pedro"
print("All informations names: {}, print(type(names)): {} ".format(names, type(names)))
print("All informations copy: {}, print(type(copy)): {} ".format(copy, type(copy)))

copy2 = names[:]
print("All informations copy2: {}, print(type(copy2)): {} ".format(copy2, type(copy2)))

copy3 = names[1:]
print("All informations copy3: {}, print(type(copy3)): {} ".format(copy3, type(copy3)))

copy4 = names[1:-1]
print("All informations copy4: {}, print(type(copy4)): {} ".format(copy4, type(copy4)))

copy5 = names[::-1]
print("All informations copy5: {}, print(type(copy5)): {} ".format(copy5, type(copy5)))