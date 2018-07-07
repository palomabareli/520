#!/usr/bin/python3

def readArchive(archiveName):
    try:
        with open(archiveName, "r") as archive:
            print(archive.readlines())
    except Exception as ex:
        print("Error the read archive {0}. Message error: {1}", archiveName, ex)
