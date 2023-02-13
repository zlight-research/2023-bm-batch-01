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
F_name = input("enter your first name:")
L_name = input("enter your last name:")
gender = input("enter your gender:")
age = int(input("enter your age:"))
rate =int( input("enter rate:"))

gender_indentity=gender.upper()
 # CHECKING THE GENDER CONDITONS
if gender_indentity=="MALE":
    print("name:Mr", F_name.capitalize(),L_name.capitalize() )
elif gender_indentity=="FEMALE":
    if age<=25:
     print("name:Miss", F_name.capitalize(),L_name.capitalize())
    else:
         print("name:Mrs", F_name.capitalize(),L_name.capitalize())
else:
        print("no gender is found")
        print("*******")
        # PERFORMANCE RATING
        print('performance Rating')
        print("*******")
        if rate>100:
            print("performance Result : Extra Milestone")
        elif rate>=90 and rate<=100:
            print("performance Result : Outstanding")
        elif rate>=60 and rate<=89:
            print("performance Result : Good")
        else:
            print("performance Result : Needs Improvement")


        


