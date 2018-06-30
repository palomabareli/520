#!/usr/bin/python3

names = ["paloma","kenji","jul","aline bergamo","aline firmino", "andreia"]

for name in names:
    if name.lower() == "rebeca":
        print("Rebeca is in the list")
else:
    print("Rebeca not found\n\n")

print("Test print with my name:")
print("paloma","ribeiro")
print("paloma","ribeiro", sep=".")
print("paloma","ribeiro", sep=".", end="\n\n")

print("\nList of my friends: ")
#list compreension
print([name.title() for name in names])

print("\nIs Paloma in the list? ")
#if ternário
print("yes" if names.__contains__("paloma") else "no")


