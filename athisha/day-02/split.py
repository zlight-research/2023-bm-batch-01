"""1.How to split the names in based on special character

Eg:

Input = “zlight research”

Assign to 2 variables, Displayed as given below"""

# Charaters


import re
s = "zlight research"  # s is a varible used to store

t = s.split()  # Calling split function

print("FirstWord =", t[0].title())  # print value
print("SecondWord =", t[1].title())

# String
s = "zlight research"

print(re.split('\W+', s))
