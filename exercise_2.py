#!/usr/bin/python3

name = input("What's your name?: ")

note1 = input("Input the note one: ")

while (int(note1) > 11) : 
    note1 = input("Error. The note is wrong. Input the note one: ")

note2 = input("Input the note two: ")

while int(note2) > 11 : 
    note2 = input("Error. The note is wrong. Input the note two: ")

note3 = input("Input the note two: ")

while int(note3) > 11 : 
    note3 = input("Error. The note is wrong. Input the note three: ")    

average = (int(note1) + int(note2) + int(note3))/3

print("")

#print(name.title() + " your average is " + str(average)) 
print("{0} your average is {1}".format(name.title(), average))

print("")

if average >= 7:
    print("You was approved!!!")
else:
    print("You wasn't approved!!!")



  