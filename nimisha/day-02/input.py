'''Enter input using python code

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

*Incase there is blank for First Name OR Last Name, display message  as "User must enter any one of the fields "First Name" or Last Name".'''
 

#to give input
first_name = input("enter your first name:")
last_name = input("enter your last name:")
gender = input("enter your gender:")
age = int(input("enter your age:"))
rate =int( input("enter rate:"))

gender_identity=gender.upper()
 # CHECKING THE GENDER CONDITONS
if not first_name or not last_name ==None:
    print("User must enter any one of the fields:")
if gender_identity=="MALE":
    print("name:Mr", first_name.capitalize(),last_name.capitalize() )
elif gender_identity=="FEMALE":
    if age<=25:
     print("name:Miss", first_name.capitalize(),last_name.capitalize())
    else:
         print("name:Mrs", first_name.capitalize(),last_name.capitalize())
else:
    print("no gender is found")
       
        # PERFORMANCE RATING 
print("Needs improvemnet" if rate<59 else "good" if rate<=89 else "outstanding" if rate<100 else "extra milestone")





