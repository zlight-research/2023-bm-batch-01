# 1) How to display the current date format of "2022, September 12 11:00 AM" ?

from datetime import datetime

now = datetime.now() # current date and time

# datetime to string using strftime()

date_time = now.strftime("%Y/%B/%d/%Y, %H:%M:%S")
print("date and time:",date_time)