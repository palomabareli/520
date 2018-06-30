#!/usr/bin/python3

from pprint import pprint

dictFruits = [
    {"fruit" : "melon", "price" : 5.90, "count" : 2}    ,
    {"fruit" : "strawberry", "price" : 1.56, "count" : 1}    ,
    {"fruit" : "lemon", "price" : 8.50, "count" : 0}    ,
    {"fruit" : "lichia", "price" : 4.99, "count" : 6}    ,
]

print("List of fruits: ")
pprint(dictFruits)

sumTotal = 0

for fruit in dictFruits:
    sumTotal = sumTotal + (fruit["price"] * fruit["count"])

if (sumTotal > 0):
    print("You win {}".format(str(sumTotal)))
    sumTotal = sumTotal * 1.1
    print("With 10% is  {}".format(str(sumTotal)))
else:
    print("You don't sell nothing")    
