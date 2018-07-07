#!/usr/bin/python3


def readArchiveAll(nameArchive, modoRead, content):
    if content == "a":
        addArchive(nameArchive)
    if content == "w":
        writeArchive(nameArchive)        
    else:
        readArchive(nameArchive)

def addArchive(nameArchive):
    with open(nameArchive, "a") as archive:
        print(archive.readlines())
        archive.close()    

def readArchive(nameArchive):
    with open(nameArchive, "r") as archive:
        print(archive.readlines())
        archive.close()    

def writeArchive(nameArchive):
    with open(nameArchive, "w") as archive:
        print(archive.readlines())  
        archive.close()          
