"""II. Look at sample complex data structure
[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
2. Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
}"""

data = [{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]

new_data = []
for item in data:
    if item['gender'] == 'M':
        new_data.append({"id": item["id"], "name": "Mr. " + item["f_name"] + " " + item["l_name"]})
    else:
        new_data.append({"id": item["id"], "name": "Mrs. " + item["f_name"] + " " + item["l_name"]})
print(new_data)

#2 
data = [{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]

new_dict={"age  of <=20":[],"age of > 20":[]}

for itemm in data:
    if itemm["age"]<=20:
        new_dict["age  of <=20"].append({"f_name": itemm["f_name"], "l_name": itemm["l_name"]})
    else:
        new_dict["age of > 20"].append({"f_name": itemm["f_name"],"l_name": itemm["l_name"]})
print(new_dict)