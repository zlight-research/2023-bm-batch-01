#4) Accept boolean variable and display "F" for False, "M" for True

"""Declaring variable "var"
 convert message to uppercase
 """

var = input("enter the boolean value:")
age = var.upper()

if age == "FALSE":
    print('F')
    
# elif evaluated to true.
elif age == "TRUE":
    print('M')
