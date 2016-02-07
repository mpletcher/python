#!/usr/bin/python
# -*- coding: utf-8 -*-
# Simple input system in Python
# Author: Marcos Pletcher

# import module sys
import sys # provides information about constants, functions ...

# Function Definition
def outputMe( str ):
   print str
   return;

# Calling a function
outputMe("This string is being passed into my function \n")

# Exit the program
sys.exit(0)