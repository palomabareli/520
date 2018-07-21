#!/usr/bin/python3

import psycopg2

try:
    con = psycopg2.connect("host=127.0.0.1 dbname=projeto user=admin password=4linux")
    cur = con.cursor()

    #cur.execute("insert into usuarios (nome, idade) values ('Aline', 35)")
    #con.commit()

    cur.execute('select * from usuarios')
    #cur.fetchone()          #primeiro objeto do cursor
    content = cur.fetchall() #todos os objetos do cursor
    print(content)
    con.commit()

    print()
    print(type(content))

    print("\nConnect success!")
except Exception as ex:
    con.rollback()
    cur.rollback()
    con.close()
    cur.close()    
    function_6.logFile(ex)
