import datetime
time=datetime.datetime.now()
""" including a date and a time"""
# print(type(time),time)
print(time.strftime("%B %d,%Y %I:%M %p"))
"""strftime is python function 
   B represent Month
   d reprent Day
   Y represent Year
   I represent Hour
   M represent Minute
   p represent AM AND PM"""