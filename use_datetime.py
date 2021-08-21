#!/usr/bin/env python
#https://docs.python.org/ja/3/library/datetime.html

import datetime

var = datetime.date(2021, 11, 22)

print(var)

# timetuple
print(var.timetuple())

# weekday 
print(var.weekday())
print(var.isoweekday())

# ctime 
print(var.ctime())

# today
print(datetime.date.today())
print(datetime.datetime.now())    #YYYY-MM-DD hh:mm:ss.ffffff

# elapsed days
print(datetime.date.today() - var)
