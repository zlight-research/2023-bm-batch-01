"""1.How to split the names in based on special character
Eg:
Input = “zlight research”
Assign to 2 variables, Displayed as given below"""


# Charaters

input_string = "zlight research"  # s is a varible used to store
t = input_string.split()  # Calling split function
print("FirstWord", t[0].title())  # print value
print("SecondWord:", t[1].title())