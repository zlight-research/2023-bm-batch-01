"""1.How to split the names in based on special character

Eg:

Input = “zlight research”

Assign to 2 variables, Displayed as given below"""


# Charaters

input = "zlight research"  # input is a varible used to store

value = input.split()  # Calling split function

print("FirstWord =", value[0].title())  # print value
print("SecondWord =", value[1].title())
print("Input =" ,input.title())
