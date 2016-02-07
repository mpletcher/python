#!/usr/bin/python
# -*- coding: utf-8 -*-
# Name: personalData.py
# Author: Marcos Pletcher
# Purpose: Program creates external files (txt, HTML) and prompts the user to enter personal information. Afterwards, conditional routenes validate inputted values.
# Moreover, the HTML file created by this program allows programmers to add CSS, bootstraps, and other templates.
# Date: Oct 11, 2015


import datetime # allows to deal with dates, times, and time intervals
import string # module processes standard Python strings
import sys # provides information about constants, functions ...

# Output initial greeting.
print "Let's create a text and HTML files with data inputted by the user.\n\n";

# Prompts the user to enter his/her first name.
while True:
    firstName = raw_input("Please, enter your first name: ").strip()
 	# If condition validates entered items
    if not firstName.isalpha():
        print "Invalid first name entered."
        continue
    else:
    	break

# Prompts the user to enter his/her last name.
while True:
    lastName = raw_input("\nPlease, enter your last name: ").strip()
    # If condition validates entered items
    if not lastName.isalpha():
        print "Invalid last name entered. Please, try again."
        continue
    else:
    	break

# Outputs first name entered
print "Thank you " + firstName

# Writes the current date and time to your file
now = datetime.datetime.now()
print now.strftime("\n%m-%d-%Y %H:%M\n")

print firstName + ", thank you for collaborating. Below, there's the path of your files:\n";
print(sys.path) # allows to print 

# Creates text file
file = open("personaldata_py.txt", "w")
file.write("\nFirst name: " + firstName)
file.write("\nLast Name: " + lastName)
file.write(now.strftime("\n\n%m-%d-%Y %H:%M")) 
file.close()

# Creates HTML file
with open('index.html', 'w') as pageHTML:
  pageHTML = open("index.html", "wt")
  pageHTML.write("""<!DOCTYPE HTML PUBLIC">
<html>
  <head>
    <title>""" + firstName + """'s Profile</title>
    <link rel="stylesheet" href="resources/style.css" type="text/css"/>
  </head>
  <body>
        <header>
        <a class="header-logo" href="index.html"></a>
        
        <hr class="style-two">
        
        <h1 id="intro">Welcome to """+lastName+"""'s Home Page</h1>
        <h2>Hi! I'm """+firstName+""". This is my page!</h2>
        <br /><br />
        </header>
  </body>
</html>""")
  pageHTML.close()

# Exit the program
sys.exit(0)
