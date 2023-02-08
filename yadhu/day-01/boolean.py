#4) Accept boolean variable and display "F" for False, "M" for True
"""
boolean_varible is a varible to store the user inputed boolean value
here,upper() is used to convert all the value inputed by user into upper case.then it store into a varible called boolean_convert
then the condition check 
            if the boolean_convert is FLASE print-F
            elif the boolean_convert is TRUE print-T
            else print invalid input
"""
boolean_varible=input("enter the boolean value:")
boolean_convert=boolean_varible.upper()
if boolean_convert=="FALSE":
    print('F')
elif boolean_convert=="TRUE":
    print('T')
else:
    print("enter a boolean value.....")