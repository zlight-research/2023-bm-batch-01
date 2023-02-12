import re

number = '9037975068'
match = re.fullmatch("^[789]\d{9}$", number)
if match != None:
    print("matching")