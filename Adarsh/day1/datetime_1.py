#1) How to display the current date format of "2022, September 12 11:00 AM

import datetime

now = datetime.datetime.now() # current date and time
print(now)
date_time = now.strftime("%Y, %B %d %H:%M") # datetime to string using strftime()

print("date and time:",date_time)
# print(datetime.__file__)
