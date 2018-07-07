#!/usr/bin/python3

def readArchiveAll(nameArchive, modoRead, content):
    if modoRead == "a":
        addArchive(nameArchive, content)
    if modoRead == "w":
        writeArchive(nameArchive, content)        
    else:
        readArchive(nameArchive), content

def addArchive(nameArchive, content):
    try:
        with open(nameArchive, "a") as archive:
            archive.write(content + "\n")
            print(archive.readlines())
            archive.close()  
    except Exception as ex:
        print("Error mensage: " + ex)

def readArchive(nameArchive, content):
    try:
        with open(nameArchive, "r") as archive:
            print(archive.readlines())
            archive.close() 
    except Exception as ex:
        print("Error mensage: " + ex)
            
def writeArchive(nameArchive, content):
    try:
        with open(nameArchive, "a") as archive:
            archive.write(content + "\n")
            print(archive.readlines())
            archive.close()  
    except Exception as ex:
        print("Error mensage: " + ex)
        
