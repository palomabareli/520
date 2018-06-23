#!/usr/bin/python3

limitNumber = input("Input the value maximum of the list: ")

limitNumber = int(limitNumber)

result = "pair"

for number in range(0, limitNumber, 2):
    #if ((number%2)==0):
    #    result = "pair"
    #else:
    #    result = "odd"
    print("The number {} is {} ".format(str(number), result))    