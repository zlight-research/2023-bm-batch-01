"""II. Look at sample complex data structure
[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
2. Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
}"""

input_data = [
    {"id": 1, "f_name": "yadhu", "l_name": "Kumar", "gender": "M", "age": 25},
    {"id": 2, "f_name": "Ajay", "l_name": "Gopi", "gender": "M", "age": 16},
    {"id": 3, "f_name": "syam", "l_name": "Warrier", "gender": "F", "age": 22}
]

output_data = []  # Create a dict and inputDataList
# prefix is using Mr,Mrs and Miss gender of the person
for person in input_data:
    name_prefix = "Mr." if person["gender"] == "M" else "Mrs."
    full_name = name_prefix + person["f_name"] + "," + person["l_name"]
    output_data.append({"id": person["id"], "name": full_name})
# Display new list
print("New list: ", output_data)

output_format = {"age <= 20": [], "age > 20": []} #create another dictionary
# 
for person in input_data:
    full_name = person["f_name"] + "," + person["l_name"]
    if person["age"] <= 20:
        output_format["age <= 20"].append(full_name)
    else:
        output_format["age > 20"].append(full_name)
# Display new dict
print("New dict: ", output_format)
