#!/usr/bin/python3

name = input("What's your name?: ")

note1 = input("Input the note one: ")

while (int(note1) > 11) : #or (len(note1) == 0):
    note1 = input("Error. The note is wrong. Input the note one: ")

note2 = input("Input the note two: ")

while int(note2) > 11 : #or (len(note2) == 0):
    note2 = input("Error. The note is wrong. Input the note one: ")

average = int(note1) + int(note2)/2

#print(name.title() + " your average is " + str(average)) 
print("{0} your average is {1}".format(name.title(), average))

  