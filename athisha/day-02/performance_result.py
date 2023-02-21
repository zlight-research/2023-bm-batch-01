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
    First_Name, Last_Name = input("Enter Your First Name:"), input(
        "Enter Your Last Name:")  # enter your name,age,gender,rating
    if First_Name or Last_Name:
        break
    else:
        print("User Must enter any one of the fields")  # entered empty filed pleace your first name
while True:
    # lower() using enter gender input lowercase
    gender = input("Enter The Gender: ").lower()
    if gender in ["male", "female"]:  # checking male or female
        break
    else:
        print("Enter Your Correct Gender")

age, rating = int(input("Enter Your Age: ")), int(
    input("Enter Your Ratings: "))  # enter your age and rating
# prefix is using Mr,Mrs and Miss gender and age
prefix = "Mr" if gender == "male" else "Miss" if age <= 30 else "Mrs"
print("Name:", prefix, Last_Name.title(), First_Name.title())
#display rating
print("Rating:", "Needs Improvement" if rating <= 60 else "Good" if rating <=89 else "Outstanding" if rating <= 100 else "Extra Milestone")
