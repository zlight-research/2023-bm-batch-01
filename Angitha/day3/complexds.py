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
stud=[]
max=[]
min=[]
for ag in school:
    if ag['age']<=20:
        name='age'+ag['f_name']+' '+ag['l_name']
        max.append({"name":ag["name"]})
    else:
        name='age'+ag['f_name']+' '+ag['l_name']
        min.append({"name":ag["name"]})
    stud.append({"age":ag["age"],"name":name})
    print(stud)
# for i in school:
#     if i['age']<=20:
#         name='Age'+i['f_name']+' '+i['l_name']
#         # i={"age":i["age"], "name":name}
        
#         max.append({"name":name})
#     else:
#         name='Age'+i['f_name']+' '+i['l_name']
#         # i={"age":i["age"], "name":name}
#         min.append({"name":name})
# # Age={"Age<=20":max,"name"=name,"Age>=20":min,"name"=name}
# print(stud)
