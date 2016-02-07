#!/usr/bin/python

from datetime import datetime
now = datetime.now()

# prints date
print '%s/%s/%s' % (now.month, now.day, now.year)

# prints time
print '%s:%s:%s'% (now.hour, now.minute, now.second) #placeholders for variables 