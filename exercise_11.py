#!/usr/bin/python3

print("\nArchive reading fruits.txt")
#"a" = caso o arquivo não exista, ele cria o arquivo
with open("fruits.txt", "r") as archive:
    lines = archive.readlines()

archive.close() 

count = 1

print("\nArchive writting fruits_2.txt")
with open("fruits_2.txt", "w") as archive2:
    for line in lines:            
        writeLine = str(count) + " - " + line
        archive2.write(writeLine)
        count += 1

    print("\nArchive adding value default in fruits_2.txt")
    newLine = ("{} - {}").format(str(999), "Mamão")
    archive2.write(newLine)

archive2.close() 
