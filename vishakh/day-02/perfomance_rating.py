'''
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

<59 :Needs Improvement

 







Additional requirements.
* Based on Rating, Performance result should be displayed according the rating table

* Name should displayed with proper salutation

* Name should be displayed with a Proper case such as the first character should be Capital.

* Incase only one name displayed, there should not comma character (,)

*Incase there is blank for First Name OR Last Name, display message  as "User must enter any one of the fields "First Name" or Last Name"



'''


#input some detailes first_name,last_name


first_name,last_name=input("enter first name:"),input("enter last name:")

#user must enter first name and last name not enter error message display

if bool(first_name)==False and bool(last_name)==False :
    print("user must enter any one of the fields first name or last name")
else:
    #condition is true then input some detailes gender,age,rating
    
    gender,age,rating=input("enter gender:").lower(),int(input("enter age:")),int(input("eneter rating:"))

    #gender is female execute this block
       
    if gender=='female':
        if gender=='female' and age>25:
            print("Mrs.",last_name.capitalize(),",",first_name.capitalize())
        else:
            print("Miss.",last_name.capitalize(),",", first_name.capitalize())
    
    #gender is male execute this block
    
    elif gender=='male':
        print("Mr.",last_name.capitalize(),",",first_name.capitalize())
    else:
        print("others")
    

    #rating table display

    print("Needs improvemnet" if rating<59 else "good" if rating<=89 else "outstanding" if rating<100 else "extra milestone")




























# print("Rating table")
# #the rate is above 100 if condition is true print result"Extra milestone" if is false then pass to elif statement
# if rate>100:

#     print("Performance Result : Extra Milestone")

# #the rate is above 90 and below or equal to 100  elif condition is true print result "Outstanding" elif is false then pass to next elif statement

# elif rate>=90 and rate<=100:
    
#     print("Performance Result : Outstanding")

# #the rate is above 60 and below or equal to 89 elif condition is true print "Good" elif is false else statement print"Needs Improvement"

# elif rate>=60 and rate<=89:
    
#     print("Performance Result : Good")

# else:
    
#     print("Performance Result : Needs Improvement")
 
 
