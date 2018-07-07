#!/usr/bin/python3

"""
Abrir um arquivo com readlineee (via função)
E devolver o conteúdo do arquivo
"""

import function_import_3 as func

def readArchive_1(archiveName):
    try:
        with open(archiveName, "r") as archive:
            return print(archive.readlines())
    except Exception as ex:
        print("Error the read archive {0}. Message error: {1}", archiveName, ex)

archiveName1 = input("Add a name in the arquive: ")
readArchive_1(archiveName1)
