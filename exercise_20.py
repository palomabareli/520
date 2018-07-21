#!/usr/bin/python3

from pymongo import MongoClient
from function_6 import logFile

try:
    """  
        Banco local = logo sem parâmetro = localhost
        Sem senha e sem usuário por default (usa o próprio)
    """
    con = MongoClient()
    db = con["4Linux"]

    db.fila.insert({"nome":"Paloma", "idade": 30})
    db.fila.insert({"nome":"Julia", "idade": 28})
    db.fila.insert({"nome":"Kenji", "idade": 27})

    db.fila.update({"nome":"Paloma", "$set":{"sobrenome":"Ribeiro"}})

    for doc in db.fila.find():
        print(doc)
   
except Exception as ex:
    function_6.logFile(ex)