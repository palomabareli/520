#!/usr/bin/python3

count = 5
number = 1


listPrincipal = ""
listOdd = ""
listPair = ""


while (number <= count):
    listPrincipal = listPrincipal.__add__(input("Add o {} element of list: ".format(str(number))))
    number = number + 1

for elementPrincipal in listPrincipal:
    if (int(elementPrincipal)%2 == 0) :
        listPair = listPair.__add__(elementPrincipal)
    else :
        listOdd = listOdd.__add__(elementPrincipal)

print("listPrincipal")        
for elementPrincipal in listPrincipal:
    print (elementPrincipal)

print("listPair")        
for elementPair in listPair:
    print (elementPair)

print("listOdd")        
for elementOdd in listOdd:
    print (elementOdd)
