firstname=input("Enter the Firstname:")
lastname=input("Enter the Lastname:")
if bool(firstname)==False and bool(lastname)==False:
    print('User must enter any one of the fields "First Name" or "Last Name" ')
else:

    gender=input("Enter the Gender:")
    age=int(input("Enter the Age:"))
    rating=int(input("Rating Table:"))

    if gender=="male":
        print(f'Name:Mr.{firstname.capitalize()} {lastname.capitalize()}')
    elif gender=="female" and age>=25:
        print(f'Name:Mrs.{firstname.capitalize()} {lastname.capitalize()}')
    else:
        
        print(f'Name:Miss".{firstname.capitalize()} {lastname.capitalize()}')
    if rating>100:
        performance="Extra Milestone"
    elif rating>=90:
        performance="Outstanding"
    elif rating>=60:
        performance="Good"
    else:
        performance="Needs Improovement"
    print("performance:",performance)

