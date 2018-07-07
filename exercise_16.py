#!/usr/bin/python3

"""
Abrir um arquivo com readlines (via função)
E devolver o conteúdo do arquivo
Passar como argumento: nome da fruta, preço e quantidade
"""

import function_import_4 as func
import re

def readArchive_1(archiveName, amount, value):
    try:
        func.readArchiveAll(archiveName, modoRead, content)
            print(archive.readlines())
    except Exception as ex:
        print("Error the read archive {0}. Message error: {1}", archiveName, ex)

archiveName1 = input("Add a name in the arquive (txt): ")
nameFruit = input("Add a name of the fruit: ")
amountFruit = input("Add the amount of fruit: ")
valueFruit = input("Add the value of fruit: ")

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

    if ((nameFruit.__len__) > 0):
        nameFruit = nameFruit
    else 
        print("Name not is validate")

    if ((int(amountFruit)) > 0):
        amountFruit = amountFruit
    else 
        print("Amount not is validate") 

    if ((int(valueFruit)) > 0):
        valueFruit = valueFruit
    else 
        print("Value not is validate")   

    dictnaryOfFruits = [amountFruit, ]
                 
except Exception as ex:
    print("Mensage error: {}".format(ex))
    
