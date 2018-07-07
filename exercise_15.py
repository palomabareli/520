#!/usr/bin/python3

"""
Abrir um arquivo com readlineee (via função)
E devolver o conteúdo do arquivo
"""

import function_import_3 as func
import re

def readArchive_1(archiveName):
    try:
        with open(archiveName, "r") as archive:
            print(archive.readlines())
    except Exception as ex:
        print("Error the read archive {0}. Message error: {1}", archiveName, ex)

archiveName1 = input("Add a name in the arquive (txt): ")

extesion = re.compile('.txt')
#match = tested string 
verification = [x for x in archiveName1 if extesion.match(x)] 

try:
    if ((verification.__len__) > 0):
        archiveName1 = archiveName1
    else:
        archiveName1 = archiveName1 +".txt"   

    archiveName1 = str(archiveName1).lower()

    readArchive_1(archiveName1)  
except Exception as ex:
    print("Mensage error: {}".format(ex))
    
