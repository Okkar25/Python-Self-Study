# * Python Dates

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects
# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object



import datetime as dt 

d = dt.datetime.now()

# print(d)
# print(d.year)
# print(d.month)
# print(d.day)
# print(d.hour)
# print(d.minute)
# print(d.second)
# print(d.microsecond)

import datetime

date = datetime.datetime.now()
# print(date.strftime("%a"))
# print(date.strftime("%A"))
# print(date.strftime("%d"))
# print(date.strftime("%b"))
# print(date.strftime("%B"))
# print(date.strftime("%m"))
# print(date.strftime("%y"))
# print(date.strftime("%Y"))
# print(date.strftime("%H"))
# print(date.strftime("%I"))
# print(date.strftime("%p"))
# print(date.strftime("%M"))
# print(date.strftime("%S"))
# print(date.strftime("%f"))
# print(date.strftime("%j"))
# print(date.strftime("%U"))
# print(date.strftime("%W"))
# print(date.strftime("%c"))
# print(date.strftime("%C"))
# print(date.strftime("%x"))
# print(date.strftime("%X"))

# * Reference

# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00


# ------------------------------------------------------------------------------------------


# * Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).


import datetime

d = datetime.datetime(2019, 2, 25)
# print(d)


# * The strftime() Method => string format time 

# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

import datetime

d = datetime.datetime(2020, 2, 1)
# print(d.strftime("%B"))
# print(d.strftime("%b"))

# https://www.w3schools.com/python/python_datetime.asp