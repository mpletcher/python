#!/usr/bin/python
# input and operator

x = int(raw_input("Please enter an number: "))

if x < 0:
      x = 0
      print 'Negative changed to zero'
elif x == 0:
      print '0'
elif x == 1:
      print '1'
else:
      print 'more than 1'