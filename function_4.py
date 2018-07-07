#!/usr/bin/python3

"""
def welcome(*args):
    print(args)
"""

def welcome(*names):
    for x in names:
        print("Welcome {}".format(x))

welcome("paloma", "julia", "kenji")