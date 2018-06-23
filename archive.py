#!/usr/bin/python3

#a = append
#archive = open("frutas.txt", "a")
#archive.write("lichia\n")
#archive.close()

#w = write
#archive = open("frutas.txt", "w")
#archive.write("lichia\n")
#archive.close()

#r = read
with open("frutas.txt", "r") as archive:
    print(archive.readlines()) #list
    #print(archive.readline()) #string