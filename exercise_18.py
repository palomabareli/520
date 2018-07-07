#!/usr/bin/python3

from datetime import datetime
import function_import_4 as func4

while True:
    fileName = input("Add the name of the file (txt) or 'S' to exit: ")
    fileName = str(fileName).lower()

    if fileName == "s":
        break

    mod = input("Shape of open the file: ")
    content = ""

    try:
        if (mod == "r") or (mod == "w") or (mod == "a"):
            if (mod == "w"):
                content = input("Add the content to add in the file: ")            
            func4.readArchiveAll(nameArchive = fileName, modoRead = mod, content = content) 
    except Exception as ex:
        print("Error message: " + ex)

    

    


