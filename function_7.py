#!/usr/bin/python3

def external(func):
    def internal(x, y):
        print(x, y)
    return internal

''' Decorator -> internal -> function decorate '''    

@decorator
def sum(x, y)
    return x + y 
