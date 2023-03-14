"""Enter input using python code
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
<59 :Needs Improvement
Performance Result : Extra Milestone
Additional requirements.
* Based on Rating, Performance result should be displayed according the rating table
* Name should displayed with proper salutation
* Name should be displayed with a Proper case such as the first character should be Capital.
* Incase only one name displayed, there should not comma character (,)
*Incase there is blank for First Name OR Last Name, display message  as "User must enter any one of the fields "First Name" or Last Name"""

firstName = input("First Name: ")
lastName = input("Last Name: ")
gender = input("Gender: ")
age = input("Age: ")
rating = int(input("Rating: "))
if gender == "male":
    salutation = "Mr."
elif gender == "female":
    if age >= 18:
        salutation = "Mrs."
    else:
        salutation = "Miss"
else:
    salutation = ""
if rating > 100:
    performance = "Extra Milestone"
elif rating >= 90:
    performance = "Outstanding"
elif rating >= 60:
    performance = "Good"
else:
    performance = "Needs Improvement"
if firstName == "" and lastName == "":
    print("enter the first name  'First Name' or 'Last Name'")
elif firstName == "":
    print("User must enter the 'First Name'")
elif lastName == "":
    print("User must enter the 'Last Name'")
else:
    if salutation != "":
        name = salutation + " " + lastName + ", " + firstName
    else:
        name = lastName + ", " + firstName
    print("Name: ", name)
    print("Performance result:",performance)
