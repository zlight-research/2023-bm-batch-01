""" 4). Enter input using python code"""


d = { } #declaring empty dictionary
for i in range(1):
    name = input("First Name: ") 
    lastname = input("Last Name: ") 
    Gender = input("Gender: ")
    Age=int(input("Age: "))
    Rating=int(input("Rating: "))

#------assinging the keys with the values---------

    d["name"] = name.capitalize() 
    d["lastname"] = lastname .capitalize()
    d["gender"] = Gender.capitalize()
    d["age"] = Age
    d["rating"] = Rating

     
#--------defining the salutation using gender and age in if condition------

if d["gender"]=="MALE":
    print("Name: Mr.",d["lastname"],d["name"])
elif d["gender"]=="FEMALE":
    if d["age"]<=30:
       print("name: Miss.",d["lastname"],d["name"])
    else:
       print("name: Mrs.",d["lastname"],d["name"])

#---------display the rating table using rating in if condition-------

print("Rating Table")
print(d["rating"])
if d["rating"]>100:
    print("Rating Result : Extra Milestone")
elif d["rating"]>=90 and d["rating"]<=100:
    print("Rating Result : Outstanding")
elif d["rating"]>=60 and d["rating"]<=89:
    print("Rating Result : Good")
else:
    print("Rating Result : Needs Improvement")