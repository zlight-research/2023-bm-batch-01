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


while True:
    # enter your name,age,gender,rating
    First_Name = input("Enter Your First Name:")
    Last_Name = input("Enter Your Last Name:")
    if First_Name or Last_Name:
        break
    else:
        print("User Must enter any one of the fields") 

while True:
    Gender = input("Enter The Gender:").lower()
    if Gender in ["male", "female"]:
        break
    else:
        print("Enter Your Correct Gender")

Age = int(input("Enter Your Age:"))
Rating = int(input("Enter Your Ratings:"))

if Gender == "male":
    prefix = "Mr"
elif Gender == "female":
    if Age <= 30:
        prefix = "Miss"
    else:
        prefix = "Mrs"

print("Name:", prefix, Last_Name.title(), First_Name.title())

# Rating table
 
if Rating < 60:
    print("Performance Result : Needs Improvement")
elif 60 <= Rating <= 89:
    print("Performance Result : Good")
elif 90 <= Rating <= 100:
    print("Performance Result : Outstanding")
else:
    print("Performance Result : Extra Milestone")


