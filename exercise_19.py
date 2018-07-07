#!/usr/bin/python3

from datetime import datetime
import function_import_6 as func6 #log error
import function_import_7 as func7 #factorial

while True:
    number = input("Enter the number to factorial or 'S' to exit: ")

    if number == "s":
        break
    else:
        try:
            number = int(number)

            print("The factorial the {0} is {1}".format(str(number), str(func7.factorial(number))))

        except Exception as ex:
            func6.logFile(ex)
