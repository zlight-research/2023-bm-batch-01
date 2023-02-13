'''
1) How to display the current date format of "2022, September 12 11:00 AM" ?


'''
#import package datetime

from datetime import datetime
#now date and time display using now() function
now=datetime.now()

#change date format to string using strftime() function
current_date_time=now.strftime("%Y, %B %d  %H:%M:%S %p")
print("current date and time :",current_date_time)

