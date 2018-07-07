#!/usr/bin/python3

"""
Abrir um arquivo com readlineee (via função)
E devolver o conteúdo do arquivo
"""

import function_import_3 as func

def readLines(archiveName):
    try:
        func.readArchive(archiveName = archiveName)
    except Exception as ex:
        print("Error the read archive {0}. Message error: {1}", archiveName, ex)

nameOfArchive = input(print("Add the name of archive: "))
readLines(nameOfArchive)