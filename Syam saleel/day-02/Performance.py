

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
4. Enter input using python code
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

"""



#Input values
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
gender = input("Enter Gender (M/F): ")
age = int(input("Enter Age: "))
rating = int(input("Enter Rating: "))

# Get salutation based on gender
if gender == "Male":
    salutation = "Mr."
elif gender == "Female":
    salutation = "Mrs"
    if age <=18:
        salutation="Miss" 
else:
    print("no gender")
    salutation = " "

# Construct full names
if first_name and last_name:
    full_name = f"{salutation} {first_name},{last_name} "
else:
     print("User must enter the first name and last name")
     full_name = " "#first_name + last_name

# Determine performance result based on rating
if rating > 100:
    performance = "Extra Milestone"
elif rating >= 90:
    performance = "Outstanding"
elif rating >= 60:
    performance = "Good"
else:
    performance = "Needs Improvement"
print(f"Name: {full_name}")
print(f"Performance Result : {performance}")




