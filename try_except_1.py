#!/usr/bin/python3

try:
    number1 = int(input("Add the number entire: "))
    number2 = int(input("Add the number entire: "))

    division = number1/number2

    print("The division between {0} and {1} is {2}".format(str(number1), str(number2), str(division)))

except ValueError as ve:
    print("Error: it is not value entire! Error Message: {}".format(ve))

except ZeroDivisionError as zde:
    print("Error: it is not possible divion by zero! Error Message: {}".format(ve))

except KeyboardInterrupt as ki:
    print("Error: it is not possible execution the aplication! Error Message: {}".format(ki))    

except Exception as e:
    print("Error: it is not possible execution the aplication! Error Message: {}".format(e))       

"""    
else:
    pass
finally:
    pass
"""    