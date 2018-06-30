#!/usr/bin/python3

"""
archive = open("fruits.txt", "r")
#caso não feche, pode conrromper o arquivo
archive.close()
"""

print("\nArchive with read(). Result in String")
with open("fruits.txt", "r") as archive:
    print(archive.read())
    print(type(archive.read()))    

print("\nArchive with readlines(). Result in List")
with open("fruits.txt", "r") as archive:
    print(archive.readlines())
    print(type(archive.readlines()))        

print("\nArchive with readline()")
with open("fruits.txt", "r") as archive:
    print(archive.readline())
    print(type(archive.readline))

print("\nArchive with readline() + Seek()")
with open("fruits.txt", "r") as archive:
    print(archive.readline(), end="")
    print(archive.readline(), end="")
    #zera o cursor do arquivo, e reinicia o arquivo, contagem por byte
    archive.seek(0) 
    print(archive.readline(), end="")

archive.close()    