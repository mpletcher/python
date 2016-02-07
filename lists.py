#!/usr/bin/python
# Most versatile datatype in Python

listx = ['marcos', 'pletcher', 2015, 2020];
listy = [10, 15, 20, 25, 30, 35];

# print lists
print listx
print listy
print "\nShow item from 2-4 "
print listy[2:4];

# Erase list elements
print "\n"
print "Erase item at index 1"
del listx[1];
print listx

# update list
print "\nUpdate item at index 1"
listx[1] = 2070;
print listx

# List() method
tuple = (123, 'xyz', 'zara', 'abc');
myList = list(tuple)

print "\nList items : ", myList

# Leave the program
raw_input("\n\nPress the enter key to exit.")
