#!/usr/bin/python3

"""
Abrir um arquivo com readlines (via função)
E devolver o conteúdo do arquivo
sortear um nome
percorre a lista de lambda
usar upper, lower e title
"""

import function_import_4 as func4
import function_import_5 as func5
import re

def readArchive_1(archiveName):
    try:
        listArchiveFinale = func4.readArchiveAll(archiveName, "r", "")
        sortName = func5.sortName(listArchiveFinale)
        print("Sort in the archive {0} is {1}".format(archiveName, sortName))
    except Exception as ex:
        print("Error the read archive {0}. Message error: {1}", archiveName, ex)

archiveName1 = input("Add a name in the arquive (txt): ")

try:
    archiveName1 = archiveName1 +".txt" 
    readArchive_1(archiveName1)  
except Exception as ex:
    print("Mensage error: {}".format(ex))