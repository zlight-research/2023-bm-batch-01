# """II. Look at sample complex data structure
# [{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
# {"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
# {"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


# 1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
# 2. Please construct below format

# {" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
# " Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
# }
# """

# """1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}"""

school=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


stud=[]
for i in school:
    if i['gender']=='M':
        name='Mr.'+i['f_name']+' '+i['l_name']
    else:
        name='Mrs.'+i['f_name']+' '+i['l_name']
    stud.append({"id":i["id"],"name":name})
print(stud)



"""Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
}"""
school=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]
my_dict = {}
for i in school:
    if i["age"] <= 20:
        my_dict["Age <= 20"] = my_dict.get("Age <= 20", []) + [{"name": f"{i['f_name']} {i['l_name']}"}]
    else:
        my_dict["Age > 20"] = my_dict.get("Age > 20", []) +  [{"name": f"{i['f_name']} {i['l_name']}"}]

print(my_dict)