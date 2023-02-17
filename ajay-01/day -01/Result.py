# Enter input using python code
#First Name
#last Name
# Gender
# Age
# Rating
# Display result as:
# Name : <Mr / Miss / Mrs.> <Last Name>, <First Name>
# Rating Table
# Rating
# Rating Result>100 : Extra Milestone
# 90-100 :Outstanding
# 60-89 :Good
# <59 :Needs Improvement
# Performance Result : Extra Milestone
# Additional requirements.
# * Based on Rating, Performance result should be displayed according the rating table
# * Name should displayed with proper salutation
# * Name should be displayed with a Proper case such as the first character should be Capital.
# * Incase only one name displayed, there should not comma character (,)
# *Incase there is blank for First Name OR Last Name, display message  as "User must enter any one of the fields "First Name" or Last Name"

first_name = input("First Name: ")
last_name = input("Last Name: ")
gender = input("Gender: ")
age = input("Age: ")
rating = int(input("Rating: "))
# Display name with proper salutation
if gender.lower() == "male":
    salutation = "Mr."
elif gender.lower() == "female":
    salutation = "Miss/Mrs."
else:
    salutation = ""

if first_name == "" and last_name == "":
    print("User must enter any one of the fields 'First Name' or 'Last Name'")
elif first_name == "":
    print("Name: " + salutation + " " + last_name.title())
elif last_name == "":
    print("Name: " + salutation + " " + first_name.title())
else:
    print("Name: " + salutation + " " + last_name.title() + ", " + first_name.title())

# Display rating result
if rating > 100:
    result = "Extra Milestone"
elif rating >= 90:
    result = "Outstanding"
elif rating >= 60:
    result = "Good"
else:
    result = "Needs Improvement"

print("Performance Result: " + result)




