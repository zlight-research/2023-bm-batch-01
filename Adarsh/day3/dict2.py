# II. Look at sample complex data structure
# [{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
# {"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
# {"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


dict=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M","age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


# 1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}

new_dict = [] #empty list created

for member in dict:  # used for-loop and if condition to append the result with new string
    if member["gender"] == "M":
        name = "Mr." + member["f_name"] + "," + member["l_name"]
    else:
        name = "Mrs." + member["f_name"] + "," + member["l_name"]
    new_dict.append({"id": member["id"], "name": name}) #Appended id and name to new_dict using append method
print(new_dict)         


# 2. Please construct below format
#
# {" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}], " Age > 20": [{<f_name,l_name>},{<f_name,l_name>}]}

# new empty list
list1=[]
list2=[]
# new empty dictionary
new_dict1={}
new_dict2={}

#check age condition
for member in dict:
    if member["age"]<=20:
        new_dict1=member["f_name"],member["l_name"]
        list1.append(new_dict1)#stored in list 
    else:
        new_dict2=member["f_name"],member["l_name"]
        list2.append(new_dict2)#stored in list  

final={"age<20":list1,"age>20":list2}#stored lists in dictionary
print(final)