#!/usr/bin/python3

"""
def welcome(**kwargs):
    print(kwargs)
"""

'''function about welcome'''
def welcome(**people):
    for x,y in people.items():
        print(x, y, sep=":")

welcome(name="paloma", yearsOld=30)
print()
welcome()