#Enter input from user
first_name=input("enter first name:")
last_name=input("enter last name:")
gender=input("enter gender:")
age=int(input("enter age:"))
rating=int(input("enter rating:"))
#convert the gender into uppercase
gender_up=gender.upper()
#checking the conditions
if gender_up=="MALE":
    print("name:Mr",last_name.capitalize(),first_name.capitalize())
elif gender_up=="FEMALE":
    if age<=30:
       print("name:Miss",last_name.capitalize(),first_name.capitalize())
    else:
       print("name:Mrs",last_name.capitalize(),first_name.capitalize())
print("Rating Table")
print("****************")
if rating>100:
    print("Performance Result : Extra Milestone")
elif rating>=90 and rating<=100:
    print("Performance Result : Outstanding")
elif rating>=60 and rating<=89:
    print("Performance Result : Good")
else:
    print("Performance Result : Needs Improvement")