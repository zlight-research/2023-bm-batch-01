""" 4). Enter input using python code"""


dict = { } #declaring empty dictionary
firstname,lastname = input("First Name: ","Last Name: ") 
Gender = input("Gender: ")
Age=int(input("Age: "))
Rating=int(input("Rating: "))

#------assinging the keys with the values---------

dict["name"] = firstname.capitalize() 
dict["lastname"] = lastname .capitalize()
dict["gender"] = Gender.capitalize()
dict["age"] = Age
dict["rating"] = Rating

     
#--------defining the salutation using gender and age in if condition------

if dict["gender"]=="MALE":
    print("Name: Mr.",dict["lastname"],dict["name"])
elif dict["gender"]=="FEMALE":
    if dict["age"]<=30:
       print("name: Miss.",dict["lastname"],dict["name"])
    else:
       print("name: Mrs.",dict["lastname"],dict["name"])

#---------display the rating table using rating in if condition-------

print("Rating Table")
print(dict["rating"])
if dict["rating"]>100:
    print("Rating Result : Extra Milestone")
elif dict["rating"]>=90 and dict["rating"]<=100:
    print("Rating Result : Outstanding")
elif dict["rating"]>=60 and dict["rating"]<=89:
    print("Rating Result : Good")
else:
    print("Rating Result : Needs Improvement")