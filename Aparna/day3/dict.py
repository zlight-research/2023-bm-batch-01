# 1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}

dict=[{"id":1, "f_name":"yadhu", "l_name":"kumar","gender":"M","age":25},
      {"id":2, "f_name":"Ajay","l_name":"Gopi","gender":"M","age":16},
      {"id":3, "f_name":"syam","l_name":"warrier","gender":"F","age":22}]
# created an empty list
new_data=[]
# used for-loop with if condition and append the resultwith new string
for i in dict:
    if i["gender"]=="M":
        name="Mr." + i["f_name"]+","+i["l_name"]
    else:
        name="Mrs."+i["f_name"]+","+i["l_name"]
    new_data.append({"id":i["id"],"name":name})
print(new_data)

# 2. Please construct below format

# {" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
# " Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
# }
data = [{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]

new_data={"age  of <=20":[],"age of > 20":[]}

for i in data:
    if i["age"]<=20:
        new_data["age  of <=20"].append({"f_name": i["f_name"], "l_name": i["l_name"]})
    else:
        new_data["age of > 20"].append({"f_name": i["f_name"],"l_name": i["l_name"]})
print(new_data)

