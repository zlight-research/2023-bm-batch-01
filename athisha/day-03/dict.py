"""II. Look at sample complex data structure
[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
2. Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
}"""

my_dict = [{"id": 1, "f_name": "yadhu", "l_name": "Kumar", "gender": "M", "age": 25},
        {"id": 2, "f_name": "Ajay", "l_name": "Gopi", "gender": "M", "age": 16},
        {"id": 3, "f_name": "Syam", "l_name": "Warrier", "gender": "F", "age": 22}]
new_dictionary = dict()
updated_list = list()

new_dictionary["age <= 20"] = [] if len(new_dictionary) == 0 else 0
new_dictionary["age > 20"] = [] if "age>20" not in new_dictionary.keys() else 0
print("new_dictionary")
# Add data to list and dictionary
for length in range(len(my_dict)):
    updated_list.append({"id": my_dict[length]["id"], "name": "Mr."+my_dict[length]["f_name"]+","+my_dict[length]["l_name"]}) if my_dict[length]["gender"] == "M" else updated_list.append(
        {"id": my_dict[length]["id"], "name": "Mrs." + my_dict[length]["f_name"] + "," + my_dict[length]["l_name"]})
    new_dictionary["age <= 20"].append({my_dict[length]["f_name"]+","+my_dict[length]["l_name"]}
                                       ) if my_dict[length]["age"] <= 20 else new_dictionary["age > 20"].append({my_dict[length]["f_name"] + "," + my_dict[length]["l_name"]})
# Display data
print("New list : ", updated_list, "\nNew dict : ", new_dictionary)

# dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
print(dict())  
