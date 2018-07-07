#!/usr/bin/python3

import function_import_6 as func6

def factorial(number):
    aux = 1

    try:
        for x in range(1, number+1):
            aux *= x
        
        return aux

    except Exception as ex:
        func6.logFile(ex)
