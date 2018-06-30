#!/usr/bin/python3

print("\nArchive writting names.txt")

name = "stop"

with open("names.txt", "w") as archive:
    name = input("Add a name in the arquive names.txt. Add exit to STOP: ")

    while (name.lower() != "stop"):
        archive.write(name+"\n")
        name = input("Add a name in the arquive names.txt. Add exit to STOP: ")

    print("\nArchive names.txt: ")
    with open("names.txt", "r") as archive:
        print(archive.readlines())

archive.close()