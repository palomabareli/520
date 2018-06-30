#!/usr/bin/python3

print("\nArchive with write()")
#"a" = caso o arquivo não exista, ele cria o arquivo
with open("fruits.txt", "a") as archive:
    archive.write("lichia\n")

archive.close()    