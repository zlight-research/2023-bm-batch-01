#Accept boolean variable and display "F" for False, "M" for True


Boolean = input("enter the boolean value:")
age = Boolean.upper()

if age == "FALSE":
    print('F')

# elif evaluated to true.
elif age == "TRUE":
    print('M')