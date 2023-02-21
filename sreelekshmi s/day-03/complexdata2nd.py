""" Look at sample complex data structure
[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
2. Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
}"""


original_list = [{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},    
                {"id":2, "f_name":"Ajay", "l_name":"Gopi", "gender":"M", "age":16},    
                {"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]

new_dict = {"Age <= 20": []}   #new dict contain age below 20 
new_dict1 = { "Age > 20": []} #new dict contain age above  20 
for item in original_list:
    full_data = {"f_name": item["f_name"], "l_name": item["l_name"],"id":item['id']}
    if item["age"] <= 20:
        new_dict["Age <= 20"].append(full_data)
    else:
        new_dict1["Age > 20"].append(full_data)

print(new_dict)
print(new_dict1)