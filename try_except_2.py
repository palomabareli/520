#!/usr/bin/python3

archiveName = "paloma.txt"

try:
    print("\nArchive with read(). Result in String")

    with open(archiveName, "r") as archive:
        print(archive.read())
        print(type(archive.read()))    

except Exception as ex:
    print("The archive {0} no exists! Error message: {1}".format(archiveName, ex))