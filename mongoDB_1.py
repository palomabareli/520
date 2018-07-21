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
    #print(db.fila.find().pretty())

    """
    for doc in db.fila.find():
        print(type(doc))
    """

    #doc = db.fila.find_one({"_id":1})

    """
    docs = [doc for doc in ]db.fila.find()
    print(type(doc))
    """
    
except Exception as ex:
    function_6.logFile(ex)