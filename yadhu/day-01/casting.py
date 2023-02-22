#1)How to display the current date format of "2022, September 12 11:00 AM" ?
import datetime
"""
current_date is a varible used to store the current date and time
strftime is use to convert dates to strings
"""
current_date=datetime.datetime.now()
print(current_date.strftime("Current Date And Time=%Y,%b %d  %H:%M:%S %p"))

