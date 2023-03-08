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

 



Performance Result : Extra Milestone



Additional requirements.
* Based on Rating, Performance result should be displayed according the rating table

* Name should displayed with proper salutation

* Name should be displayed with a Proper case such as the first character should be Capital.

* Incase only one name displayed, there should not comma character (,)

*Incase there is blank for First Name OR Last Name, display message  as "User must enter any one of the fields "First Name" or Last Name"



'''


#input some detailes first_name,last_name,gender,age,rate


first_name=input("enter first name :")

last_name=input("enter last name :")

gender1=input("enter gender :")

age=int(input("enter age:"))

rate=int(input("enter rate:"))

#gender letter case changed to lower case

gender=gender1.lower()
print("*"*100)

#if condition  is True then pass to next if condition if condition is false else statement can print

if first_name or last_name :
    #if condition is true gender is male then execute the print statement if condition false then pass to elif condition
    
    if gender=='male' :
            print("Mr",last_name.capitalize(),first_name.capitalize())
    
    #elif condition is true then pass to next if condition   false then execute else statement
    
    elif gender=='female':
        #if condition is true then print statement execute if ststement is false else statement can execute and print
        if age<=30:
            print("Miss",last_name.capitalize(),first_name.capitalize())
        else:
            print("Mrs.",last_name.capitalize(),first_name.capitalize())    
    
    else:
        print("gender not find")
        

else:        
     
    print("user must enter any one of the fields first name or last name")    
    
print("*"*100)

#display rating table

print("Rating table")
#the rate is above 100 if condition is true print result"Extra milestone" if is false then pass to elif statement
if rate>100:

    print("Performance Result : Extra Milestone")

#the rate is above 90 and below or equal to 100  elif condition is true print result "Outstanding" elif is false then pass to next elif statement

elif rate>=90 and rate<=100:
    
    print("Performance Result : Outstanding")

#the rate is above 60 and below or equal to 89 elif condition is true print "Good" elif is false else statement print"Needs Improvement"

elif rate>=60 and rate<=89:
    
    print("Performance Result : Good")

else:
    
    print("Performance Result : Needs Improvement")
 

