# How to display the current date format of "2022, September 12 11:00 AM" ?

import datetime
date=(datetime.datetime.now())
print ("current date is :",date.strftime("%Y, %B %d %H:%M:%S %p")) 
