#!/usr/bin/python


# Return more than one value
def moreThanOne (value1):
    x = value1
    y = value1 * 2

    return (x,y)
    return str(x,y).replace('[','').replace(']','')

(x,y) = moreThanOne(20)
print "Values are: ", (x,y)

# Leave the program
raw_input("\n\nPress the enter key to exit.")