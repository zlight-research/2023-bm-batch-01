#How to split the names in based on special character
import re
input = "two months"
# printing original string
print("The original string is : " + input)
 
# Using re.split()
# Splitting characters in String
res = re.split(' ', input)
print("firstword:", (res))