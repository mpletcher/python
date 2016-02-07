#!/usr/bin/python

name = raw_input("Please, enter your name: ")

print name          # Prints complete string
print name[0]       # Prints first character of the string
print len(name)		# prints the length of the string

number = int(raw_input("Please, enter a number: "))
print "Hello " + name + ". Your score is " + str(number) # method turns non-strings into strings

# Leave the program
raw_input("\nPress the enter key to exit.")
