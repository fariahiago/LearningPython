import datetime as dt

# 1. Write a Python script to display the various Date Time formats - Go to the editor
#a) Current date and time

print(dt.datetime.now(None))

#b) Current year

print(dt.date.today().strftime("%Y"))

#c) Month of year

print(dt.date.today().strftime("%B"))

#d) Week number of the year

print(dt.date.today().strftime("%W"))

#e) Weekday of the week

print(dt.date.today().strftime("%w"))

#f) Day of year

print(dt.date.today().strftime("%j"))

#g) Day of the month

print(dt.date.today().strftime("%d"))

#h) Day of week 

print("Day of week: ", dt.date.today().strftime("%A"))



