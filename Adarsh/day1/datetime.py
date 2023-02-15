#1) How to display the current date format of "2022, September 12 11:00 AM


from _datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%Y, %B %d %H:%M") # datetime to string using strftime()

print("date and time:",date_time)
