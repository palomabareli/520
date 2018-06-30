#!/usr/bin/python3

dictPersons = [
    {"name" : "aline bergamo", "years old" : "30", "phone" : "0000-0000"}    ,
    {"name" : "aline firmino", "years old" : "35", "phone" : "1111-1111"}    ,
    {"name" : "julia botan", "years old" : "28", "phone" : "2222-2222"}    ,
    {"name" : "andreia kawata", "years old" : "28", "phone" : "3333-3333"}    ,
]

print("What's Maria? How old is she?")
print(dictPersons[2].get("idade"))