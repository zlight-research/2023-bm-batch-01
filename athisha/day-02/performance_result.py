"""4. Enter input using python code

First Name
Last Name
Gender
Age
Rating
Display result as:
Name : <Mr / Miss / Mrs.> <Last Name>, <First Name>
Rating Table
Rating
Rating Result>100 : Extra Milestone
90-100 :Outstanding
60-89 :Good
<59 :Needs Improvement"""


First_name = input("Enter Your First name:")  # Enter name,age,rating,gender
Last_name = input("Enter Your last name:")
Gender = input("Enter Your gender:").lower()  # convert the lowercase
Age = int(input("Enter Your age:"))
Rating = int(input("Enter Your rating:"))

# the conditions
if Gender == "MALE":
    print("name:Mr", Last_name.title(), First_name.title())
elif Gender == "FEMALE":
    if Age <= 30:
        print("name:Miss", Last_name.title(), First_name.title())
    else:
        print("name:Mrs", Last_name.title(), First_name.title())
print("Rating Table")
