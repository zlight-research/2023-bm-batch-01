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
*Incase there is blank for First Name OR Last Name, display message  as "User must enter any one of the fields "First Name" or Last Name"
"""

first_name=input("Enter your First name:")
last_name=input("Enter your Last name:")
gender=input("Enter your Gender(Male\Female):")
age=int(input("Enter your Age:"))
rating=int(input("enter your rating :"))
#check  missing first name or last name
if len(first_name)==0 and len(last_name)==0:
    print("User must enter any one of the fields First Name or Lastname the Name")
else:
   if gender =="Male":
     name="Mr." +first_name.capitalize() + " "+ last_name.capitalize()  #salutation and first letter should be capitalize in name
   else:
    gender =="Female"
    name="Ms."+first_name.capitalize()+ " "+ last_name.capitalize()

if rating > 100:
     Performance_Result="Extra Milestone"  #performance result based on rating
elif rating >=90:
     Performance_Result="Out standing"

elif rating >= 60:
    Performance_Result= "Good"
else:
    Performance_Result = "Needs Improvement"

print("name:",name)
print("Rating Table")
print(">100  :", "Extra Milestone" ,"\n" "90-100:", "Outstanding","\n" "60-89 :", "Good","\n" "<59   :", "Needs Improvement")
print("Performance Result:", Performance_Result)


