#Accept boolean variable and display "F" for False, "M" for True


new = input("enter the boolean value:")
age = new.upper()

if age == "FALSE":
    print('F')
    
# elif evaluated to true.
elif age == "TRUE":
    print('M')